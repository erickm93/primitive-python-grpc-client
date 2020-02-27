# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: postalcodetable/v2/postal_code_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from postalcodetable.v2 import mongo_pb2 as postalcodetable_dot_v2_dot_mongo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='postalcodetable/v2/postal_code_info.proto',
  package='loggi.postalcodetable.v2',
  syntax='proto3',
  serialized_options=_b('\n\034com.loggi.postalcodetable.v2B\023PostalCodeInfoProtoP\001Z\021postalcodetablev2\242\002\003LPX\252\002\030Loggi.Postalcodetable.V2\312\002\030Loggi\\Postalcodetable\\V2'),
  serialized_pb=_b('\n)postalcodetable/v2/postal_code_info.proto\x12\x18loggi.postalcodetable.v2\x1a\x1epostalcodetable/v2/mongo.proto\"\xc1\x01\n\x0ePostalCodeInfo\x12\x34\n\x02id\x18\x01 \x01(\x0b\x32#.loggi.postalcodetable.v2.MongoDBIdR\x03_id\x12\x13\n\x0bpostal_code\x18\x02 \x01(\t\x12,\n\x04info\x18\x03 \x01(\x0b\x32\x1e.loggi.postalcodetable.v2.Info\x12\x36\n\x04type\x18\x04 \x01(\x0e\x32(.loggi.postalcodetable.v2.PostalCodeType\"\x80\x01\n\x04Info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x14\n\x0cneighborhood\x18\x03 \x01(\t\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x12\n\nstate_enum\x18\x06 \x01(\t\x12\x11\n\tcity_enum\x18\x07 \x01(\t*\xdb\x01\n\x0ePostalCodeType\x12\x1c\n\x18POSTAL_CODE_TYPE_INVALID\x10\x00\x12\x1c\n\x18POSTAL_CODE_TYPE_ADDRESS\x10\x01\x12\x1d\n\x19POSTAL_CODE_TYPE_LOCALITY\x10\x02\x12\x1e\n\x1aPOSTAL_CODE_TYPE_HUGE_USER\x10\x03\x12&\n\"POSTAL_CODE_TYPE_COMMUNITY_MAILBOX\x10\x04\x12&\n\"POSTAL_CODE_TYPE_OPERATIONAL_UNITY\x10\x05\x42\x84\x01\n\x1c\x63om.loggi.postalcodetable.v2B\x13PostalCodeInfoProtoP\x01Z\x11postalcodetablev2\xa2\x02\x03LPX\xaa\x02\x18Loggi.Postalcodetable.V2\xca\x02\x18Loggi\\Postalcodetable\\V2b\x06proto3')
  ,
  dependencies=[postalcodetable_dot_v2_dot_mongo__pb2.DESCRIPTOR,])

_POSTALCODETYPE = _descriptor.EnumDescriptor(
  name='PostalCodeType',
  full_name='loggi.postalcodetable.v2.PostalCodeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE_TYPE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE_TYPE_ADDRESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE_TYPE_LOCALITY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE_TYPE_HUGE_USER', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE_TYPE_COMMUNITY_MAILBOX', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE_TYPE_OPERATIONAL_UNITY', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=431,
  serialized_end=650,
)
_sym_db.RegisterEnumDescriptor(_POSTALCODETYPE)

PostalCodeType = enum_type_wrapper.EnumTypeWrapper(_POSTALCODETYPE)
POSTAL_CODE_TYPE_INVALID = 0
POSTAL_CODE_TYPE_ADDRESS = 1
POSTAL_CODE_TYPE_LOCALITY = 2
POSTAL_CODE_TYPE_HUGE_USER = 3
POSTAL_CODE_TYPE_COMMUNITY_MAILBOX = 4
POSTAL_CODE_TYPE_OPERATIONAL_UNITY = 5



_POSTALCODEINFO = _descriptor.Descriptor(
  name='PostalCodeInfo',
  full_name='loggi.postalcodetable.v2.PostalCodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='loggi.postalcodetable.v2.PostalCodeInfo.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='_id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postal_code', full_name='loggi.postalcodetable.v2.PostalCodeInfo.postal_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='loggi.postalcodetable.v2.PostalCodeInfo.info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='loggi.postalcodetable.v2.PostalCodeInfo.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=104,
  serialized_end=297,
)


_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='loggi.postalcodetable.v2.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='loggi.postalcodetable.v2.Info.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='loggi.postalcodetable.v2.Info.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='neighborhood', full_name='loggi.postalcodetable.v2.Info.neighborhood', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='city', full_name='loggi.postalcodetable.v2.Info.city', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='loggi.postalcodetable.v2.Info.state', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_enum', full_name='loggi.postalcodetable.v2.Info.state_enum', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='city_enum', full_name='loggi.postalcodetable.v2.Info.city_enum', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=300,
  serialized_end=428,
)

_POSTALCODEINFO.fields_by_name['id'].message_type = postalcodetable_dot_v2_dot_mongo__pb2._MONGODBID
_POSTALCODEINFO.fields_by_name['info'].message_type = _INFO
_POSTALCODEINFO.fields_by_name['type'].enum_type = _POSTALCODETYPE
DESCRIPTOR.message_types_by_name['PostalCodeInfo'] = _POSTALCODEINFO
DESCRIPTOR.message_types_by_name['Info'] = _INFO
DESCRIPTOR.enum_types_by_name['PostalCodeType'] = _POSTALCODETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostalCodeInfo = _reflection.GeneratedProtocolMessageType('PostalCodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _POSTALCODEINFO,
  '__module__' : 'postalcodetable.v2.postal_code_info_pb2'
  # @@protoc_insertion_point(class_scope:loggi.postalcodetable.v2.PostalCodeInfo)
  })
_sym_db.RegisterMessage(PostalCodeInfo)

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), {
  'DESCRIPTOR' : _INFO,
  '__module__' : 'postalcodetable.v2.postal_code_info_pb2'
  # @@protoc_insertion_point(class_scope:loggi.postalcodetable.v2.Info)
  })
_sym_db.RegisterMessage(Info)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
