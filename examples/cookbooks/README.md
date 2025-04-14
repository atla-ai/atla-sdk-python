# Choosing a Model (Guide)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/Atla_Selene_Model_Selection.ipynb)

This cookbook presents a structured way to approach picking the right model for your use case.

We take Chat as an example use case, where we build a playful and helpful assistant that is cost-effective. We evaluate the performance of two popular models against criteria we are interested in - clarity, objectivity and tone.

We demonstrate how Selene can be used to guide the decision.

# Improving your Prompts (Guide)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/Atla_Selene_Prompt_Improvement.ipynb)

This cookbook presents a structured way to improve your prompts to get the best out of your foundation model for your use case.

We take Chat as an example use case and demonstrate how Selene can be used to guide the decision.

# Implementing Guardrails (Guide)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/Atla_Selene_Mini_Guardrails.ipynb)

This cookbook demonstrates how to implement **inference-time guardrails to validate and filter your AI outputs.** We evaluate GPT-4o outputs against example safety dimensions (toxicity, bias, and medical advice) to replace problematic outputs before they are delivered to users.

We use Selene Mini, our state-of-the-art small-LLM-as-a-Judge that excels in low latency use cases.

# Absolute Scoring (Tutorial)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/Atla_Selene_Absolute_Scoring.ipynb)

This cookbook gets you started running evals with absolute scores using Selene, and does so on a sample set from the public benchmark [FLASK](https://arxiv.org/pdf/2307.10928) dataset - a collection of 1,740 human-annotated samples from 120 NLP datasets. Evaluators assign scores ranging from 1 to 5 for each annotated skill based on the reference (ground-truth) answer and skill-specific scoring rubrics.

We evaluate logical robustness (whether the model avoids logical contradictions in its reasoning) and completeness (whether the response provides sufficient explanation) using default and custom-defined metrics respectively, then compare how Selene's scores align with the human labels.

# Hallucination Scoring (Tutorial)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/Atla_Selene_Hallucination.ipynb)

This cookbook gets you started detecting hallucinations using Selene, and runs over a sample set from the public benchmark [RAGTruth](https://arxiv.org/abs/2401.00396) benchmark - a large-scale corpus of naturally generated hallucinations, featuring detailed word-level annotations specifically designed for retrieval-augmented generation (RAG) scenarios.

We check for hallucination in AI responses i.e. 'Is the information provided in the response directly supported by the context given in the related passages?' and compare how Selene's scores align with the human labels.

# Multi-Criteria Evals (Tutorial)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/Atla_Selene_Multi_Criteria_Evals.ipynb)

This cookbook gets you started on running multi-criteria evals with Selene, to help you get a comprehensive picture of your model's performance. We follow eval best practices by evaluating each criterion as an individual metric to receive clearer insights and more reliable scores.

The first section will show you how to run multi-criteria evals on one/many datapoints across 3 criteria using our async client. The second section will showcase how our model performs on multi-criteria evals, across 12 criteria on the public [FLASK](https://arxiv.org/pdf/2307.10928) dataset.

# Atla on Langfuse

You can use Selene as an LLM Judge in Langfuse to monitor your app’s performance in production using traces, as well as to run experiments over datasets pre-production. We provide demo videos and cookbooks for both use cases. Click [here](https://github.com/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/langfuse) to go to our Langfuse cookbooks.

# Contact
Get in touch with us if there's another use case you'd like to see a cookbook for!

<p align="left">
  <a href="https://x.com/Atla_AI"><img src="https://img.shields.io/badge/Atla_AI-000?color=00bd83&style=plastic&logo=twitter&logoColor=white&label=X"></a>
  <a href="https://discord.com/invite/qFCMgkGwUK"><img src="https://img.shields.io/discord/1280604142536232972?color=00bd83&style=plastic&label=Discord&logo=discord&logoColor=white"></a>
  <a href="https://www.linkedin.com/company/atla-ai/"><img src="https://img.shields.io/badge/LinkedIn-Atla_AI-00bd83?style=plastic"></a>
<br></br>