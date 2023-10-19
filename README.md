## Example custom integration
This repository contains an example custom integration that can be connected to a HumanFirst namespace in order to extend its functionality.

Custom integrations are a set of GRPC services that can be implemented by a third party in order to provide extensibility, there are currently two types of services that can be implemented: Workspace and Model.

### Workspace
A workspace integration allows importing and exporting data. Once a custom integration with workspace support is added, it appears in the "Import > From Integration" and "Export > From Integration" workflows, allowing the users to import/export directly from the user interface.

Typically, a such service would merge a workspace's data before exporting a workspace (HF only deals with training data, anything else needs to be reconciliated). While you can use any supported data format, using [HumanFirst JSON](https://docs.humanfirst.ai/docs/advanced/humanfirst-json/) is recommended because it is the most feature-complete export format available.

#### Import
The import-related methods in the service are called whenever an export is done from the application's perspective.

- The `ListWorkspaces` method is called so the user can select which workspace to target
- The `GetImportParameters` method is called in order for the `Import` call to receive data in the right format
- The `Import` method is called with the exported data in the right format

#### Export
The export-related methods in the service are called whenever an import is performed from the application's perspective.

- The `ListWorkspaces` method is called so the user can select which workspace to export
- The `Export` method is called, which returns the exported data, along with information around its data format.

### Model
A model integration allows training and evaluating NLU models, and optionally provide support for custom embedding models. The same abstraction handles both kinds of model since it's typical to use an embedding space as an intermediate latent representation inside a classification objective. 

## Creating a custom integration
Custom integrations use GRPC with Mutual TLS authentication. The [hf](https://github.com/zia-ai/humanfirst/releases?q=cli&expanded=true) command-line tool contains a command allowing you to create an integration and generate MTLS credentials simultaneously.

1. Download the [hf](https://github.com/zia-ai/humanfirst/releases?q=cli&expanded=true) command line tool
1. [Authenticate](https://docs.humanfirst.ai/docs/cli/overview#authenticating) using your HF account
1. Create the integration
    ```
    hf integrations create custom --workspace --name my-integration --address remote-host.example.com:8443 --key-out ./mtls-credentials.json
    ```
1. Launch the integration service: `poetry install && poetry run python3 -m example_integration.main ./mtls-credentials.json 0.0.0.0:8443`

You can also build a docker container for the integration and launch it directly:

```
docker build -t example-integration .
docker run -it --rm -v /tmp/hf:/tmp/hf -v $(pwd):/src -p 8443:8443 example-integration ./mtls-credentials.json 0.0.0.0:8443
```

The example workspace integration will read and write JSON files to `/tmp/hf` (it is not advised to run this example code in a production setting, because it lacks the proper path validation to prevent path injection vulnerabilities)


You may change the address of the integration's endpoint using `hf integrations set-address` (use `--help` for a usage example)
