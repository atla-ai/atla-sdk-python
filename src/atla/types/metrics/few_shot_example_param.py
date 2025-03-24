# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FewShotExampleParam"]


class FewShotExampleParam(TypedDict, total=False):
    model_input: Required[str]
    """The input to the model for the few-shot example."""

    model_output: Required[str]
    """The output from the model for the few-shot example."""

    score: Required[str]
    """The score for the few-shot example."""

    critique: Optional[str]
    """The critique for the few-shot example."""

    expected_model_output: Optional[str]
    """The expected output from the model for the few-shot example."""

    model_context: Optional[str]
    """The context for the few-shot example."""
