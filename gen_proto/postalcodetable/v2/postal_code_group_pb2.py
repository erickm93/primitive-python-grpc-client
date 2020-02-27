# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: postalcodetable/v2/postal_code_group.proto

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
from postalcodetable.v2 import service_type_group_info_pb2 as postalcodetable_dot_v2_dot_service__type__group__info__pb2
from postalcodetable.v2 import last_mile_company_group_info_pb2 as postalcodetable_dot_v2_dot_last__mile__company__group__info__pb2
from postalcodetable.v2 import postal_code_info_pb2 as postalcodetable_dot_v2_dot_postal__code__info__pb2
from postalcodetable.v2 import pricing_region_group_info_pb2 as postalcodetable_dot_v2_dot_pricing__region__group__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='postalcodetable/v2/postal_code_group.proto',
  package='loggi.postalcodetable.v2',
  syntax='proto3',
  serialized_options=_b('\n\034com.loggi.postalcodetable.v2B\024PostalCodeGroupProtoP\001Z\021postalcodetablev2\242\002\003LPX\252\002\030Loggi.Postalcodetable.V2\312\002\030Loggi\\Postalcodetable\\V2'),
  serialized_pb=_b('\n*postalcodetable/v2/postal_code_group.proto\x12\x18loggi.postalcodetable.v2\x1a\x1epostalcodetable/v2/mongo.proto\x1a\x30postalcodetable/v2/service_type_group_info.proto\x1a\x35postalcodetable/v2/last_mile_company_group_info.proto\x1a)postalcodetable/v2/postal_code_info.proto\x1a\x32postalcodetable/v2/pricing_region_group_info.proto\"\x1a\n\nPostalCode\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"|\n\x0bPostalCodes\x12\x32\n\x04list\x18\x01 \x03(\x0b\x32$.loggi.postalcodetable.v2.PostalCode\x12\x39\n\x06ranges\x18\x02 \x03(\x0b\x32).loggi.postalcodetable.v2.PostalCodeRange\"\x88\x02\n\x0fPostalCodeRange\x12\n\n\x02id\x18\x01 \x01(\t\x12\x33\n\x05start\x18\x02 \x01(\x0b\x32$.loggi.postalcodetable.v2.PostalCode\x12\x31\n\x03\x65nd\x18\x03 \x01(\x0b\x32$.loggi.postalcodetable.v2.PostalCode\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x37\n\x05types\x18\x05 \x03(\x0e\x32(.loggi.postalcodetable.v2.PostalCodeType\x12:\n\x0cpostal_codes\x18\x06 \x03(\x0b\x32$.loggi.postalcodetable.v2.PostalCode\"\xc3\x03\n\x0fPostalCodeGroup\x12\x34\n\x02id\x18\x01 \x01(\x0b\x32#.loggi.postalcodetable.v2.MongoDBIdR\x03_id\x12;\n\x04type\x18\x02 \x01(\x0e\x32-.loggi.postalcodetable.v2.PostalCodeGroupType\x12;\n\x0cpostal_codes\x18\x03 \x01(\x0b\x32%.loggi.postalcodetable.v2.PostalCodes\x12K\n\x11service_type_info\x18\x04 \x01(\x0b\x32..loggi.postalcodetable.v2.ServiceTypeGroupInfoH\x00\x12T\n\x16last_mile_company_info\x18\x05 \x01(\x0b\x32\x32.loggi.postalcodetable.v2.LastMileCompanyGroupInfoH\x00\x12O\n\x13pricing_region_info\x18\x06 \x01(\x0b\x32\x30.loggi.postalcodetable.v2.PricingRegionGroupInfoH\x00\x42\x0c\n\ngroup_info\"\xe6\x02\n\x1fListPostalCodeGroupInfosElement\x12\x34\n\x02id\x18\x01 \x01(\x0b\x32#.loggi.postalcodetable.v2.MongoDBIdR\x03_id\x12\x0c\n\x04name\x18\x02 \x01(\t\x12K\n\x11service_type_info\x18\x03 \x01(\x0b\x32..loggi.postalcodetable.v2.ServiceTypeGroupInfoH\x00\x12T\n\x16last_mile_company_info\x18\x04 \x01(\x0b\x32\x32.loggi.postalcodetable.v2.LastMileCompanyGroupInfoH\x00\x12N\n\x12pricing_group_info\x18\x05 \x01(\x0b\x32\x30.loggi.postalcodetable.v2.PricingRegionGroupInfoH\x00\x42\x0c\n\ngroup_info*\xbb\x01\n\x13PostalCodeGroupType\x12\"\n\x1ePOSTAL_CODE_GROUP_TYPE_INVALID\x10\x00\x12\'\n#POSTAL_CODE_GROUP_TYPE_SERVICE_TYPE\x10\x01\x12,\n(POSTAL_CODE_GROUP_TYPE_LAST_MILE_COMPANY\x10\x02\x12)\n%POSTAL_CODE_GROUP_TYPE_PRICING_REGION\x10\x03\x42\x85\x01\n\x1c\x63om.loggi.postalcodetable.v2B\x14PostalCodeGroupProtoP\x01Z\x11postalcodetablev2\xa2\x02\x03LPX\xaa\x02\x18Loggi.Postalcodetable.V2\xca\x02\x18Loggi\\Postalcodetable\\V2b\x06proto3')
  ,
  dependencies=[postalcodetable_dot_v2_dot_mongo__pb2.DESCRIPTOR,postalcodetable_dot_v2_dot_service__type__group__info__pb2.DESCRIPTOR,postalcodetable_dot_v2_dot_last__mile__company__group__info__pb2.DESCRIPTOR,postalcodetable_dot_v2_dot_postal__code__info__pb2.DESCRIPTOR,postalcodetable_dot_v2_dot_pricing__region__group__info__pb2.DESCRIPTOR,])

