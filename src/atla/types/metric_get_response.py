# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .metric import Metric
from .._models import BaseModel

__all__ = ["MetricGetResponse"]


class MetricGetResponse(BaseModel):
    metric: Metric
    """The metric retrieved."""

    request_id: str
    """The ID of the request the response is for."""

    status: Optional[Literal["success"]] = None
