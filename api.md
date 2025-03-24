# Evaluation

Types:

```python
from atla.types import Evaluation
```

Methods:

- <code title="post /v1/eval">client.evaluation.<a href="./src/atla/resources/evaluation.py">create</a>(\*\*<a href="src/atla/types/evaluation_create_params.py">params</a>) -> <a href="./src/atla/types/evaluation.py">Evaluation</a></code>

# Metrics

Types:

```python
from atla.types import (
    Metric,
    MetricCreateResponse,
    MetricListResponse,
    MetricDeleteResponse,
    MetricGetResponse,
)
```

Methods:

- <code title="post /v1/metrics">client.metrics.<a href="./src/atla/resources/metrics/metrics.py">create</a>(\*\*<a href="src/atla/types/metric_create_params.py">params</a>) -> <a href="./src/atla/types/metric_create_response.py">MetricCreateResponse</a></code>
- <code title="get /v1/metrics">client.metrics.<a href="./src/atla/resources/metrics/metrics.py">list</a>(\*\*<a href="src/atla/types/metric_list_params.py">params</a>) -> <a href="./src/atla/types/metric_list_response.py">MetricListResponse</a></code>
- <code title="delete /v1/metrics/{metric_id}">client.metrics.<a href="./src/atla/resources/metrics/metrics.py">delete</a>(metric_id) -> <a href="./src/atla/types/metric_delete_response.py">MetricDeleteResponse</a></code>
- <code title="get /v1/metrics/{metric_id}">client.metrics.<a href="./src/atla/resources/metrics/metrics.py">get</a>(metric_id) -> <a href="./src/atla/types/metric_get_response.py">MetricGetResponse</a></code>

## Prompts

Types:

```python
from atla.types.metrics import (
    Prompt,
    PromptCreateResponse,
    PromptListResponse,
    PromptGetResponse,
    PromptSetActivePromptVersionResponse,
)
```

Methods:

- <code title="post /v1/metrics/{metric_id}/prompts">client.metrics.prompts.<a href="./src/atla/resources/metrics/prompts.py">create</a>(metric_id, \*\*<a href="src/atla/types/metrics/prompt_create_params.py">params</a>) -> <a href="./src/atla/types/metrics/prompt_create_response.py">PromptCreateResponse</a></code>
- <code title="get /v1/metrics/{metric_id}/prompts">client.metrics.prompts.<a href="./src/atla/resources/metrics/prompts.py">list</a>(metric_id) -> <a href="./src/atla/types/metrics/prompt_list_response.py">PromptListResponse</a></code>
- <code title="get /v1/metrics/{metric_id}/prompts/{version}">client.metrics.prompts.<a href="./src/atla/resources/metrics/prompts.py">get</a>(version, \*, metric_id) -> <a href="./src/atla/types/metrics/prompt_get_response.py">PromptGetResponse</a></code>
- <code title="patch /v1/metrics/{metric_id}/active_prompt_version">client.metrics.prompts.<a href="./src/atla/resources/metrics/prompts.py">set_active_prompt_version</a>(metric_id, \*\*<a href="src/atla/types/metrics/prompt_set_active_prompt_version_params.py">params</a>) -> <a href="./src/atla/types/metrics/prompt_set_active_prompt_version_response.py">PromptSetActivePromptVersionResponse</a></code>

## FewShotExamples

Types:

```python
from atla.types.metrics import FewShotExample, FewShotExampleSetResponse
```

Methods:

- <code title="put /v1/metrics/{metric_id}/few_shot_examples">client.metrics.few_shot_examples.<a href="./src/atla/resources/metrics/few_shot_examples.py">set</a>(metric_id, \*\*<a href="src/atla/types/metrics/few_shot_example_set_params.py">params</a>) -> <a href="./src/atla/types/metrics/few_shot_example_set_response.py">FewShotExampleSetResponse</a></code>
