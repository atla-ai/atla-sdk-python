# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MetricCreateResponse"]


class MetricCreateResponse(BaseModel):
    metric_id: str
    """The ID of the created metric."""

    request_id: str
    """The ID of the request the response is for."""

    status: Optional[Literal["success"]] = None
