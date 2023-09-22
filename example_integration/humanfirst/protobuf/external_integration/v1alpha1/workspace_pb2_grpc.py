# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from external_integration.v1alpha1 import workspace_pb2 as external__integration_dot_v1alpha1_dot_workspace__pb2


class WorkspacesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListWorkspaces = channel.unary_unary(
                '/zia.ai.external_integration.v1alpha1.Workspaces/ListWorkspaces',
                request_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ListWorkspacesRequest.SerializeToString,
                response_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ListWorkspacesResponse.FromString,
                )
        self.GetWorkspace = channel.unary_unary(
                '/zia.ai.external_integration.v1alpha1.Workspaces/GetWorkspace',
                request_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.GetWorkspaceRequest.SerializeToString,
                response_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.Workspace.FromString,
                )
        self.CreateWorkspace = channel.unary_unary(
                '/zia.ai.external_integration.v1alpha1.Workspaces/CreateWorkspace',
                request_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.CreateWorkspaceRequest.SerializeToString,
                response_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.Workspace.FromString,
                )
        self.GetImportParameters = channel.unary_unary(
                '/zia.ai.external_integration.v1alpha1.Workspaces/GetImportParameters',
                request_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.GetImportParametersRequest.SerializeToString,
                response_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.GetImportParametersResponse.FromString,
                )
        self.ImportWorkspace = channel.unary_unary(
                '/zia.ai.external_integration.v1alpha1.Workspaces/ImportWorkspace',
                request_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ImportWorkspaceRequest.SerializeToString,
                response_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ImportWorkspaceResponse.FromString,
                )
        self.ExportWorkspace = channel.unary_unary(
                '/zia.ai.external_integration.v1alpha1.Workspaces/ExportWorkspace',
                request_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ExportWorkspaceRequest.SerializeToString,
                response_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ExportWorkspaceResponse.FromString,
                )


class WorkspacesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListWorkspaces(self, request, context):
        """Gets the workspaces supported by this integration
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWorkspace(self, request, context):
        """Get information about a specific workspace. The application may request unlisted workspaces if they are manually entered by the user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateWorkspace(self, request, context):
        """Creates a new blank workspace in order to import things
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetImportParameters(self, request, context):
        """Retrieves the parameters to use for an Export request (such as the expected workspace export format)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportWorkspace(self, request, context):
        """Imports a workspace into the integration. This is triggered by a workspace export from Studio.
        It can optionally reference an existing workspace, in which case the integration would replace the relevant part of the training data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportWorkspace(self, request, context):
        """Exports a workspace from the integration. This is triggered by a workspace import from Studio.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkspacesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListWorkspaces': grpc.unary_unary_rpc_method_handler(
                    servicer.ListWorkspaces,
                    request_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ListWorkspacesRequest.FromString,
                    response_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ListWorkspacesResponse.SerializeToString,
            ),
            'GetWorkspace': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWorkspace,
                    request_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.GetWorkspaceRequest.FromString,
                    response_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.Workspace.SerializeToString,
            ),
            'CreateWorkspace': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWorkspace,
                    request_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.CreateWorkspaceRequest.FromString,
                    response_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.Workspace.SerializeToString,
            ),
            'GetImportParameters': grpc.unary_unary_rpc_method_handler(
                    servicer.GetImportParameters,
                    request_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.GetImportParametersRequest.FromString,
                    response_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.GetImportParametersResponse.SerializeToString,
            ),
            'ImportWorkspace': grpc.unary_unary_rpc_method_handler(
                    servicer.ImportWorkspace,
                    request_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ImportWorkspaceRequest.FromString,
                    response_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ImportWorkspaceResponse.SerializeToString,
            ),
            'ExportWorkspace': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportWorkspace,
                    request_deserializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ExportWorkspaceRequest.FromString,
                    response_serializer=external__integration_dot_v1alpha1_dot_workspace__pb2.ExportWorkspaceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'zia.ai.external_integration.v1alpha1.Workspaces', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Workspaces(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListWorkspaces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zia.ai.external_integration.v1alpha1.Workspaces/ListWorkspaces',
            external__integration_dot_v1alpha1_dot_workspace__pb2.ListWorkspacesRequest.SerializeToString,
            external__integration_dot_v1alpha1_dot_workspace__pb2.ListWorkspacesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWorkspace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zia.ai.external_integration.v1alpha1.Workspaces/GetWorkspace',
            external__integration_dot_v1alpha1_dot_workspace__pb2.GetWorkspaceRequest.SerializeToString,
            external__integration_dot_v1alpha1_dot_workspace__pb2.Workspace.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateWorkspace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zia.ai.external_integration.v1alpha1.Workspaces/CreateWorkspace',
            external__integration_dot_v1alpha1_dot_workspace__pb2.CreateWorkspaceRequest.SerializeToString,
            external__integration_dot_v1alpha1_dot_workspace__pb2.Workspace.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetImportParameters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zia.ai.external_integration.v1alpha1.Workspaces/GetImportParameters',
            external__integration_dot_v1alpha1_dot_workspace__pb2.GetImportParametersRequest.SerializeToString,
            external__integration_dot_v1alpha1_dot_workspace__pb2.GetImportParametersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ImportWorkspace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zia.ai.external_integration.v1alpha1.Workspaces/ImportWorkspace',
            external__integration_dot_v1alpha1_dot_workspace__pb2.ImportWorkspaceRequest.SerializeToString,
            external__integration_dot_v1alpha1_dot_workspace__pb2.ImportWorkspaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportWorkspace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zia.ai.external_integration.v1alpha1.Workspaces/ExportWorkspace',
            external__integration_dot_v1alpha1_dot_workspace__pb2.ExportWorkspaceRequest.SerializeToString,
            external__integration_dot_v1alpha1_dot_workspace__pb2.ExportWorkspaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)