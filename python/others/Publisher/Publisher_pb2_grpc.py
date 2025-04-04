# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
import python.others.Publisher.Publisher_pb2 as others_dot_Publisher__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in others/Publisher_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PublisherStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTopics = channel.unary_unary(
                '/Publisher/GetTopics',
                request_serializer=others_dot_Publisher__pb2.GetTopicsRequestPub.SerializeToString,
                response_deserializer=others_dot_Publisher__pb2.GetTopicsResponsePub.FromString,
                _registered_method=True)
        self.CreateTopic = channel.unary_unary(
                '/Publisher/CreateTopic',
                request_serializer=others_dot_Publisher__pb2.CreateTopicRequestPub.SerializeToString,
                response_deserializer=others_dot_Publisher__pb2.CreateTopicResponsePub.FromString,
                _registered_method=True)
        self.GetTopic = channel.unary_unary(
                '/Publisher/GetTopic',
                request_serializer=others_dot_Publisher__pb2.GetTopicRequestPub.SerializeToString,
                response_deserializer=others_dot_Publisher__pb2.GetTopicResponsePub.FromString,
                _registered_method=True)
        self.Publish = channel.unary_unary(
                '/Publisher/Publish',
                request_serializer=others_dot_Publisher__pb2.PublishInTopicRequestPub.SerializeToString,
                response_deserializer=others_dot_Publisher__pb2.PublishInTopicResponsePub.FromString,
                _registered_method=True)
        self.Karma = channel.unary_unary(
                '/Publisher/Karma',
                request_serializer=others_dot_Publisher__pb2.KarmaRequestPub.SerializeToString,
                response_deserializer=others_dot_Publisher__pb2.KarmaResponsePub.FromString,
                _registered_method=True)


class PublisherServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTopics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTopic(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTopic(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Karma(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PublisherServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTopics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTopics,
                    request_deserializer=others_dot_Publisher__pb2.GetTopicsRequestPub.FromString,
                    response_serializer=others_dot_Publisher__pb2.GetTopicsResponsePub.SerializeToString,
            ),
            'CreateTopic': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTopic,
                    request_deserializer=others_dot_Publisher__pb2.CreateTopicRequestPub.FromString,
                    response_serializer=others_dot_Publisher__pb2.CreateTopicResponsePub.SerializeToString,
            ),
            'GetTopic': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTopic,
                    request_deserializer=others_dot_Publisher__pb2.GetTopicRequestPub.FromString,
                    response_serializer=others_dot_Publisher__pb2.GetTopicResponsePub.SerializeToString,
            ),
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=others_dot_Publisher__pb2.PublishInTopicRequestPub.FromString,
                    response_serializer=others_dot_Publisher__pb2.PublishInTopicResponsePub.SerializeToString,
            ),
            'Karma': grpc.unary_unary_rpc_method_handler(
                    servicer.Karma,
                    request_deserializer=others_dot_Publisher__pb2.KarmaRequestPub.FromString,
                    response_serializer=others_dot_Publisher__pb2.KarmaResponsePub.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Publisher', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Publisher', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Publisher(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTopics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Publisher/GetTopics',
            others_dot_Publisher__pb2.GetTopicsRequestPub.SerializeToString,
            others_dot_Publisher__pb2.GetTopicsResponsePub.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateTopic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Publisher/CreateTopic',
            others_dot_Publisher__pb2.CreateTopicRequestPub.SerializeToString,
            others_dot_Publisher__pb2.CreateTopicResponsePub.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTopic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Publisher/GetTopic',
            others_dot_Publisher__pb2.GetTopicRequestPub.SerializeToString,
            others_dot_Publisher__pb2.GetTopicResponsePub.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Publisher/Publish',
            others_dot_Publisher__pb2.PublishInTopicRequestPub.SerializeToString,
            others_dot_Publisher__pb2.PublishInTopicResponsePub.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Karma(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Publisher/Karma',
            others_dot_Publisher__pb2.KarmaRequestPub.SerializeToString,
            others_dot_Publisher__pb2.KarmaResponsePub.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
