import grpc
from typing import Callable, Dict, List, Literal, Optional
import numpy as np

# Import the generated protobuf modules
from protos import app_pb2
from protos import app_pb2_grpc
from protos import content_pb2
from protos import context_pb2


class Client:
    """A client for interacting with the Truffle gRPC server.

    This class provides methods for generating text, getting embeddings, handling user input/output,
    and managing callbacks for generation events.

    Example:
        >>> client = Client()
        >>> response = client.generate("What is the capital of France?")
        >>> print(response)
        'The capital of France is Paris.'

    Attributes:
        start_cbs (Dict[str, Callable[[], None]]): Dictionary of callback functions to run when generation starts
        stop_cbs (Dict[str, Callable[[], None]]): Dictionary of callback functions to run when generation stops
    """

    start_cbs: Dict[str, Callable[[], None]]
    stop_cbs: Dict[str, Callable[[], None]]

    def __init__(self, server_address: str = "localhost:50051"):
        """Initialize the Client.

        Args:
            server_address (str, optional): Address of the gRPC server. Defaults to "localhost:50051".

        Example:
            >>> client = Client("localhost:50051")
        """
        self.start_cbs = {}

        # Initialize the gRPC channel and stub
        self.channel = grpc.insecure_channel(server_address)
        self.stub = app_pb2_grpc.AppStub(self.channel)

        # Initialize the context
        self.context = context_pb2.PrevContext(state={})

    def __del__(self):
        """Clean up by closing the gRPC channel."""
        # Close the channel
        self.channel.close()

    def generate(
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
        """Generate a response from the model.

        Args:
            prompt (str): The input prompt for generation
            max_tokens (Optional[int], optional): Maximum number of tokens to generate. Defaults to None.
            temperature (Optional[float], optional): Sampling temperature. Defaults to None.
            frequency_penalty (Optional[float], optional): Frequency penalty. Defaults to None.
            presence_penalty (Optional[float], optional): Presence penalty. Defaults to None.
            top_p (Optional[float], optional): Top-p sampling parameter. Defaults to None.
            stop_strings (Optional[List[str]], optional): Strings that stop generation. Defaults to None.
            streaming (Optional[bool], optional): Whether to stream the response. Defaults to False.
            on_chunk (Optional[Callable[[str], None]], optional): Callback for each generated chunk. Defaults to None.
            on_start (Optional[Callable[[], None]], optional): Callback when generation starts. Defaults to None.
            on_stop (Optional[Callable[[], None]], optional): Callback when generation stops. Defaults to None.

        Returns:
            str: The generated text

        Example:
            >>> client = Client()
            >>> # Basic generation
            >>> response = client.generate("Write a haiku about programming")
            >>> print(response)
            'Code flows like water
            Bugs crawl through my sleepless mind
            Debug until dawn'
            >>> 
            >>> # Streaming generation with callbacks
            >>> def on_chunk(chunk):
            ...     print(f"Received chunk: {chunk}")
            >>> response = client.generate(
            ...     "Count to 5",
            ...     streaming=True,
            ...     on_chunk=on_chunk
            ... )
        """

        # Handle callbacks
        if on_start:
            on_start()
        for cb in self.start_cbs.values():
            cb()

        if streaming:
            output = ""
            for chunk in self._generate_stream(
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
            response = self._generate_sync(
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

    def _generate_stream(
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
        """Generate a stream of responses from the model.

        Args:
            prompt (str): The input prompt for generation
            max_tokens (Optional[int], optional): Maximum number of tokens to generate. Defaults to None.
            temperature (Optional[float], optional): Sampling temperature. Defaults to None.
            frequency_penalty (Optional[float], optional): Frequency penalty. Defaults to None.
            presence_penalty (Optional[float], optional): Presence penalty. Defaults to None.
            top_p (Optional[float], optional): Top-p sampling parameter. Defaults to None.
            stop_strings (Optional[List[str]], optional): Strings that stop generation. Defaults to None.
            on_chunk (Optional[Callable[[str], None]], optional): Callback for each generated chunk. Defaults to None.

        Yields:
            str: Generated text chunks

        Example:
            >>> client = Client()
            >>> for chunk in client._generate_stream("Count to 3"):
            ...     print(chunk, end='')
            1, 2, 3
        """

        # Create the GenerateRequest message
        generate_request = app_pb2.GenerateRequest(
            id="generate_request_1",
            prompt=prompt,
            context=self.context,
            max_tokens=max_tokens or 512,
            temperature=temperature or 1.0,
            frequency_penalty=frequency_penalty or 0.0,
            presence_penalty=presence_penalty or 0.0,
            top_p=top_p or 1.0,
            stop_strings=",".join(stop_strings) if stop_strings else "",
            stream=app_pb2.StreamingGeneration(content_type=content_pb2.Content.CONTENT_DEFAULT),
        )

        app_request = app_pb2.AppRequest(generate_request=generate_request)

        # Send the request and receive streaming responses
        response_iterator = self.stub.Generate(self._request_iterator(app_request))

        for response in response_iterator:
            if response.HasField("token_response"):
                token_response = response.token_response
                token = token_response.token
                if on_chunk:
                    on_chunk(token)
                yield token
            elif response.HasField("error"):
                error = response.error
                self.error(error.error)
                break

    def _request_iterator(self, app_request):
        """Create an iterator that yields the AppRequest.

        Args:
            app_request: The AppRequest to yield

        Yields:
            The AppRequest

        Example:
            >>> client = Client()
            >>> request = app_pb2.AppRequest()
            >>> iterator = client._request_iterator(request)
            >>> next(iterator) == request
            True
        """
        yield app_request

    def _generate_sync(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        top_p: Optional[float] = None,
        stop_strings: Optional[List[str]] = None,
    ) -> str:
        """Generate a synchronous response from the model.

        Args:
            prompt (str): The input prompt for generation
            max_tokens (Optional[int], optional): Maximum number of tokens to generate. Defaults to None.
            temperature (Optional[float], optional): Sampling temperature. Defaults to None.
            frequency_penalty (Optional[float], optional): Frequency penalty. Defaults to None.
            presence_penalty (Optional[float], optional): Presence penalty. Defaults to None.
            top_p (Optional[float], optional): Top-p sampling parameter. Defaults to None.
            stop_strings (Optional[List[str]], optional): Strings that stop generation. Defaults to None.

        Returns:
            str: The generated text

        Example:
            >>> client = Client()
            >>> response = client._generate_sync("What is 2+2?")
            >>> print(response)
            '4'
        """

        output = ""
        for chunk in self._generate_stream(
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

    def embed(self, docs: List[str], **kwargs) -> np.ndarray:
        """Get embeddings for a list of documents.

        Args:
            docs (List[str]): List of documents to embed
            **kwargs: Additional keyword arguments

        Returns:
            np.ndarray: Array of embeddings

        Example:
            >>> client = Client()
            >>> docs = ["Hello world", "Goodbye world"]
            >>> embeddings = client.embed(docs)
            >>> embeddings.shape
            (2, 768)  # Assuming 768-dimensional embeddings
        """

        embed_docs = []
        for doc in docs:
            embed_doc = app_pb2.EmbedDoc(doc=doc)
            embed_docs.append(embed_doc)

        embed_request = app_pb2.EmbedRequest(
            embed_request_id="embed_request_1", op=app_pb2.EmbedRequest.EQ_GET_RAW, docs=embed_docs
        )

        app_request = app_pb2.AppRequest(embed_request=embed_request)

        # Send the request and receive the response
        response = self.stub.Embed(app_request)

        embeddings = []
        for embedding in response.embedding:
            embeddings.append(embedding.data)

        return np.array(embeddings)
    
    def set_status(self, status: Literal["idle", "busy", "error", "ready"]):
        """Set the status of the client.

        Args:
            status (str): The status to set
        """
        # Set the status in the context state
        self.context.state['status'] = status

    def input(self, prompt: str, **kwargs) -> str:
        """Send a user response request and wait for response.

        Args:
            prompt (str): The prompt to show the user
            **kwargs: Additional keyword arguments

        Returns:
            str: The user's response

        Raises:
            Exception: If there is an error or unexpected response

        Example:
            >>> client = Client()
            >>> response = client.input("What is your name?")
            What is your name? Alice
            >>> print(response)
            'Alice'
        """
        # Create the UserResponseRequest message
        user_response_request = app_pb2.UserResponseRequest(
            id="user_response_request_1",
            reason=prompt
        )

        app_request = app_pb2.AppRequest(
            user_request=user_response_request
        )

        # Send the request to the server
        response = self.stub.HandleAppRequest(app_request)

        # Check for UserResponse in the response
        if response.HasField('user_request'):
            user_response = response.user_request
            return user_response.response
        elif response.HasField('error'):
            raise Exception(response.error.error)
        else:
            raise Exception("Unexpected response from server.")

    def print(self, message: str, **kwargs):
        """Send a message to be displayed.

        Args:
            message (str): The message to display
            **kwargs: Additional keyword arguments

        Raises:
            Exception: If there is an error response

        Example:
            >>> client = Client()
            >>> client.print("Hello, world!")
            Hello, world!
        """
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

        # Send the request to the server
        response = self.stub.HandleAppRequest(app_request)

        # Optionally handle the response or errors
        if response.HasField('error'):
            raise Exception(response.error.error)

    def error(self, message: str, **kwargs):
        """Send an error message.

        Args:
            message (str): The error message
            **kwargs: Additional keyword arguments

        Raises:
            Exception: If there is an error response

        Example:
            >>> client = Client()
            >>> client.error("Something went wrong!")
            Error: Something went wrong!
        """
        # Create the ErrorRequest message
        error_request = app_pb2.ErrorRequest(
            fatal=False,
            error=message,
            details=""
        )

        app_request = app_pb2.AppRequest(
            error=error_request
        )

        # Send the request to the server
        response = self.stub.HandleAppRequest(app_request)

        # Optionally handle the response or log the error
        if response.HasField('error'):
            raise Exception(response.error.error)
