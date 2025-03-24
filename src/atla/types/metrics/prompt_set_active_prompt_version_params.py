# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PromptSetActivePromptVersionParams"]


class PromptSetActivePromptVersionParams(TypedDict, total=False):
    version: Required[int]
    """The version of the prompt to set as active."""
