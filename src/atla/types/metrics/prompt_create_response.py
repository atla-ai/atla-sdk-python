# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PromptCreateResponse"]


class PromptCreateResponse(BaseModel):
    request_id: str
    """The ID of the request the response is for."""

    version: int
    """The version of the created prompt."""

    status: Optional[Literal["success"]] = None
