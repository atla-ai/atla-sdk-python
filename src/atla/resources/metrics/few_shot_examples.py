# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.metrics import few_shot_example_set_params
from ...types.metrics.few_shot_example_param import FewShotExampleParam
from ...types.metrics.few_shot_example_set_response import FewShotExampleSetResponse

__all__ = ["FewShotExamplesResource", "AsyncFewShotExamplesResource"]


class FewShotExamplesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FewShotExamplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FewShotExamplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FewShotExamplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#with_streaming_response
        """
        return FewShotExamplesResourceWithStreamingResponse(self)

    def set(
        self,
        metric_id: str,
        *,
        few_shot_examples: Iterable[FewShotExampleParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FewShotExampleSetResponse:
        """
        Set few-shot examples for a metric.

        Args:
          metric_id: The ID of the metric to set few-shot examples for.

          few_shot_examples: The few-shot examples to upsert.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return self._put(
            f"/v1/metrics/{metric_id}/few_shot_examples",
            body=maybe_transform(
                {"few_shot_examples": few_shot_examples}, few_shot_example_set_params.FewShotExampleSetParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FewShotExampleSetResponse,
        )


class AsyncFewShotExamplesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFewShotExamplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFewShotExamplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFewShotExamplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#with_streaming_response
        """
        return AsyncFewShotExamplesResourceWithStreamingResponse(self)

    async def set(
        self,
        metric_id: str,
        *,
        few_shot_examples: Iterable[FewShotExampleParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FewShotExampleSetResponse:
        """
        Set few-shot examples for a metric.

        Args:
          metric_id: The ID of the metric to set few-shot examples for.

          few_shot_examples: The few-shot examples to upsert.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return await self._put(
            f"/v1/metrics/{metric_id}/few_shot_examples",
            body=await async_maybe_transform(
                {"few_shot_examples": few_shot_examples}, few_shot_example_set_params.FewShotExampleSetParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FewShotExampleSetResponse,
        )


class FewShotExamplesResourceWithRawResponse:
    def __init__(self, few_shot_examples: FewShotExamplesResource) -> None:
        self._few_shot_examples = few_shot_examples

        self.set = to_raw_response_wrapper(
            few_shot_examples.set,
        )


class AsyncFewShotExamplesResourceWithRawResponse:
    def __init__(self, few_shot_examples: AsyncFewShotExamplesResource) -> None:
        self._few_shot_examples = few_shot_examples

        self.set = async_to_raw_response_wrapper(
            few_shot_examples.set,
        )


class FewShotExamplesResourceWithStreamingResponse:
    def __init__(self, few_shot_examples: FewShotExamplesResource) -> None:
        self._few_shot_examples = few_shot_examples

        self.set = to_streamed_response_wrapper(
            few_shot_examples.set,
        )


class AsyncFewShotExamplesResourceWithStreamingResponse:
    def __init__(self, few_shot_examples: AsyncFewShotExamplesResource) -> None:
        self._few_shot_examples = few_shot_examples

        self.set = async_to_streamed_response_wrapper(
            few_shot_examples.set,
        )
