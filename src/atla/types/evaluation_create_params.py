# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "EvaluationCreateParams",
    "Config",
    "ConfigCriteria",
    "ConfigCriteriaDirectEvaluationCriteriaConfig",
    "ConfigCriteriaMetricBasedEvaluationCriteriaConfig",
    "ConfigFewShotExample",
    "ConfigFewShotExampleEvalInputs",
    "ConfigFewShotExampleEvaluation",
    "Inputs",
]


class EvaluationCreateParams(TypedDict, total=False):
    config: Required[Config]
    """The configuration for the evaluation request."""

    inputs: Required[Inputs]
    """The inputs for the evaluation request."""

    model_id: Required[str]
    """The ID or name of the Atla evaluator model to use.

    This may point to a specific model version or a model family. If a model family
    is provided, the default model version for that family will be used.
    """


class ConfigCriteriaDirectEvaluationCriteriaConfig(TypedDict, total=False):
    evaluation_criteria: Required[str]
    """The criteria used to evaluate the `model_output`."""

    type: Literal["direct"]


class ConfigCriteriaMetricBasedEvaluationCriteriaConfig(TypedDict, total=False):
    metric_name: Required[str]
    """The name of the metric to use for the evaluation."""

    prompt_version: Optional[int]
    """The version of the prompt to use for the evaluation.

    If not set, the active prompt for the metric will be used.
    """

    type: Literal["metric"]


ConfigCriteria: TypeAlias = Union[
    ConfigCriteriaDirectEvaluationCriteriaConfig, ConfigCriteriaMetricBasedEvaluationCriteriaConfig
]


class ConfigFewShotExampleEvalInputs(TypedDict, total=False):
    model_input: Required[str]
    """The input given to a model which produced the `model_output` to be evaluated."""

    model_output: Required[str]
    """The output of the model which is being evaluated.

    This is the `model_output` from the `model_input`.
    """

    expected_model_output: Optional[str]
    """
    An optional reference ("ground-truth" / "gold standard") answer against which to
    evaluate the `model_output`.
    """

    model_context: Optional[str]
    """
    Any additional context provided to the model which received the `model_input`
    and produced the `model_output`.
    """


class ConfigFewShotExampleEvaluation(TypedDict, total=False):
    critique: Required[Optional[str]]
    """An optional explanation of the evaluation."""

    score: Required[float]
    """A numeric value representing the evaluation result."""


class ConfigFewShotExample(TypedDict, total=False):
    eval_inputs: Required[ConfigFewShotExampleEvalInputs]
    """The complete set of inputs for this example evaluation."""

    evaluation: Required[ConfigFewShotExampleEvaluation]
    """The demonstration evaluation results for these inputs."""


class Config(TypedDict, total=False):
    criteria: Required[ConfigCriteria]
    """Configuration for direct evaluation criteria."""

    few_shot_examples: Optional[Iterable[ConfigFewShotExample]]
    """Optional few-shot examples to guide the evaluation."""


class Inputs(TypedDict, total=False):
    model_input: Required[str]
    """The input given to a model which produced the `model_output` to be evaluated."""

    model_output: Required[str]
    """The output of the model which is being evaluated.

    This is the `model_output` from the `model_input`.
    """

    expected_model_output: Optional[str]
    """
    An optional reference ("ground-truth" / "gold standard") answer against which to
    evaluate the `model_output`.
    """

    model_context: Optional[str]
    """
    Any additional context provided to the model which received the `model_input`
    and produced the `model_output`.
    """
