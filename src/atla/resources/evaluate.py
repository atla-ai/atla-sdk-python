# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional

import httpx

from ..types import evaluate_create_params
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

from ..types.evaluate import Evaluate

__all__ = ["EvaluateResource", "AsyncEvaluateResource"]


class EvaluateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluateResourceWithRawResponse:
        return EvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluateResourceWithStreamingResponse:
        return EvaluateResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: Union[str, Iterable[Dict[str, str]]],
        metrics: List[str],
        response: str,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        reference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Evaluate:
        """
        Create Evaluation

        Args:
          input: Input messages to evaluate the assistant's response for.

              Atla will evaluate an AI response based on the input message that was used to
              generate the response. Typically the input message is a single question or
              prompt used within some context.

              Example with a single input message:

              ```
              Is it permissible for a cookie banner to obscure the imprint?
              ```

              Atla is able to generate an evaluation for multi-turn input messages, typically
              a conversation. The input message should be a list of alternating `user` and
              `assistant` messages.Each message should be a dictionary with a `role` and
              `content` key.

              Example with multiple conversational turns:

              ```
              [
                  {"role": "user", "content": "Is it permissible for a cookie banner to obscure the imprint?"},
                  {
                      "role": "assistant",
                      "content": "I could not find a specific source addressing the permissibility of a cookie banner obscuring the imprint.",
                  },
              ]
              ```

          metrics: Metrics to evaluate on.

              Our models have been trained to evaluate on specific metrics ensuring the
              highest performance. Each metric passed will by default use the best model for
              that metric.

              You can include multiple metrics to get multiple evaluations in one request or
              pass just a single metric.

              Example with a single metric:

              ```
              ["recall"]
              ```

              Example with multiple metrics:

              ```
              ["recall", "precision"]
              ```

          response: The response generated by the AI model which will be evaluated.

              When using multi-turn input messages, the response should be the last
              `assistant` message in the conversation

          context: The context in which the input message is used.

              In a Retrieval-Augmented Generation (RAG) setting, the context parameter is
              crucial for evaluating how well the AI system integrates retrieved information
              with generated responses. By providing the relevant context, Atla can measure
              the accuracy and relevance of the AI's responses based on the given context.

          model: The model version that will perform the evaluation. By default, the latest
              `atla` model will be used.

          reference: The reference or ground-truth answer against which the AI response will be
              evaluated.

              This parameter is used to provide the correct or expected answer for the given
              input. Atla will compare the AI-generated response against this reference to
              assess the response's correctness and relevance. By providing a reference, you
              enable Atla to perform a detailed evaluation of the AI's performance in terms of
              accuracy and factual consistency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/eval",
            body=maybe_transform(
                {
                    "input": input,
                    "metrics": metrics,
                    "response": response,
                    "context": context,
                    "model": model,
                    "reference": reference,
                },
                evaluate_create_params.EvaluateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Evaluate,
        )


class AsyncEvaluateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluateResourceWithRawResponse:
        return AsyncEvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluateResourceWithStreamingResponse:
        return AsyncEvaluateResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: Union[str, Iterable[Dict[str, str]]],
        metrics: List[str],
        response: str,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        reference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Evaluate:
        """
        Create Evaluation

        Args:
          input: Input messages to evaluate the assistant's response for.

              Atla will evaluate an AI response based on the input message that was used to
              generate the response. Typically the input message is a single question or
              prompt used within some context.

              Example with a single input message:

              ```
              Is it permissible for a cookie banner to obscure the imprint?
              ```

              Atla is able to generate an evaluation for multi-turn input messages, typically
              a conversation. The input message should be a list of alternating `user` and
              `assistant` messages.Each message should be a dictionary with a `role` and
              `content` key.

              Example with multiple conversational turns:

              ```
              [
                  {"role": "user", "content": "Is it permissible for a cookie banner to obscure the imprint?"},
                  {
                      "role": "assistant",
                      "content": "I could not find a specific source addressing the permissibility of a cookie banner obscuring the imprint.",
                  },
              ]
              ```

          metrics: Metrics to evaluate on.

              Our models have been trained to evaluate on specific metrics ensuring the
              highest performance. Each metric passed will by default use the best model for
              that metric.

              You can include multiple metrics to get multiple evaluations in one request or
              pass just a single metric.

              Example with a single metric:

              ```
              ["recall"]
              ```

              Example with multiple metrics:

              ```
              ["recall", "precision"]
              ```

          response: The response generated by the AI model which will be evaluated.

              When using multi-turn input messages, the response should be the last
              `assistant` message in the conversation

          context: The context in which the input message is used.

              In a Retrieval-Augmented Generation (RAG) setting, the context parameter is
              crucial for evaluating how well the AI system integrates retrieved information
              with generated responses. By providing the relevant context, Atla can measure
              the accuracy and relevance of the AI's responses based on the given context.

          model: The model version that will perform the evaluation. By default, the latest
              `atla` model will be used.

          reference: The reference or ground-truth answer against which the AI response will be
              evaluated.

              This parameter is used to provide the correct or expected answer for the given
              input. Atla will compare the AI-generated response against this reference to
              assess the response's correctness and relevance. By providing a reference, you
              enable Atla to perform a detailed evaluation of the AI's performance in terms of
              accuracy and factual consistency.
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/eval",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "metrics": metrics,
                    "response": response,
                    "context": context,
                    "model": model,
                    "reference": reference,
                },
                evaluate_create_params.EvaluateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Evaluate,
        )


class EvaluateResourceWithRawResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.create = to_raw_response_wrapper(
            evaluate.create,
        )


class AsyncEvaluateResourceWithRawResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.create = async_to_raw_response_wrapper(
            evaluate.create,
        )


class EvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.create = to_streamed_response_wrapper(
            evaluate.create,
        )


class AsyncEvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.create = async_to_streamed_response_wrapper(
            evaluate.create,
        )
