# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from atla import Atla, AsyncAtla
from atla.types import ChatCompletion
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Atla) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "You are an expert evaluator.\n\nYou have been asked to evaluate an LLM's response to a given instruction.\n\nModel input:\nIs it legal to monitor employee emails under European privacy laws?\n\nModel output:\nMonitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.\n\nModel context:\nEuropean privacy laws, including GDPR, allow for the monitoring of employee emails under strict conditions. The employer must demonstrate that the monitoring is necessary for a legitimate purpose, such as protecting company assets or compliance with legal obligations. Employees must be informed about the monitoring in advance, and the privacy impact should be assessed to minimize intrusion.\n\nScore rubric:\nEvaluate the answer based on its factual correctness. Assign a score of 1 if the answer is factually correct, otherwise assign a score of 0. Only scores of 0 or 1 are allowed.\n\nYour response should strictly follow this format:\n**Reasoning:** <your feedback>\n\n**Result:** <your score>\n",
                    "role": "user",
                }
            ],
            model="atla-selene",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Atla) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "You are an expert evaluator.\n\nYou have been asked to evaluate an LLM's response to a given instruction.\n\nModel input:\nIs it legal to monitor employee emails under European privacy laws?\n\nModel output:\nMonitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.\n\nModel context:\nEuropean privacy laws, including GDPR, allow for the monitoring of employee emails under strict conditions. The employer must demonstrate that the monitoring is necessary for a legitimate purpose, such as protecting company assets or compliance with legal obligations. Employees must be informed about the monitoring in advance, and the privacy impact should be assessed to minimize intrusion.\n\nScore rubric:\nEvaluate the answer based on its factual correctness. Assign a score of 1 if the answer is factually correct, otherwise assign a score of 0. Only scores of 0 or 1 are allowed.\n\nYour response should strictly follow this format:\n**Reasoning:** <your feedback>\n\n**Result:** <your score>\n",
                    "role": "user",
                    "name": "name",
                }
            ],
            model="atla-selene",
            max_completion_tokens=0,
            max_tokens=0,
            temperature=0,
            top_p=0,
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Atla) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "You are an expert evaluator.\n\nYou have been asked to evaluate an LLM's response to a given instruction.\n\nModel input:\nIs it legal to monitor employee emails under European privacy laws?\n\nModel output:\nMonitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.\n\nModel context:\nEuropean privacy laws, including GDPR, allow for the monitoring of employee emails under strict conditions. The employer must demonstrate that the monitoring is necessary for a legitimate purpose, such as protecting company assets or compliance with legal obligations. Employees must be informed about the monitoring in advance, and the privacy impact should be assessed to minimize intrusion.\n\nScore rubric:\nEvaluate the answer based on its factual correctness. Assign a score of 1 if the answer is factually correct, otherwise assign a score of 0. Only scores of 0 or 1 are allowed.\n\nYour response should strictly follow this format:\n**Reasoning:** <your feedback>\n\n**Result:** <your score>\n",
                    "role": "user",
                }
            ],
            model="atla-selene",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Atla) -> None:
        with client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "You are an expert evaluator.\n\nYou have been asked to evaluate an LLM's response to a given instruction.\n\nModel input:\nIs it legal to monitor employee emails under European privacy laws?\n\nModel output:\nMonitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.\n\nModel context:\nEuropean privacy laws, including GDPR, allow for the monitoring of employee emails under strict conditions. The employer must demonstrate that the monitoring is necessary for a legitimate purpose, such as protecting company assets or compliance with legal obligations. Employees must be informed about the monitoring in advance, and the privacy impact should be assessed to minimize intrusion.\n\nScore rubric:\nEvaluate the answer based on its factual correctness. Assign a score of 1 if the answer is factually correct, otherwise assign a score of 0. Only scores of 0 or 1 are allowed.\n\nYour response should strictly follow this format:\n**Reasoning:** <your feedback>\n\n**Result:** <your score>\n",
                    "role": "user",
                }
            ],
            model="atla-selene",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(ChatCompletion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncAtla) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "You are an expert evaluator.\n\nYou have been asked to evaluate an LLM's response to a given instruction.\n\nModel input:\nIs it legal to monitor employee emails under European privacy laws?\n\nModel output:\nMonitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.\n\nModel context:\nEuropean privacy laws, including GDPR, allow for the monitoring of employee emails under strict conditions. The employer must demonstrate that the monitoring is necessary for a legitimate purpose, such as protecting company assets or compliance with legal obligations. Employees must be informed about the monitoring in advance, and the privacy impact should be assessed to minimize intrusion.\n\nScore rubric:\nEvaluate the answer based on its factual correctness. Assign a score of 1 if the answer is factually correct, otherwise assign a score of 0. Only scores of 0 or 1 are allowed.\n\nYour response should strictly follow this format:\n**Reasoning:** <your feedback>\n\n**Result:** <your score>\n",
                    "role": "user",
                }
            ],
            model="atla-selene",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAtla) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "You are an expert evaluator.\n\nYou have been asked to evaluate an LLM's response to a given instruction.\n\nModel input:\nIs it legal to monitor employee emails under European privacy laws?\n\nModel output:\nMonitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.\n\nModel context:\nEuropean privacy laws, including GDPR, allow for the monitoring of employee emails under strict conditions. The employer must demonstrate that the monitoring is necessary for a legitimate purpose, such as protecting company assets or compliance with legal obligations. Employees must be informed about the monitoring in advance, and the privacy impact should be assessed to minimize intrusion.\n\nScore rubric:\nEvaluate the answer based on its factual correctness. Assign a score of 1 if the answer is factually correct, otherwise assign a score of 0. Only scores of 0 or 1 are allowed.\n\nYour response should strictly follow this format:\n**Reasoning:** <your feedback>\n\n**Result:** <your score>\n",
                    "role": "user",
                    "name": "name",
                }
            ],
            model="atla-selene",
            max_completion_tokens=0,
            max_tokens=0,
            temperature=0,
            top_p=0,
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAtla) -> None:
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "You are an expert evaluator.\n\nYou have been asked to evaluate an LLM's response to a given instruction.\n\nModel input:\nIs it legal to monitor employee emails under European privacy laws?\n\nModel output:\nMonitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.\n\nModel context:\nEuropean privacy laws, including GDPR, allow for the monitoring of employee emails under strict conditions. The employer must demonstrate that the monitoring is necessary for a legitimate purpose, such as protecting company assets or compliance with legal obligations. Employees must be informed about the monitoring in advance, and the privacy impact should be assessed to minimize intrusion.\n\nScore rubric:\nEvaluate the answer based on its factual correctness. Assign a score of 1 if the answer is factually correct, otherwise assign a score of 0. Only scores of 0 or 1 are allowed.\n\nYour response should strictly follow this format:\n**Reasoning:** <your feedback>\n\n**Result:** <your score>\n",
                    "role": "user",
                }
            ],
            model="atla-selene",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAtla) -> None:
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "You are an expert evaluator.\n\nYou have been asked to evaluate an LLM's response to a given instruction.\n\nModel input:\nIs it legal to monitor employee emails under European privacy laws?\n\nModel output:\nMonitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.\n\nModel context:\nEuropean privacy laws, including GDPR, allow for the monitoring of employee emails under strict conditions. The employer must demonstrate that the monitoring is necessary for a legitimate purpose, such as protecting company assets or compliance with legal obligations. Employees must be informed about the monitoring in advance, and the privacy impact should be assessed to minimize intrusion.\n\nScore rubric:\nEvaluate the answer based on its factual correctness. Assign a score of 1 if the answer is factually correct, otherwise assign a score of 0. Only scores of 0 or 1 are allowed.\n\nYour response should strictly follow this format:\n**Reasoning:** <your feedback>\n\n**Result:** <your score>\n",
                    "role": "user",
                }
            ],
            model="atla-selene",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(ChatCompletion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
