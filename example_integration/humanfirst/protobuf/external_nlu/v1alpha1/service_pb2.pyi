"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetSupportedEnginesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetSupportedEnginesRequest = GetSupportedEnginesRequest

class GetSupportedEnginesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENGINES_FIELD_NUMBER: builtins.int
    @property
    def engines(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Engine]: ...
    def __init__(
        self,
        *,
        engines: collections.abc.Iterable[global___Engine] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["engines", b"engines"]) -> None: ...

global___GetSupportedEnginesResponse = GetSupportedEnginesResponse

class TrainModelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENGINE_FIELD_NUMBER: builtins.int
    TRAINING_DATA_PATH_FIELD_NUMBER: builtins.int
    MODEL_OUTPUT_PATH_FIELD_NUMBER: builtins.int
    SKIP_LOAD_FIELD_NUMBER: builtins.int
    engine: builtins.str
    """Name of the NLU engine to use"""
    training_data_path: builtins.str
    """Local path to the training data, in the format specified by `EngineSpec.export_format`"""
    model_output_path: builtins.str
    """Local path to where the saved model should be located"""
    skip_load: builtins.bool
    """If set, do not return a model handle. It will be used to
    avoid loading the model in the event where the training process
    doesn't already yield an in-memory model.
    """
    def __init__(
        self,
        *,
        engine: builtins.str = ...,
        training_data_path: builtins.str = ...,
        model_output_path: builtins.str = ...,
        skip_load: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["engine", b"engine", "model_output_path", b"model_output_path", "skip_load", b"skip_load", "training_data_path", b"training_data_path"]) -> None: ...

global___TrainModelRequest = TrainModelRequest

class TrainModelResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_HANDLE_FIELD_NUMBER: builtins.int
    model_handle: builtins.int
    """A handle to the loaded model that was just trained
    Needs to be unloaded with UnloadModel
    """
    def __init__(
        self,
        *,
        model_handle: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["model_handle", b"model_handle"]) -> None: ...

global___TrainModelResponse = TrainModelResponse

class LoadModelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    path: builtins.str
    """Local path to the model to load"""
    def __init__(
        self,
        *,
        path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path", b"path"]) -> None: ...

global___LoadModelRequest = LoadModelRequest

class LoadModelResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_HANDLE_FIELD_NUMBER: builtins.int
    model_handle: builtins.int
    """Handle to the loaded model, valid for the lifetime of this connection"""
    def __init__(
        self,
        *,
        model_handle: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["model_handle", b"model_handle"]) -> None: ...

global___LoadModelResponse = LoadModelResponse

class BatchPredictRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_HANDLE_FIELD_NUMBER: builtins.int
    EXAMPLES_FIELD_NUMBER: builtins.int
    model_handle: builtins.int
    """Handle obtained from LoadModel"""
    @property
    def examples(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Example]:
        """Examples to predict using the loaded model, the order will be respected in the response"""
    def __init__(
        self,
        *,
        model_handle: builtins.int = ...,
        examples: collections.abc.Iterable[global___Example] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["examples", b"examples", "model_handle", b"model_handle"]) -> None: ...

global___BatchPredictRequest = BatchPredictRequest

class BatchPredictResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PREDICTIONS_FIELD_NUMBER: builtins.int
    @property
    def predictions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Predictions]:
        """List of predictions for the requested batch, this will contain as many elements
        as present in the `examples` request parameter.
        """
    def __init__(
        self,
        *,
        predictions: collections.abc.Iterable[global___Predictions] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["predictions", b"predictions"]) -> None: ...

global___BatchPredictResponse = BatchPredictResponse

class UnloadModelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_HANDLE_FIELD_NUMBER: builtins.int
    model_handle: builtins.int
    """Handle obtained from LoadModel"""
    def __init__(
        self,
        *,
        model_handle: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["model_handle", b"model_handle"]) -> None: ...

global___UnloadModelRequest = UnloadModelRequest

class UnloadModelResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UnloadModelResponse = UnloadModelResponse

