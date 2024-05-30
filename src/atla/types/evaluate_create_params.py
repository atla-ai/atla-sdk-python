# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EvaluateCreateParams"]


class EvaluateCreateParams(TypedDict, total=False):
    input: Required[Union[str, Iterable[Dict[str, str]]]]
    """Input messages to evaluate the assistant's response for.

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
       {'role': 'user', 'content': 'Is it permissible for a cookie banner to obscure the imprint?'},
       {'role': 'assistant', 'content': 'I could not find a specific source addressing the permissibility of a cookie banner obscuring the imprint.'}
    ]
    ```
    """

    metrics: Required[List[str]]
    """Metrics to evaluate on.

    Our models have been trained to evaluate on specific metrics ensuring the
    highest performance. Each metric passed will by default use the best model for
    that metric.

    You can include multiple metrics to get multiple evaluations in one request or
    pass just a single metric.

    Example with a single metric:

    ```
    ['recall']
    ```

    Example with multiple metrics:

    ```
    ['recall', 'precision']
    ```
    """

    response: Required[str]
    """The response generated by the AI model which will be evaluated.

    When using multi-turn input messages, the response should be the last
    `assistant` message in the conversation
    """

    context: Optional[str]
    """The context in which the input message is used.

    In a Retrieval-Augmented Generation (RAG) setting, the context parameter is
    crucial for evaluating how well the AI system integrates retrieved information
    with generated responses. By providing the relevant context, Atla can measure
    the accuracy and relevance of the AI's responses based on the given context.
    """

    model: str
    """The model version that will perform the evaluation.

    By default, the latest `atla` model will be used.
    """

    reference: Optional[str]
    """
    The reference or ground-truth answer against which the AI response will be
    evaluated.

    This parameter is used to provide the correct or expected answer for the given
    input. Atla will compare the AI-generated response against this reference to
    assess the response's correctness and relevance. By providing a reference, you
    enable Atla to perform a detailed evaluation of the AI's performance in terms of
    accuracy and factual consistency.
    """