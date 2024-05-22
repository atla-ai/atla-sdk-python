# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional

import httpx

from ..types import method_evaluate_params
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
from ..types.method_evaluate_response import MethodEvaluateResponse

__all__ = ["MethodsResource", "AsyncMethodsResource"]


class MethodsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MethodsResourceWithRawResponse:
        return MethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MethodsResourceWithStreamingResponse:
        return MethodsResourceWithStreamingResponse(self)

    def evaluate(
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
    ) -> MethodEvaluateResponse:
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
                method_evaluate_params.MethodEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MethodEvaluateResponse,
        )


class AsyncMethodsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMethodsResourceWithRawResponse:
        return AsyncMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMethodsResourceWithStreamingResponse:
        return AsyncMethodsResourceWithStreamingResponse(self)

    async def evaluate(
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
    ) -> MethodEvaluateResponse:
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
                method_evaluate_params.MethodEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MethodEvaluateResponse,
        )


class MethodsResourceWithRawResponse:
    def __init__(self, methods: MethodsResource) -> None:
        self._methods = methods

        self.evaluate = to_raw_response_wrapper(
            methods.evaluate,
        )


class AsyncMethodsResourceWithRawResponse:
    def __init__(self, methods: AsyncMethodsResource) -> None:
        self._methods = methods

        self.evaluate = async_to_raw_response_wrapper(
            methods.evaluate,
        )


class MethodsResourceWithStreamingResponse:
    def __init__(self, methods: MethodsResource) -> None:
        self._methods = methods

        self.evaluate = to_streamed_response_wrapper(
            methods.evaluate,
        )


class AsyncMethodsResourceWithStreamingResponse:
    def __init__(self, methods: AsyncMethodsResource) -> None:
        self._methods = methods

        self.evaluate = async_to_streamed_response_wrapper(
            methods.evaluate,
        )
