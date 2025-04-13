# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "CompletionCreateParams",
    "Message",
    "MessageChatCompletionDeveloperMessageParam",
    "MessageChatCompletionDeveloperMessageParamContentUnionMember1",
    "MessageChatCompletionSystemMessageParam",
    "MessageChatCompletionSystemMessageParamContentUnionMember1",
    "MessageChatCompletionUserMessageParam",
    "MessageChatCompletionUserMessageParamContentUnionMember1",
    "MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartTextParam",
    "MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParam",
    "MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParamImageURL",
    "MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParam",
    "MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio",
    "MessageChatCompletionAssistantMessageParam",
    "MessageChatCompletionAssistantMessageParamAudio",
    "MessageChatCompletionAssistantMessageParamContentUnionMember1",
    "MessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartTextParam",
    "MessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartRefusalParam",
    "MessageChatCompletionAssistantMessageParamFunctionCall",
    "MessageChatCompletionAssistantMessageParamToolCall",
    "MessageChatCompletionAssistantMessageParamToolCallFunction",
    "MessageChatCompletionToolMessageParam",
    "MessageChatCompletionToolMessageParamContentUnionMember1",
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


class MessageChatCompletionDeveloperMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageChatCompletionDeveloperMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageChatCompletionDeveloperMessageParamContentUnionMember1]]]

    role: Required[Literal["developer"]]

    name: str


class MessageChatCompletionSystemMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageChatCompletionSystemMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageChatCompletionSystemMessageParamContentUnionMember1]]]

    role: Required[Literal["system"]]

    name: str


class MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartTextParam(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParamImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["auto", "low", "high"]


class MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParam(
    TypedDict, total=False
):
    image_url: Required[
        MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParamImageURL
    ]

    type: Required[Literal["image_url"]]


class MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio(
    TypedDict, total=False
):
    data: Required[str]

    format: Required[Literal["wav", "mp3"]]


class MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParam(
    TypedDict, total=False
):
    input_audio: Required[
        MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio
    ]

    type: Required[Literal["input_audio"]]


MessageChatCompletionUserMessageParamContentUnionMember1: TypeAlias = Union[
    MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartTextParam,
    MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParam,
    MessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParam,
]


class MessageChatCompletionUserMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageChatCompletionUserMessageParamContentUnionMember1]]]

    role: Required[Literal["user"]]

    name: str


class MessageChatCompletionAssistantMessageParamAudio(TypedDict, total=False):
    id: Required[str]


class MessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartTextParam(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartRefusalParam(
    TypedDict, total=False
):
    refusal: Required[str]

    type: Required[Literal["refusal"]]


MessageChatCompletionAssistantMessageParamContentUnionMember1: TypeAlias = Union[
    MessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartTextParam,
    MessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartRefusalParam,
]


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

    content: Union[str, Iterable[MessageChatCompletionAssistantMessageParamContentUnionMember1], None]

    function_call: Optional[MessageChatCompletionAssistantMessageParamFunctionCall]

    name: str

    refusal: Optional[str]

    tool_calls: Iterable[MessageChatCompletionAssistantMessageParamToolCall]


class MessageChatCompletionToolMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageChatCompletionToolMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageChatCompletionToolMessageParamContentUnionMember1]]]

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
