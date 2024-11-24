import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SystemInfo(_message.Message):
    __slots__ = ("wifi_ssid", "wifi_rssi", "led_color", "last_authenticated", "truffle_name", "developer_mode", "network_status", "available_apps")
    class NetworkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NET_DEFAULT: _ClassVar[SystemInfo.NetworkStatus]
        NET_NOT_CONNECTED: _ClassVar[SystemInfo.NetworkStatus]
        NET_NO_INTERNET: _ClassVar[SystemInfo.NetworkStatus]
        NET_CONNECTED: _ClassVar[SystemInfo.NetworkStatus]
    NET_DEFAULT: SystemInfo.NetworkStatus
    NET_NOT_CONNECTED: SystemInfo.NetworkStatus
    NET_NO_INTERNET: SystemInfo.NetworkStatus
    NET_CONNECTED: SystemInfo.NetworkStatus
    WIFI_SSID_FIELD_NUMBER: _ClassVar[int]
    WIFI_RSSI_FIELD_NUMBER: _ClassVar[int]
    LED_COLOR_FIELD_NUMBER: _ClassVar[int]
    LAST_AUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    TRUFFLE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_MODE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_STATUS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_APPS_FIELD_NUMBER: _ClassVar[int]
    wifi_ssid: str
    wifi_rssi: int
    led_color: int
    last_authenticated: int
    truffle_name: str
    developer_mode: bool
    network_status: SystemInfo.NetworkStatus
    available_apps: _containers.RepeatedCompositeFieldContainer[AppInfo]
    def __init__(self, wifi_ssid: _Optional[str] = ..., wifi_rssi: _Optional[int] = ..., led_color: _Optional[int] = ..., last_authenticated: _Optional[int] = ..., truffle_name: _Optional[str] = ..., developer_mode: bool = ..., network_status: _Optional[_Union[SystemInfo.NetworkStatus, str]] = ..., available_apps: _Optional[_Iterable[_Union[AppInfo, _Mapping]]] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ("search_id", "results")
    SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    search_id: str
    results: _containers.RepeatedCompositeFieldContainer[SearchResult]
    def __init__(self, search_id: _Optional[str] = ..., results: _Optional[_Iterable[_Union[SearchResult, _Mapping]]] = ...) -> None: ...

class AppInfo(_message.Message):
    __slots__ = ("app_icon_name", "app_name", "app_description", "third_party_app")
    APP_ICON_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_APP_FIELD_NUMBER: _ClassVar[int]
    app_icon_name: str
    app_name: str
    app_description: str
    third_party_app: bool
    def __init__(self, app_icon_name: _Optional[str] = ..., app_name: _Optional[str] = ..., app_description: _Optional[str] = ..., third_party_app: bool = ...) -> None: ...

class PromptClassification(_message.Message):
    __slots__ = ("prompt_id", "apps")
    PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    APPS_FIELD_NUMBER: _ClassVar[int]
    prompt_id: str
    apps: _containers.RepeatedCompositeFieldContainer[AppInfo]
    def __init__(self, prompt_id: _Optional[str] = ..., apps: _Optional[_Iterable[_Union[AppInfo, _Mapping]]] = ...) -> None: ...

class UserResponseRequest(_message.Message):
    __slots__ = ("prompt_id", "urr_id", "reason", "type")
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_REQUEST: _ClassVar[UserResponseRequest.RequestType]
        INLINE_REQUEST: _ClassVar[UserResponseRequest.RequestType]
    DEFAULT_REQUEST: UserResponseRequest.RequestType
    INLINE_REQUEST: UserResponseRequest.RequestType
    PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    URR_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    prompt_id: str
    urr_id: str
    reason: str
    type: UserResponseRequest.RequestType
    def __init__(self, prompt_id: _Optional[str] = ..., urr_id: _Optional[str] = ..., reason: _Optional[str] = ..., type: _Optional[_Union[UserResponseRequest.RequestType, str]] = ...) -> None: ...

class PromptInfo(_message.Message):
    __slots__ = ("status", "title", "subtitle", "type", "app_info")
    class PromptType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_DEFAULT: _ClassVar[PromptInfo.PromptType]
        TYPE_CHAT: _ClassVar[PromptInfo.PromptType]
        TYPE_TASK: _ClassVar[PromptInfo.PromptType]
        TYPE_BGTASK: _ClassVar[PromptInfo.PromptType]
        TYPE_OTHER: _ClassVar[PromptInfo.PromptType]
    TYPE_DEFAULT: PromptInfo.PromptType
    TYPE_CHAT: PromptInfo.PromptType
    TYPE_TASK: PromptInfo.PromptType
    TYPE_BGTASK: PromptInfo.PromptType
    TYPE_OTHER: PromptInfo.PromptType
    class PromptStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROMPT_STARTING: _ClassVar[PromptInfo.PromptStatus]
        PROMPT_LOADING_APP: _ClassVar[PromptInfo.PromptStatus]
        PROMPT_NEED_USER_RESPONSE: _ClassVar[PromptInfo.PromptStatus]
        PROMPT_IN_APP_ENVIROMENT: _ClassVar[PromptInfo.PromptStatus]
        PROMPT_ERROR: _ClassVar[PromptInfo.PromptStatus]
        PROMPT_UNAVAILABLE: _ClassVar[PromptInfo.PromptStatus]
        PROMPT_HAS_RESULTS: _ClassVar[PromptInfo.PromptStatus]
    PROMPT_STARTING: PromptInfo.PromptStatus
    PROMPT_LOADING_APP: PromptInfo.PromptStatus
    PROMPT_NEED_USER_RESPONSE: PromptInfo.PromptStatus
    PROMPT_IN_APP_ENVIROMENT: PromptInfo.PromptStatus
    PROMPT_ERROR: PromptInfo.PromptStatus
    PROMPT_UNAVAILABLE: PromptInfo.PromptStatus
    PROMPT_HAS_RESULTS: PromptInfo.PromptStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    APP_INFO_FIELD_NUMBER: _ClassVar[int]
    status: PromptInfo.PromptStatus
    title: str
    subtitle: str
    type: PromptInfo.PromptType
    app_info: AppInfo
    def __init__(self, status: _Optional[_Union[PromptInfo.PromptStatus, str]] = ..., title: _Optional[str] = ..., subtitle: _Optional[str] = ..., type: _Optional[_Union[PromptInfo.PromptType, str]] = ..., app_info: _Optional[_Union[AppInfo, _Mapping]] = ...) -> None: ...

class SearchResult(_message.Message):
    __slots__ = ("message_id", "content", "parent_prompt_id", "timestamp", "sent_by_user", "parent_prompt_info", "content_start_index", "content_end_index")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SENT_BY_USER_FIELD_NUMBER: _ClassVar[int]
    PARENT_PROMPT_INFO_FIELD_NUMBER: _ClassVar[int]
    CONTENT_START_INDEX_FIELD_NUMBER: _ClassVar[int]
    CONTENT_END_INDEX_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    content: str
    parent_prompt_id: str
    timestamp: str
    sent_by_user: bool
    parent_prompt_info: PromptInfo
    content_start_index: int
    content_end_index: int
    def __init__(self, message_id: _Optional[str] = ..., content: _Optional[str] = ..., parent_prompt_id: _Optional[str] = ..., timestamp: _Optional[str] = ..., sent_by_user: bool = ..., parent_prompt_info: _Optional[_Union[PromptInfo, _Mapping]] = ..., content_start_index: _Optional[int] = ..., content_end_index: _Optional[int] = ...) -> None: ...

class AttachedFile(_message.Message):
    __slots__ = ("filename", "file_url", "is_text", "expiry_time")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    IS_TEXT_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    file_url: str
    is_text: bool
    expiry_time: int
    def __init__(self, filename: _Optional[str] = ..., file_url: _Optional[str] = ..., is_text: bool = ..., expiry_time: _Optional[int] = ...) -> None: ...

class PromptEntry(_message.Message):
    __slots__ = ("message_id", "role", "content", "in_progress", "timestamp", "files", "root_message_id")
    class PromptEntryRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_UNKNOWN: _ClassVar[PromptEntry.PromptEntryRole]
        ROLE_USER: _ClassVar[PromptEntry.PromptEntryRole]
        ROLE_ASSISTANT: _ClassVar[PromptEntry.PromptEntryRole]
        ROLE_TOOL: _ClassVar[PromptEntry.PromptEntryRole]
    ROLE_UNKNOWN: PromptEntry.PromptEntryRole
    ROLE_USER: PromptEntry.PromptEntryRole
    ROLE_ASSISTANT: PromptEntry.PromptEntryRole
    ROLE_TOOL: PromptEntry.PromptEntryRole
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    ROOT_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    role: PromptEntry.PromptEntryRole
    content: _content_pb2.Content
    in_progress: bool
    timestamp: int
    files: _containers.RepeatedCompositeFieldContainer[AttachedFile]
    root_message_id: str
    def __init__(self, message_id: _Optional[str] = ..., role: _Optional[_Union[PromptEntry.PromptEntryRole, str]] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., in_progress: bool = ..., timestamp: _Optional[int] = ..., files: _Optional[_Iterable[_Union[AttachedFile, _Mapping]]] = ..., root_message_id: _Optional[str] = ...) -> None: ...

class PromptResponse(_message.Message):
    __slots__ = ("prompt_id", "info", "user_response_request", "messages", "jump_to_message_id")
    PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    USER_RESPONSE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    JUMP_TO_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    prompt_id: str
    info: PromptInfo
    user_response_request: UserResponseRequest
    messages: _containers.RepeatedCompositeFieldContainer[PromptEntry]
    jump_to_message_id: str
    def __init__(self, prompt_id: _Optional[str] = ..., info: _Optional[_Union[PromptInfo, _Mapping]] = ..., user_response_request: _Optional[_Union[UserResponseRequest, _Mapping]] = ..., messages: _Optional[_Iterable[_Union[PromptEntry, _Mapping]]] = ..., jump_to_message_id: _Optional[str] = ...) -> None: ...

class StreamingPromptEntry(_message.Message):
    __slots__ = ("prompt_id", "entry")
    PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    prompt_id: str
    entry: PromptEntry
    def __init__(self, prompt_id: _Optional[str] = ..., entry: _Optional[_Union[PromptEntry, _Mapping]] = ...) -> None: ...

class FirmwareError(_message.Message):
    __slots__ = ("error", "details", "errnum")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    ERRNUM_FIELD_NUMBER: _ClassVar[int]
    error: str
    details: str
    errnum: int
    def __init__(self, error: _Optional[str] = ..., details: _Optional[str] = ..., errnum: _Optional[int] = ...) -> None: ...

class DevModeCommand(_message.Message):
    __slots__ = ("prompt_id_to_load", "active_dev_app_name")
    PROMPT_ID_TO_LOAD_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DEV_APP_NAME_FIELD_NUMBER: _ClassVar[int]
    prompt_id_to_load: str
    active_dev_app_name: str
    def __init__(self, prompt_id_to_load: _Optional[str] = ..., active_dev_app_name: _Optional[str] = ...) -> None: ...

class FirmwareMessage(_message.Message):
    __slots__ = ("system_info", "response", "search", "stream", "error", "dev")
    SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    DEV_FIELD_NUMBER: _ClassVar[int]
    system_info: SystemInfo
    response: PromptResponse
    search: SearchResponse
    stream: StreamingPromptEntry
    error: FirmwareError
    dev: DevModeCommand
    def __init__(self, system_info: _Optional[_Union[SystemInfo, _Mapping]] = ..., response: _Optional[_Union[PromptResponse, _Mapping]] = ..., search: _Optional[_Union[SearchResponse, _Mapping]] = ..., stream: _Optional[_Union[StreamingPromptEntry, _Mapping]] = ..., error: _Optional[_Union[FirmwareError, _Mapping]] = ..., dev: _Optional[_Union[DevModeCommand, _Mapping]] = ..., **kwargs) -> None: ...
