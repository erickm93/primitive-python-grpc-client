# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: annotator/v1/package_annotator_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from annotator.v1 import package_annotation_pb2 as annotator_dot_v1_dot_package__annotation__pb2
from loggi_web import dispatch_pb2 as loggi__web_dot_dispatch__pb2
from loggi_web.v1 import dispatch_pb2 as loggi__web_dot_v1_dot_dispatch__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='annotator/v1/package_annotator_api.proto',
  package='loggi.annotator.v1',
  syntax='proto3',
  serialized_options=_b('\n\026com.loggi.annotator.v1B\030PackageAnnotatorApiProtoP\001Z\013annotatorv1\242\002\003LAX\252\002\022Loggi.Annotator.V1\312\002\022Loggi\\Annotator\\V1'),
  serialized_pb=_b('\n(annotator/v1/package_annotator_api.proto\x12\x12loggi.annotator.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/rpc/status.proto\x1a%annotator/v1/package_annotation.proto\x1a\x18loggi_web/dispatch.proto\x1a\x1bloggi_web/v1/dispatch.proto\"\xac\x01\n\x0f\x41nnotateRequest\x12\x34\n\x12\x64\x65precated_package\x18\x01 \x01(\x0b\x32\x14.loggi.proto.PackageB\x02\x18\x01\x12;\n\x0f\x61nnotation_type\x18\x02 \x01(\x0e\x32\".loggi.annotator.v1.AnnotationType\x12&\n\x07package\x18\x03 \x01(\x0b\x32\x15.loggi.web.v1.Package\"y\n\x10\x41nnotateResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x41\n\x12package_annotation\x18\x02 \x01(\x0b\x32%.loggi.annotator.v1.PackageAnnotation\"q\n\x1eGetLastAnnotationByTypeRequest\x12\x12\n\npackage_id\x18\x01 \x01(\x03\x12;\n\x0f\x61nnotation_type\x18\x02 \x01(\x0e\x32\".loggi.annotator.v1.AnnotationType\"d\n\x1fGetLastAnnotationByTypeResponse\x12\x41\n\x12package_annotation\x18\x02 \x01(\x0b\x32%.loggi.annotator.v1.PackageAnnotation\".\n\x18GetAllAnnotationsRequest\x12\x12\n\npackage_id\x18\x01 \x01(\x03\"_\n\x19GetAllAnnotationsResponse\x12\x42\n\x13package_annotations\x18\x02 \x03(\x0b\x32%.loggi.annotator.v1.PackageAnnotation2\xe9\x02\n\x13PackageAnnotatorAPI\x12W\n\x08\x41nnotate\x12#.loggi.annotator.v1.AnnotateRequest\x1a$.loggi.annotator.v1.AnnotateResponse\"\x00\x12\x84\x01\n\x17GetLastAnnotationByType\x12\x32.loggi.annotator.v1.GetLastAnnotationByTypeRequest\x1a\x33.loggi.annotator.v1.GetLastAnnotationByTypeResponse\"\x00\x12r\n\x11GetAllAnnotations\x12,.loggi.annotator.v1.GetAllAnnotationsRequest\x1a-.loggi.annotator.v1.GetAllAnnotationsResponse\"\x00\x42q\n\x16\x63om.loggi.annotator.v1B\x18PackageAnnotatorApiProtoP\x01Z\x0b\x61nnotatorv1\xa2\x02\x03LAX\xaa\x02\x12Loggi.Annotator.V1\xca\x02\x12Loggi\\Annotator\\V1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,annotator_dot_v1_dot_package__annotation__pb2.DESCRIPTOR,loggi__web_dot_dispatch__pb2.DESCRIPTOR,loggi__web_dot_v1_dot_dispatch__pb2.DESCRIPTOR,])




_ANNOTATEREQUEST = _descriptor.Descriptor(
  name='AnnotateRequest',
  full_name='loggi.annotator.v1.AnnotateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deprecated_package', full_name='loggi.annotator.v1.AnnotateRequest.deprecated_package', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotation_type', full_name='loggi.annotator.v1.AnnotateRequest.annotation_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package', full_name='loggi.annotator.v1.AnnotateRequest.package', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=214,
  serialized_end=386,
)


_ANNOTATERESPONSE = _descriptor.Descriptor(
  name='AnnotateResponse',
  full_name='loggi.annotator.v1.AnnotateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='loggi.annotator.v1.AnnotateResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_annotation', full_name='loggi.annotator.v1.AnnotateResponse.package_annotation', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=388,
  serialized_end=509,
)


_GETLASTANNOTATIONBYTYPEREQUEST = _descriptor.Descriptor(
  name='GetLastAnnotationByTypeRequest',
  full_name='loggi.annotator.v1.GetLastAnnotationByTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_id', full_name='loggi.annotator.v1.GetLastAnnotationByTypeRequest.package_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotation_type', full_name='loggi.annotator.v1.GetLastAnnotationByTypeRequest.annotation_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=511,
  serialized_end=624,
)


_GETLASTANNOTATIONBYTYPERESPONSE = _descriptor.Descriptor(
  name='GetLastAnnotationByTypeResponse',
  full_name='loggi.annotator.v1.GetLastAnnotationByTypeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_annotation', full_name='loggi.annotator.v1.GetLastAnnotationByTypeResponse.package_annotation', index=0,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=626,
  serialized_end=726,
)


_GETALLANNOTATIONSREQUEST = _descriptor.Descriptor(
  name='GetAllAnnotationsRequest',
  full_name='loggi.annotator.v1.GetAllAnnotationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_id', full_name='loggi.annotator.v1.GetAllAnnotationsRequest.package_id', index=0,
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
  serialized_start=728,
  serialized_end=774,
)


_GETALLANNOTATIONSRESPONSE = _descriptor.Descriptor(
  name='GetAllAnnotationsResponse',
  full_name='loggi.annotator.v1.GetAllAnnotationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_annotations', full_name='loggi.annotator.v1.GetAllAnnotationsResponse.package_annotations', index=0,
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
  serialized_start=776,
  serialized_end=871,
)

_ANNOTATEREQUEST.fields_by_name['deprecated_package'].message_type = loggi__web_dot_dispatch__pb2._PACKAGE
_ANNOTATEREQUEST.fields_by_name['annotation_type'].enum_type = annotator_dot_v1_dot_package__annotation__pb2._ANNOTATIONTYPE
_ANNOTATEREQUEST.fields_by_name['package'].message_type = loggi__web_dot_v1_dot_dispatch__pb2._PACKAGE
_ANNOTATERESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_ANNOTATERESPONSE.fields_by_name['package_annotation'].message_type = annotator_dot_v1_dot_package__annotation__pb2._PACKAGEANNOTATION
_GETLASTANNOTATIONBYTYPEREQUEST.fields_by_name['annotation_type'].enum_type = annotator_dot_v1_dot_package__annotation__pb2._ANNOTATIONTYPE
_GETLASTANNOTATIONBYTYPERESPONSE.fields_by_name['package_annotation'].message_type = annotator_dot_v1_dot_package__annotation__pb2._PACKAGEANNOTATION
_GETALLANNOTATIONSRESPONSE.fields_by_name['package_annotations'].message_type = annotator_dot_v1_dot_package__annotation__pb2._PACKAGEANNOTATION
DESCRIPTOR.message_types_by_name['AnnotateRequest'] = _ANNOTATEREQUEST
DESCRIPTOR.message_types_by_name['AnnotateResponse'] = _ANNOTATERESPONSE
DESCRIPTOR.message_types_by_name['GetLastAnnotationByTypeRequest'] = _GETLASTANNOTATIONBYTYPEREQUEST
DESCRIPTOR.message_types_by_name['GetLastAnnotationByTypeResponse'] = _GETLASTANNOTATIONBYTYPERESPONSE
DESCRIPTOR.message_types_by_name['GetAllAnnotationsRequest'] = _GETALLANNOTATIONSREQUEST
DESCRIPTOR.message_types_by_name['GetAllAnnotationsResponse'] = _GETALLANNOTATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnnotateRequest = _reflection.GeneratedProtocolMessageType('AnnotateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANNOTATEREQUEST,
  '__module__' : 'annotator.v1.package_annotator_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.annotator.v1.AnnotateRequest)
  })
