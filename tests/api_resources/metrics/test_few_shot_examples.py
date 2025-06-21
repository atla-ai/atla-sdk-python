# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from atla import Atla, AsyncAtla
from tests.utils import assert_matches_type
from atla.types.metrics import FewShotExampleSetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFewShotExamples:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_set(self, client: Atla) -> None:
        few_shot_example = client.metrics.few_shot_examples.set(
            metric_id="metric_id",
            few_shot_examples=[
                {
                    "model_input": "Few-shot `model_input`.",
                    "model_output": "Few-shot `model_output`.",
                    "score": "1",
                }
            ],
        )
        assert_matches_type(FewShotExampleSetResponse, few_shot_example, path=["response"])

    @parametrize
    def test_raw_response_set(self, client: Atla) -> None:
        response = client.metrics.few_shot_examples.with_raw_response.set(
            metric_id="metric_id",
            few_shot_examples=[
                {
                    "model_input": "Few-shot `model_input`.",
                    "model_output": "Few-shot `model_output`.",
                    "score": "1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        few_shot_example = response.parse()
        assert_matches_type(FewShotExampleSetResponse, few_shot_example, path=["response"])

    @parametrize
    def test_streaming_response_set(self, client: Atla) -> None:
        with client.metrics.few_shot_examples.with_streaming_response.set(
            metric_id="metric_id",
            few_shot_examples=[
                {
                    "model_input": "Few-shot `model_input`.",
                    "model_output": "Few-shot `model_output`.",
                    "score": "1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            few_shot_example = response.parse()
            assert_matches_type(FewShotExampleSetResponse, few_shot_example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set(self, client: Atla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.few_shot_examples.with_raw_response.set(
                metric_id="",
                few_shot_examples=[
                    {
                        "model_input": "Few-shot `model_input`.",
                        "model_output": "Few-shot `model_output`.",
                        "score": "1",
                    }
                ],
            )


class TestAsyncFewShotExamples:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_set(self, async_client: AsyncAtla) -> None:
        few_shot_example = await async_client.metrics.few_shot_examples.set(
            metric_id="metric_id",
            few_shot_examples=[
                {
                    "model_input": "Few-shot `model_input`.",
                    "model_output": "Few-shot `model_output`.",
                    "score": "1",
                }
            ],
        )
        assert_matches_type(FewShotExampleSetResponse, few_shot_example, path=["response"])

    @parametrize
    async def test_raw_response_set(self, async_client: AsyncAtla) -> None:
        response = await async_client.metrics.few_shot_examples.with_raw_response.set(
            metric_id="metric_id",
            few_shot_examples=[
                {
                    "model_input": "Few-shot `model_input`.",
                    "model_output": "Few-shot `model_output`.",
                    "score": "1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        few_shot_example = await response.parse()
        assert_matches_type(FewShotExampleSetResponse, few_shot_example, path=["response"])

    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncAtla) -> None:
        async with async_client.metrics.few_shot_examples.with_streaming_response.set(
            metric_id="metric_id",
            few_shot_examples=[
                {
                    "model_input": "Few-shot `model_input`.",
                    "model_output": "Few-shot `model_output`.",
                    "score": "1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            few_shot_example = await response.parse()
            assert_matches_type(FewShotExampleSetResponse, few_shot_example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set(self, async_client: AsyncAtla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.few_shot_examples.with_raw_response.set(
                metric_id="",
                few_shot_examples=[
                    {
                        "model_input": "Few-shot `model_input`.",
                        "model_output": "Few-shot `model_output`.",
                        "score": "1",
                    }
                ],
            )
