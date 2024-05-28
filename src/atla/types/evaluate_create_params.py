# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EvaluateCreateParams"]


class EvaluateCreateParams(TypedDict, total=False):
    input: Required[Union[str, Iterable[Dict[str, str]]]]

    metrics: Required[List[str]]

    response: Required[str]

    context: Optional[str]

    model: str

    reference: Optional[str]
