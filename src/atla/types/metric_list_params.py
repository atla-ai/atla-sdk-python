# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MetricListParams"]


class MetricListParams(TypedDict, total=False):
    include_default: bool
    """Whether to include default metrics."""
