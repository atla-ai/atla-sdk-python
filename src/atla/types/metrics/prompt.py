# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Prompt"]


class Prompt(BaseModel):
    content: str
    """The content of the prompt."""

    version: int
    """The version of the prompt."""

    created_at: Optional[datetime] = None
    """The creation time of the prompt."""

    updated_at: Optional[datetime] = None
    """The last update time of the prompt."""
