---
description: >-
  AI Studio 可讓 IT 人員串聯外部訂閱的大語言模型 (LLM) 服務，如 ChatGPT 或是
  Gemini，或是設定串接在自有算力上部署的地端大語言模型。
---

# Model

## **New large language model**

<figure><img src="../.gitbook/assets/image (286).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (287).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (288).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (289).png" alt=""><figcaption></figcaption></figure>

1. After entering, click "+Add" in the upper right corner to start setting.
2. Choose a service provider (for example: OpenAI / Azure / Gemini / Ollama / Claude)
3. Set content according to different service providers
 1. Name: Customizable, the name of the model that will be displayed in the system
 2. Model: Please enter the model to use

> Note: Please fill in manually, the system will not automatically list the options. (Example: `gpt-5`, `gpt-4o`, `gemini-pro`, `llama3-70b`…etc.)
 >
 > For example, if it is mistakenly planted as `gpt-6`, an error message will appear during Agent testing:
 >
 > Received Model Group=gpt-6
 >
 > Available Model Group Fallbacks=None
 >
 > Mode: If you input the model yourself, you will need to select another mode (for example: Chat / Embedding)
 3. API basics: Please enter the API Key provided by the service provider

> Note: If the input is incorrect, the system will return an authorization error.
 >
 > * OpenAI: Please fill in the API prefix (Prefix). For example: `https://api.openai.com/v1`
 > * Gemini: No need to fill in the API Base URL, the system will automatically handle the routing.
 4. API Key: Please fill in the API Key
 5. Organization: Optional. Generally, Key can be left blank. Some OpenAI may need to fill in if short Key is used.
4. advanced settings
 1. If using **Cloud Model** → It is recommended to leave it blank and the system will automatically update the latest price.
 2. If you use **your own deployment model**→ you can evaluate whether to fill in the rate yourself.
5. Click Create to complete the settings.

## **Model setting content description**

<table><thead><tr><th width="186">Setting Item</th><th width="288">Description</th><th>Options</th></tr>⟬PH001 0⟭<tbody><tr><td>Service name</td><td>Service name of the provided model</td><td><code>openai</code>, <code>gemini</code>, <code>ollama</code> (on-premises)</td></tr><tr><td>Mode⟬PH00 28⟭<td>Type of model</td><td><code>chat</code>, <code>embedding</code></td></tr><tr><td>Model⟬PH0 040⟭<td>Service provides usable model </td><td>Example: <code>gpt-4.1</code>, <code>gemini-2.0-flash</code> etc., depending on the settings during system installation </td></tr><tr><td>Name </td><td> in AI Studio The name used to identify this model </td><td> is by default the same as the model, and the user enters </td></tr><tr><td>Description</td><td>Model description</td><td>User input</td></tr><tr><td>API Key/API Basics </td><td>Service selection <code>openai</code> and <code>gemini</code> Enter the key and select <code>ollama</code> When entering the URL of the model API service </td><td> the user inputs </td></tr><tr><td>custom price (Advanced settings)</td><td>Whether to provide model service prices for calculating the cost of using generative AI</td><td>User options</td></tr><tr><td>Pricing model (Advanced Settings) How is the </td><td> service priced? </td><td>Preset to mark per million </td></tr><tr><td>Enter cost (Advanced settings)</td><td>Enter the amount value</td><td>User input</td></tr><tr><td>Output cost (Advanced settings)</td><td>Enter the amount value</td><td>User input</td></tr><tr><td>Enable Status</td><td>Enable/Stop Model</td><td>User Options</td></tr></tbody></table>

> Note: The service name, mode and model cannot be changed after the model is created.
