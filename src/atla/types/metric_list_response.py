# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .metric import Metric
from .._models import BaseModel

__all__ = ["MetricListResponse"]


class MetricListResponse(BaseModel):
    metrics: List[Metric]
    """The metrics retrieved."""

    request_id: str
    """The ID of the request the response is for."""

    status: Optional[Literal["success"]] = None
