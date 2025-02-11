# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EvaluationCreateParams", "FewShotExample"]


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

    expected_model_output: str
    """
    An optional reference ("ground-truth" / "gold standard") answer against which to
    evaluate the `model_output`.
    """

    few_shot_examples: Iterable[FewShotExample]
    """A list of few-shot examples for the evaluation."""

    metric_name: Optional[str]
    """The name of the metric to use for the evaluation.

    Only one of `evaluation_criteria` or `metric_name` can be provided.
    """

    model_context: str
    """
    Any additional context provided to the model which received the `model_input`
    and produced the `model_output`.
    """


class FewShotExample(TypedDict, total=False):
    model_input: Required[str]
    """The input given to a model which produced the `model_output` to be evaluated."""

    model_output: Required[str]
    """The output of the model which is being evaluated.

    This is the `model_output` from the `model_input`.
    """

    score: Required[str]
    """A value representing the evaluation result."""

    critique: Optional[str]
    """An optional explanation of the evaluation."""

    expected_model_output: str
    """
    An optional reference ("ground-truth" / "gold standard") answer against which to
    evaluate the `model_output`.
    """

    model_context: str
    """
    Any additional context provided to the model which received the `model_input`
    and produced the `model_output`.
    """
