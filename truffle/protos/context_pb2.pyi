from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ContextEntry(_message.Message):
    __slots__ = ("type", "content", "index")

    class ContextEntryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CTX_UNDEFINED: _ClassVar[ContextEntry.ContextEntryType]
        CTX_USER_RESPONSE: _ClassVar[ContextEntry.ContextEntryType]
        CTX_ASSISTANT: _ClassVar[ContextEntry.ContextEntryType]
        CTX_TOOL_RESULT: _ClassVar[ContextEntry.ContextEntryType]
        CTX_SYSTEM: _ClassVar[ContextEntry.ContextEntryType]
        CTX_FILE: _ClassVar[ContextEntry.ContextEntryType]

    CTX_UNDEFINED: ContextEntry.ContextEntryType
    CTX_USER_RESPONSE: ContextEntry.ContextEntryType
    CTX_ASSISTANT: ContextEntry.ContextEntryType
    CTX_TOOL_RESULT: ContextEntry.ContextEntryType
    CTX_SYSTEM: ContextEntry.ContextEntryType
    CTX_FILE: ContextEntry.ContextEntryType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    type: ContextEntry.ContextEntryType
    content: str
    index: int
    def __init__(
        self,
        type: _Optional[_Union[ContextEntry.ContextEntryType, str]] = ...,
        content: _Optional[str] = ...,
        index: _Optional[int] = ...,
    ) -> None: ...

class PrevContext(_message.Message):
    __slots__ = ("state", "context")

    class StateEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

    STATE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    state: _containers.ScalarMap[str, str]
    context: _containers.RepeatedCompositeFieldContainer[ContextEntry]
    def __init__(
        self,
        state: _Optional[_Mapping[str, str]] = ...,
        context: _Optional[_Iterable[_Union[ContextEntry, _Mapping]]] = ...,
    ) -> None: ...
