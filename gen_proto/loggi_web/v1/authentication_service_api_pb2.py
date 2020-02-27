# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loggi_web/v1/authentication_service_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='loggi_web/v1/authentication_service_api.proto',
  package='loggi.web.v1',
  syntax='proto3',
  serialized_options=_b('\n\020com.loggi.web.v1B\035AuthenticationServiceApiProtoP\001Z\005webv1\242\002\003LWX\252\002\014Loggi.Web.V1\312\002\014Loggi\\Web\\V1'),
  serialized_pb=_b('\n-loggi_web/v1/authentication_service_api.proto\x12\x0cloggi.web.v1\x1a\x1cgoogle/api/annotations.proto\"G\n\x13\x41uthenticateRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x03 \x01(\t\"\xa8\x01\n\x14\x41uthenticateResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\x03\x12!\n\x19\x64istributions_centers_ids\x18\x03 \x03(\x03\x12\x0c\n\x04role\x18\x04 \x01(\t\x12\r\n\x05phone\x18\x05 \x01(\t\x12\x1c\n\x14last_mile_company_id\x18\x06 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x07 \x01(\t2\x89\x01\n\x18\x41uthenticationServiceAPI\x12m\n\x0c\x41uthenticate\x12!.loggi.web.v1.AuthenticateRequest\x1a\".loggi.web.v1.AuthenticateResponse\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0e/v1/user/auth/B^\n\x10\x63om.loggi.web.v1B\x1d\x41uthenticationServiceApiProtoP\x01Z\x05webv1\xa2\x02\x03LWX\xaa\x02\x0cLoggi.Web.V1\xca\x02\x0cLoggi\\Web\\V1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_AUTHENTICATEREQUEST = _descriptor.Descriptor(
  name='AuthenticateRequest',
  full_name='loggi.web.v1.AuthenticateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='loggi.web.v1.AuthenticateRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='loggi.web.v1.AuthenticateRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_key', full_name='loggi.web.v1.AuthenticateRequest.api_key', index=2,
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
  serialized_start=93,
  serialized_end=164,
)


_AUTHENTICATERESPONSE = _descriptor.Descriptor(
  name='AuthenticateResponse',
  full_name='loggi.web.v1.AuthenticateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='loggi.web.v1.AuthenticateResponse.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='loggi.web.v1.AuthenticateResponse.user_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distributions_centers_ids', full_name='loggi.web.v1.AuthenticateResponse.distributions_centers_ids', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='loggi.web.v1.AuthenticateResponse.role', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone', full_name='loggi.web.v1.AuthenticateResponse.phone', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_mile_company_id', full_name='loggi.web.v1.AuthenticateResponse.last_mile_company_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_key', full_name='loggi.web.v1.AuthenticateResponse.api_key', index=6,
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
  serialized_start=167,
  serialized_end=335,
)

DESCRIPTOR.message_types_by_name['AuthenticateRequest'] = _AUTHENTICATEREQUEST
DESCRIPTOR.message_types_by_name['AuthenticateResponse'] = _AUTHENTICATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthenticateRequest = _reflection.GeneratedProtocolMessageType('AuthenticateRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATEREQUEST,
  '__module__' : 'loggi_web.v1.authentication_service_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.web.v1.AuthenticateRequest)
  })
_sym_db.RegisterMessage(AuthenticateRequest)

AuthenticateResponse = _reflection.GeneratedProtocolMessageType('AuthenticateResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATERESPONSE,
  '__module__' : 'loggi_web.v1.authentication_service_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.web.v1.AuthenticateResponse)
  })
_sym_db.RegisterMessage(AuthenticateResponse)


DESCRIPTOR._options = None

_AUTHENTICATIONSERVICEAPI = _descriptor.ServiceDescriptor(
  name='AuthenticationServiceAPI',
  full_name='loggi.web.v1.AuthenticationServiceAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=338,
  serialized_end=475,
  methods=[
  _descriptor.MethodDescriptor(
    name='Authenticate',
    full_name='loggi.web.v1.AuthenticationServiceAPI.Authenticate',
    index=0,
    containing_service=None,
    input_type=_AUTHENTICATEREQUEST,
    output_type=_AUTHENTICATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\020\"\016/v1/user/auth/'),
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHENTICATIONSERVICEAPI)

DESCRIPTOR.services_by_name['AuthenticationServiceAPI'] = _AUTHENTICATIONSERVICEAPI

# @@protoc_insertion_point(module_scope)
