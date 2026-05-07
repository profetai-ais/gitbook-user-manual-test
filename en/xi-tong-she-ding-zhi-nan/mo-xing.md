---
description: >-
  AI Studio 可讓 IT 人員串聯外部訂閱的大語言模型 (LLM) 服務，如 ChatGPT 或是
  Gemini，或是設定串接在自有算力上部署的地端大語言模型。
---

# Model

## **New large language model**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. After entering, click "+Add" in the upper right corner to start setting.
2. Choose a service provider (for example: OpenAI / Azure / Gemini / Ollama / Claude)
3. Set content according to different service providers
 1. Name: Customizable, the name of the model that will be displayed in the system
 2. Model: Please enter the model to use

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
 5. Organization: Optional. Generally, Key can be left blank. Some OpenAI may need to fill in if short Key is used.
4. advanced settings
 1. If using **Cloud Model** → It is recommended to leave it blank and the system will automatically update the latest price.
 2. If you use **your own deployment model**→ you can evaluate whether to fill in the rate yourself.
5. Click Create to complete the settings.

## **Model setting content description**

<table><thead><tr><th width="186">設定項目</th><th width="288">說明</th><th>選項</th></tr></thead><tbody><tr><td>服務名稱</td><td>提供模型的服務名稱</td><td><code>openai</code>, <code>gemini</code>, <code>ollama</code> (on-premises)</td></tr><tr><td>模式</td><td>模型的類型</td><td><code>chat</code>, <code>embedding</code></td></tr><tr><td>模型</td><td>服務提供可使用的模型</td><td>例：<code>gpt-4.1</code>, <code>gemini-2.0-flash</code> 等，視系統安裝時的設定</td></tr><tr><td>名稱</td><td>在 AI Studio 裡辨識此模型使用的名稱</td><td>預設與模型相同，使用者輸入</td></tr><tr><td>描述</td><td>模型的描述</td><td>使用者輸入</td></tr><tr><td>API 金鑰/API 基礎</td><td>服務選擇 <code>openai</code> 與 <code>gemini</code> 時輸入金鑰，選擇 <code>ollama</code> 時輸入模型 API 服務的 URL 網址</td><td>使用者輸入</td></tr><tr><td>自訂價格 (進階設定)</td><td>是否提供模型服務價格，用於計算使用生成式 AI 的成本</td><td>使用者選項</td></tr><tr><td>定價模型 (進階設定)</td><td>服務如何定價？</td><td>預設為每百萬個標記</td></tr><tr><td>輸入成本 (進階設定)</td><td>輸入金額數值</td><td>使用者輸入</td></tr><tr><td>輸出成本 (進階設定)</td><td>輸入金額數值</td><td>使用者輸入</td></tr><tr><td>啟用狀態</td><td>啟用/停止模型</td><td>使用者選項</td></tr></tbody></table>

> Note: The service name, mode and model cannot be changed after the model is created.
