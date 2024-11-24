import content_pb2 as _content_pb2
import context_pb2 as _context_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppRequest(_message.Message):
    __slots__ = ("generate_request", "stop_request", "user_request", "message", "error", "embed_request")
    GENERATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    STOP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    USER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EMBED_REQUEST_FIELD_NUMBER: _ClassVar[int]
    generate_request: GenerateRequest
    stop_request: StopRequest
    user_request: UserResponseRequest
    message: AppMessage
    error: ErrorRequest
    embed_request: EmbedRequest
    def __init__(self, generate_request: _Optional[_Union[GenerateRequest, _Mapping]] = ..., stop_request: _Optional[_Union[StopRequest, _Mapping]] = ..., user_request: _Optional[_Union[UserResponseRequest, _Mapping]] = ..., message: _Optional[_Union[AppMessage, _Mapping]] = ..., error: _Optional[_Union[ErrorRequest, _Mapping]] = ..., embed_request: _Optional[_Union[EmbedRequest, _Mapping]] = ...) -> None: ...

class StreamingGeneration(_message.Message):
    __slots__ = ("content_type", "additional_content")
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_CONTENT_FIELD_NUMBER: _ClassVar[int]
    content_type: _content_pb2.Content.ContentType
    additional_content: str
    def __init__(self, content_type: _Optional[_Union[_content_pb2.Content.ContentType, str]] = ..., additional_content: _Optional[str] = ...) -> None: ...

class GenerateResponseFormat(_message.Message):
    __slots__ = ("format", "schema")
    class ResponseFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESPONSE_TEXT: _ClassVar[GenerateResponseFormat.ResponseFormat]
        RESPONSE_JSON: _ClassVar[GenerateResponseFormat.ResponseFormat]
        RESPONSE_EBNF: _ClassVar[GenerateResponseFormat.ResponseFormat]
    RESPONSE_TEXT: GenerateResponseFormat.ResponseFormat
    RESPONSE_JSON: GenerateResponseFormat.ResponseFormat
    RESPONSE_EBNF: GenerateResponseFormat.ResponseFormat
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    format: GenerateResponseFormat.ResponseFormat
    schema: str
    def __init__(self, format: _Optional[_Union[GenerateResponseFormat.ResponseFormat, str]] = ..., schema: _Optional[str] = ...) -> None: ...

class GenerateRequest(_message.Message):
    __slots__ = ("id", "prompt", "context", "max_tokens", "fmt", "temperature", "frequency_penalty", "presence_penalty", "top_p", "stream", "stop_strings")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    FMT_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PENALTY_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_PENALTY_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    STOP_STRINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    prompt: str
    context: _context_pb2.PrevContext
    max_tokens: int
    fmt: GenerateResponseFormat
    temperature: float
    frequency_penalty: float
    presence_penalty: float
    top_p: float
    stream: StreamingGeneration
    stop_strings: str
    def __init__(self, id: _Optional[str] = ..., prompt: _Optional[str] = ..., context: _Optional[_Union[_context_pb2.PrevContext, _Mapping]] = ..., max_tokens: _Optional[int] = ..., fmt: _Optional[_Union[GenerateResponseFormat, _Mapping]] = ..., temperature: _Optional[float] = ..., frequency_penalty: _Optional[float] = ..., presence_penalty: _Optional[float] = ..., top_p: _Optional[float] = ..., stream: _Optional[_Union[StreamingGeneration, _Mapping]] = ..., stop_strings: _Optional[str] = ...) -> None: ...

class Embedding(_message.Message):
    __slots__ = ("size", "data")
    SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    size: int
    data: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, size: _Optional[int] = ..., data: _Optional[_Iterable[float]] = ...) -> None: ...

class EmbedDoc(_message.Message):
    __slots__ = ("doc", "tag", "sim")
    DOC_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    SIM_FIELD_NUMBER: _ClassVar[int]
    doc: str
    tag: str
    sim: float
    def __init__(self, doc: _Optional[str] = ..., tag: _Optional[str] = ..., sim: _Optional[float] = ...) -> None: ...

class EmbedResponse(_message.Message):
    __slots__ = ("embed_request_id", "embedding", "num_affected", "results")
    EMBED_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    NUM_AFFECTED_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    embed_request_id: str
    embedding: _containers.RepeatedCompositeFieldContainer[Embedding]
    num_affected: int
    results: _containers.RepeatedCompositeFieldContainer[EmbedDoc]
    def __init__(self, embed_request_id: _Optional[str] = ..., embedding: _Optional[_Iterable[_Union[Embedding, _Mapping]]] = ..., num_affected: _Optional[int] = ..., results: _Optional[_Iterable[_Union[EmbedDoc, _Mapping]]] = ...) -> None: ...

