# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protobufs/others/FeedGenerator.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'protobufs/others/FeedGenerator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from python.Common import User_pb2 as protobufs_dot_Common_dot_User__pb2
from python.Common import Topic_pb2 as protobufs_dot_Common_dot_Topic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$protobufs/others/FeedGenerator.proto\x1a\x1bprotobufs/Common/User.proto\x1a\x1cprotobufs/Common/Topic.proto\" \n\x0b\x46\x65\x65\x64Request\x12\x11\n\tuser_name\x18\x01 \x01(\t\"*\n\x0c\x46\x65\x65\x64Response\x12\x1a\n\x04\x66\x65\x65\x64\x18\x01 \x03(\x0b\x32\x0c.Publication\"%\n\x10TopicFeedRequest\x12\x11\n\tuser_name\x18\x01 \x01(\t\"/\n\x11TopicFeedResponse\x12\x1a\n\ntopic_feed\x18\x01 \x03(\x0b\x32\x06.Topic2u\n\x14\x46\x65\x65\x64GeneratorService\x12&\n\x07GetFeed\x12\x0c.FeedRequest\x1a\r.FeedResponse\x12\x35\n\x0cGetTopicFeed\x12\x11.TopicFeedRequest\x1a\x12.TopicFeedResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobufs.others.FeedGenerator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FEEDREQUEST']._serialized_start=99
  _globals['_FEEDREQUEST']._serialized_end=131
  _globals['_FEEDRESPONSE']._serialized_start=133
  _globals['_FEEDRESPONSE']._serialized_end=175
  _globals['_TOPICFEEDREQUEST']._serialized_start=177
  _globals['_TOPICFEEDREQUEST']._serialized_end=214
  _globals['_TOPICFEEDRESPONSE']._serialized_start=216
  _globals['_TOPICFEEDRESPONSE']._serialized_end=263
  _globals['_FEEDGENERATORSERVICE']._serialized_start=265
  _globals['_FEEDGENERATORSERVICE']._serialized_end=382
# @@protoc_insertion_point(module_scope)
