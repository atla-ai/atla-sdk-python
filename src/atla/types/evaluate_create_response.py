# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["EvaluateCreateResponse", "EvaluateCreateResponseItem"]


class EvaluateCreateResponseItem(BaseModel):
    critique: object

    score: int


EvaluateCreateResponse = Dict[str, EvaluateCreateResponseItem]
