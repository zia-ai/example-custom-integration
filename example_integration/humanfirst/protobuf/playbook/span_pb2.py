# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: playbook/span.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13playbook/span.proto\x12\x0fzia.ai.playbook\"e\n\tSpanIndex\x12,\n\x05start\x18\x01 \x01(\x0b\x32\x1d.zia.ai.playbook.SpanPosition\x12*\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1d.zia.ai.playbook.SpanPosition\"<\n\x0cSpanPosition\x12\x13\n\x0binput_index\x18\x01 \x01(\r\x12\x17\n\x0f\x63haracter_index\x18\x02 \x01(\rB6Z4github.com/zia-ai/platform/pkg/api/playbook;playbookb\x06proto3')



_SPANINDEX = DESCRIPTOR.message_types_by_name['SpanIndex']
_SPANPOSITION = DESCRIPTOR.message_types_by_name['SpanPosition']
SpanIndex = _reflection.GeneratedProtocolMessageType('SpanIndex', (_message.Message,), {
  'DESCRIPTOR' : _SPANINDEX,
  '__module__' : 'playbook.span_pb2'
  # @@protoc_insertion_point(class_scope:zia.ai.playbook.SpanIndex)
  })
_sym_db.RegisterMessage(SpanIndex)

SpanPosition = _reflection.GeneratedProtocolMessageType('SpanPosition', (_message.Message,), {
  'DESCRIPTOR' : _SPANPOSITION,
  '__module__' : 'playbook.span_pb2'
  # @@protoc_insertion_point(class_scope:zia.ai.playbook.SpanPosition)
  })
_sym_db.RegisterMessage(SpanPosition)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/zia-ai/platform/pkg/api/playbook;playbook'
  _SPANINDEX._serialized_start=40
  _SPANINDEX._serialized_end=141
  _SPANPOSITION._serialized_start=143
  _SPANPOSITION._serialized_end=203
# @@protoc_insertion_point(module_scope)
