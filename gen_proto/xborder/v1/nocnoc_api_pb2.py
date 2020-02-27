# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xborder/v1/nocnoc_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from xborder.v1 import nocnoc_pb2 as xborder_dot_v1_dot_nocnoc__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='xborder/v1/nocnoc_api.proto',
  package='loggi.xborder.nocnoc.v1',
  syntax='proto3',
  serialized_options=_b('\n\033com.loggi.xborder.nocnoc.v1B\016NocnocApiProtoP\001Z\010nocnocv1\242\002\003LXN\252\002\027Loggi.Xborder.Nocnoc.V1\312\002\027Loggi\\Xborder\\Nocnoc\\V1'),
  serialized_pb=_b('\n\x1bxborder/v1/nocnoc_api.proto\x12\x17loggi.xborder.nocnoc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17xborder/v1/nocnoc.proto\"\xb1\x02\n\x19NocnocUpdateStatusRequest\x12\x12\n\npackage_id\x18\x01 \x01(\x03\x12\n\n\x02id\x18\x02 \x01(\x03\x12 \n\x0btracking_id\x18\x03 \x01(\tR\x0btracking_id\x12\x36\n\x16\x65stimated_time_arrival\x18\x04 \x01(\tR\x16\x65stimated_time_arrival\x12\x33\n\x06status\x18\x05 \x01(\x0e\x32#.loggi.xborder.nocnoc.v1.StatusEnum\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x07 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x08 \x01(\t\x12\x31\n\x08historic\x18\t \x03(\x0b\x32\x1f.loggi.xborder.nocnoc.v1.Status\"7\n\x1aNocnocUpdateStatusResponse\x12\x0f\n\x05\x65rror\x18\x01 \x01(\tH\x00\x42\x08\n\x06option2\xbd\x01\n\tNocnocAPI\x12\xaf\x01\n\x12NocnocUpdateStatus\x12\x32.loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest\x1a\x33.loggi.xborder.nocnoc.v1.NocnocUpdateStatusResponse\"0\x82\xd3\xe4\x93\x02*\"%/v1/nocnoc/update-status/{package_id}:\x01*Bs\n\x1b\x63om.loggi.xborder.nocnoc.v1B\x0eNocnocApiProtoP\x01Z\x08nocnocv1\xa2\x02\x03LXN\xaa\x02\x17Loggi.Xborder.Nocnoc.V1\xca\x02\x17Loggi\\Xborder\\Nocnoc\\V1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,xborder_dot_v1_dot_nocnoc__pb2.DESCRIPTOR,])




_NOCNOCUPDATESTATUSREQUEST = _descriptor.Descriptor(
  name='NocnocUpdateStatusRequest',
  full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_id', full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest.package_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tracking_id', full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest.tracking_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tracking_id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='estimated_time_arrival', full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest.estimated_time_arrival', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='estimated_time_arrival', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest.date', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country', full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest.country', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='historic', full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest.historic', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=417,
)


_NOCNOCUPDATESTATUSRESPONSE = _descriptor.Descriptor(
  name='NocnocUpdateStatusResponse',
  full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusResponse.error', index=0,
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
    _descriptor.OneofDescriptor(
      name='option', full_name='loggi.xborder.nocnoc.v1.NocnocUpdateStatusResponse.option',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=419,
  serialized_end=474,
)

_NOCNOCUPDATESTATUSREQUEST.fields_by_name['status'].enum_type = xborder_dot_v1_dot_nocnoc__pb2._STATUSENUM
_NOCNOCUPDATESTATUSREQUEST.fields_by_name['historic'].message_type = xborder_dot_v1_dot_nocnoc__pb2._STATUS
_NOCNOCUPDATESTATUSRESPONSE.oneofs_by_name['option'].fields.append(
  _NOCNOCUPDATESTATUSRESPONSE.fields_by_name['error'])
_NOCNOCUPDATESTATUSRESPONSE.fields_by_name['error'].containing_oneof = _NOCNOCUPDATESTATUSRESPONSE.oneofs_by_name['option']
DESCRIPTOR.message_types_by_name['NocnocUpdateStatusRequest'] = _NOCNOCUPDATESTATUSREQUEST
DESCRIPTOR.message_types_by_name['NocnocUpdateStatusResponse'] = _NOCNOCUPDATESTATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NocnocUpdateStatusRequest = _reflection.GeneratedProtocolMessageType('NocnocUpdateStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _NOCNOCUPDATESTATUSREQUEST,
  '__module__' : 'xborder.v1.nocnoc_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.xborder.nocnoc.v1.NocnocUpdateStatusRequest)
  })
_sym_db.RegisterMessage(NocnocUpdateStatusRequest)

NocnocUpdateStatusResponse = _reflection.GeneratedProtocolMessageType('NocnocUpdateStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _NOCNOCUPDATESTATUSRESPONSE,
  '__module__' : 'xborder.v1.nocnoc_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.xborder.nocnoc.v1.NocnocUpdateStatusResponse)
  })
_sym_db.RegisterMessage(NocnocUpdateStatusResponse)


DESCRIPTOR._options = None

_NOCNOCAPI = _descriptor.ServiceDescriptor(
  name='NocnocAPI',
  full_name='loggi.xborder.nocnoc.v1.NocnocAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=477,
  serialized_end=666,
  methods=[
  _descriptor.MethodDescriptor(
    name='NocnocUpdateStatus',
    full_name='loggi.xborder.nocnoc.v1.NocnocAPI.NocnocUpdateStatus',
    index=0,
    containing_service=None,
    input_type=_NOCNOCUPDATESTATUSREQUEST,
    output_type=_NOCNOCUPDATESTATUSRESPONSE,
    serialized_options=_b('\202\323\344\223\002*\"%/v1/nocnoc/update-status/{package_id}:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_NOCNOCAPI)

DESCRIPTOR.services_by_name['NocnocAPI'] = _NOCNOCAPI

# @@protoc_insertion_point(module_scope)