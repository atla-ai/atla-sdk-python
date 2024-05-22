# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from atla import Atla, AsyncAtla
from atla.types import EvaluationCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Atla) -> None:
        evaluation = client.evaluations.create(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        )
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Atla) -> None:
        evaluation = client.evaluations.create(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
            model="string",
        )
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Atla) -> None:
        response = client.evaluations.with_raw_response.create(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Atla) -> None:
        with client.evaluations.with_streaming_response.create(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAtla) -> None:
        evaluation = await async_client.evaluations.create(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        )
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAtla) -> None:
        evaluation = await async_client.evaluations.create(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
            model="string",
        )
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAtla) -> None:
        response = await async_client.evaluations.with_raw_response.create(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAtla) -> None:
        async with async_client.evaluations.with_streaming_response.create(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True