_POSTALCODEGROUPTYPE = _descriptor.EnumDescriptor(
  name='PostalCodeGroupType',
  full_name='loggi.postalcodetable.v2.PostalCodeGroupType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE_GROUP_TYPE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE_GROUP_TYPE_SERVICE_TYPE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE_GROUP_TYPE_LAST_MILE_COMPANY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE_GROUP_TYPE_PRICING_REGION', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1541,
  serialized_end=1728,
)
_sym_db.RegisterEnumDescriptor(_POSTALCODEGROUPTYPE)

PostalCodeGroupType = enum_type_wrapper.EnumTypeWrapper(_POSTALCODEGROUPTYPE)
POSTAL_CODE_GROUP_TYPE_INVALID = 0
POSTAL_CODE_GROUP_TYPE_SERVICE_TYPE = 1
POSTAL_CODE_GROUP_TYPE_LAST_MILE_COMPANY = 2
POSTAL_CODE_GROUP_TYPE_PRICING_REGION = 3



_POSTALCODE = _descriptor.Descriptor(
  name='PostalCode',
  full_name='loggi.postalcodetable.v2.PostalCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='loggi.postalcodetable.v2.PostalCode.code', index=0,
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
  serialized_start=304,
  serialized_end=330,
)


_POSTALCODES = _descriptor.Descriptor(
  name='PostalCodes',
  full_name='loggi.postalcodetable.v2.PostalCodes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='loggi.postalcodetable.v2.PostalCodes.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ranges', full_name='loggi.postalcodetable.v2.PostalCodes.ranges', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=332,
  serialized_end=456,
)


_POSTALCODERANGE = _descriptor.Descriptor(
  name='PostalCodeRange',
  full_name='loggi.postalcodetable.v2.PostalCodeRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='loggi.postalcodetable.v2.PostalCodeRange.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='loggi.postalcodetable.v2.PostalCodeRange.start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='loggi.postalcodetable.v2.PostalCodeRange.end', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='loggi.postalcodetable.v2.PostalCodeRange.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='types', full_name='loggi.postalcodetable.v2.PostalCodeRange.types', index=4,
      number=5, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postal_codes', full_name='loggi.postalcodetable.v2.PostalCodeRange.postal_codes', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=459,
  serialized_end=723,
)


_POSTALCODEGROUP = _descriptor.Descriptor(
  name='PostalCodeGroup',
  full_name='loggi.postalcodetable.v2.PostalCodeGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='loggi.postalcodetable.v2.PostalCodeGroup.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='_id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='loggi.postalcodetable.v2.PostalCodeGroup.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postal_codes', full_name='loggi.postalcodetable.v2.PostalCodeGroup.postal_codes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_type_info', full_name='loggi.postalcodetable.v2.PostalCodeGroup.service_type_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_mile_company_info', full_name='loggi.postalcodetable.v2.PostalCodeGroup.last_mile_company_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pricing_region_info', full_name='loggi.postalcodetable.v2.PostalCodeGroup.pricing_region_info', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='group_info', full_name='loggi.postalcodetable.v2.PostalCodeGroup.group_info',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=726,
  serialized_end=1177,
)


