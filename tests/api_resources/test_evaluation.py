# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from atla import Atla, AsyncAtla
from atla.types import EvaluationCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Atla) -> None:
        evaluation = client.evaluation.create(
            config={
                "criteria": {
                    "evaluation_criteria": "Assign a score of 5 if the answer is factually correct and well-formatted, otherwise assign a score of 0."
                }
            },
            inputs={
                "model_input": "What is the capital of France?",
                "model_output": "Paris",
            },
            model_id="atla-selene-mini",
        )
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Atla) -> None:
        evaluation = client.evaluation.create(
            config={
                "criteria": {
                    "evaluation_criteria": "Assign a score of 5 if the answer is factually correct and well-formatted, otherwise assign a score of 0.",
                    "type": "direct",
                },
                "few_shot_examples": [
                    {
                        "eval_inputs": {
                            "model_input": "What is the capital of the United States?",
                            "model_output": "New York",
                            "expected_model_output": "The capital of the United States is Washington D.C.",
                            "model_context": "Washington D.C. is the capital of the United States.",
                        },
                        "evaluation": {
                            "critique": "critique",
                            "score": 0,
                        },
                    }
                ],
            },
            inputs={
                "model_input": "What is the capital of France?",
                "model_output": "Paris",
                "expected_model_output": "The capital of France is Paris.",
                "model_context": "Paris is the capital of France.",
            },
            model_id="atla-selene-mini",
        )
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Atla) -> None:
        response = client.evaluation.with_raw_response.create(
            config={
                "criteria": {
                    "evaluation_criteria": "Assign a score of 5 if the answer is factually correct and well-formatted, otherwise assign a score of 0."
                }
            },
            inputs={
                "model_input": "What is the capital of France?",
                "model_output": "Paris",
            },
            model_id="atla-selene-mini",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Atla) -> None:
        with client.evaluation.with_streaming_response.create(
            config={
                "criteria": {
                    "evaluation_criteria": "Assign a score of 5 if the answer is factually correct and well-formatted, otherwise assign a score of 0."
                }
            },
            inputs={
                "model_input": "What is the capital of France?",
                "model_output": "Paris",
            },
            model_id="atla-selene-mini",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAtla) -> None:
        evaluation = await async_client.evaluation.create(
            config={
                "criteria": {
                    "evaluation_criteria": "Assign a score of 5 if the answer is factually correct and well-formatted, otherwise assign a score of 0."
                }
            },
            inputs={
                "model_input": "What is the capital of France?",
                "model_output": "Paris",
            },
            model_id="atla-selene-mini",
        )
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAtla) -> None:
        evaluation = await async_client.evaluation.create(
            config={
                "criteria": {
                    "evaluation_criteria": "Assign a score of 5 if the answer is factually correct and well-formatted, otherwise assign a score of 0.",
                    "type": "direct",
                },
                "few_shot_examples": [
                    {
                        "eval_inputs": {
                            "model_input": "What is the capital of the United States?",
                            "model_output": "New York",
                            "expected_model_output": "The capital of the United States is Washington D.C.",
                            "model_context": "Washington D.C. is the capital of the United States.",
                        },
                        "evaluation": {
                            "critique": "critique",
                            "score": 0,
                        },
                    }
                ],
            },
            inputs={
                "model_input": "What is the capital of France?",
                "model_output": "Paris",
                "expected_model_output": "The capital of France is Paris.",
                "model_context": "Paris is the capital of France.",
            },
            model_id="atla-selene-mini",
        )
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAtla) -> None:
        response = await async_client.evaluation.with_raw_response.create(
            config={
                "criteria": {
                    "evaluation_criteria": "Assign a score of 5 if the answer is factually correct and well-formatted, otherwise assign a score of 0."
                }
            },
            inputs={
                "model_input": "What is the capital of France?",
                "model_output": "Paris",
            },
            model_id="atla-selene-mini",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAtla) -> None:
        async with async_client.evaluation.with_streaming_response.create(
            config={
                "criteria": {
                    "evaluation_criteria": "Assign a score of 5 if the answer is factually correct and well-formatted, otherwise assign a score of 0."
                }
            },
            inputs={
                "model_input": "What is the capital of France?",
                "model_output": "Paris",
            },
            model_id="atla-selene-mini",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True
