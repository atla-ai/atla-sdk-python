# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

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
from ...types.chat import completion_create_params
from ..._base_client import make_request_options
from ...types.chat_completion import ChatCompletion

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        messages: Iterable[completion_create_params.Message],
        model: str,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """
        Run an evaluation via an
        [OpenAI-compatible](https://platform.openai.com/docs/api-reference/chat/create)
        `/chat/completions` endpoint. **Note that Atla models do not support the full
        OpenAI API spec.** Specifically, the following OpenAI API `/chat/completions`
        fields are not supported and will raise an error if provided: `audio`,
        `frequency_penalty`, `function_call`, `functions`, `logit_bias`, `logprobs`,
        `metadata`, `modalities`, `n`, `parallel_tool_calls`, `prediction`,
        `presence_penalty`, `reasoning_effort`, `response_format`, `seed`,
        `service_tier`, `stop`, `store`, `stream`, `stream_options`, `tool_choice`,
        `tools`, `top_logprobs`, `user`. See our docs for more information:
        https://docs.atla-ai.com.

        Args:
          messages: A list of messages comprising the conversation so far. See the
              [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
              for more information.

          model: The ID or name of the Atla evaluator model to use. This may point to a specific
              model version or a model family. If a model family is provided, the default
              model version for that family will be used.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for an evaluation.
              See the
              [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
              for more information.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the
              evaluation. This value is now deprecated in favor of `max_completion_tokens`.
              See the
              [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
              for more information.

          temperature: What sampling temperature to use, between 0 and 2. See the
              [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
              for more information

          top_p: An alternative to sampling with temperature, called nucleus sampling, wherethe
              model considers the results of the tokens with top_p probability mass. See the
              [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
              for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/atla-ai/atla-sdk-python#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        messages: Iterable[completion_create_params.Message],
        model: str,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """
        Run an evaluation via an
        [OpenAI-compatible](https://platform.openai.com/docs/api-reference/chat/create)
        `/chat/completions` endpoint. **Note that Atla models do not support the full
        OpenAI API spec.** Specifically, the following OpenAI API `/chat/completions`
        fields are not supported and will raise an error if provided: `audio`,
        `frequency_penalty`, `function_call`, `functions`, `logit_bias`, `logprobs`,
        `metadata`, `modalities`, `n`, `parallel_tool_calls`, `prediction`,
        `presence_penalty`, `reasoning_effort`, `response_format`, `seed`,
        `service_tier`, `stop`, `store`, `stream`, `stream_options`, `tool_choice`,
        `tools`, `top_logprobs`, `user`. See our docs for more information:
        https://docs.atla-ai.com.

        Args:
          messages: A list of messages comprising the conversation so far. See the
              [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
              for more information.

          model: The ID or name of the Atla evaluator model to use. This may point to a specific
              model version or a model family. If a model family is provided, the default
              model version for that family will be used.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for an evaluation.
              See the
              [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
              for more information.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the
              evaluation. This value is now deprecated in favor of `max_completion_tokens`.
              See the
              [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
              for more information.

          temperature: What sampling temperature to use, between 0 and 2. See the
              [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
              for more information

          top_p: An alternative to sampling with temperature, called nucleus sampling, wherethe
              model considers the results of the tokens with top_p probability mass. See the
              [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
              for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
