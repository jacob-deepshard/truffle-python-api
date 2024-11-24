from google.protobuf.internal import containers as _containers
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

class Metadata(_message.Message):
    __slots__ = ("version", "os")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    version: str
    os: str
    def __init__(self, version: _Optional[str] = ..., os: _Optional[str] = ...) -> None: ...

class Info(_message.Message):
    __slots__ = ("truffle_id", "metadata")
    TRUFFLE_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    truffle_id: str
    metadata: Metadata
    def __init__(
        self,
        truffle_id: _Optional[str] = ...,
        metadata: _Optional[_Union[Metadata, _Mapping]] = ...,
    ) -> None: ...

class FileUpload(_message.Message):
    __slots__ = ("filename", "prompt_id", "size_bytes", "urr_id")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    URR_ID_FIELD_NUMBER: _ClassVar[int]
    filename: str
    prompt_id: str
    size_bytes: int
    urr_id: str
    def __init__(
        self,
        filename: _Optional[str] = ...,
        prompt_id: _Optional[str] = ...,
        size_bytes: _Optional[int] = ...,
        urr_id: _Optional[str] = ...,
    ) -> None: ...

class Prompt(_message.Message):
    __slots__ = ("prompt_id", "message", "submitted", "file", "override_app")
    PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_APP_FIELD_NUMBER: _ClassVar[int]
    prompt_id: str
    message: str
    submitted: bool
    file: _containers.RepeatedCompositeFieldContainer[FileUpload]
    override_app: str
    def __init__(
        self,
        prompt_id: _Optional[str] = ...,
        message: _Optional[str] = ...,
        submitted: bool = ...,
        file: _Optional[_Iterable[_Union[FileUpload, _Mapping]]] = ...,
        override_app: _Optional[str] = ...,
    ) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ("prompt_id", "urr_id", "message", "file")
    PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    URR_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    prompt_id: str
    urr_id: str
    message: str
    file: _containers.RepeatedCompositeFieldContainer[FileUpload]
    def __init__(
        self,
        prompt_id: _Optional[str] = ...,
        urr_id: _Optional[str] = ...,
        message: _Optional[str] = ...,
        file: _Optional[_Iterable[_Union[FileUpload, _Mapping]]] = ...,
    ) -> None: ...

class StartSearch(_message.Message):
    __slots__ = ("search_id", "current_input")
    SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_INPUT_FIELD_NUMBER: _ClassVar[int]
    search_id: str
    current_input: str
    def __init__(
        self, search_id: _Optional[str] = ..., current_input: _Optional[str] = ...
    ) -> None: ...

class LoadPromptHistory(_message.Message):
    __slots__ = ("message_id", "prompt_id", "start_now")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    START_NOW_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    prompt_id: str
    start_now: bool
    def __init__(
        self,
        message_id: _Optional[str] = ...,
        prompt_id: _Optional[str] = ...,
        start_now: bool = ...,
    ) -> None: ...

class SetSettings(_message.Message):
    __slots__ = (
        "wifi_ssid",
        "wifi_pwd",
        "disable_leds",
        "get_settings",
        "truffle_name",
        "developer_mode",
        "get_apps",
    )
    WIFI_SSID_FIELD_NUMBER: _ClassVar[int]
    WIFI_PWD_FIELD_NUMBER: _ClassVar[int]
    DISABLE_LEDS_FIELD_NUMBER: _ClassVar[int]
    GET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TRUFFLE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_MODE_FIELD_NUMBER: _ClassVar[int]
    GET_APPS_FIELD_NUMBER: _ClassVar[int]
    wifi_ssid: str
    wifi_pwd: str
    disable_leds: bool
    get_settings: bool
    truffle_name: str
    developer_mode: bool
    get_apps: bool
    def __init__(
        self,
        wifi_ssid: _Optional[str] = ...,
        wifi_pwd: _Optional[str] = ...,
        disable_leds: bool = ...,
        get_settings: bool = ...,
        truffle_name: _Optional[str] = ...,
        developer_mode: bool = ...,
        get_apps: bool = ...,
    ) -> None: ...

class CancelPrompt(_message.Message):
    __slots__ = ("prompt_id", "pause")
    PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    PAUSE_FIELD_NUMBER: _ClassVar[int]
    prompt_id: str
    pause: bool
    def __init__(self, prompt_id: _Optional[str] = ..., pause: bool = ...) -> None: ...

class ClientMessage(_message.Message):
    __slots__ = ("info", "prompt", "user_response", "search", "settings", "cancel", "load")
    INFO_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    USER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    LOAD_FIELD_NUMBER: _ClassVar[int]
    info: Info
    prompt: Prompt
    user_response: UserResponse
    search: StartSearch
    settings: SetSettings
    cancel: CancelPrompt
    load: LoadPromptHistory
    def __init__(
        self,
        info: _Optional[_Union[Info, _Mapping]] = ...,
        prompt: _Optional[_Union[Prompt, _Mapping]] = ...,
        user_response: _Optional[_Union[UserResponse, _Mapping]] = ...,
        search: _Optional[_Union[StartSearch, _Mapping]] = ...,
        settings: _Optional[_Union[SetSettings, _Mapping]] = ...,
        cancel: _Optional[_Union[CancelPrompt, _Mapping]] = ...,
        load: _Optional[_Union[LoadPromptHistory, _Mapping]] = ...,
    ) -> None: ...
