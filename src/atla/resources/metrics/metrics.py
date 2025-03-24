# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...types import metric_list_params, metric_create_params
from .prompts import (
    PromptsResource,
    AsyncPromptsResource,
    PromptsResourceWithRawResponse,
    AsyncPromptsResourceWithRawResponse,
    PromptsResourceWithStreamingResponse,
    AsyncPromptsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .few_shot_examples import (
    FewShotExamplesResource,
    AsyncFewShotExamplesResource,
    FewShotExamplesResourceWithRawResponse,
    AsyncFewShotExamplesResourceWithRawResponse,
    FewShotExamplesResourceWithStreamingResponse,
    AsyncFewShotExamplesResourceWithStreamingResponse,
)
from ...types.metric_get_response import MetricGetResponse
from ...types.metric_list_response import MetricListResponse
from ...types.metric_create_response import MetricCreateResponse
from ...types.metric_delete_response import MetricDeleteResponse

__all__ = ["MetricsResource", "AsyncMetricsResource"]


class MetricsResource(SyncAPIResource):
    @cached_property
    def prompts(self) -> PromptsResource:
        return PromptsResource(self._client)

    @cached_property
    def few_shot_examples(self) -> FewShotExamplesResource:
        return FewShotExamplesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#with_streaming_response
        """
        return MetricsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        metric_type: Literal["binary", "likert_1_to_5"],
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        required_fields: List[Literal["model_input", "model_output", "model_context", "expected_model_output"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetricCreateResponse:
        """
        Create a new metric.

        Args:
          metric_type: The type of metric.

          name: The name of the metric. Metric names must contain only lowercase letters,
              numbers, hyphens, or underscores, and must start with a lowercase letter and end
              with either a lowercase letter or number. Metric names must be unique within a
              project.

          description: An optional description of the metric.

          required_fields: The fields that are required for the metric. All metrics must require at least
              `model_input` and `model_output`, which are the default values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/metrics",
            body=maybe_transform(
                {
                    "metric_type": metric_type,
                    "name": name,
                    "description": description,
                    "required_fields": required_fields,
                },
                metric_create_params.MetricCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricCreateResponse,
        )

    def list(
        self,
        *,
        include_default: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetricListResponse:
        """List all metrics for a project.

        Optionally include Atla default metrics that the
        project has access to.

        Args:
          include_default: Whether to include default metrics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_default": include_default}, metric_list_params.MetricListParams),
            ),
            cast_to=MetricListResponse,
        )

    def delete(
        self,
        metric_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetricDeleteResponse:
        """
        Delete a metric by ID.

        Args:
          metric_id: The ID of the metric to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return self._delete(
            f"/v1/metrics/{metric_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricDeleteResponse,
        )

    def get(
        self,
        metric_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetricGetResponse:
        """
        Get a metric by ID.

        Args:
          metric_id: The ID of the metric to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return self._get(
            f"/v1/metrics/{metric_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGetResponse,
        )


class AsyncMetricsResource(AsyncAPIResource):
    @cached_property
    def prompts(self) -> AsyncPromptsResource:
        return AsyncPromptsResource(self._client)

    @cached_property
    def few_shot_examples(self) -> AsyncFewShotExamplesResource:
        return AsyncFewShotExamplesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#with_streaming_response
        """
        return AsyncMetricsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        metric_type: Literal["binary", "likert_1_to_5"],
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        required_fields: List[Literal["model_input", "model_output", "model_context", "expected_model_output"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetricCreateResponse:
        """
        Create a new metric.

        Args:
          metric_type: The type of metric.

          name: The name of the metric. Metric names must contain only lowercase letters,
              numbers, hyphens, or underscores, and must start with a lowercase letter and end
              with either a lowercase letter or number. Metric names must be unique within a
              project.

          description: An optional description of the metric.

          required_fields: The fields that are required for the metric. All metrics must require at least
              `model_input` and `model_output`, which are the default values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/metrics",
            body=await async_maybe_transform(
                {
                    "metric_type": metric_type,
                    "name": name,
                    "description": description,
                    "required_fields": required_fields,
                },
                metric_create_params.MetricCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricCreateResponse,
        )

    async def list(
        self,
        *,
        include_default: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetricListResponse:
        """List all metrics for a project.

        Optionally include Atla default metrics that the
        project has access to.

        Args:
          include_default: Whether to include default metrics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_default": include_default}, metric_list_params.MetricListParams
                ),
            ),
            cast_to=MetricListResponse,
        )

    async def delete(
        self,
        metric_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetricDeleteResponse:
        """
        Delete a metric by ID.

        Args:
          metric_id: The ID of the metric to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return await self._delete(
            f"/v1/metrics/{metric_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricDeleteResponse,
        )

    async def get(
        self,
        metric_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetricGetResponse:
        """
        Get a metric by ID.

        Args:
          metric_id: The ID of the metric to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return await self._get(
            f"/v1/metrics/{metric_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGetResponse,
        )


class MetricsResourceWithRawResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.create = to_raw_response_wrapper(
            metrics.create,
        )
        self.list = to_raw_response_wrapper(
            metrics.list,
        )
        self.delete = to_raw_response_wrapper(
            metrics.delete,
        )
        self.get = to_raw_response_wrapper(
            metrics.get,
        )

    @cached_property
    def prompts(self) -> PromptsResourceWithRawResponse:
        return PromptsResourceWithRawResponse(self._metrics.prompts)

    @cached_property
    def few_shot_examples(self) -> FewShotExamplesResourceWithRawResponse:
        return FewShotExamplesResourceWithRawResponse(self._metrics.few_shot_examples)


class AsyncMetricsResourceWithRawResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.create = async_to_raw_response_wrapper(
            metrics.create,
        )
        self.list = async_to_raw_response_wrapper(
            metrics.list,
        )
        self.delete = async_to_raw_response_wrapper(
            metrics.delete,
        )
        self.get = async_to_raw_response_wrapper(
            metrics.get,
        )

    @cached_property
    def prompts(self) -> AsyncPromptsResourceWithRawResponse:
        return AsyncPromptsResourceWithRawResponse(self._metrics.prompts)

    @cached_property
    def few_shot_examples(self) -> AsyncFewShotExamplesResourceWithRawResponse:
        return AsyncFewShotExamplesResourceWithRawResponse(self._metrics.few_shot_examples)


class MetricsResourceWithStreamingResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.create = to_streamed_response_wrapper(
            metrics.create,
        )
        self.list = to_streamed_response_wrapper(
            metrics.list,
        )
        self.delete = to_streamed_response_wrapper(
            metrics.delete,
        )
        self.get = to_streamed_response_wrapper(
            metrics.get,
        )

    @cached_property
    def prompts(self) -> PromptsResourceWithStreamingResponse:
        return PromptsResourceWithStreamingResponse(self._metrics.prompts)

    @cached_property
    def few_shot_examples(self) -> FewShotExamplesResourceWithStreamingResponse:
        return FewShotExamplesResourceWithStreamingResponse(self._metrics.few_shot_examples)


class AsyncMetricsResourceWithStreamingResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.create = async_to_streamed_response_wrapper(
            metrics.create,
        )
        self.list = async_to_streamed_response_wrapper(
            metrics.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            metrics.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            metrics.get,
        )

    @cached_property
    def prompts(self) -> AsyncPromptsResourceWithStreamingResponse:
        return AsyncPromptsResourceWithStreamingResponse(self._metrics.prompts)

    @cached_property
    def few_shot_examples(self) -> AsyncFewShotExamplesResourceWithStreamingResponse:
        return AsyncFewShotExamplesResourceWithStreamingResponse(self._metrics.few_shot_examples)
