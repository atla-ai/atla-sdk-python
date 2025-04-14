# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "CompletionCreateParams",
    "Message",
    "MessageChatCompletionDeveloperMessageParam",
    "MessageChatCompletionSystemMessageParam",
    "MessageChatCompletionUserMessageParam",
    "MessageChatCompletionAssistantMessageParam",
    "MessageChatCompletionAssistantMessageParamAudio",
    "MessageChatCompletionAssistantMessageParamFunctionCall",
    "MessageChatCompletionAssistantMessageParamToolCall",
    "MessageChatCompletionAssistantMessageParamToolCallFunction",
    "MessageChatCompletionToolMessageParam",
    "MessageChatCompletionFunctionMessageParam",
]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """A list of messages comprising the conversation so far.

    See the
    [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
    for more information.
    """

    model: Required[str]
    """The ID or name of the Atla evaluator model to use.

    This may point to a specific model version or a model family. If a model family
    is provided, the default model version for that family will be used.
    """

    max_completion_tokens: Optional[int]
    """An upper bound for the number of tokens that can be generated for an evaluation.

    See the
    [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
    for more information.
    """

    max_tokens: Optional[int]
    """
    The maximum number of [tokens](/tokenizer) that can be generated in the
    evaluation. This value is now deprecated in favor of `max_completion_tokens`.
    See the
    [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
    for more information.
    """

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    See the
    [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
    for more information
    """

    top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, wherethe
    model considers the results of the tokens with top_p probability mass. See the
    [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create)
    for more information.
    """


class MessageChatCompletionDeveloperMessageParam(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["developer"]]

    name: str


class MessageChatCompletionSystemMessageParam(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["system"]]

    name: str


class MessageChatCompletionUserMessageParam(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["user"]]

    name: str


class MessageChatCompletionAssistantMessageParamAudio(TypedDict, total=False):
    id: Required[str]


class MessageChatCompletionAssistantMessageParamFunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class MessageChatCompletionAssistantMessageParamToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class MessageChatCompletionAssistantMessageParamToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[MessageChatCompletionAssistantMessageParamToolCallFunction]

    type: Required[Literal["function"]]


class MessageChatCompletionAssistantMessageParam(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    audio: Optional[MessageChatCompletionAssistantMessageParamAudio]

    content: Optional[str]

    function_call: Optional[MessageChatCompletionAssistantMessageParamFunctionCall]

    name: str

    refusal: Optional[str]

    tool_calls: Iterable[MessageChatCompletionAssistantMessageParamToolCall]


class MessageChatCompletionToolMessageParam(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool"]]

    tool_call_id: Required[str]


class MessageChatCompletionFunctionMessageParam(TypedDict, total=False):
    content: Required[Optional[str]]

    name: Required[str]

    role: Required[Literal["function"]]


Message: TypeAlias = Union[
    MessageChatCompletionDeveloperMessageParam,
    MessageChatCompletionSystemMessageParam,
    MessageChatCompletionUserMessageParam,
    MessageChatCompletionAssistantMessageParam,
    MessageChatCompletionToolMessageParam,
    MessageChatCompletionFunctionMessageParam,
]
