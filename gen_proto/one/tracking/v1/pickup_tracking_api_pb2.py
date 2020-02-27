# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: one/tracking/v1/pickup_tracking_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import money_pb2 as google_dot_type_dot_money__pb2
from wally.v1 import address_pb2 as wally_dot_v1_dot_address__pb2
from one.tracking.v1 import pickup_tracking_pb2 as one_dot_tracking_dot_v1_dot_pickup__tracking__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='one/tracking/v1/pickup_tracking_api.proto',
  package='loggi.one.tracking.v1',
  syntax='proto3',
  serialized_options=_b('\n\031com.loggi.one.tracking.v1B\026PickupTrackingApiProtoP\001Z\ntrackingv1\242\002\003LOT\252\002\025Loggi.One.Tracking.V1\312\002\025Loggi\\One\\Tracking\\V1'),
  serialized_pb=_b('\n)one/tracking/v1/pickup_tracking_api.proto\x12\x15loggi.one.tracking.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/type/money.proto\x1a\x16wally/v1/address.proto\x1a%one/tracking/v1/pickup_tracking.proto\"\xdc\x02\n\x1d\x43reatePickupAllocationRequest\x12\"\n\x1apickup_order_scheduling_id\x18\x01 \x01(\x03\x12.\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x0flocation_origin\x18\x04 \x01(\x0b\x32\x1b.loggi.wally.v1.GeoLocation\x12\x44\n\x13modal_possibilities\x18\x05 \x03(\x0b\x32\'.loggi.one.tracking.v1.ModalCombination\x12-\n\x11\x61llocation_budget\x18\x06 \x01(\x0b\x32\x12.google.type.Money\x12\x0e\n\x06volume\x18\x07 \x01(\x02\"Z\n\x1e\x43reatePickupAllocationResponse\x12\x38\n\x0c\x61\x63k_response\x18\x01 \x01(\x0b\x32\".loggi.one.tracking.v1.AckResponse\"C\n\x1d\x43\x61ncelPickupAllocationRequest\x12\"\n\x1apickup_order_scheduling_id\x18\x01 \x01(\x03\"Z\n\x1e\x43\x61ncelPickupAllocationResponse\x12\x38\n\x0c\x61\x63k_response\x18\x01 \x01(\x0b\x32\".loggi.one.tracking.v1.AckResponse2\xa7\x02\n\x11PickupTrackingAPI\x12\x87\x01\n\x16\x43reatePickupAllocation\x12\x34.loggi.one.tracking.v1.CreatePickupAllocationRequest\x1a\x35.loggi.one.tracking.v1.CreatePickupAllocationResponse\"\x00\x12\x87\x01\n\x16\x43\x61ncelPickupAllocation\x12\x34.loggi.one.tracking.v1.CancelPickupAllocationRequest\x1a\x35.loggi.one.tracking.v1.CancelPickupAllocationResponse\"\x00\x42w\n\x19\x63om.loggi.one.tracking.v1B\x16PickupTrackingApiProtoP\x01Z\ntrackingv1\xa2\x02\x03LOT\xaa\x02\x15Loggi.One.Tracking.V1\xca\x02\x15Loggi\\One\\Tracking\\V1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_type_dot_money__pb2.DESCRIPTOR,wally_dot_v1_dot_address__pb2.DESCRIPTOR,one_dot_tracking_dot_v1_dot_pickup__tracking__pb2.DESCRIPTOR,])




_CREATEPICKUPALLOCATIONREQUEST = _descriptor.Descriptor(
  name='CreatePickupAllocationRequest',
  full_name='loggi.one.tracking.v1.CreatePickupAllocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pickup_order_scheduling_id', full_name='loggi.one.tracking.v1.CreatePickupAllocationRequest.pickup_order_scheduling_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='loggi.one.tracking.v1.CreatePickupAllocationRequest.start_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='loggi.one.tracking.v1.CreatePickupAllocationRequest.end_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location_origin', full_name='loggi.one.tracking.v1.CreatePickupAllocationRequest.location_origin', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modal_possibilities', full_name='loggi.one.tracking.v1.CreatePickupAllocationRequest.modal_possibilities', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allocation_budget', full_name='loggi.one.tracking.v1.CreatePickupAllocationRequest.allocation_budget', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='loggi.one.tracking.v1.CreatePickupAllocationRequest.volume', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=190,
  serialized_end=538,
)


_CREATEPICKUPALLOCATIONRESPONSE = _descriptor.Descriptor(
  name='CreatePickupAllocationResponse',
  full_name='loggi.one.tracking.v1.CreatePickupAllocationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack_response', full_name='loggi.one.tracking.v1.CreatePickupAllocationResponse.ack_response', index=0,
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
  serialized_start=540,
  serialized_end=630,
)


_CANCELPICKUPALLOCATIONREQUEST = _descriptor.Descriptor(
  name='CancelPickupAllocationRequest',
  full_name='loggi.one.tracking.v1.CancelPickupAllocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pickup_order_scheduling_id', full_name='loggi.one.tracking.v1.CancelPickupAllocationRequest.pickup_order_scheduling_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=632,
  serialized_end=699,
)


_CANCELPICKUPALLOCATIONRESPONSE = _descriptor.Descriptor(
  name='CancelPickupAllocationResponse',
  full_name='loggi.one.tracking.v1.CancelPickupAllocationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack_response', full_name='loggi.one.tracking.v1.CancelPickupAllocationResponse.ack_response', index=0,
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
  serialized_start=701,
  serialized_end=791,
)

_CREATEPICKUPALLOCATIONREQUEST.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CREATEPICKUPALLOCATIONREQUEST.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CREATEPICKUPALLOCATIONREQUEST.fields_by_name['location_origin'].message_type = wally_dot_v1_dot_address__pb2._GEOLOCATION
_CREATEPICKUPALLOCATIONREQUEST.fields_by_name['modal_possibilities'].message_type = one_dot_tracking_dot_v1_dot_pickup__tracking__pb2._MODALCOMBINATION
_CREATEPICKUPALLOCATIONREQUEST.fields_by_name['allocation_budget'].message_type = google_dot_type_dot_money__pb2._MONEY
_CREATEPICKUPALLOCATIONRESPONSE.fields_by_name['ack_response'].message_type = one_dot_tracking_dot_v1_dot_pickup__tracking__pb2._ACKRESPONSE
_CANCELPICKUPALLOCATIONRESPONSE.fields_by_name['ack_response'].message_type = one_dot_tracking_dot_v1_dot_pickup__tracking__pb2._ACKRESPONSE
DESCRIPTOR.message_types_by_name['CreatePickupAllocationRequest'] = _CREATEPICKUPALLOCATIONREQUEST
DESCRIPTOR.message_types_by_name['CreatePickupAllocationResponse'] = _CREATEPICKUPALLOCATIONRESPONSE
DESCRIPTOR.message_types_by_name['CancelPickupAllocationRequest'] = _CANCELPICKUPALLOCATIONREQUEST
DESCRIPTOR.message_types_by_name['CancelPickupAllocationResponse'] = _CANCELPICKUPALLOCATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreatePickupAllocationRequest = _reflection.GeneratedProtocolMessageType('CreatePickupAllocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPICKUPALLOCATIONREQUEST,
  '__module__' : 'one.tracking.v1.pickup_tracking_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.one.tracking.v1.CreatePickupAllocationRequest)
  })
