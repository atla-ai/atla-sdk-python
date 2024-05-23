# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EvaluateParams"]


class EvaluateParams(TypedDict, total=False):
    context: Required[Optional[str]]

    input: Required[Union[str, Iterable[Dict[str, str]]]]

    metrics: Required[List[str]]

    reference: Required[Optional[str]]

    response: Required[str]

    model: Optional[str]
