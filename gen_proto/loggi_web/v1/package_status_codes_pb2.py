# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loggi_web/v1/package_status_codes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='loggi_web/v1/package_status_codes.proto',
  package='loggi.web.v1',
  syntax='proto3',
  serialized_options=_b('\n\020com.loggi.web.v1B\027PackageStatusCodesProtoP\001Z\005webv1\242\002\003LWX\252\002\014Loggi.Web.V1\312\002\014Loggi\\Web\\V1'),
  serialized_pb=_b('\n\'loggi_web/v1/package_status_codes.proto\x12\x0cloggi.web.v1\"R\n\x12PackageStatusCodes\x12<\n\x13package_status_code\x18\x01 \x01(\x0e\x32\x1f.loggi.web.v1.PackageStatusCode*\xa3\x15\n\x11PackageStatusCode\x12#\n\x1fPACKAGE_STATUS_CODE_UNAVAILABLE\x10\x00\x12!\n\x1dPACKAGE_STATUS_CODE_SCHEDULED\x10\x01\x12!\n\x1dPACKAGE_STATUS_CODE_DELIVERED\x10\x02\x12\x1e\n\x1aPACKAGE_STATUS_CODE_PICKUP\x10\x03\x12\'\n#PACKAGE_STATUS_CODE_GOING_TO_PICKUP\x10\x04\x12(\n$PACKAGE_STATUS_CODE_GOING_TO_DELIVER\x10\x05\x12(\n$PACKAGE_STATUS_CODE_GOING_TO_RESTOCK\x10\x06\x12\'\n#PACKAGE_STATUS_CODE_GOING_TO_RETURN\x10\x07\x12!\n\x1dPACKAGE_STATUS_CODE_RESTOCKED\x10\x08\x12 \n\x1cPACKAGE_STATUS_CODE_RETURNED\x10\t\x12)\n%PACKAGE_STATUS_CODE_RECIPIENT_REFUSED\x10\x0b\x12-\n)PACKAGE_STATUS_CODE_RECIPIENT_UNAVAILABLE\x10\x0c\x12+\n\'PACKAGE_STATUS_CODE_INVALID_DESTINATION\x10\r\x12\x1f\n\x1bPACKAGE_STATUS_CODE_DAMAGED\x10\x0e\x12\x1c\n\x18PACKAGE_STATUS_CODE_LOST\x10\x0f\x12\x1f\n\x1bPACKAGE_STATUS_CODE_FAILURE\x10\x10\x12!\n\x1dPACKAGE_STATUS_CODE_SUSPENDED\x10\x11\x12*\n&PACKAGE_STATUS_CODE_INVALID_DIMENSIONS\x10\x12\x12!\n\x1dPACKAGE_STATUS_CODE_NOT_FOUND\x10\x13\x12\x1e\n\x1aPACKAGE_STATUS_CODE_STOLEN\x10\x14\x12\x36\n2PACKAGE_STATUS_CODE_RECIPIENT_UNAVAILABLE_2ND_TIME\x10\x15\x12\x36\n2PACKAGE_STATUS_CODE_RECIPIENT_UNAVAILABLE_3RD_TIME\x10\x16\x12)\n%PACKAGE_STATUS_CODE_IMPAIRED_DELIVERY\x10\x17\x12(\n$PACKAGE_STATUS_CODE_GOING_TO_CONFIRM\x10\x18\x12(\n$PACKAGE_STATUS_CODE_GOING_TO_MEASURE\x10\x19\x12+\n\'PACKAGE_STATUS_CODE_REMOVED_FROM_CUTOFF\x10\x1a\x12,\n(PACKAGE_STATUS_CODE_MAX_RETRIES_EXCEEDED\x10\x1b\x12+\n\'PACKAGE_STATUS_CODE_AWAITING_RESOLUTION\x10\x1c\x12\'\n#PACKAGE_STATUS_CODE_READY_TO_RESEND\x10\x1d\x12\'\n#PACKAGE_STATUS_CODE_READY_TO_RETURN\x10\x1e\x12%\n!PACKAGE_STATUS_CODE_PICKUP_FAILED\x10\x1f\x12&\n\"PACKAGE_STATUS_CODE_RETURN_REFUSED\x10 \x12&\n\"PACKAGE_STATUS_CODE_REFUSED_VOLUME\x10!\x12-\n)PACKAGE_STATUS_CODE_REMOVED_FROM_TRANSFER\x10\"\x12*\n&PACKAGE_STATUS_CODE_REDISPATCH_REFUSED\x10l\x12\x30\n,PACKAGE_STATUS_CODE_REDISPATCH_ORDER_CREATED\x10o\x12\'\n#PACKAGE_STATUS_CODE_CUSTOMER_PICKUP\x10Q\x12\x1f\n\x1bPACKAGE_STATUS_CODE_FETCHED\x10R\x12!\n\x1dPACKAGE_STATUS_CODE_CONFIRMED\x10T\x12 \n\x1cPACKAGE_STATUS_CODE_MEASURED\x10S\x12%\n!PACKAGE_STATUS_CODE_NOT_CONFIRMED\x10U\x12\'\n#PACKAGE_STATUS_CODE_MEASURED_FAILED\x10V\x12\x1f\n\x1bPACKAGE_STATUS_CODE_SORTING\x10W\x12(\n$PACKAGE_STATUS_CODE_TRANSFER_STARTED\x10X\x12*\n&PACKAGE_STATUS_CODE_TRANSFER_COMPLETED\x10Y\x12%\n!PACKAGE_STATUS_CODE_TRANSFER_LOST\x10Z\x12\"\n\x1ePACKAGE_STATUS_CODE_INTEGRATED\x10[\x12&\n\"PACKAGE_STATUS_CODE_RETURN_STARTED\x10]\x12%\n!PACKAGE_STATUS_CODE_X_RAY_REFUSED\x10^\x12%\n!PACKAGE_STATUS_CODE_X_RAY_CLEARED\x10_\x12+\n\'PACKAGE_STATUS_CODE_TAX_OFFICE_RETAINED\x10`\x12+\n\'PACKAGE_STATUS_CODE_TAX_OFFICE_RELEASED\x10\x61\x12(\n$PACKAGE_STATUS_CODE_RECIPIENT_PICKUP\x10h\x12%\n!PACKAGE_STATUS_CODE_LABEL_CREATED\x10i\x12$\n PACKAGE_STATUS_CODE_REDISPATCHED\x10j\x12.\n*PACKAGE_STATUS_CODE_LEVE_RECEIVING_REFUSED\x10n\x12+\n\'PACKAGE_STATUS_CODE_REDISPATCH_RETURNED\x10p\x12(\n$PACKAGE_STATUS_CODE_TRANSFER_ONGOING\x10q\x12\'\n#PACKAGE_STATUS_CODE_TRANSFER_PICKUP\x10r\x12/\n+PACKAGE_STATUS_CODE_INTL_GOING_TO_WAREHOUSE\x10\x62\x12&\n\"PACKAGE_STATUS_CODE_INTL_WAREHOUSE\x10\x63\x12-\n)PACKAGE_STATUS_CODE_INTL_TRANSFER_STARTED\x10\x64\x12/\n+PACKAGE_STATUS_CODE_INTL_TRANSFER_COMPLETED\x10\x65\x12,\n(PACKAGE_STATUS_CODE_INTL_CUSTOMS_CLEARED\x10\x66\x12#\n\x1fPACKAGE_STATUS_CODE_INTL_FAILED\x10g\x12.\n*PACKAGE_STATUS_CODE_INTL_FREIGHT_FORWARDED\x10kBX\n\x10\x63om.loggi.web.v1B\x17PackageStatusCodesProtoP\x01Z\x05webv1\xa2\x02\x03LWX\xaa\x02\x0cLoggi.Web.V1\xca\x02\x0cLoggi\\Web\\V1b\x06proto3')
)

