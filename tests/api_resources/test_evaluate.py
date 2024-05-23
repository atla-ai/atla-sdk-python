# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from atla import Atla, AsyncAtla
from atla.types import EvaluateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method(self, client: Atla) -> None:
        evaluate = client.evaluate._(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        )
        assert_matches_type(EvaluateResponse, evaluate, path=["response"])

    @parametrize
    def test_method_with_all_params(self, client: Atla) -> None:
        evaluate = client.evaluate._(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
            model="string",
        )
        assert_matches_type(EvaluateResponse, evaluate, path=["response"])

    @parametrize
    def test_raw_response(self, client: Atla) -> None:
        response = client.evaluate.with_raw_response._(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(EvaluateResponse, evaluate, path=["response"])

    @parametrize
    def test_streaming_response(self, client: Atla) -> None:
        with client.evaluate.with_streaming_response._(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(EvaluateResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method(self, async_client: AsyncAtla) -> None:
        evaluate = await async_client.evaluate._(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        )
        assert_matches_type(EvaluateResponse, evaluate, path=["response"])

    @parametrize
    async def test_method_with_all_params(self, async_client: AsyncAtla) -> None:
        evaluate = await async_client.evaluate._(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
            model="string",
        )
        assert_matches_type(EvaluateResponse, evaluate, path=["response"])

    @parametrize
    async def test_raw_response(self, async_client: AsyncAtla) -> None:
        response = await async_client.evaluate.with_raw_response._(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(EvaluateResponse, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response(self, async_client: AsyncAtla) -> None:
        async with async_client.evaluate.with_streaming_response._(
            context="string",
            input="string",
            metrics=["string", "string", "string"],
            reference="string",
            response="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(EvaluateResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True
