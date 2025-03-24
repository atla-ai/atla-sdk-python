# Monitoring (Tutorial)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/langfuse/Atla_Langfuse_Monitoring)

This cookbook builds a Gradio application with a complete RAG pipeline. The app is a simple chatbot that answers questions based on a single webpage, which is set to Google’s Q4 2024 earnings call transcript. 

Traces will automatically be sent to Langfuse and scored by Selene. The evaluation example in this cookbook is evaluating the retrieval component of the RAG app by assessing ‘context relevance.’ 

<br>

# Offline Evals (Tutorial)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/atla-ai/atla-sdk-python/blob/main/examples/cookbooks/langfuse/Atla_Langfuse_Offline_Evals.ipynb)

This cookbook compares the performance of various models (o1-mini, o3-mini, and gpt-4o) on function calling tasks using the [Salesforce ShareGPT dataset](https://huggingface.co/datasets/arcee-ai/agent-data/viewer/default/train?f%5Bdataset%5D%5Bvalue%5D=%27glaive-function-calling-v2-extended%27&sql=SELECT+*%0AFROM+train%0AWHERE+dataset+%3D+%27salesforce_sharegpt%27%0ALIMIT+10%3B&views%5B%5D=train). The notebook uploads the dataset to Langfuse and sets up experiment runs on different models. The various outputs are automatically evaluated by Selene. 

# Contact
Get in touch with us if there's another use case you'd like to see a cookbook for!

<p align="left">
  <a href="https://x.com/Atla_AI"><img src="https://img.shields.io/badge/Atla_AI-000?color=00bd83&style=plastic&logo=twitter&logoColor=white&label=X"></a>
  <a href="https://discord.com/invite/qFCMgkGwUK"><img src="https://img.shields.io/discord/1280604142536232972?color=00bd83&style=plastic&label=Discord&logo=discord&logoColor=white"></a>
  <a href="https://www.linkedin.com/company/atla-ai/"><img src="https://img.shields.io/badge/LinkedIn-Atla_AI-00bd83?style=plastic"></a>
<br></br>