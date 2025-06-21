# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from atla import Atla, AsyncAtla
from tests.utils import assert_matches_type
from atla.types.metrics import (
    PromptGetResponse,
    PromptListResponse,
    PromptCreateResponse,
    PromptSetActivePromptVersionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Atla) -> None:
        prompt = client.metrics.prompts.create(
            metric_id="metric_id",
            content="content",
        )
        assert_matches_type(PromptCreateResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Atla) -> None:
        response = client.metrics.prompts.with_raw_response.create(
            metric_id="metric_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptCreateResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Atla) -> None:
        with client.metrics.prompts.with_streaming_response.create(
            metric_id="metric_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptCreateResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Atla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.prompts.with_raw_response.create(
                metric_id="",
                content="content",
            )

    @parametrize
    def test_method_list(self, client: Atla) -> None:
        prompt = client.metrics.prompts.list(
            "metric_id",
        )
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Atla) -> None:
        response = client.metrics.prompts.with_raw_response.list(
            "metric_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Atla) -> None:
        with client.metrics.prompts.with_streaming_response.list(
            "metric_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Atla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.prompts.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_get(self, client: Atla) -> None:
        prompt = client.metrics.prompts.get(
            version=1,
            metric_id="metric_id",
        )
        assert_matches_type(PromptGetResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Atla) -> None:
        response = client.metrics.prompts.with_raw_response.get(
            version=1,
            metric_id="metric_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptGetResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Atla) -> None:
        with client.metrics.prompts.with_streaming_response.get(
            version=1,
            metric_id="metric_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptGetResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Atla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.prompts.with_raw_response.get(
                version=1,
                metric_id="",
            )

    @parametrize
    def test_method_set_active_prompt_version(self, client: Atla) -> None:
        prompt = client.metrics.prompts.set_active_prompt_version(
            metric_id="metric_id",
            version=1,
        )
        assert_matches_type(PromptSetActivePromptVersionResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_set_active_prompt_version(self, client: Atla) -> None:
        response = client.metrics.prompts.with_raw_response.set_active_prompt_version(
            metric_id="metric_id",
            version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptSetActivePromptVersionResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_set_active_prompt_version(self, client: Atla) -> None:
        with client.metrics.prompts.with_streaming_response.set_active_prompt_version(
            metric_id="metric_id",
            version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptSetActivePromptVersionResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_active_prompt_version(self, client: Atla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.prompts.with_raw_response.set_active_prompt_version(
                metric_id="",
                version=1,
            )


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncAtla) -> None:
        prompt = await async_client.metrics.prompts.create(
            metric_id="metric_id",
            content="content",
        )
        assert_matches_type(PromptCreateResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAtla) -> None:
        response = await async_client.metrics.prompts.with_raw_response.create(
            metric_id="metric_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptCreateResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAtla) -> None:
        async with async_client.metrics.prompts.with_streaming_response.create(
            metric_id="metric_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptCreateResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncAtla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.prompts.with_raw_response.create(
                metric_id="",
                content="content",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAtla) -> None:
        prompt = await async_client.metrics.prompts.list(
            "metric_id",
        )
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAtla) -> None:
        response = await async_client.metrics.prompts.with_raw_response.list(
            "metric_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAtla) -> None:
        async with async_client.metrics.prompts.with_streaming_response.list(
            "metric_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncAtla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.prompts.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncAtla) -> None:
        prompt = await async_client.metrics.prompts.get(
            version=1,
            metric_id="metric_id",
        )
        assert_matches_type(PromptGetResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncAtla) -> None:
        response = await async_client.metrics.prompts.with_raw_response.get(
            version=1,
            metric_id="metric_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptGetResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncAtla) -> None:
        async with async_client.metrics.prompts.with_streaming_response.get(
            version=1,
            metric_id="metric_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptGetResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncAtla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.prompts.with_raw_response.get(
                version=1,
                metric_id="",
            )

    @parametrize
    async def test_method_set_active_prompt_version(self, async_client: AsyncAtla) -> None:
        prompt = await async_client.metrics.prompts.set_active_prompt_version(
            metric_id="metric_id",
            version=1,
        )
        assert_matches_type(PromptSetActivePromptVersionResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_set_active_prompt_version(self, async_client: AsyncAtla) -> None:
        response = await async_client.metrics.prompts.with_raw_response.set_active_prompt_version(
            metric_id="metric_id",
            version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptSetActivePromptVersionResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_set_active_prompt_version(self, async_client: AsyncAtla) -> None:
        async with async_client.metrics.prompts.with_streaming_response.set_active_prompt_version(
            metric_id="metric_id",
            version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptSetActivePromptVersionResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_active_prompt_version(self, async_client: AsyncAtla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.prompts.with_raw_response.set_active_prompt_version(
                metric_id="",
                version=1,
            )
