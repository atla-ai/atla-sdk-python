# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Generic, TypeVar

from ._models import GenericModel

__all__ = ["EvaluationsWrapper"]

_T = TypeVar("_T")


class EvaluationsWrapper(GenericModel, Generic[_T]):
    evaluations: _T

    @staticmethod
    def _unwrapper(obj: "EvaluationsWrapper[_T]") -> _T:
        return obj.evaluations
