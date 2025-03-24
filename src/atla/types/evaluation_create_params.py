# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .metrics.few_shot_example_param import FewShotExampleParam

__all__ = ["EvaluationCreateParams"]


class EvaluationCreateParams(TypedDict, total=False):
    model_id: Required[str]
    """The ID or name of the Atla evaluator model to use.

    This may point to a specific model version or a model family. If a model family
    is provided, the default model version for that family will be used.
    """

    model_input: Required[str]
    """The input given to a model which produced the `model_output` to be evaluated."""

    model_output: Required[str]
    """The output of the model which is being evaluated.

    This is the `model_output` from the `model_input`.
    """

    evaluation_criteria: Optional[str]
    """The criteria used to evaluate the `model_output`.

    Only one of `evaluation_criteria` or `metric_name` can be provided.
    """

    expected_model_output: Optional[str]
    """
    An optional reference ("ground-truth" / "gold standard") answer against which to
    evaluate the `model_output`.
    """

    few_shot_examples: Iterable[FewShotExampleParam]
    """A list of few-shot examples for the evaluation."""

    metric_name: Optional[str]
    """The name of the metric to use for the evaluation.

    Only one of `evaluation_criteria` or `metric_name` can be provided.
    """

    model_context: Optional[str]
    """
    Any additional context provided to the model which received the `model_input`
    and produced the `model_output`.
    """

    prompt_version: Optional[int]
    """The version of the prompt to use for the evaluation.

    If not provided, the active prompt version will be used.
    """