_PACKAGESTATUSCODE = _descriptor.EnumDescriptor(
  name='PackageStatusCode',
  full_name='loggi.web.v1.PackageStatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_UNAVAILABLE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_SCHEDULED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_DELIVERED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_PICKUP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_GOING_TO_PICKUP', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_GOING_TO_DELIVER', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_GOING_TO_RESTOCK', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_GOING_TO_RETURN', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_RESTOCKED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_RETURNED', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_RECIPIENT_REFUSED', index=10, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_RECIPIENT_UNAVAILABLE', index=11, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_INVALID_DESTINATION', index=12, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_DAMAGED', index=13, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_LOST', index=14, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_FAILURE', index=15, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_SUSPENDED', index=16, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_INVALID_DIMENSIONS', index=17, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_NOT_FOUND', index=18, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_STOLEN', index=19, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_RECIPIENT_UNAVAILABLE_2ND_TIME', index=20, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_RECIPIENT_UNAVAILABLE_3RD_TIME', index=21, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_IMPAIRED_DELIVERY', index=22, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_GOING_TO_CONFIRM', index=23, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_GOING_TO_MEASURE', index=24, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_REMOVED_FROM_CUTOFF', index=25, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_MAX_RETRIES_EXCEEDED', index=26, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_AWAITING_RESOLUTION', index=27, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_READY_TO_RESEND', index=28, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_READY_TO_RETURN', index=29, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_PICKUP_FAILED', index=30, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_RETURN_REFUSED', index=31, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_REFUSED_VOLUME', index=32, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_REMOVED_FROM_TRANSFER', index=33, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_REDISPATCH_REFUSED', index=34, number=108,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_REDISPATCH_ORDER_CREATED', index=35, number=111,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_CUSTOMER_PICKUP', index=36, number=81,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_FETCHED', index=37, number=82,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_CONFIRMED', index=38, number=84,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_MEASURED', index=39, number=83,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_NOT_CONFIRMED', index=40, number=85,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_MEASURED_FAILED', index=41, number=86,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_SORTING', index=42, number=87,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_TRANSFER_STARTED', index=43, number=88,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_TRANSFER_COMPLETED', index=44, number=89,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_TRANSFER_LOST', index=45, number=90,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_INTEGRATED', index=46, number=91,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_RETURN_STARTED', index=47, number=93,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_X_RAY_REFUSED', index=48, number=94,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_X_RAY_CLEARED', index=49, number=95,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_TAX_OFFICE_RETAINED', index=50, number=96,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_TAX_OFFICE_RELEASED', index=51, number=97,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_RECIPIENT_PICKUP', index=52, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_LABEL_CREATED', index=53, number=105,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_REDISPATCHED', index=54, number=106,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_LEVE_RECEIVING_REFUSED', index=55, number=110,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_REDISPATCH_RETURNED', index=56, number=112,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_TRANSFER_ONGOING', index=57, number=113,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_TRANSFER_PICKUP', index=58, number=114,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_INTL_GOING_TO_WAREHOUSE', index=59, number=98,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_INTL_WAREHOUSE', index=60, number=99,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_INTL_TRANSFER_STARTED', index=61, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_INTL_TRANSFER_COMPLETED', index=62, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_INTL_CUSTOMS_CLEARED', index=63, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_INTL_FAILED', index=64, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE_STATUS_CODE_INTL_FREIGHT_FORWARDED', index=65, number=107,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=142,
  serialized_end=2865,
)
_sym_db.RegisterEnumDescriptor(_PACKAGESTATUSCODE)

