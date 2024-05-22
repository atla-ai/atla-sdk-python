# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["EvaluationCreateResponse", "Evaluations", "Usage"]


class Evaluations(BaseModel):
    critique: object

    score: int


class Usage(BaseModel):
    evaluation_tokens: int

    prompt_tokens: int

    total_tokens: int


class EvaluationCreateResponse(BaseModel):
    id: str

    evaluations: Dict[str, Evaluations]

    model: str

    usage: Usage

    created: Optional[int] = None