_sym_db.RegisterMessage(AnnotateRequest)

AnnotateResponse = _reflection.GeneratedProtocolMessageType('AnnotateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANNOTATERESPONSE,
  '__module__' : 'annotator.v1.package_annotator_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.annotator.v1.AnnotateResponse)
  })
_sym_db.RegisterMessage(AnnotateResponse)

GetLastAnnotationByTypeRequest = _reflection.GeneratedProtocolMessageType('GetLastAnnotationByTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTANNOTATIONBYTYPEREQUEST,
  '__module__' : 'annotator.v1.package_annotator_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.annotator.v1.GetLastAnnotationByTypeRequest)
  })
_sym_db.RegisterMessage(GetLastAnnotationByTypeRequest)

GetLastAnnotationByTypeResponse = _reflection.GeneratedProtocolMessageType('GetLastAnnotationByTypeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTANNOTATIONBYTYPERESPONSE,
  '__module__' : 'annotator.v1.package_annotator_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.annotator.v1.GetLastAnnotationByTypeResponse)
  })
_sym_db.RegisterMessage(GetLastAnnotationByTypeResponse)

GetAllAnnotationsRequest = _reflection.GeneratedProtocolMessageType('GetAllAnnotationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETALLANNOTATIONSREQUEST,
  '__module__' : 'annotator.v1.package_annotator_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.annotator.v1.GetAllAnnotationsRequest)
  })
