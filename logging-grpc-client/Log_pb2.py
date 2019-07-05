# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Log.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\010Messages'),
  serialized_pb=_b('\n\tLog.proto\"9\n\nLogMessage\x12\x0c\n\x04guid\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"&\n\nLogRequest\x12\x18\n\x03log\x18\x01 \x01(\x0b\x32\x0b.LogMessage\"\x1b\n\x0bLogResponse\x12\x0c\n\x04guid\x18\x01 \x01(\t\"\x1d\n\rGetLogRequest\x12\x0c\n\x04guid\x18\x01 \x01(\t\"*\n\x0eGetLogResponse\x12\x18\n\x03log\x18\x01 \x01(\x0b\x32\x0b.LogMessage2Y\n\nLogService\x12 \n\x03Log\x12\x0b.LogRequest\x1a\x0c.LogResponse\x12)\n\x06GetLog\x12\x0e.GetLogRequest\x1a\x0f.GetLogResponseB\x0b\xaa\x02\x08Messagesb\x06proto3')
)




_LOGMESSAGE = _descriptor.Descriptor(
  name='LogMessage',
  full_name='LogMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='guid', full_name='LogMessage.guid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='LogMessage.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='LogMessage.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=70,
)


_LOGREQUEST = _descriptor.Descriptor(
  name='LogRequest',
  full_name='LogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log', full_name='LogRequest.log', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=110,
)


_LOGRESPONSE = _descriptor.Descriptor(
  name='LogResponse',
  full_name='LogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='guid', full_name='LogResponse.guid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=139,
)


_GETLOGREQUEST = _descriptor.Descriptor(
  name='GetLogRequest',
  full_name='GetLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='guid', full_name='GetLogRequest.guid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=170,
)


_GETLOGRESPONSE = _descriptor.Descriptor(
  name='GetLogResponse',
  full_name='GetLogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log', full_name='GetLogResponse.log', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=214,
)

_LOGREQUEST.fields_by_name['log'].message_type = _LOGMESSAGE
_GETLOGRESPONSE.fields_by_name['log'].message_type = _LOGMESSAGE
DESCRIPTOR.message_types_by_name['LogMessage'] = _LOGMESSAGE
DESCRIPTOR.message_types_by_name['LogRequest'] = _LOGREQUEST
DESCRIPTOR.message_types_by_name['LogResponse'] = _LOGRESPONSE
DESCRIPTOR.message_types_by_name['GetLogRequest'] = _GETLOGREQUEST
DESCRIPTOR.message_types_by_name['GetLogResponse'] = _GETLOGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogMessage = _reflection.GeneratedProtocolMessageType('LogMessage', (_message.Message,), dict(
  DESCRIPTOR = _LOGMESSAGE,
  __module__ = 'Log_pb2'
  # @@protoc_insertion_point(class_scope:LogMessage)
  ))
_sym_db.RegisterMessage(LogMessage)

LogRequest = _reflection.GeneratedProtocolMessageType('LogRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGREQUEST,
  __module__ = 'Log_pb2'
  # @@protoc_insertion_point(class_scope:LogRequest)
  ))
_sym_db.RegisterMessage(LogRequest)

LogResponse = _reflection.GeneratedProtocolMessageType('LogResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOGRESPONSE,
  __module__ = 'Log_pb2'
  # @@protoc_insertion_point(class_scope:LogResponse)
  ))
_sym_db.RegisterMessage(LogResponse)

GetLogRequest = _reflection.GeneratedProtocolMessageType('GetLogRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETLOGREQUEST,
  __module__ = 'Log_pb2'
  # @@protoc_insertion_point(class_scope:GetLogRequest)
  ))
_sym_db.RegisterMessage(GetLogRequest)

GetLogResponse = _reflection.GeneratedProtocolMessageType('GetLogResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETLOGRESPONSE,
  __module__ = 'Log_pb2'
  # @@protoc_insertion_point(class_scope:GetLogResponse)
  ))
_sym_db.RegisterMessage(GetLogResponse)


DESCRIPTOR._options = None

_LOGSERVICE = _descriptor.ServiceDescriptor(
  name='LogService',
  full_name='LogService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=216,
  serialized_end=305,
  methods=[
  _descriptor.MethodDescriptor(
    name='Log',
    full_name='LogService.Log',
    index=0,
    containing_service=None,
    input_type=_LOGREQUEST,
    output_type=_LOGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLog',
    full_name='LogService.GetLog',
    index=1,
    containing_service=None,
    input_type=_GETLOGREQUEST,
    output_type=_GETLOGRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGSERVICE)

DESCRIPTOR.services_by_name['LogService'] = _LOGSERVICE

# @@protoc_insertion_point(module_scope)
