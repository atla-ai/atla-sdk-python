# Absolute Scoring (Tutorial)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/Atla_Selene_Absolute_Scoring.ipynb)

This cookbook gets you started running evals with absolute scores, and does so on a sample set from the public benchmark [FLASK](https://arxiv.org/pdf/2307.10928) dataset - a collection of 1,740 human-annotated samples from 120 NLP datasets. Evaluators assign scores ranging from 1 to 5 for each annotated skill based on the reference (ground-truth) answer and skill-specific scoring rubrics.
<br>

We evaluate logical robustness (whether the model avoids logical contradictions in its reasoning) and completeness (whether the response provides sufficient explanation) using default and custom-defined metrics respectively, then compare how Selene's scores align with the human labels.

# Hallucination Scoring (Tutorial)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/Atla_Selene_Hallucination.ipynb)

This cookbook gets you started detecting hallucinations, and runs over a sample set from the public benchmark [RAGTruth](https://arxiv.org/abs/2401.00396) benchmark - a large-scale corpus of naturally generated hallucinations, featuring detailed word-level annotations specifically designed for retrieval-augmented generation (RAG) scenarios.
<br>

We check for hallucination in AI responses i.e. 'Is the information provided in the response directly supported by the context given in the related passages?' and compare how Selene's scores align with the human labels.

# Multi-Criteria Evals (Tutorial)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/Atla_Selene_Multi_Criteria_Evals.ipynb)

This cookbook gets you started on running multi-criteria evals with Selene, to help you get a comprehensive picture of your model's performance. We follow eval best practices by evaluating each criterion as an individual metric to receive clearer insights and more reliable scores.

The first section will show you how to run multi-criteria evals on one/many datapoints across 3 criteria using our async client. The second section will showcase how our model performs on multi-criteria evals, across 12 criteria on the public [FLASK](https://arxiv.org/pdf/2307.10928) dataset.

# Contact
Get in touch with us if there's another use case you'd like to see a cookbook for!

<p align="left">
  <a href="https://x.com/Atla_AI"><img src="https://img.shields.io/badge/Atla_AI-000?color=00bd83&style=plastic&logo=twitter&logoColor=white&label=X"></a>
  <a href="https://discord.com/invite/qFCMgkGwUK"><img src="https://img.shields.io/discord/1280604142536232972?color=00bd83&style=plastic&label=Discord&logo=discord&logoColor=white"></a>
  <a href="https://www.linkedin.com/company/atla-ai/"><img src="https://img.shields.io/badge/LinkedIn-Atla_AI-00bd83?style=plastic"></a>
<br></br>