_sym_db.RegisterMessage(GetAllAnnotationsRequest)

GetAllAnnotationsResponse = _reflection.GeneratedProtocolMessageType('GetAllAnnotationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETALLANNOTATIONSRESPONSE,
  '__module__' : 'annotator.v1.package_annotator_api_pb2'
  # @@protoc_insertion_point(class_scope:loggi.annotator.v1.GetAllAnnotationsResponse)
  })
_sym_db.RegisterMessage(GetAllAnnotationsResponse)


DESCRIPTOR._options = None
_ANNOTATEREQUEST.fields_by_name['deprecated_package']._options = None

_PACKAGEANNOTATORAPI = _descriptor.ServiceDescriptor(
  name='PackageAnnotatorAPI',
  full_name='loggi.annotator.v1.PackageAnnotatorAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=874,
  serialized_end=1235,
  methods=[
  _descriptor.MethodDescriptor(
    name='Annotate',
    full_name='loggi.annotator.v1.PackageAnnotatorAPI.Annotate',
    index=0,
    containing_service=None,
    input_type=_ANNOTATEREQUEST,
    output_type=_ANNOTATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLastAnnotationByType',
    full_name='loggi.annotator.v1.PackageAnnotatorAPI.GetLastAnnotationByType',
    index=1,
    containing_service=None,
    input_type=_GETLASTANNOTATIONBYTYPEREQUEST,
    output_type=_GETLASTANNOTATIONBYTYPERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllAnnotations',
    full_name='loggi.annotator.v1.PackageAnnotatorAPI.GetAllAnnotations',
    index=2,
    containing_service=None,
    input_type=_GETALLANNOTATIONSREQUEST,
    output_type=_GETALLANNOTATIONSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PACKAGEANNOTATORAPI)

DESCRIPTOR.services_by_name['PackageAnnotatorAPI'] = _PACKAGEANNOTATORAPI

# @@protoc_insertion_point(module_scope)