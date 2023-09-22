# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: playbook/data/config/v1alpha1/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tags import tags_pb2 as tags_dot_tags__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*playbook/data/config/v1alpha1/config.proto\x12$zia.ai.playbook.data.config.v1alpha1\x1a\x0ftags/tags.proto\"\xdc\x02\n\x12IntentsDataOptions\x12)\n!hierarchical_intent_name_disabled\x18\x01 \x01(\x08\x12\x1e\n\x16hierarchical_delimiter\x18\x02 \x01(\t\x12\x14\n\x0czip_encoding\x18\x03 \x01(\x08\x12\x15\n\rgzip_encoding\x18\x06 \x01(\x08\x12\x1e\n\x16hierarchical_follow_up\x18\x04 \x01(\x08\x12 \n\x18include_negative_phrases\x18\x05 \x01(\x08\x12\x37\n\x14intent_tag_predicate\x18\x07 \x01(\x0b\x32\x19.zia.ai.tags.TagPredicate\x12\x37\n\x14phrase_tag_predicate\x18\x08 \x01(\x0b\x32\x19.zia.ai.tags.TagPredicate\x12\x1a\n\x12skip_empty_intents\x18\t \x01(\x08\"\xb3\x02\n\rImportOptions\x12\x15\n\rclear_intents\x18\x01 \x01(\x08\x12\x16\n\x0e\x63lear_entities\x18\x02 \x01(\x08\x12\x12\n\nclear_tags\x18\x03 \x01(\x08\x12\x15\n\rmerge_intents\x18\x04 \x01(\x08\x12\x16\n\x0emerge_entities\x18\x05 \x01(\x08\x12\x12\n\nmerge_tags\x18\x06 \x01(\x08\x12\x34\n\x11\x65xtra_intent_tags\x18\x07 \x03(\x0b\x32\x19.zia.ai.tags.TagReference\x12\x34\n\x11\x65xtra_phrase_tags\x18\x08 \x03(\x0b\x32\x19.zia.ai.tags.TagReference\x12\x19\n\x11override_metadata\x18\t \x01(\x08\x12\x15\n\roverride_name\x18\n \x01(\x08*\xe5\x02\n\x11IntentsDataFormat\x12\x1a\n\x16INTENTS_FORMAT_INVALID\x10\x00\x12%\n!INTENTS_FORMAT_CSV_SIMPLE_INTENTS\x10\x01\x12 \n\x1cINTENTS_FORMAT_RASA_MARKDOWN\x10\x02\x12\x1c\n\x18INTENTS_FORMAT_RASA_YAML\x10\x04\x12 \n\x1cINTENTS_FORMAT_BOTPRESS_JSON\x10\x03\x12&\n\"INTENTS_FORMAT_DIALOGFLOW_ES_AGENT\x10\x05\x12\x1e\n\x1aINTENTS_FORMAT_TXT_PHRASES\x10\x06\x12\x1a\n\x16INTENTS_FORMAT_HF_JSON\x10\x07\x12\x1f\n\x1bINTENTS_FORMAT_COGNIGY_JSON\x10\x08\x12&\n\"INTENTS_FORMAT_DIALOGFLOW_CX_AGENT\x10\tBRZPgithub.com/zia-ai/platform/pkg/api/playbook/data/config/v1alpha1;config_v1alpha1b\x06proto3')

_INTENTSDATAFORMAT = DESCRIPTOR.enum_types_by_name['IntentsDataFormat']
IntentsDataFormat = enum_type_wrapper.EnumTypeWrapper(_INTENTSDATAFORMAT)
INTENTS_FORMAT_INVALID = 0
INTENTS_FORMAT_CSV_SIMPLE_INTENTS = 1
INTENTS_FORMAT_RASA_MARKDOWN = 2
INTENTS_FORMAT_RASA_YAML = 4
INTENTS_FORMAT_BOTPRESS_JSON = 3
INTENTS_FORMAT_DIALOGFLOW_ES_AGENT = 5
INTENTS_FORMAT_TXT_PHRASES = 6
INTENTS_FORMAT_HF_JSON = 7
INTENTS_FORMAT_COGNIGY_JSON = 8
INTENTS_FORMAT_DIALOGFLOW_CX_AGENT = 9


_INTENTSDATAOPTIONS = DESCRIPTOR.message_types_by_name['IntentsDataOptions']
_IMPORTOPTIONS = DESCRIPTOR.message_types_by_name['ImportOptions']
IntentsDataOptions = _reflection.GeneratedProtocolMessageType('IntentsDataOptions', (_message.Message,), {
  'DESCRIPTOR' : _INTENTSDATAOPTIONS,
  '__module__' : 'playbook.data.config.v1alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:zia.ai.playbook.data.config.v1alpha1.IntentsDataOptions)
  })
_sym_db.RegisterMessage(IntentsDataOptions)

ImportOptions = _reflection.GeneratedProtocolMessageType('ImportOptions', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTOPTIONS,
  '__module__' : 'playbook.data.config.v1alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:zia.ai.playbook.data.config.v1alpha1.ImportOptions)
  })
_sym_db.RegisterMessage(ImportOptions)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZPgithub.com/zia-ai/platform/pkg/api/playbook/data/config/v1alpha1;config_v1alpha1'
  _INTENTSDATAFORMAT._serialized_start=763
  _INTENTSDATAFORMAT._serialized_end=1120
  _INTENTSDATAOPTIONS._serialized_start=102
  _INTENTSDATAOPTIONS._serialized_end=450
  _IMPORTOPTIONS._serialized_start=453
  _IMPORTOPTIONS._serialized_end=760
# @@protoc_insertion_point(module_scope)