_LISTPOSTALCODEGROUPINFOSELEMENT = _descriptor.Descriptor(
  name='ListPostalCodeGroupInfosElement',
  full_name='loggi.postalcodetable.v2.ListPostalCodeGroupInfosElement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='loggi.postalcodetable.v2.ListPostalCodeGroupInfosElement.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='_id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='loggi.postalcodetable.v2.ListPostalCodeGroupInfosElement.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_type_info', full_name='loggi.postalcodetable.v2.ListPostalCodeGroupInfosElement.service_type_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_mile_company_info', full_name='loggi.postalcodetable.v2.ListPostalCodeGroupInfosElement.last_mile_company_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pricing_group_info', full_name='loggi.postalcodetable.v2.ListPostalCodeGroupInfosElement.pricing_group_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='group_info', full_name='loggi.postalcodetable.v2.ListPostalCodeGroupInfosElement.group_info',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1180,
  serialized_end=1538,
)

_POSTALCODES.fields_by_name['list'].message_type = _POSTALCODE
_POSTALCODES.fields_by_name['ranges'].message_type = _POSTALCODERANGE
_POSTALCODERANGE.fields_by_name['start'].message_type = _POSTALCODE
_POSTALCODERANGE.fields_by_name['end'].message_type = _POSTALCODE
_POSTALCODERANGE.fields_by_name['types'].enum_type = postalcodetable_dot_v2_dot_postal__code__info__pb2._POSTALCODETYPE
_POSTALCODERANGE.fields_by_name['postal_codes'].message_type = _POSTALCODE
_POSTALCODEGROUP.fields_by_name['id'].message_type = postalcodetable_dot_v2_dot_mongo__pb2._MONGODBID
_POSTALCODEGROUP.fields_by_name['type'].enum_type = _POSTALCODEGROUPTYPE
_POSTALCODEGROUP.fields_by_name['postal_codes'].message_type = _POSTALCODES
_POSTALCODEGROUP.fields_by_name['service_type_info'].message_type = postalcodetable_dot_v2_dot_service__type__group__info__pb2._SERVICETYPEGROUPINFO
_POSTALCODEGROUP.fields_by_name['last_mile_company_info'].message_type = postalcodetable_dot_v2_dot_last__mile__company__group__info__pb2._LASTMILECOMPANYGROUPINFO
_POSTALCODEGROUP.fields_by_name['pricing_region_info'].message_type = postalcodetable_dot_v2_dot_pricing__region__group__info__pb2._PRICINGREGIONGROUPINFO
_POSTALCODEGROUP.oneofs_by_name['group_info'].fields.append(
  _POSTALCODEGROUP.fields_by_name['service_type_info'])
_POSTALCODEGROUP.fields_by_name['service_type_info'].containing_oneof = _POSTALCODEGROUP.oneofs_by_name['group_info']
_POSTALCODEGROUP.oneofs_by_name['group_info'].fields.append(
  _POSTALCODEGROUP.fields_by_name['last_mile_company_info'])
_POSTALCODEGROUP.fields_by_name['last_mile_company_info'].containing_oneof = _POSTALCODEGROUP.oneofs_by_name['group_info']
_POSTALCODEGROUP.oneofs_by_name['group_info'].fields.append(
  _POSTALCODEGROUP.fields_by_name['pricing_region_info'])
_POSTALCODEGROUP.fields_by_name['pricing_region_info'].containing_oneof = _POSTALCODEGROUP.oneofs_by_name['group_info']
_LISTPOSTALCODEGROUPINFOSELEMENT.fields_by_name['id'].message_type = postalcodetable_dot_v2_dot_mongo__pb2._MONGODBID
_LISTPOSTALCODEGROUPINFOSELEMENT.fields_by_name['service_type_info'].message_type = postalcodetable_dot_v2_dot_service__type__group__info__pb2._SERVICETYPEGROUPINFO
_LISTPOSTALCODEGROUPINFOSELEMENT.fields_by_name['last_mile_company_info'].message_type = postalcodetable_dot_v2_dot_last__mile__company__group__info__pb2._LASTMILECOMPANYGROUPINFO
_LISTPOSTALCODEGROUPINFOSELEMENT.fields_by_name['pricing_group_info'].message_type = postalcodetable_dot_v2_dot_pricing__region__group__info__pb2._PRICINGREGIONGROUPINFO
_LISTPOSTALCODEGROUPINFOSELEMENT.oneofs_by_name['group_info'].fields.append(
  _LISTPOSTALCODEGROUPINFOSELEMENT.fields_by_name['service_type_info'])
