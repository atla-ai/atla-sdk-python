# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from atla import Atla, AsyncAtla
from atla.types import Evaluation
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Atla) -> None:
        evaluation = client.evaluation.create(
            model_id="atla-selene-20250214",
            model_input="Is it legal to monitor employee emails under European privacy laws?",
            model_output="Monitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.",
        )
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Atla) -> None:
        evaluation = client.evaluation.create(
            model_id="atla-selene-20250214",
            model_input="Is it legal to monitor employee emails under European privacy laws?",
            model_output="Monitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.",
            evaluation_criteria="Evaluate the answer based on its factual correctness. Assign a score of 1 if the answer is factually correct, otherwise assign a score of 0.",
            expected_model_output="Yes, but only under strict conditions. European privacy laws, including GDPR, require that monitoring be necessary for a legitimate purpose, employees be informed in advance, and privacy impact be minimized.",
            few_shot_examples=[
                {
                    "model_input": "Can employers require employees to use personal devices for work?",
                    "model_output": "Employers can require employees to use personal devices for work, but legal and privacy considerations must be addressed.",
                    "score": "1",
                    "critique": "The model output is factually correct and accurately describes the Bring Your Own Device (BYOD) policy that an employer may choose to implement while highlighting the relevant legal and privacy considerations.",
                    "expected_model_output": "Yes, but privacy and security concerns must be addressed. Employers must ensure compliance with data protection laws, inform employees about data handling, and offer alternatives where necessary.",
                    "model_context": "Employers implementing Bring Your Own Device (BYOD) policies must consider data protection laws and employee privacy rights. Under regulations like GDPR, companies must ensure adequate data security, inform employees of monitoring or data collection practices, and provide alternatives if necessary. Failure to implement safeguards could lead to legal challenges or data breaches.",
                }
            ],
            metric_name="metric_name",
            model_context="European privacy laws, including GDPR, allow for the monitoring of employee emails under strict conditions. The employer must demonstrate that the monitoring is necessary for a legitimate purpose, such as protecting company assets or compliance with legal obligations. Employees must be informed about the monitoring in advance, and the privacy impact should be assessed to minimize intrusion.",
            prompt_version=0,
        )
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Atla) -> None:
        response = client.evaluation.with_raw_response.create(
            model_id="atla-selene-20250214",
            model_input="Is it legal to monitor employee emails under European privacy laws?",
            model_output="Monitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Atla) -> None:
        with client.evaluation.with_streaming_response.create(
            model_id="atla-selene-20250214",
            model_input="Is it legal to monitor employee emails under European privacy laws?",
            model_output="Monitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(Evaluation, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAtla) -> None:
        evaluation = await async_client.evaluation.create(
            model_id="atla-selene-20250214",
            model_input="Is it legal to monitor employee emails under European privacy laws?",
            model_output="Monitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.",
        )
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAtla) -> None:
        evaluation = await async_client.evaluation.create(
            model_id="atla-selene-20250214",
            model_input="Is it legal to monitor employee emails under European privacy laws?",
            model_output="Monitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.",
            evaluation_criteria="Evaluate the answer based on its factual correctness. Assign a score of 1 if the answer is factually correct, otherwise assign a score of 0.",
            expected_model_output="Yes, but only under strict conditions. European privacy laws, including GDPR, require that monitoring be necessary for a legitimate purpose, employees be informed in advance, and privacy impact be minimized.",
            few_shot_examples=[
                {
                    "model_input": "Can employers require employees to use personal devices for work?",
                    "model_output": "Employers can require employees to use personal devices for work, but legal and privacy considerations must be addressed.",
                    "score": "1",
                    "critique": "The model output is factually correct and accurately describes the Bring Your Own Device (BYOD) policy that an employer may choose to implement while highlighting the relevant legal and privacy considerations.",
                    "expected_model_output": "Yes, but privacy and security concerns must be addressed. Employers must ensure compliance with data protection laws, inform employees about data handling, and offer alternatives where necessary.",
                    "model_context": "Employers implementing Bring Your Own Device (BYOD) policies must consider data protection laws and employee privacy rights. Under regulations like GDPR, companies must ensure adequate data security, inform employees of monitoring or data collection practices, and provide alternatives if necessary. Failure to implement safeguards could lead to legal challenges or data breaches.",
                }
            ],
            metric_name="metric_name",
            model_context="European privacy laws, including GDPR, allow for the monitoring of employee emails under strict conditions. The employer must demonstrate that the monitoring is necessary for a legitimate purpose, such as protecting company assets or compliance with legal obligations. Employees must be informed about the monitoring in advance, and the privacy impact should be assessed to minimize intrusion.",
            prompt_version=0,
        )
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAtla) -> None:
        response = await async_client.evaluation.with_raw_response.create(
            model_id="atla-selene-20250214",
            model_input="Is it legal to monitor employee emails under European privacy laws?",
            model_output="Monitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAtla) -> None:
        async with async_client.evaluation.with_streaming_response.create(
            model_id="atla-selene-20250214",
            model_input="Is it legal to monitor employee emails under European privacy laws?",
            model_output="Monitoring employee emails is permissible under European privacy laws like GDPR, provided there is a legitimate purpose.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(Evaluation, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True
