# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: external_integration/v1alpha1/discovery.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-external_integration/v1alpha1/discovery.proto\x12$zia.ai.external_integration.v1alpha1\"\x18\n\x16GetCapabilitiesRequest\"\x97\x01\n\x17GetCapabilitiesResponse\x12\x17\n\x0fsupports_models\x18\x01 \x01(\x08\x12\x1b\n\x13supports_workspaces\x18\x02 \x01(\x08\x12\x1d\n\x15max_concurrent_models\x18\n \x01(\r\x12\'\n\x1fmodel_classification_batch_size\x18\x0b \x01(\r2\x9e\x01\n\tDiscovery\x12\x90\x01\n\x0fGetCapabilities\x12<.zia.ai.external_integration.v1alpha1.GetCapabilitiesRequest\x1a=.zia.ai.external_integration.v1alpha1.GetCapabilitiesResponse\"\x00\x42`Z^github.com/zia-ai/platform/pkg/api/external_integration/v1alpha1;external_integration_v1alpha1b\x06proto3')



_GETCAPABILITIESREQUEST = DESCRIPTOR.message_types_by_name['GetCapabilitiesRequest']
_GETCAPABILITIESRESPONSE = DESCRIPTOR.message_types_by_name['GetCapabilitiesResponse']
GetCapabilitiesRequest = _reflection.GeneratedProtocolMessageType('GetCapabilitiesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCAPABILITIESREQUEST,
  '__module__' : 'external_integration.v1alpha1.discovery_pb2'
  # @@protoc_insertion_point(class_scope:zia.ai.external_integration.v1alpha1.GetCapabilitiesRequest)
  })
_sym_db.RegisterMessage(GetCapabilitiesRequest)

GetCapabilitiesResponse = _reflection.GeneratedProtocolMessageType('GetCapabilitiesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCAPABILITIESRESPONSE,
  '__module__' : 'external_integration.v1alpha1.discovery_pb2'
  # @@protoc_insertion_point(class_scope:zia.ai.external_integration.v1alpha1.GetCapabilitiesResponse)
  })
_sym_db.RegisterMessage(GetCapabilitiesResponse)

_DISCOVERY = DESCRIPTOR.services_by_name['Discovery']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z^github.com/zia-ai/platform/pkg/api/external_integration/v1alpha1;external_integration_v1alpha1'
  _GETCAPABILITIESREQUEST._serialized_start=87
  _GETCAPABILITIESREQUEST._serialized_end=111
  _GETCAPABILITIESRESPONSE._serialized_start=114
  _GETCAPABILITIESRESPONSE._serialized_end=265
  _DISCOVERY._serialized_start=268
  _DISCOVERY._serialized_end=426
# @@protoc_insertion_point(module_scope)