_LISTPOSTALCODEGROUPINFOSELEMENT.fields_by_name['service_type_info'].containing_oneof = _LISTPOSTALCODEGROUPINFOSELEMENT.oneofs_by_name['group_info']
_LISTPOSTALCODEGROUPINFOSELEMENT.oneofs_by_name['group_info'].fields.append(
  _LISTPOSTALCODEGROUPINFOSELEMENT.fields_by_name['last_mile_company_info'])
_LISTPOSTALCODEGROUPINFOSELEMENT.fields_by_name['last_mile_company_info'].containing_oneof = _LISTPOSTALCODEGROUPINFOSELEMENT.oneofs_by_name['group_info']
_LISTPOSTALCODEGROUPINFOSELEMENT.oneofs_by_name['group_info'].fields.append(
  _LISTPOSTALCODEGROUPINFOSELEMENT.fields_by_name['pricing_group_info'])
_LISTPOSTALCODEGROUPINFOSELEMENT.fields_by_name['pricing_group_info'].containing_oneof = _LISTPOSTALCODEGROUPINFOSELEMENT.oneofs_by_name['group_info']
DESCRIPTOR.message_types_by_name['PostalCode'] = _POSTALCODE
DESCRIPTOR.message_types_by_name['PostalCodes'] = _POSTALCODES
DESCRIPTOR.message_types_by_name['PostalCodeRange'] = _POSTALCODERANGE
DESCRIPTOR.message_types_by_name['PostalCodeGroup'] = _POSTALCODEGROUP
DESCRIPTOR.message_types_by_name['ListPostalCodeGroupInfosElement'] = _LISTPOSTALCODEGROUPINFOSELEMENT
DESCRIPTOR.enum_types_by_name['PostalCodeGroupType'] = _POSTALCODEGROUPTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostalCode = _reflection.GeneratedProtocolMessageType('PostalCode', (_message.Message,), {
  'DESCRIPTOR' : _POSTALCODE,
  '__module__' : 'postalcodetable.v2.postal_code_group_pb2'
  # @@protoc_insertion_point(class_scope:loggi.postalcodetable.v2.PostalCode)
  })
_sym_db.RegisterMessage(PostalCode)

PostalCodes = _reflection.GeneratedProtocolMessageType('PostalCodes', (_message.Message,), {
  'DESCRIPTOR' : _POSTALCODES,
  '__module__' : 'postalcodetable.v2.postal_code_group_pb2'
  # @@protoc_insertion_point(class_scope:loggi.postalcodetable.v2.PostalCodes)
  })
_sym_db.RegisterMessage(PostalCodes)

PostalCodeRange = _reflection.GeneratedProtocolMessageType('PostalCodeRange', (_message.Message,), {
  'DESCRIPTOR' : _POSTALCODERANGE,
  '__module__' : 'postalcodetable.v2.postal_code_group_pb2'
  # @@protoc_insertion_point(class_scope:loggi.postalcodetable.v2.PostalCodeRange)
  })
_sym_db.RegisterMessage(PostalCodeRange)

PostalCodeGroup = _reflection.GeneratedProtocolMessageType('PostalCodeGroup', (_message.Message,), {
  'DESCRIPTOR' : _POSTALCODEGROUP,
  '__module__' : 'postalcodetable.v2.postal_code_group_pb2'
  # @@protoc_insertion_point(class_scope:loggi.postalcodetable.v2.PostalCodeGroup)
  })
_sym_db.RegisterMessage(PostalCodeGroup)

ListPostalCodeGroupInfosElement = _reflection.GeneratedProtocolMessageType('ListPostalCodeGroupInfosElement', (_message.Message,), {
  'DESCRIPTOR' : _LISTPOSTALCODEGROUPINFOSELEMENT,
  '__module__' : 'postalcodetable.v2.postal_code_group_pb2'
  # @@protoc_insertion_point(class_scope:loggi.postalcodetable.v2.ListPostalCodeGroupInfosElement)
  })
_sym_db.RegisterMessage(ListPostalCodeGroupInfosElement)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
