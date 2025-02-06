# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Evaluation", "Result", "ResultEvaluation"]


class ResultEvaluation(BaseModel):
    critique: str
    """The critique of the evaluation."""

    score: float
    """A numeric value representing the evaluation result."""


class Result(BaseModel):
    evaluation: ResultEvaluation
    """The evaluation results."""

    api_model_id: str = FieldInfo(alias="model_id")
    """The ID of the Atla evaluator model used."""


class Evaluation(BaseModel):
    request_id: str
    """The ID of the request the response is for."""

    result: Result
    """The result of the evaluation."""

    status: Optional[Literal["success", "error"]] = None
    """Response status enum."""
