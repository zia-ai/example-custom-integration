# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from longrunning.v1alpha1 import operations_pb2 as longrunning_dot_v1alpha1_dot_operations__pb2


class OperationsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOperation = channel.unary_unary(
                '/zia.ai.longrunning.v1alpha1.Operations/GetOperation',
                request_serializer=longrunning_dot_v1alpha1_dot_operations__pb2.GetOperationRequest.SerializeToString,
                response_deserializer=longrunning_dot_v1alpha1_dot_operations__pb2.GetOperationResponse.FromString,
                )


class OperationsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOperation(self, request, context):
        """Get the status of an operation, including its result or error if has completed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OperationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOperation,
                    request_deserializer=longrunning_dot_v1alpha1_dot_operations__pb2.GetOperationRequest.FromString,
                    response_serializer=longrunning_dot_v1alpha1_dot_operations__pb2.GetOperationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'zia.ai.longrunning.v1alpha1.Operations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Operations(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zia.ai.longrunning.v1alpha1.Operations/GetOperation',
            longrunning_dot_v1alpha1_dot_operations__pb2.GetOperationRequest.SerializeToString,
            longrunning_dot_v1alpha1_dot_operations__pb2.GetOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
