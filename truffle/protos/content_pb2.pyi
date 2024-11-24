from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CodeContent(_message.Message):
    __slots__ = ("metadata", "content")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    metadata: str
    content: str
    def __init__(self, metadata: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class TextContent(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class ErrorContent(_message.Message):
    __slots__ = ("error", "details")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    error: str
    details: str
    def __init__(self, error: _Optional[str] = ..., details: _Optional[str] = ...) -> None: ...

class FileContent(_message.Message):
    __slots__ = ("filename", "filesize", "file_id")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILESIZE_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    filename: str
    filesize: int
    file_id: str
    def __init__(
        self,
        filename: _Optional[str] = ...,
        filesize: _Optional[int] = ...,
        file_id: _Optional[str] = ...,
    ) -> None: ...

class MediaContent(_message.Message):
    __slots__ = ("metadata", "data")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    metadata: str
    data: str
    def __init__(self, metadata: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class RichContent(_message.Message):
    __slots__ = ("type", "content")

    class RichContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RICHCONTENT_DEFAULT: _ClassVar[RichContent.RichContentType]
        RICHCONTENT_MARKDOWN: _ClassVar[RichContent.RichContentType]
        RICHCONTENT_UNKNOWN: _ClassVar[RichContent.RichContentType]

    RICHCONTENT_DEFAULT: RichContent.RichContentType
    RICHCONTENT_MARKDOWN: RichContent.RichContentType
    RICHCONTENT_UNKNOWN: RichContent.RichContentType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    type: RichContent.RichContentType
    content: str
    def __init__(
        self,
        type: _Optional[_Union[RichContent.RichContentType, str]] = ...,
        content: _Optional[str] = ...,
    ) -> None: ...

class ToolUse(_message.Message):
    __slots__ = ("name", "description", "has_response", "tool_icon_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HAS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TOOL_ICON_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    has_response: bool
    tool_icon_name: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        description: _Optional[str] = ...,
        has_response: bool = ...,
        tool_icon_name: _Optional[str] = ...,
    ) -> None: ...

class Content(_message.Message):
    __slots__ = ("type", "code", "rtf", "media", "text", "error", "file", "tool_use")

    class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTENT_DEFAULT: _ClassVar[Content.ContentType]
        CONTENT_CODE: _ClassVar[Content.ContentType]
        CONTENT_MEDIA: _ClassVar[Content.ContentType]
        CONTENT_RICH: _ClassVar[Content.ContentType]
        CONTENT_ERROR: _ClassVar[Content.ContentType]
        CONTENT_OTHER: _ClassVar[Content.ContentType]
        CONTENT_FILE: _ClassVar[Content.ContentType]

    CONTENT_DEFAULT: Content.ContentType
    CONTENT_CODE: Content.ContentType
    CONTENT_MEDIA: Content.ContentType
    CONTENT_RICH: Content.ContentType
    CONTENT_ERROR: Content.ContentType
    CONTENT_OTHER: Content.ContentType
    CONTENT_FILE: Content.ContentType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    RTF_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    TOOL_USE_FIELD_NUMBER: _ClassVar[int]
    type: Content.ContentType
    code: CodeContent
    rtf: RichContent
    media: MediaContent
    text: TextContent
    error: ErrorContent
    file: FileContent
    tool_use: ToolUse
    def __init__(
        self,
        type: _Optional[_Union[Content.ContentType, str]] = ...,
        code: _Optional[_Union[CodeContent, _Mapping]] = ...,
        rtf: _Optional[_Union[RichContent, _Mapping]] = ...,
        media: _Optional[_Union[MediaContent, _Mapping]] = ...,
        text: _Optional[_Union[TextContent, _Mapping]] = ...,
        error: _Optional[_Union[ErrorContent, _Mapping]] = ...,
        file: _Optional[_Union[FileContent, _Mapping]] = ...,
        tool_use: _Optional[_Union[ToolUse, _Mapping]] = ...,
    ) -> None: ...