class Engine(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Display name"""
    version: builtins.str
    """Version of the given engine, if available"""
    @property
    def spec(self) -> global___EngineSpec:
        """Technical specifications"""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        version: builtins.str = ...,
        spec: global___EngineSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "spec", b"spec", "version", b"version"]) -> None: ...

global___Engine = Engine

class EngineSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXPORT_FORMAT_FIELD_NUMBER: builtins.int
    export_format: builtins.int
    """If valid, the caller will provide the exported playbook into a format supported by the intent exporter
    Sync with zia.ai.playbook.data.config.v1alpha1.IntentsDataFormat
    """
    def __init__(
        self,
        *,
        export_format: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["export_format", b"export_format"]) -> None: ...

global___EngineSpec = EngineSpec

class Example(google.protobuf.message.Message):
    """Defines an example to be classified.
    For future proofing, this is in its own message to allow non-breaking spec changes
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENTS_FIELD_NUMBER: builtins.int
    contents: builtins.str
    def __init__(
        self,
        *,
        contents: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["contents", b"contents"]) -> None: ...

global___Example = Example

class Predictions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MATCHES_FIELD_NUMBER: builtins.int
    ENTITY_MATCHES_FIELD_NUMBER: builtins.int
    @property
    def matches(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___IntentMatch]:
        """Intent matches for this example"""
    @property
    def entity_matches(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityMatch]:
        """Entity matches for this example, if available"""
    def __init__(
        self,
        *,
        matches: collections.abc.Iterable[global___IntentMatch] | None = ...,
        entity_matches: collections.abc.Iterable[global___EntityMatch] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_matches", b"entity_matches", "matches", b"matches"]) -> None: ...

global___Predictions = Predictions

class IntentMatch(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """The intent id that was matched."""
    name: builtins.str
    """The name of the intent when the model was trained."""
    score: builtins.float
    """The probability of this being the right matched, as determined by the underlying model."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        score: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name", "score", b"score"]) -> None: ...

global___IntentMatch = IntentMatch

class EntityMatch(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENTITY_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    SPAN_FIELD_NUMBER: builtins.int
    EXTRACTOR_FIELD_NUMBER: builtins.int
    @property
    def entity(self) -> global___EntityReference:
        """The entity that was matched, with its parameters"""
    score: builtins.float
    """The confidence score for this match"""
    @property
    def span(self) -> global___Span:
        """The text span where this entity was found"""
    extractor: builtins.str
    """(Rasa specific) Name of the pipline component that found this entity"""
    def __init__(
        self,
        *,
        entity: global___EntityReference | None = ...,
        score: builtins.float = ...,
        span: global___Span | None = ...,
        extractor: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["entity", b"entity", "span", b"span"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity", b"entity", "extractor", b"extractor", "score", b"score", "span", b"span"]) -> None: ...

global___EntityMatch = EntityMatch

class EntityReference(google.protobuf.message.Message):
    """Sync from zia.ai.playbook.EntityReference"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    ENTITY_ID_FIELD_NUMBER: builtins.int
    ENTITY_VALUE_ID_FIELD_NUMBER: builtins.int
    key: builtins.str
    """Key by which we can refer to this entity in the utterance.
    Ex (rasa): `I'd like to visit [New York City](city)` where `city` is the key
    """
    text: builtins.str
    """Text used to reference the entity in the utterance
    Ex (rasa): `I'd like to visit [New York City](city)` where `New York City` is the text.
    """
    value: builtins.str
    """If the reference text isn't the main entity value, this value points to the right
    key value to use.

    For example, for a `city` entity, if a synonym was used, this value would contain the
    key value it refers to in the entity.

       (rasa long): I went to [NYC]{"entity": "city", "value": "New York City"}
                    where 'New York City' is the value

       (rasa short): I went to [NYC](city:New York City)
    """
    role: builtins.str
    """If entity has repeated usage in the utterance, assigns role for each usage
    Ex (rasa): I want to fly from [Berlin]{"entity": "city", "role": "departure"} to [San Francisco]{"entity": "city", "role": "destination"}.
    """
    entity_id: builtins.str
    """If available, our internal entity id"""
    entity_value_id: builtins.str
    """If available, our internal entity value id"""
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        text: builtins.str = ...,
        value: builtins.str = ...,
        role: builtins.str = ...,
        entity_id: builtins.str = ...,
        entity_value_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_id", b"entity_id", "entity_value_id", b"entity_value_id", "key", b"key", "role", b"role", "text", b"text", "value", b"value"]) -> None: ...

global___EntityReference = EntityReference

class Span(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_FIELD_NUMBER: builtins.int
    END_FIELD_NUMBER: builtins.int
    start: builtins.int
    """The start of this entity, as the utf8 byte index"""
    end: builtins.int
    """The end of this entity, as the utf8 byte index"""
    def __init__(
        self,
        *,
        start: builtins.int = ...,
        end: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["end", b"end", "start", b"start"]) -> None: ...

global___Span = Span
