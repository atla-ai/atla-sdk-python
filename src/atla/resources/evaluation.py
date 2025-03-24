# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import evaluation_create_params
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
from .._base_client import make_request_options
from ..types.evaluation import Evaluation
from ..types.metrics.few_shot_example_param import FewShotExampleParam

__all__ = ["EvaluationResource", "AsyncEvaluationResource"]


class EvaluationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#with_streaming_response
        """
        return EvaluationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model_id: str,
        model_input: str,
        model_output: str,
        evaluation_criteria: Optional[str] | NotGiven = NOT_GIVEN,
        expected_model_output: Optional[str] | NotGiven = NOT_GIVEN,
        few_shot_examples: Iterable[FewShotExampleParam] | NotGiven = NOT_GIVEN,
        metric_name: Optional[str] | NotGiven = NOT_GIVEN,
        model_context: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_version: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Evaluation:
        """
        Run an evaluation directly via the Atla evaluation service.

        Args:
          model_id: The ID or name of the Atla evaluator model to use. This may point to a specific
              model version or a model family. If a model family is provided, the default
              model version for that family will be used.

          model_input: The input given to a model which produced the `model_output` to be evaluated.

          model_output: The output of the model which is being evaluated. This is the `model_output`
              from the `model_input`.

          evaluation_criteria: The criteria used to evaluate the `model_output`. Only one of
              `evaluation_criteria` or `metric_name` can be provided.

          expected_model_output: An optional reference ("ground-truth" / "gold standard") answer against which to
              evaluate the `model_output`.

          few_shot_examples: A list of few-shot examples for the evaluation.

          metric_name: The name of the metric to use for the evaluation. Only one of
              `evaluation_criteria` or `metric_name` can be provided.

          model_context: Any additional context provided to the model which received the `model_input`
              and produced the `model_output`.

          prompt_version: The version of the prompt to use for the evaluation. If not provided, the active
              prompt version will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/eval",
            body=maybe_transform(
                {
                    "model_id": model_id,
                    "model_input": model_input,
                    "model_output": model_output,
                    "evaluation_criteria": evaluation_criteria,
                    "expected_model_output": expected_model_output,
                    "few_shot_examples": few_shot_examples,
                    "metric_name": metric_name,
                    "model_context": model_context,
                    "prompt_version": prompt_version,
                },
                evaluation_create_params.EvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Evaluation,
        )


class AsyncEvaluationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#with_streaming_response
        """
        return AsyncEvaluationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model_id: str,
        model_input: str,
        model_output: str,
        evaluation_criteria: Optional[str] | NotGiven = NOT_GIVEN,
        expected_model_output: Optional[str] | NotGiven = NOT_GIVEN,
        few_shot_examples: Iterable[FewShotExampleParam] | NotGiven = NOT_GIVEN,
        metric_name: Optional[str] | NotGiven = NOT_GIVEN,
        model_context: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_version: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Evaluation:
        """
        Run an evaluation directly via the Atla evaluation service.

        Args:
          model_id: The ID or name of the Atla evaluator model to use. This may point to a specific
              model version or a model family. If a model family is provided, the default
              model version for that family will be used.

          model_input: The input given to a model which produced the `model_output` to be evaluated.

          model_output: The output of the model which is being evaluated. This is the `model_output`
              from the `model_input`.

          evaluation_criteria: The criteria used to evaluate the `model_output`. Only one of
              `evaluation_criteria` or `metric_name` can be provided.

          expected_model_output: An optional reference ("ground-truth" / "gold standard") answer against which to
              evaluate the `model_output`.

          few_shot_examples: A list of few-shot examples for the evaluation.

          metric_name: The name of the metric to use for the evaluation. Only one of
              `evaluation_criteria` or `metric_name` can be provided.

          model_context: Any additional context provided to the model which received the `model_input`
              and produced the `model_output`.

          prompt_version: The version of the prompt to use for the evaluation. If not provided, the active
              prompt version will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/eval",
            body=await async_maybe_transform(
                {
                    "model_id": model_id,
                    "model_input": model_input,
                    "model_output": model_output,
                    "evaluation_criteria": evaluation_criteria,
                    "expected_model_output": expected_model_output,
                    "few_shot_examples": few_shot_examples,
                    "metric_name": metric_name,
                    "model_context": model_context,
                    "prompt_version": prompt_version,
                },
                evaluation_create_params.EvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Evaluation,
        )


class EvaluationResourceWithRawResponse:
    def __init__(self, evaluation: EvaluationResource) -> None:
        self._evaluation = evaluation

        self.create = to_raw_response_wrapper(
            evaluation.create,
        )


class AsyncEvaluationResourceWithRawResponse:
    def __init__(self, evaluation: AsyncEvaluationResource) -> None:
        self._evaluation = evaluation

        self.create = async_to_raw_response_wrapper(
            evaluation.create,
        )


class EvaluationResourceWithStreamingResponse:
    def __init__(self, evaluation: EvaluationResource) -> None:
        self._evaluation = evaluation

        self.create = to_streamed_response_wrapper(
            evaluation.create,
        )


class AsyncEvaluationResourceWithStreamingResponse:
    def __init__(self, evaluation: AsyncEvaluationResource) -> None:
        self._evaluation = evaluation

        self.create = async_to_streamed_response_wrapper(
            evaluation.create,
        )
