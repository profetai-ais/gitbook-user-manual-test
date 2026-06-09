---
description: >-
  AI Studio allows IT staff to connect externally subscribed large language
  model (LLM) services, such as ChatGPT or Gemini, or set up local large
  language models deployed on their own computing power.
---

# Model

## **New large language model**

<figure><img src="../.gitbook/assets/image (269).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (270).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (271).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (272).png" alt=""><figcaption></figcaption></figure>

1. After entering, click "+Add" in the upper right corner to start setting.
2. Choose a service provider (for example: OpenAI / Azure / Gemini / Ollama / Claude)
3. Set content according to different service providers
4. Name: Customizable, the name of the model that will be displayed in the system
5. Model: Please enter the model to use

> Note: Please fill in manually, the system will not automatically list the options. (Example: , , , ...etc.)
>
> For example, if it is mistakenly planted as , an error message will appear during Agent testing:
>
> Received Model Group=gpt-6
>
> Available Model Group Fallbacks=None
>
> Mode: If you input the model yourself, you will need to select another mode (for example: Chat / Embedding)

3. API basics: Please enter the API Key provided by the service provider

> Note: If the input is incorrect, the system will return an authorization error.
>
> * OpenAI: Please fill in the API prefix (Prefix). For example:
> * Gemini: No need to fill in the API Base URL, the system will automatically handle the routing.

4. API Key: Please fill in the API Key
5. Organization: Optional. Generally, Key can be left blank. Some OpenAI may need to fill in if short Key is used.
6. advanced settings
7. If using **Cloud Model** → It is recommended to leave it blank and the system will automatically update the latest price.
8. If you use **your own deployment model**→ you can evaluate whether to fill in the rate yourself.
9. Click Create to complete the settings.

### FAQ: Model logo does not match the actual connected provider

<figure><img src="../.gitbook/assets/image (200).png" alt="" width="561"><figcaption></figcaption></figure>



In the Model Management page, the model logo is displayed based on the provider selected when the model was created.

For example, if the selected provider is OpenAI, the page displays the GPT / OpenAI logo. If the selected provider is Azure OpenAI, the page displays the Azure-related logo.

If a model is actually connected to Azure API, but the provider was selected as OpenAI when the model was created, the page may display a GPT logo even though the model is using Azure API.

This is related to the provider selection and display logic during model creation. It does not affect the actual API connection. The model will still call the configured API URL, API key, and related parameters. If the model can pass the connection test and be used normally, it means the API connection is working correctly.

To make the displayed logo match the actual provider, please make sure the correct provider is selected when adding or recreating the model.

## **Model setting content description**

<table><thead><tr><th width="186">Setting items</th><th width="288">illustrate</th><th>Options</th></tr></thead><tbody><tr><td>Service name</td><td>The name of the service that provides the model</td><td><code>openai</code>, <code>gemini</code>, <code>ollama</code> (on-premises)</td></tr><tr><td>model</td><td>Type of model</td><td><code>chat</code>, <code>embedding</code></td></tr><tr><td>Model</td><td>The service provides a model that can be used</td><td>example:<code>gpt-4.1</code>, <code>gemini-2.0-flash</code> etc., depending on the settings during system installation.</td></tr><tr><td>name</td><td>The name used to identify this model in AI Studio</td><td>Default is the same as model, user input</td></tr><tr><td>describe</td><td>Description of the model</td><td>user input</td></tr><tr><td>API Key/API Basics</td><td>Service options <code>openai</code> and <code>gemini</code> Enter the key and select <code>ollama</code> Enter the URL of the model API service when</td><td>user input</td></tr><tr><td>Custom price (advanced settings)</td><td>Whether to provide a model service price to calculate the cost of using generative AI</td><td>User options</td></tr><tr><td>Pricing model (advanced settings)</td><td>How are services priced?</td><td>Default is marks per million</td></tr><tr><td>Enter costs (advanced settings)</td><td>Enter amount value</td><td>user input</td></tr><tr><td>Output cost (advanced settings)</td><td>Enter amount value</td><td>user input</td></tr><tr><td>Enabled status</td><td>Enable/stop model</td><td>User options</td></tr></tbody></table>

> Note: The service name, mode and model cannot be changed after the model is created.

## Model Support List

AI Studio currently supports integrations with multiple model providers, including:

* OpenAI
* Azure OpenAI
* Google / Gemini
* Ollama
* Anthropic Claude
* AWS Bedrock
* Google Vertex AI
* DeepSeek
* Mistral AI
* Cohere
* OpenRouter
* NVIDIA NIM
* GLM
* MiniMax
* Qwen

> Note: The list above refers primarily to the model integration sources currently supported by AI Studio. In actual use, models may be deployed either in the cloud or on-premises, depending on the customer’s environment requirements, model licensing, API services, or private deployment conditions.
