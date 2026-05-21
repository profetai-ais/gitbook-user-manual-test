---
description: >-
  AI Studio 可讓 IT 人員串聯外部訂閱的大語言模型 (LLM) 服務，如 ChatGPT 或是
  Gemini，或是設定串接在自有算力上部署的地端大語言模型。
---

# 模型

## **新增大語言模型**

<figure><img src="../.gitbook/assets/image (269).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (270).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (271).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (272).png" alt=""><figcaption></figcaption></figure>

1. 進入後，點擊右上角 「＋新增」 開始設定。
2. 選擇服務商 (例如：OpenAI / Azure / Gemini / Ollama / Claude)
3. 根據不同服務商設定內容
   1. 名稱：可自訂，將顯示於系統內的模型名稱
   2.  模型：請輸入使用模型

       > 注意：請手動填寫，系統不會自動列出選項。 (例：`gpt-5`、`gpt-4o`、`gemini-pro`、`llama3-70b` …等)
       >
       > 例如若有誤植為 `gpt-6`，在 Agent 測試時會出現錯誤訊息提示：
       >
       > Received Model Group=gpt-6
       >
       > Available Model Group Fallbacks=None
       >
       > 模式：若是自行輸入模型，將需要另外選擇模式 (例如：Chat / Embedding)
   3.  API 基礎：請輸入服務商提供的 API Key

       > 注意：若輸入錯誤，系統會回傳授權錯誤
       >
       > * OpenAI：請填寫 API 前綴（Prefix）即可。例如：`https://api.openai.com/v1`
       > * Gemini：不需填寫 API Base URL，系統會自動處理路由。
   4. API Key：請填入 API Key
   5. 組織：非必填，一般 Key 可留空，有部分 OpenAI 若使用短 Key 可能會需要填寫。
4. 進階設定
   1. 若使用 **雲端模型** → 建議留白，由系統自動更新最新價格。
   2. 若使用 **自家部署模型**→ 可評估是否自行填入費率。
5. 點擊創建，完成設定。

## **模型設定內容說明**

<table><thead><tr><th width="186">設定項目</th><th width="288">說明</th><th>選項</th></tr></thead><tbody><tr><td>服務名稱</td><td>提供模型的服務名稱</td><td><code>openai</code>, <code>gemini</code>, <code>ollama</code> (on-premises)</td></tr><tr><td>模式</td><td>模型的類型</td><td><code>chat</code>, <code>embedding</code></td></tr><tr><td>模型</td><td>服務提供可使用的模型</td><td>例：<code>gpt-4.1</code>, <code>gemini-2.0-flash</code> 等，視系統安裝時的設定</td></tr><tr><td>名稱</td><td>在 AI Studio 裡辨識此模型使用的名稱</td><td>預設與模型相同，使用者輸入</td></tr><tr><td>描述</td><td>模型的描述</td><td>使用者輸入</td></tr><tr><td>API 金鑰/API 基礎</td><td>服務選擇 <code>openai</code> 與 <code>gemini</code> 時輸入金鑰，選擇 <code>ollama</code> 時輸入模型 API 服務的 URL 網址</td><td>使用者輸入</td></tr><tr><td>自訂價格 (進階設定)</td><td>是否提供模型服務價格，用於計算使用生成式 AI 的成本</td><td>使用者選項</td></tr><tr><td>定價模型 (進階設定)</td><td>服務如何定價？</td><td>預設為每百萬個標記</td></tr><tr><td>輸入成本 (進階設定)</td><td>輸入金額數值</td><td>使用者輸入</td></tr><tr><td>輸出成本 (進階設定)</td><td>輸入金額數值</td><td>使用者輸入</td></tr><tr><td>啟用狀態</td><td>啟用/停止模型</td><td>使用者選項</td></tr></tbody></table>

> 注意：模型建立完成後無法變更 服務名稱、模式 與 模型。

## 模型支援清單

AI Studio 目前支援多種模型接入來源，包含：

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



> 注意：上述清單主要是 AI Studio 目前支援的模型接入來源。實際使用時，模型可採用 Cloud 或 On-premise 方式部署，會依客戶的環境需求、模型授權、API 服務或私有化部署條件而定。
