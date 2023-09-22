import os

from .humanfirst.protobuf.external_integration.v1alpha1 import workspace_pb2, workspace_pb2_grpc
from .humanfirst.protobuf.playbook.data.config.v1alpha1 import config_pb2

class WorkspaceService(workspace_pb2_grpc.WorkspacesServicer):
    """
    This is a demonstration workspace service that can read and write HF json files from a local directory, and make them available for use
    via the integration.
    """

    def __init__(self, base_path: str) -> None:
        """
        base_path: The directory where the HF json files are stored.
        """
        super().__init__()
        self.base_path = base_path
        self.data_format = config_pb2.IntentsDataFormat.INTENTS_FORMAT_HF_JSON
        self.format_options = config_pb2.IntentsDataOptions(
            hierarchical_intent_name_disabled=False,
            hierarchical_delimiter="",
            zip_encoding=False,
            gzip_encoding=False,
            hierarchical_follow_up=False,
            include_negative_phrases=False,
            intent_tag_predicate=None,
            phrase_tag_predicate=None,
            skip_empty_intents=False,
        )
    def ListWorkspaces(self, request: workspace_pb2.ListWorkspacesRequest, context) -> workspace_pb2.ListWorkspacesResponse:
        # List json files inside the base directory
        workspaces = []
        for filename in os.listdir(self.base_path):
            if filename.endswith('.json'):
                id = filename[:-5]
                workspaces.append(workspace_pb2.Workspace(id=id, name=id))

        return workspace_pb2.ListWorkspacesResponse(workspaces=workspaces)

    def GetWorkspace(self, request: workspace_pb2.GetWorkspaceRequest, context) -> workspace_pb2.Workspace:
        if os.path.exists(os.path.join(self.base_path, request.workspace_id + '.json')):
            return workspace_pb2.Workspace(id=request.workspace_id, name=request.workspace_id)
        else:
            raise RuntimeError("no such workspace")

    def CreateWorkspace(self, request: workspace_pb2.CreateWorkspaceRequest, context) -> workspace_pb2.Workspace:
        """
        Create a new workspace
        """

        # Create a new workspace
        with open(os.path.join(self.base_path, request.workspace.name + '.json'), 'w') as f:
            f.write("{}")

        return workspace_pb2.Workspace(id=request.workspace.name, name=request.workspace.name)


    def GetImportParameters(self, request: workspace_pb2.GetImportParametersRequest, context) -> workspace_pb2.GetImportParametersResponse:
        """
        Indicate the data format in which the workspace data should be provided

        In this case, we specifically request the HF json format
        """

        return workspace_pb2.GetImportParametersResponse(data_format=self.data_format, format_options=self.format_options)

    def ImportWorkspace(self, request: workspace_pb2.ImportWorkspaceRequest, context) -> workspace_pb2.ImportWorkspaceResponse:
        """
        Import a workspace into the integration, from the provided data exported from Studio
        """

        # Write the HF json data to a file (in the real world, you would want to make sure there are no path injection attempts)
        with open(os.path.join(self.base_path, request.workspace_id + '.json'), 'wb') as f:
            f.write(request.data)

        return workspace_pb2.ImportWorkspaceResponse()

    def ExportWorkspace(self, request: workspace_pb2.ExportWorkspaceRequest, context) -> workspace_pb2.ExportWorkspaceResponse:
        """
        Exports a workspace from the integration, importing it into Studio
        """
        # Read the HF json data from the file
        with open(os.path.join(self.base_path, request.workspace_id + '.json'), 'rb') as f:
            return workspace_pb2.ExportWorkspaceResponse(
                data_format=config_pb2.IntentsDataFormat.INTENTS_FORMAT_HF_JSON,
                format_options=self.format_options,
                data=f.read(),
            )
