# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: app.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'app.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import content_pb2 as content__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapp.proto\x12\x03\x61pp\x1a\rcontent.proto\"\xeb\x01\n\nAppRequest\x12\x30\n\x10generate_request\x18\x01 \x01(\x0b\x32\x14.app.GenerateRequestH\x00\x12(\n\x0cstop_request\x18\x02 \x01(\x0b\x32\x10.app.StopRequestH\x00\x12.\n\x0cuser_request\x18\x03 \x01(\x0b\x32\x16.app.UserPromptRequestH\x00\x12\"\n\x07message\x18\x04 \x01(\x0b\x32\x0f.app.AppMessageH\x00\x12\"\n\x05\x66inal\x18\x05 \x01(\x0b\x32\x11.app.FinalRequestH\x00\x42\t\n\x07request\"e\n\x13StreamingGeneration\x12\x32\n\x0c\x63ontent_type\x18\x01 \x01(\x0e\x32\x1c.truffle.Content.ContentType\x12\x1a\n\x12\x61\x64\x64itional_content\x18\x02 \x01(\t\"\xbd\x03\n\x0fGenerateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06prompt\x18\x02 \x01(\t\x12\x12\n\nmax_tokens\x18\x03 \x01(\x05\x12\x1e\n\x11\x66requency_penalty\x18\x04 \x01(\x02H\x00\x88\x01\x01\x12\x1d\n\x10presence_penalty\x18\x05 \x01(\x02H\x01\x88\x01\x01\x12\x18\n\x0btemperature\x18\x06 \x01(\x02H\x02\x88\x01\x01\x12\x12\n\x05top_p\x18\x07 \x01(\x02H\x03\x88\x01\x01\x12\x1c\n\x0fresponse_format\x18\x08 \x01(\tH\x04\x88\x01\x01\x12\x1c\n\x0fresponse_schema\x18\t \x01(\tH\x05\x88\x01\x01\x12\x19\n\x0cstop_strings\x18\n \x01(\tH\x06\x88\x01\x01\x12-\n\x06stream\x18\x0b \x01(\x0b\x32\x18.app.StreamingGenerationH\x07\x88\x01\x01\x42\x14\n\x12_frequency_penaltyB\x13\n\x11_presence_penaltyB\x0e\n\x0c_temperatureB\x08\n\x06_top_pB\x12\n\x10_response_formatB\x12\n\x10_response_schemaB\x0f\n\r_stop_stringsB\t\n\x07_stream\"D\n\x11UserPromptRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\">\n\nAppMessage\x12\r\n\x05title\x18\x01 \x01(\t\x12!\n\x07\x63ontent\x18\x02 \x01(\x0b\x32\x10.truffle.Content\"B\n\x0c\x46inalRequest\x12!\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\x10.truffle.Content\x12\x0f\n\x07metrics\x18\x02 \x01(\t\"\x19\n\x0bStopRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xa4\x01\n\x0b\x41ppResponse\x12\x30\n\x10initial_response\x18\x01 \x01(\x0b\x32\x14.app.InitialResponseH\x00\x12,\n\x0etoken_response\x18\x02 \x01(\x0b\x32\x12.app.TokenResponseH\x00\x12)\n\x0cuser_request\x18\x03 \x01(\x0b\x32\x11.app.UserResponseH\x00\x42\n\n\x08response\"/\n\x10GenerateResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"\x1f\n\x0fInitialResponse\x12\x0c\n\x04\x61rgs\x18\x01 \x01(\t\"\xcf\x02\n\rTokenResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12;\n\rfinish_reason\x18\x03 \x01(\x0e\x32\x1f.app.TokenResponse.FinishReasonH\x00\x88\x01\x01\x12,\n\x05usage\x18\x04 \x03(\x0b\x32\x1d.app.TokenResponse.UsageEntry\x1a,\n\nUsageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"x\n\x0c\x46inishReason\x12\x1d\n\x19\x46INISH_REASON_UNSPECIFIED\x10\x00\x12\x18\n\x14\x46INISH_REASON_LENGTH\x10\x01\x12\x16\n\x12\x46INISH_REASON_STOP\x10\x02\x12\x17\n\x13\x46INISH_REASON_ERROR\x10\x03\x42\x10\n\x0e_finish_reason\",\n\x0cUserResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08response\x18\x02 \x01(\tB\x0fZ\rcore/protobufb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\rcore/protobuf'
  _globals['_TOKENRESPONSE_USAGEENTRY']._loaded_options = None
  _globals['_TOKENRESPONSE_USAGEENTRY']._serialized_options = b'8\001'
  _globals['_APPREQUEST']._serialized_start=34
  _globals['_APPREQUEST']._serialized_end=269
  _globals['_STREAMINGGENERATION']._serialized_start=271
  _globals['_STREAMINGGENERATION']._serialized_end=372
  _globals['_GENERATEREQUEST']._serialized_start=375
  _globals['_GENERATEREQUEST']._serialized_end=820
  _globals['_USERPROMPTREQUEST']._serialized_start=822
  _globals['_USERPROMPTREQUEST']._serialized_end=890
  _globals['_APPMESSAGE']._serialized_start=892
  _globals['_APPMESSAGE']._serialized_end=954
  _globals['_FINALREQUEST']._serialized_start=956
  _globals['_FINALREQUEST']._serialized_end=1022
  _globals['_STOPREQUEST']._serialized_start=1024
  _globals['_STOPREQUEST']._serialized_end=1049
  _globals['_APPRESPONSE']._serialized_start=1052
  _globals['_APPRESPONSE']._serialized_end=1216
  _globals['_GENERATERESPONSE']._serialized_start=1218
  _globals['_GENERATERESPONSE']._serialized_end=1265
  _globals['_INITIALRESPONSE']._serialized_start=1267
  _globals['_INITIALRESPONSE']._serialized_end=1298
  _globals['_TOKENRESPONSE']._serialized_start=1301
  _globals['_TOKENRESPONSE']._serialized_end=1636
  _globals['_TOKENRESPONSE_USAGEENTRY']._serialized_start=1452
  _globals['_TOKENRESPONSE_USAGEENTRY']._serialized_end=1496
  _globals['_TOKENRESPONSE_FINISHREASON']._serialized_start=1498
  _globals['_TOKENRESPONSE_FINISHREASON']._serialized_end=1618
  _globals['_USERRESPONSE']._serialized_start=1638
  _globals['_USERRESPONSE']._serialized_end=1682
# @@protoc_insertion_point(module_scope)
