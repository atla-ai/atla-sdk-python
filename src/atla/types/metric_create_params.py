# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MetricCreateParams"]


class MetricCreateParams(TypedDict, total=False):
    metric_type: Required[Literal["binary", "likert_1_to_5"]]
    """The type of metric."""

    name: Required[str]
    """The name of the metric.

    Metric names must contain only lowercase letters, numbers, hyphens, or
    underscores, and must start with a lowercase letter and end with either a
    lowercase letter or number. Metric names must be unique within a project.
    """

    description: Optional[str]
    """An optional description of the metric."""

    required_fields: List[Literal["model_input", "model_output", "model_context", "expected_model_output"]]
    """The fields that are required for the metric.

    All metrics must require at least `model_input` and `model_output`, which are
    the default values.
    """
