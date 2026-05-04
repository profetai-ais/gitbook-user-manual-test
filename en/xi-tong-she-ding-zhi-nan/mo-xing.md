---
description: >-
  AI Studio allows IT to connect externally subscribed large language model (LLM) services such as ChatGPT or
  Gemini, or a local large language model configured in series and deployed on its own computing power.
---

# Model

## **New large language model**

<figure><img src="../.gitbook/assets/image (286).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (287).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (288).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (289).png" alt=""><figcaption></figcaption></figure>

1. After entering, click "+Add" in the upper right corner to start setting.
2. Select a service provider (for example: OpenAI / Azure / Gemini / Ollama / Claude)
3. Set content according to different service providers
   1. Name: Customizable, the name of the model that will be displayed in the system
   2. Model: Please enter the usage model

> Note: Please fill in manually, the system will not automatically list the options. (Example: `gpt-5`, `gpt-4o`, `gemini-pro`, `llama3-70b`...etc.)
       >
       > For example, if `gpt-6` is mistakenly planted, an error message will appear during Agent testing:
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
   5. Organization: Optional. Generally, the Key can be left blank. Some OpenAI may need to fill it in if it uses a short Key.
4. Advanced settings
   1. If you use **Cloud Model** → It is recommended to leave it blank and the system will automatically update the latest price.
   2. If you use **your own deployment model**→ you can evaluate whether to fill in the rate yourself.
5. Click Create to complete the settings.

## **Model setting content description**

<table><thead><tr><th width="186"> Setting item </th>ZXQPL ACEHOLDER5QXZ Description</th><th>Options</th></tr>ZXQPLACEHOL DER10QXZ<tbody><tr><td>Service name</td>ZXQPLACEHOL DER15QXZ provides the service name of the model </td><td><code>openai</code>, <code>gemini</code>, <code>ollama</code> (on-premises)</td></tr><tr><td> modeZXQPLACEHOLDER28 Type of QXZ<td> model </td><td><code>chat</code>, <code>embedding</code></td></tr><tr><td> model ZXQP The LACEHOLDER40QXZ<td> service provides usable model </td><td>. Example: <code>gpt-4.1</code>, <code>gemini-2.0-flash</code> etc., depending on the settings during system installation </td></tr><tr><td> name </td><td> in AI Studio The name used to identify this model is </td><td>. The default is the same as the model. The user enters </td></tr><tr><td>. Description ZXQPLACEHOLD Description of ER60QXZ<td> model </td><td> User input </td></tr><tr><td>API Key/API basic </td><td> service selection <code>openai</code> and <code>gemini</code> Enter the key and select Enter the URL of the model API service when <code>ollama</code> Website </td><td> User enters </td></tr><tr><td> to customize the price (Advanced settings) Whether </td><td> provides model service prices for calculation using generative AI Cost of </td><td>User Options</td></tr><tr><td> Pricing Model (Advanced Settings) How is the </td><td> service priced? </td><td> is preset to enter cost per million marks </td></tr><tr><td> (Advanced settings) </td><td>Enter the amount </td>ZXQPLACEHOLDER101QX ZUser inputs </td></tr><tr><td>output cost (Advanced settings) </td><td>Enter the amount </td>ZXQPLACEHOLDER10 9QXZ user input </td></tr><tr>ZXQPLACEHOLDER113QX ZEnable status</td><td>Enable/Stop model</td>ZXQPLACEHOLDER11 7QXZUser Options</td></tr></tbody></table>

> Note: The service name, mode and model cannot be changed after the model is created.
