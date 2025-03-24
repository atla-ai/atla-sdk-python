# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._compat import PYDANTIC_V2, ConfigDict
from .._models import BaseModel

__all__ = ["Evaluation", "Result", "ResultEvaluation"]


class ResultEvaluation(BaseModel):
    critique: str
    """The critique of the evaluation."""

    score: str
    """A value representing the evaluation result."""


class Result(BaseModel):
    evaluation: ResultEvaluation
    """The evaluation results."""

    model_id: str
    """The ID of the Atla evaluator model used."""

    if PYDANTIC_V2:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class Evaluation(BaseModel):
    request_id: str
    """The ID of the request the response is for."""

    result: Result
    """The result of the evaluation."""

    status: Optional[Literal["success"]] = None