_sym_db.RegisterMessage(CreatePickupAllocationRequest)

CreatePickupAllocationResponse = _reflection.GeneratedProtocolMessageType('CreatePickupAllocationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPICKUPALLOCATIONRESPONSE,
  '__module__' : 'one.tracking.v1.pickup_tracking_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.one.tracking.v1.CreatePickupAllocationResponse)
  })
_sym_db.RegisterMessage(CreatePickupAllocationResponse)

CancelPickupAllocationRequest = _reflection.GeneratedProtocolMessageType('CancelPickupAllocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELPICKUPALLOCATIONREQUEST,
  '__module__' : 'one.tracking.v1.pickup_tracking_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.one.tracking.v1.CancelPickupAllocationRequest)
  })
_sym_db.RegisterMessage(CancelPickupAllocationRequest)

CancelPickupAllocationResponse = _reflection.GeneratedProtocolMessageType('CancelPickupAllocationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELPICKUPALLOCATIONRESPONSE,
  '__module__' : 'one.tracking.v1.pickup_tracking_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.one.tracking.v1.CancelPickupAllocationResponse)
  })
_sym_db.RegisterMessage(CancelPickupAllocationResponse)


DESCRIPTOR._options = None

_PICKUPTRACKINGAPI = _descriptor.ServiceDescriptor(
  name='PickupTrackingAPI',
  full_name='loggi.one.tracking.v1.PickupTrackingAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=794,
  serialized_end=1089,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreatePickupAllocation',
    full_name='loggi.one.tracking.v1.PickupTrackingAPI.CreatePickupAllocation',
    index=0,
    containing_service=None,
    input_type=_CREATEPICKUPALLOCATIONREQUEST,
    output_type=_CREATEPICKUPALLOCATIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CancelPickupAllocation',
    full_name='loggi.one.tracking.v1.PickupTrackingAPI.CancelPickupAllocation',
    index=1,
    containing_service=None,
    input_type=_CANCELPICKUPALLOCATIONREQUEST,
    output_type=_CANCELPICKUPALLOCATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PICKUPTRACKINGAPI)

DESCRIPTOR.services_by_name['PickupTrackingAPI'] = _PICKUPTRACKINGAPI

# @@protoc_insertion_point(module_scope)
