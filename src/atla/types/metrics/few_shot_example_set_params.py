# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .few_shot_example_param import FewShotExampleParam

__all__ = ["FewShotExampleSetParams"]


class FewShotExampleSetParams(TypedDict, total=False):
    few_shot_examples: Required[Iterable[FewShotExampleParam]]
    """The few-shot examples to upsert."""
