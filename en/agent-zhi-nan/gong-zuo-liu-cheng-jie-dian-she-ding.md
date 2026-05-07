---
description: 本指南將逐步示範如何依據工作流程編輯器中的 UI 元素設定 LLM 節點。
---

# Workflow node settings



## Page introduction

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">步驟</th><th width="180">區塊</th><th>操作說明</th></tr></thead><tbody><tr><td>1</td><td>節點名稱</td><td>為 LLM 節點命名清楚且具描述性（例如：2. 產業趨勢）。這有助於在視覺與邏輯上組織流程，特別是在複雜流程中。<strong>注意：</strong> 節點名稱必須唯一才能儲存設定。</td></tr><tr><td>2</td><td>節點描述</td><td>為 LLM 節點提供簡短描述（例如：包含產業動態、政策變化、技術驅動與企業行為）。這有助於在視覺與邏輯上組織流程，特別是在複雜流程中。</td></tr><tr><td>3</td><td>模型選擇</td><td>從下拉選單選擇一個語言模型（例如：gpt-5.2-thinking 或 gpt-5.2-instant）。請確保該模型符合回應品質與預算需求。</td></tr><tr><td>4</td><td>情境（輸入變數）</td><td>設定 LLM 在推理時應參考的輸入內容。可使用來自其他節點或使用者輸入的變數傳遞動態輸入。在情境視窗中輸入 <code>/</code> 可查看可用變數。⚠️ 若要存取來自前序節點的 <code>result</code>、<code>usage</code> 或 <code>execution_time</code> 等變數，這些節點必須 <strong>明確連結</strong> 至當前節點，否則情境無法正確解析變數。</td></tr><tr><td>5</td><td>使用節點檔案</td><td>允許LLM從前面節點取得哪些檔案</td></tr><tr><td>6</td><td>檔案處理（選用）</td><td>選擇如何處理上傳的檔案。更多資訊請參考 <a href="liao-tian-agent.md#dang-an-chu-li">檔案處理</a> 章節。</td></tr><tr><td>7</td><td>知識庫</td><td>啟用時，對話時會自動查詢選用的知識。</td></tr><tr><td>13</td><td>推理設定</td><td>點擊模型選擇區旁的齒輪圖示 () 來自訂模型行為，包括：<br><em>1. 參數調整</em>：Temperature、Top P、Max Tokens（更多資訊請參閱參數表）。<br><em>2. 系統提示詞</em>：撰寫提示詞以定義角色、任務、語氣及工具行為。</td></tr></tbody></table>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">步驟</th><th width="180">區塊</th><th>操作說明</th></tr></thead><tbody><tr><td>8</td><td>Agent 協作</td><td>讓 Agent 串接並協同其他 Agent 執行任務。</td></tr><tr><td>9</td><td>技能</td><td>透過設定不同的技能，Agent 能支援更多功能與任務處理情境。</td></tr><tr><td>10</td><td>參考記憶</td><td>啟用後，對話時會參考個人的記憶庫。</td></tr><tr><td>11</td><td>記憶體設定（選用）</td><td>若需要多輪對話情境，請啟用記憶體功能。在建立多輪對話或推理鏈時設定記憶視窗大小（建議值：3–5）。<strong>注意：</strong> 建議統一會話記憶輪數以確保流程一致性且避免資訊遺失。⚠️ 一輪對話指一次問題（使用者提示）與一次回應（助手回答）的配對。</td></tr><tr><td>12</td><td>工具（選用）</td><td>若任務需要超出 LLM 原生能力的功能，可附加工具（例如使用 <strong>Serper Search</strong> 工具在生成過程中進行即時網路搜尋）。</td></tr></tbody></table>

## **How ​​to use Context and System Prompt**

When setting up the LLM node, both **Context** and **System Prompt** can contain instructions, but their purposes are different and have clear priorities:

### **Context**

> Purpose: Set dynamic input variables, which can be regarded as the "workspace" of the model - that is, the content currently referenced by the model.

**Note:**

* Use the **Context** field to pass in **query text**, **user input** or **preceding node data**.
* Supports using variables such as `${start.query}` or `${llm-nodeA.result}` to make responses more personal or contextual.
* Although you can put brief instructions here, the context field should be focused on **content** rather than rules of conduct.

### **System Prompt**

> Purpose: Define the behavior and role of the model, which can be regarded as the "permanent job description" of this node.

**Note:**

* Used to define who the model is, how it should act, and what it should accomplish.
* Commands in the system prompt word will take precedence over commands in the context.
* It is recommended to always clearly define:
 * **Role** (e.g. Product Manager, Analyst, Mentor)
 * **Task Objective** (e.g. writing a report, interpreting code)
 * **Tone** (e.g. formal, friendly)
 * **Tool usage rules** (if tools are attached)

### **File Handling**

The **File Handling** setting allows the user to define how the Assistant handles uploaded files in the workspace. This is especially useful when the assistant needs to interpret, convert or extract file content (e.g. PDF, DOCX, images) in a conversation.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="143">選項</th><th width="120">MCP 工具可見</th><th width="102">LLM 可見</th><th>說明</th><th>範例應用情境</th></tr></thead><tbody><tr><td>不處理</td><td>X</td><td>X</td><td>檔案已上傳但對 LLM 與 MCP 工具均不可見，不會被開啟或解析。</td><td>– </td></tr><tr><td>僅用工具處理</td><td>O</td><td>X</td><td>檔案傳遞至 MCP 工具處理，但不提供給 LLM。</td><td>適用於需要從 CSV 或 PDF 擷取資料但不需要 AI 評述的情況。</td></tr><tr><td>檔案轉為圖片</td><td>X</td><td>O</td><td>將檔案轉換為圖片並僅供 LLM 參考。</td><td>適用於掃描文件或需要參考版面結構的視覺資料。</td></tr><tr><td>轉為圖片與工具處理</td><td>O</td><td>O</td><td>同時將檔案轉換為圖片供 LLM 參考，並傳遞給 MCP 工具處理。</td><td>適用於需要同時解析視覺結構與結構化資料的發票或表單。</td></tr></tbody></table>
