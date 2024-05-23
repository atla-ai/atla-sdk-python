# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional

import httpx

from ..types import evaluate_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.evaluate_response import EvaluateResponse

__all__ = ["EvaluateResource", "AsyncEvaluateResource"]


class EvaluateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluateResourceWithRawResponse:
        return EvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluateResourceWithStreamingResponse:
        return EvaluateResourceWithStreamingResponse(self)

    def _(
        self,
        *,
        context: Optional[str],
        input: Union[str, Iterable[Dict[str, str]]],
        metrics: List[str],
        reference: Optional[str],
        response: str,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResponse:
        """
        Creates a model evaluation for a given LLM input and response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/evaluate",
            body=maybe_transform(
                {
                    "context": context,
                    "input": input,
                    "metrics": metrics,
                    "reference": reference,
                    "response": response,
                    "model": model,
                },
                evaluate_params.EvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )


class AsyncEvaluateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluateResourceWithRawResponse:
        return AsyncEvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluateResourceWithStreamingResponse:
        return AsyncEvaluateResourceWithStreamingResponse(self)

    async def _(
        self,
        *,
        context: Optional[str],
        input: Union[str, Iterable[Dict[str, str]]],
        metrics: List[str],
        reference: Optional[str],
        response: str,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResponse:
        """
        Creates a model evaluation for a given LLM input and response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/evaluate",
            body=await async_maybe_transform(
                {
                    "context": context,
                    "input": input,
                    "metrics": metrics,
                    "reference": reference,
                    "response": response,
                    "model": model,
                },
                evaluate_params.EvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )


class EvaluateResourceWithRawResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self._ = to_raw_response_wrapper(
            evaluate._,
        )


class AsyncEvaluateResourceWithRawResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self._ = async_to_raw_response_wrapper(
            evaluate._,
        )


class EvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self._ = to_streamed_response_wrapper(
            evaluate._,
        )


class AsyncEvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self._ = async_to_streamed_response_wrapper(
            evaluate._,
        )