class EmbedRequest(_message.Message):
    __slots__ = ("embed_request_id", "op", "limit", "query_tag", "docs")
    class EmbedQueryOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EQ_UNDEFINED: _ClassVar[EmbedRequest.EmbedQueryOp]
        EQ_STORE: _ClassVar[EmbedRequest.EmbedQueryOp]
        EQ_GET_SIM: _ClassVar[EmbedRequest.EmbedQueryOp]
        EQ_DEL_SIM: _ClassVar[EmbedRequest.EmbedQueryOp]
        EQ_GET_RAW: _ClassVar[EmbedRequest.EmbedQueryOp]
    EQ_UNDEFINED: EmbedRequest.EmbedQueryOp
    EQ_STORE: EmbedRequest.EmbedQueryOp
    EQ_GET_SIM: EmbedRequest.EmbedQueryOp
    EQ_DEL_SIM: EmbedRequest.EmbedQueryOp
    EQ_GET_RAW: EmbedRequest.EmbedQueryOp
    EMBED_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    QUERY_TAG_FIELD_NUMBER: _ClassVar[int]
    DOCS_FIELD_NUMBER: _ClassVar[int]
    embed_request_id: str
    op: EmbedRequest.EmbedQueryOp
    limit: int
    query_tag: str
    docs: _containers.RepeatedCompositeFieldContainer[EmbedDoc]
    def __init__(self, embed_request_id: _Optional[str] = ..., op: _Optional[_Union[EmbedRequest.EmbedQueryOp, str]] = ..., limit: _Optional[int] = ..., query_tag: _Optional[str] = ..., docs: _Optional[_Iterable[_Union[EmbedDoc, _Mapping]]] = ...) -> None: ...

class UserResponseRequest(_message.Message):
    __slots__ = ("id", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    reason: str
    def __init__(self, id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ("id", "response", "interjection")
    ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INTERJECTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    response: str
    interjection: bool
    def __init__(self, id: _Optional[str] = ..., response: _Optional[str] = ..., interjection: bool = ...) -> None: ...

class AppMessage(_message.Message):
    __slots__ = ("app_message_id", "content", "partial")
    APP_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FIELD_NUMBER: _ClassVar[int]
    app_message_id: str
    content: _content_pb2.Content
    partial: bool
    def __init__(self, app_message_id: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., partial: bool = ...) -> None: ...

class ErrorRequest(_message.Message):
    __slots__ = ("fatal", "error", "details")
    FATAL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    fatal: bool
    error: str
    details: str
    def __init__(self, fatal: bool = ..., error: _Optional[str] = ..., details: _Optional[str] = ...) -> None: ...

class StopRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AppResponse(_message.Message):
    __slots__ = ("initial_response", "token_response", "user_request", "embed_response")
    INITIAL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    USER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    EMBED_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    initial_response: InitialResponse
    token_response: TokenResponse
    user_request: UserResponse
    embed_response: EmbedResponse
    def __init__(self, initial_response: _Optional[_Union[InitialResponse, _Mapping]] = ..., token_response: _Optional[_Union[TokenResponse, _Mapping]] = ..., user_request: _Optional[_Union[UserResponse, _Mapping]] = ..., embed_response: _Optional[_Union[EmbedResponse, _Mapping]] = ...) -> None: ...

class AttachedFile(_message.Message):
    __slots__ = ("name", "path")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    def __init__(self, name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class InitialResponse(_message.Message):
    __slots__ = ("args", "file", "context")
    class ArgsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ARGS_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    args: _containers.ScalarMap[str, str]
    file: AttachedFile
    context: _context_pb2.PrevContext
    def __init__(self, args: _Optional[_Mapping[str, str]] = ..., file: _Optional[_Union[AttachedFile, _Mapping]] = ..., context: _Optional[_Union[_context_pb2.PrevContext, _Mapping]] = ...) -> None: ...

class GenerationUsage(_message.Message):
    __slots__ = ("prompt_tokens", "completion_tokens", "approx_time")
    PROMPT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    APPROX_TIME_FIELD_NUMBER: _ClassVar[int]
    prompt_tokens: int
    completion_tokens: int
    approx_time: int
    def __init__(self, prompt_tokens: _Optional[int] = ..., completion_tokens: _Optional[int] = ..., approx_time: _Optional[int] = ...) -> None: ...

class TokenResponse(_message.Message):
    __slots__ = ("id", "token", "finish_reason", "usage", "error")
    class FinishReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FINISH_REASON_UNSPECIFIED: _ClassVar[TokenResponse.FinishReason]
        FINISH_REASON_LENGTH: _ClassVar[TokenResponse.FinishReason]
        FINISH_REASON_STOP: _ClassVar[TokenResponse.FinishReason]
        FINISH_REASON_ERROR: _ClassVar[TokenResponse.FinishReason]
        FINISH_REASON_USER: _ClassVar[TokenResponse.FinishReason]
    FINISH_REASON_UNSPECIFIED: TokenResponse.FinishReason
    FINISH_REASON_LENGTH: TokenResponse.FinishReason
    FINISH_REASON_STOP: TokenResponse.FinishReason
    FINISH_REASON_ERROR: TokenResponse.FinishReason
    FINISH_REASON_USER: TokenResponse.FinishReason
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    id: str
    token: str
    finish_reason: TokenResponse.FinishReason
    usage: GenerationUsage
    error: str
    def __init__(self, id: _Optional[str] = ..., token: _Optional[str] = ..., finish_reason: _Optional[_Union[TokenResponse.FinishReason, str]] = ..., usage: _Optional[_Union[GenerationUsage, _Mapping]] = ..., error: _Optional[str] = ...) -> None: ...
