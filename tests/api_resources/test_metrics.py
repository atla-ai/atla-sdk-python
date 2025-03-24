# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from atla import Atla, AsyncAtla
from atla.types import (
    MetricGetResponse,
    MetricListResponse,
    MetricCreateResponse,
    MetricDeleteResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Atla) -> None:
        metric = client.metrics.create(
            metric_type="binary",
            name="my_metric",
        )
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Atla) -> None:
        metric = client.metrics.create(
            metric_type="binary",
            name="my_metric",
            description="An example metric demonstrating functionality.",
            required_fields=["model_input", "model_output", "model_context", "expected_model_output"],
        )
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Atla) -> None:
        response = client.metrics.with_raw_response.create(
            metric_type="binary",
            name="my_metric",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Atla) -> None:
        with client.metrics.with_streaming_response.create(
            metric_type="binary",
            name="my_metric",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricCreateResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Atla) -> None:
        metric = client.metrics.list()
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Atla) -> None:
        metric = client.metrics.list(
            include_default=True,
        )
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Atla) -> None:
        response = client.metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Atla) -> None:
        with client.metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricListResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Atla) -> None:
        metric = client.metrics.delete(
            "metric_id",
        )
        assert_matches_type(MetricDeleteResponse, metric, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Atla) -> None:
        response = client.metrics.with_raw_response.delete(
            "metric_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricDeleteResponse, metric, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Atla) -> None:
        with client.metrics.with_streaming_response.delete(
            "metric_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricDeleteResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Atla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Atla) -> None:
        metric = client.metrics.get(
            "metric_id",
        )
        assert_matches_type(MetricGetResponse, metric, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Atla) -> None:
        response = client.metrics.with_raw_response.get(
            "metric_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricGetResponse, metric, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Atla) -> None:
        with client.metrics.with_streaming_response.get(
            "metric_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricGetResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Atla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.get(
                "",
            )


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAtla) -> None:
        metric = await async_client.metrics.create(
            metric_type="binary",
            name="my_metric",
        )
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAtla) -> None:
        metric = await async_client.metrics.create(
            metric_type="binary",
            name="my_metric",
            description="An example metric demonstrating functionality.",
            required_fields=["model_input", "model_output", "model_context", "expected_model_output"],
        )
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAtla) -> None:
        response = await async_client.metrics.with_raw_response.create(
            metric_type="binary",
            name="my_metric",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAtla) -> None:
        async with async_client.metrics.with_streaming_response.create(
            metric_type="binary",
            name="my_metric",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricCreateResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncAtla) -> None:
        metric = await async_client.metrics.list()
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAtla) -> None:
        metric = await async_client.metrics.list(
            include_default=True,
        )
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAtla) -> None:
        response = await async_client.metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAtla) -> None:
        async with async_client.metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricListResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAtla) -> None:
        metric = await async_client.metrics.delete(
            "metric_id",
        )
        assert_matches_type(MetricDeleteResponse, metric, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAtla) -> None:
        response = await async_client.metrics.with_raw_response.delete(
            "metric_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricDeleteResponse, metric, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAtla) -> None:
        async with async_client.metrics.with_streaming_response.delete(
            "metric_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricDeleteResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAtla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncAtla) -> None:
        metric = await async_client.metrics.get(
            "metric_id",
        )
        assert_matches_type(MetricGetResponse, metric, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncAtla) -> None:
        response = await async_client.metrics.with_raw_response.get(
            "metric_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricGetResponse, metric, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncAtla) -> None:
        async with async_client.metrics.with_streaming_response.get(
            "metric_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricGetResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncAtla) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.get(
                "",
            )