PackageStatusCode = enum_type_wrapper.EnumTypeWrapper(_PACKAGESTATUSCODE)
PACKAGE_STATUS_CODE_UNAVAILABLE = 0
PACKAGE_STATUS_CODE_SCHEDULED = 1
PACKAGE_STATUS_CODE_DELIVERED = 2
PACKAGE_STATUS_CODE_PICKUP = 3
PACKAGE_STATUS_CODE_GOING_TO_PICKUP = 4
PACKAGE_STATUS_CODE_GOING_TO_DELIVER = 5
PACKAGE_STATUS_CODE_GOING_TO_RESTOCK = 6
PACKAGE_STATUS_CODE_GOING_TO_RETURN = 7
PACKAGE_STATUS_CODE_RESTOCKED = 8
PACKAGE_STATUS_CODE_RETURNED = 9
PACKAGE_STATUS_CODE_RECIPIENT_REFUSED = 11
PACKAGE_STATUS_CODE_RECIPIENT_UNAVAILABLE = 12
PACKAGE_STATUS_CODE_INVALID_DESTINATION = 13
PACKAGE_STATUS_CODE_DAMAGED = 14
PACKAGE_STATUS_CODE_LOST = 15
PACKAGE_STATUS_CODE_FAILURE = 16
PACKAGE_STATUS_CODE_SUSPENDED = 17
PACKAGE_STATUS_CODE_INVALID_DIMENSIONS = 18
PACKAGE_STATUS_CODE_NOT_FOUND = 19
PACKAGE_STATUS_CODE_STOLEN = 20
PACKAGE_STATUS_CODE_RECIPIENT_UNAVAILABLE_2ND_TIME = 21
PACKAGE_STATUS_CODE_RECIPIENT_UNAVAILABLE_3RD_TIME = 22
PACKAGE_STATUS_CODE_IMPAIRED_DELIVERY = 23
PACKAGE_STATUS_CODE_GOING_TO_CONFIRM = 24
PACKAGE_STATUS_CODE_GOING_TO_MEASURE = 25
PACKAGE_STATUS_CODE_REMOVED_FROM_CUTOFF = 26
PACKAGE_STATUS_CODE_MAX_RETRIES_EXCEEDED = 27
PACKAGE_STATUS_CODE_AWAITING_RESOLUTION = 28
PACKAGE_STATUS_CODE_READY_TO_RESEND = 29
PACKAGE_STATUS_CODE_READY_TO_RETURN = 30
PACKAGE_STATUS_CODE_PICKUP_FAILED = 31
PACKAGE_STATUS_CODE_RETURN_REFUSED = 32
PACKAGE_STATUS_CODE_REFUSED_VOLUME = 33
PACKAGE_STATUS_CODE_REMOVED_FROM_TRANSFER = 34
PACKAGE_STATUS_CODE_REDISPATCH_REFUSED = 108
PACKAGE_STATUS_CODE_REDISPATCH_ORDER_CREATED = 111
PACKAGE_STATUS_CODE_CUSTOMER_PICKUP = 81
PACKAGE_STATUS_CODE_FETCHED = 82
PACKAGE_STATUS_CODE_CONFIRMED = 84
PACKAGE_STATUS_CODE_MEASURED = 83
PACKAGE_STATUS_CODE_NOT_CONFIRMED = 85
PACKAGE_STATUS_CODE_MEASURED_FAILED = 86
PACKAGE_STATUS_CODE_SORTING = 87
PACKAGE_STATUS_CODE_TRANSFER_STARTED = 88
PACKAGE_STATUS_CODE_TRANSFER_COMPLETED = 89
PACKAGE_STATUS_CODE_TRANSFER_LOST = 90
PACKAGE_STATUS_CODE_INTEGRATED = 91
PACKAGE_STATUS_CODE_RETURN_STARTED = 93
PACKAGE_STATUS_CODE_X_RAY_REFUSED = 94
PACKAGE_STATUS_CODE_X_RAY_CLEARED = 95
PACKAGE_STATUS_CODE_TAX_OFFICE_RETAINED = 96
PACKAGE_STATUS_CODE_TAX_OFFICE_RELEASED = 97
PACKAGE_STATUS_CODE_RECIPIENT_PICKUP = 104
PACKAGE_STATUS_CODE_LABEL_CREATED = 105
PACKAGE_STATUS_CODE_REDISPATCHED = 106
PACKAGE_STATUS_CODE_LEVE_RECEIVING_REFUSED = 110
PACKAGE_STATUS_CODE_REDISPATCH_RETURNED = 112
PACKAGE_STATUS_CODE_TRANSFER_ONGOING = 113
PACKAGE_STATUS_CODE_TRANSFER_PICKUP = 114
PACKAGE_STATUS_CODE_INTL_GOING_TO_WAREHOUSE = 98
PACKAGE_STATUS_CODE_INTL_WAREHOUSE = 99
PACKAGE_STATUS_CODE_INTL_TRANSFER_STARTED = 100
PACKAGE_STATUS_CODE_INTL_TRANSFER_COMPLETED = 101
PACKAGE_STATUS_CODE_INTL_CUSTOMS_CLEARED = 102
PACKAGE_STATUS_CODE_INTL_FAILED = 103
PACKAGE_STATUS_CODE_INTL_FREIGHT_FORWARDED = 107



_PACKAGESTATUSCODES = _descriptor.Descriptor(
  name='PackageStatusCodes',
  full_name='loggi.web.v1.PackageStatusCodes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_status_code', full_name='loggi.web.v1.PackageStatusCodes.package_status_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=57,
  serialized_end=139,
)

_PACKAGESTATUSCODES.fields_by_name['package_status_code'].enum_type = _PACKAGESTATUSCODE
DESCRIPTOR.message_types_by_name['PackageStatusCodes'] = _PACKAGESTATUSCODES
DESCRIPTOR.enum_types_by_name['PackageStatusCode'] = _PACKAGESTATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PackageStatusCodes = _reflection.GeneratedProtocolMessageType('PackageStatusCodes', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGESTATUSCODES,
  '__module__' : 'loggi_web.v1.package_status_codes_pb2'
  # @@protoc_insertion_point(class_scope:loggi.web.v1.PackageStatusCodes)
  })
_sym_db.RegisterMessage(PackageStatusCodes)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
