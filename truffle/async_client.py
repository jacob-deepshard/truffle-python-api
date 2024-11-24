import grpc
import asyncio
from typing import Callable, Dict, List, Optional
import numpy as np

# Import the generated protobuf modules
from protos import app_pb2
from protos import app_pb2_grpc
from protos import content_pb2
from protos import context_pb2

class AsyncClient:
    start_cbs: Dict[str, Callable[[], None]]
    stop_cbs: Dict[str, Callable[[], None]]

    def __init__(self, server_address: str = "localhost:50051"):
        self.start_cbs = {}
        self.stop_cbs = {}

        # Initialize the gRPC channel and stub using the async API
        self.channel = grpc.aio.insecure_channel(server_address)
        self.stub = app_pb2_grpc.AppStub(self.channel)

    async def __aenter__(self):
        """Enable use as an async context manager."""
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """Handle cleanup when exiting async context."""
        await self.channel.close()

    async def generate(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        top_p: Optional[float] = None,
        stop_strings: Optional[List[str]] = None,
        streaming: Optional[bool] = False,
        on_chunk: Optional[Callable[[str], None]] = None,
        on_start: Optional[Callable[[], None]] = None,
        on_stop: Optional[Callable[[], None]] = None,
        **kwargs,
    ) -> str:
        """Generates a response from the model asynchronously."""

        # Handle callbacks
        if on_start:
            on_start()
        for cb in self.start_cbs.values():
            cb()

        if streaming:
            output = ""
            async for chunk in self._generate_stream(
                prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                top_p=top_p,
                stop_strings=stop_strings,
                on_chunk=on_chunk,
            ):
                output += chunk
            if on_stop:
                on_stop()
            for cb in self.stop_cbs.values():
                cb()
            return output
        else:
            response = await self._generate_sync(
                prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                top_p=top_p,
                stop_strings=stop_strings,
            )
            if on_stop:
                on_stop()
            for cb in self.stop_cbs.values():
                cb()
            return response

    async def _generate_stream(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        top_p: Optional[float] = None,
        stop_strings: Optional[List[str]] = None,
        on_chunk: Optional[Callable[[str], None]] = None,
    ):
        """Generates a stream of responses from the model asynchronously."""

        # Create the GenerateRequest message
        generate_request = app_pb2.GenerateRequest(
            id="generate_request_1",
            prompt=prompt,
            max_tokens=max_tokens or 512,
            temperature=temperature or 1.0,
            frequency_penalty=frequency_penalty or 0.0,
            presence_penalty=presence_penalty or 0.0,
            top_p=top_p or 1.0,
            stop_strings=",".join(stop_strings) if stop_strings else "",
            stream=app_pb2.StreamingGeneration(content_type=content_pb2.Content.CONTENT_DEFAULT),
        )

        app_request = app_pb2.AppRequest(generate_request=generate_request)

        # Send the request and receive streaming responses asynchronously
        response_iterator = self.stub.Generate(self._request_iterator(app_request))

        async for response in response_iterator:
            if response.HasField("token_response"):
                token_response = response.token_response
                token = token_response.token
                if on_chunk:
                    on_chunk(token)
                yield token
            elif response.HasField("error"):
                error = response.error
                await self.error(error.error)
                break

    async def _request_iterator(self, app_request):
        """An async iterator that yields the AppRequest."""
        yield app_request

    async def _generate_sync(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        top_p: Optional[float] = None,
        stop_strings: Optional[List[str]] = None,
    ) -> str:
        """Generates a synchronous response from the model asynchronously."""

        output = ""
        async for chunk in self._generate_stream(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            top_p=top_p,
            stop_strings=stop_strings,
        ):
            output += chunk
        return output

    async def embed(self, docs: List[str], **kwargs) -> np.ndarray:
        """Returns a numpy array of embeddings for the given documents asynchronously."""

        embed_docs = [app_pb2.EmbedDoc(doc=doc) for doc in docs]

        embed_request = app_pb2.EmbedRequest(
            embed_request_id="embed_request_1",
            op=app_pb2.EmbedRequest.EQ_GET_RAW,
            docs=embed_docs
        )

        app_request = app_pb2.AppRequest(embed_request=embed_request)

        # Send the request and receive the response asynchronously
        response = await self.stub.Embed(app_request)

        embeddings = [embedding.data for embedding in response.embedding]

        return np.array(embeddings)

    async def input(self, prompt: str, **kwargs) -> str:
        """Sends a UserResponseRequest to the server and waits for a UserResponse asynchronously."""
        # Create the UserResponseRequest message
        user_response_request = app_pb2.UserResponseRequest(
            id="user_response_request_1",
            reason=prompt
        )

        app_request = app_pb2.AppRequest(
            user_request=user_response_request
        )

        # Send the request to the server asynchronously
        response = await self.stub.HandleAppRequest(app_request)

        # Check for UserResponse in the response
        if response.HasField('user_request'):
            user_response = response.user_request
            return user_response.response
        elif response.HasField('error'):
            raise Exception(response.error.error)
        else:
            raise Exception("Unexpected response from server.")

    async def print(self, message: str, **kwargs):
        """Sends an AppMessage containing the message to the server asynchronously."""
        # Create the Content message
        content = content_pb2.Content(
            content_type=content_pb2.Content.CONTENT_DEFAULT,
            text=message
        )

        # Create the AppMessage
        app_message = app_pb2.AppMessage(
            app_message_id="app_message_1",
            content=content,
            partial=False
        )

        app_request = app_pb2.AppRequest(
            message=app_message
        )

        # Send the request to the server asynchronously
        response = await self.stub.HandleAppRequest(app_request)

        # Optionally handle the response or errors
        if response.HasField('error'):
            raise Exception(response.error.error)

    async def error(self, message: str, **kwargs):
        """Sends an ErrorRequest containing the error message to the server asynchronously."""
        # Create the ErrorRequest message
        error_request = app_pb2.ErrorRequest(
            fatal=False,
            error=message,
            details=""
        )

        app_request = app_pb2.AppRequest(
            error=error_request
        )

        # Send the request to the server asynchronously
        response = await self.stub.HandleAppRequest(app_request)

        # Optionally handle the response or log the error
        if response.HasField('error'):
            raise Exception(response.error.error)

    def add_start_callback(self, cb: Callable[[], None]) -> str:
        """Adds a start callback."""
        callback_id = str(id(cb))
        self.start_cbs[callback_id] = cb
        return callback_id

    def add_stop_callback(self, cb: Callable[[], None]) -> str:
        """Adds a stop callback."""
        callback_id = str(id(cb))
        self.stop_cbs[callback_id] = cb
        return callback_id

    def remove_start_callback(self, cb_or_id: Callable[[], None] or str):
        """Removes a start callback."""
        if isinstance(cb_or_id, str):
            self.start_cbs.pop(cb_or_id, None)
        else:
            callback_id = str(id(cb_or_id))
            self.start_cbs.pop(callback_id, None)

    def remove_stop_callback(self, cb_or_id: Callable[[], None] or str):
        """Removes a stop callback."""
        if isinstance(cb_or_id, str):
            self.stop_cbs.pop(cb_or_id, None)
        else:
            callback_id = str(id(cb_or_id))
            self.stop_cbs.pop(callback_id, None) 