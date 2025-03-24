# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metrics.prompt import Prompt
from .metrics.few_shot_example import FewShotExample

__all__ = ["Metric"]


class Metric(BaseModel):
    metric_type: Literal["binary", "likert_1_to_5"]
    """The type of metric."""

    name: str
    """The name of the metric.

    Metric names must contain only lowercase letters, numbers, hyphens, or
    underscores, and must start with a lowercase letter and end with either a
    lowercase letter or number. Metric names must be unique within a project.
    """

    project_id: Optional[str] = None
    """The ID of the project that the metric belongs to.

    If the metric is shared, this field will be `null`.
    """

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)
    """The ID of the metric in the database."""

    active_prompt_version: Optional[int] = None
    """The version of the prompt that is currently active for the metric."""

    created_at: Optional[datetime] = None
    """The creation time of the metric."""

    description: Optional[str] = None
    """An optional description of the metric."""

    few_shot_examples: Optional[List[FewShotExample]] = None
    """The few-shot examples for the metric. At most 3 examples are allowed."""

    prompts: Optional[Dict[str, Prompt]] = None
    """The prompts for the metric, keyed by version."""

    required_fields: Optional[
        List[Literal["model_input", "model_output", "model_context", "expected_model_output"]]
    ] = None
    """The fields that are required for the metric.

    All metrics must require at least `model_input` and `model_output`, which are
    the default values.
    """

    updated_at: Optional[datetime] = None
    """The last update time of the metric."""
