# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: others/UserStatistics.proto
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
    'others/UserStatistics.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from python.Common import Anime_pb2 as Common_dot_Anime__pb2
from python.Common import User_pb2 as Common_dot_User__pb2
from python.Common import Topic_pb2 as Common_dot_Topic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bothers/UserStatistics.proto\x1a\x12\x43ommon/Anime.proto\x1a\x11\x43ommon/User.proto\x1a\x12\x43ommon/Topic.proto\"\x07\n\x05\x45mpty\"2\n\x0eMostUsedTopics\x12 \n\x10most_used_topics\x18\x01 \x03(\x0b\x32\x06.Topic\"\"\n\rTop10_Request\x12\x11\n\tuser_name\x18\x01 \x01(\t\"(\n\x0eTop10_Response\x12\x16\n\x06\x61nimes\x18\x01 \x03(\x0b\x32\x06.Anime\"$\n\rKarmaResponse\x12\x13\n\x0bkarma_Value\x18\x01 \x01(\x05\",\n\x15GetUserByNameResponse\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\")\n\x14GetUserByNameRequest\x12\x11\n\tuser_name\x18\x01 \x01(\t\"+\n\x13GetAllUsersResponse\x12\x14\n\x05users\x18\x01 \x03(\x0b\x32\x05.User2\x87\x02\n\x15UserStatisticsService\x12,\n\x11GetMostUsedTopics\x12\x06.Empty\x1a\x0f.MostUsedTopics\x12+\n\x08GetTop10\x12\x0e.Top10_Request\x1a\x0f.Top10_Response\x12&\n\x0cGetUserKarma\x12\x06.Empty\x1a\x0e.KarmaResponse\x12+\n\x0bGetAllUsers\x12\x06.Empty\x1a\x14.GetAllUsersResponse\x12>\n\rGetUserByName\x12\x15.GetUserByNameRequest\x1a\x16.GetUserByNameResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'others.UserStatistics_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=90
  _globals['_EMPTY']._serialized_end=97
  _globals['_MOSTUSEDTOPICS']._serialized_start=99
  _globals['_MOSTUSEDTOPICS']._serialized_end=149
  _globals['_TOP10_REQUEST']._serialized_start=151
  _globals['_TOP10_REQUEST']._serialized_end=185
  _globals['_TOP10_RESPONSE']._serialized_start=187
  _globals['_TOP10_RESPONSE']._serialized_end=227
  _globals['_KARMARESPONSE']._serialized_start=229
  _globals['_KARMARESPONSE']._serialized_end=265
  _globals['_GETUSERBYNAMERESPONSE']._serialized_start=267
  _globals['_GETUSERBYNAMERESPONSE']._serialized_end=311
  _globals['_GETUSERBYNAMEREQUEST']._serialized_start=313
  _globals['_GETUSERBYNAMEREQUEST']._serialized_end=354
  _globals['_GETALLUSERSRESPONSE']._serialized_start=356
  _globals['_GETALLUSERSRESPONSE']._serialized_end=399
  _globals['_USERSTATISTICSSERVICE']._serialized_start=402
  _globals['_USERSTATISTICSSERVICE']._serialized_end=665
# @@protoc_insertion_point(module_scope)
