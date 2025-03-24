# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .prompt import Prompt
from ..._models import BaseModel

__all__ = ["PromptListResponse"]


class PromptListResponse(BaseModel):
    prompts: List[Prompt]
    """The prompts retrieved."""

    request_id: str
    """The ID of the request the response is for."""

    status: Optional[Literal["success"]] = None
