# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._compat import PYDANTIC_V2, ConfigDict
from ..._models import BaseModel

__all__ = ["FewShotExample"]


class FewShotExample(BaseModel):
    model_input: str
    """The input to the model for the few-shot example."""

    model_output: str
    """The output from the model for the few-shot example."""

    score: str
    """The score for the few-shot example."""

    critique: Optional[str] = None
    """The critique for the few-shot example."""

    expected_model_output: Optional[str] = None
    """The expected output from the model for the few-shot example."""

    model_context: Optional[str] = None
    """The context for the few-shot example."""

    if PYDANTIC_V2:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())
