---
description: "Chat Agent allows users to directly interact with large-scale language models, and is suitable for tasks such as brainstorming, information summarization, and generating formatted text content, without worrying about the leakage of sensitive data."
---
---
# Chat Agent

## **Create Agent**

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (155).png" alt=""><figcaption></figcaption></figure>

1. Click the "+ Create" button in the upper right corner of the screen
2. Select "Agent Type" in the pop-up window
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multi-language label. Please refer to 
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to 
5. Click the "Label" menu to select the label to be brought into this Agent
6. Click the "Model" menu to select the large language model used by this Agent
7. Click the "Save" button to complete the addition, and the system will automatically enter the Agent editing screen for the user to complete the settings.





### Multi-language settings <a href="#duo-guo-yu-yan-she-ding" id="duo-guo-yu-yan-she-ding"></a>

<figure><img src="../.gitbook/assets/image (157).png" alt=""><figcaption></figcaption></figure>

1. Click the "Earth" button on the screen for automatic translation. Users can also manually edit the content.
2. After automatic translation is completed, click the "OK" button to save the content.

> Note: The large language model options in the "Model" menu should be based on the configuration of the actual installation environment. The options presented in the documentation are for reference only.

## Chat Agent functional interface

<figure><img src="../.gitbook/assets/image (158).png" alt=""><figcaption></figcaption></figure>

The chat agent homepage is mainly divided into several parts, as shown below:

1. **Agent Function Options**: The function options area contains the following links, each link will open the corresponding setting page

| name | illustrate |
| --------- | ------------------- |
| Basic settings | Edit the Agent's home page |
| session log | Provide conversation history for this Agent |
| Member management | Manage access to this Agent |
| AI WEBAPP | Configure web embedding for this Agent |
| API Key | Provide credentials for third-party applications to securely call the API |

2. **Basic information**: You can view the Agent name, creation and editing time and personnel, and activation status
3. **Application Settings:** Provides settings related to Agent behavior based on Agent type

| name | illustrate |
| ---------- | --------------------------- |
| Inference parameters | Control how responses are generated |
| Knowledge base configuration | Select parameters and available knowledge sources |
| tool | Enable and configure available tools |
| Skill | Functions used to expand Agent capabilities |
| Agent collaboration | Allows Agents to connect in series and collaborate with other Agents to perform tasks |
| Agent welcome page | Set initial conversation content |
| prompt word template | Provides reusable prompt word templates for quick use |
| File handling | Control how uploaded files are processed |
| guardrail | Control content output |

4. **Adaptation Preview:** Allows users to test whether the Q&A results are as expected

## **Basic settings**

<figure><img src="../.gitbook/assets/image (159).png" alt=""><figcaption></figcaption></figure>

All types of Agent homepages share the **Basic Settings** section, which includes an **Enabled Status** switch and a **Settings** button for updating the Agent name and description. Clicking the Settings button will pop up the following dialog box:

1. **Agent Status**: Users can edit the activation status of Agent, and the status will change immediately when the switch is switched.
2. **Basic Settings Edit**: Can edit the most basic name, description and international language translation.

### Agent status settings

<figure><img src="../.gitbook/assets/image (160).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (161).png" alt=""><figcaption></figcaption></figure>

1. Click the status bar to open the interface
2. Click the Publish button
3. URL that can be copied in the workspace
4. After clicking the dialog button, the workspace dialog opens
5. Click the Unpublished button to unpublish

## **APP SETTINGS**

### **Inference Parameters**

The settings include two tabs: "**Parameters**" and "**System Prompt Words**".

#### **parameter**

Users can control the Agent's reply behavior by adjusting the items in the "**Parameters**" tab.

<figure><img src="../.gitbook/assets/image (163).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="98">項目</th><th width="112">參數</th><th width="238">說明</th><th>範圍與數值</th></tr></thead><tbody><tr><td>1</td><td>模型</td><td>Agent 建立時選擇的預設模型；可在這裡變更</td><td>n/a</td></tr><tr><td>2</td><td>溫度</td><td>控制回覆的創造力。數值越高，回應越多元和有創意；數值越低，回應越精確和一致</td><td>0–1</td></tr><tr><td>3</td><td>Top P</td><td>控制隨機性和多樣性。數值越低，產生越保守和可預測的文字；數值越高，產生越多樣的結果</td><td>0–1</td></tr><tr><td>4</td><td>最大標記</td><td>限制最大輸出長度</td><td>依需求設定</td></tr><tr><td>5</td><td>對話記憶</td><td>儲存問答歷史以增強連貫性（可能會減慢回應時間）</td><td><code>0</code>表示無狀態回應；<code>5-10</code>可在連貫性和效能之間取得平衡。記憶越多，速度越慢。</td></tr></tbody></table>

#### instruction

Users can use the "Commands" tab to define prompts to control the Agent's language, role, tone, etc.

<figure><img src="../.gitbook/assets/image (164).png" alt=""><figcaption></figcaption></figure>



* **Use template to add new prompt words**

Users can quickly add required application templates from templates.

<figure><img src="../.gitbook/assets/image (165).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (166).png" alt=""><figcaption></figcaption></figure>

1. Add directly from the blank space; or when prompted, use the mouse to select the location to be added.
2. Click the "Template" button to open the template list and select the type of template you want to add.
3. Generate corresponding templates. New templates will be generated by inverse selection. You can edit the templates according to your own needs.
4. Click the "Save" button to complete editing.



* **Input requirements to generate prompt words**

The prompt word generation function supports "rewriting existing content" or "generating from blank". The red box above can be filled in as the basis for rewriting, and the green input box below can fill in the generation guidelines to produce results.

<figure><img src="../.gitbook/assets/image (167).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

1. Select the dialog box below and enter your requirements for prompt words.
2. Press the Enter key on the keyboard or the generate button on the right and wait for AI to automatically generate the template.
3. It is automatically generated and can be edited according to your own needs.
4. Click the "Save" button to complete editing.

### knowledge base

#### Knowledge base sources

<figure><img src="../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>

#### Knowledge base parameters

<figure><img src="../.gitbook/assets/image (169).png" alt=""><figcaption></figcaption></figure>

### **tool**

Users can enable/disable tools accessible to Agent in settings.

<figure><img src="../.gitbook/assets/image (170).png" alt=""><figcaption></figcaption></figure>



#### **Session Memory**

<table><thead><tr><th width="250">工具</th><th>說明</th></tr></thead><tbody><tr><td>KV 會話短期記憶</td><td>能夠在會話期間精確地、基於鍵地儲存和檢索臨時資料。對於追蹤動態變數（例如<code>使用者名稱</code>、<code>所選方案</code>）非常有用。</td></tr><tr><td>graphiti - 新增記憶資料</td><td>將情節性資訊（例如互動或事件）儲存到知識圖譜中。</td></tr><tr><td>graphiti - 查詢記憶節點</td><td>檢索實體摘要或節點層級的記憶表示。</td></tr><tr><td>graphiti - 查詢記憶事實</td><td>在記憶圖譜中搜尋相關事實和結構化關係。</td></tr><tr><td>graphiti - 刪除實體關係</td><td>從圖譜中刪除實體之間定義的關係。</td></tr><tr><td>graphiti - 刪除事件片段</td><td>刪除記憶圖譜中的特定事件區段。</td></tr><tr><td>graphiti - 取得實體關係</td><td>檢索與特定實體相關的結構化關係。</td></tr><tr><td>graphiti - 取得事件片段</td><td>返回最近的記憶情節，以提供對話或決策背景。</td></tr><tr><td>graphiti - 清除記憶圖譜</td><td>重置整個基於圖譜的記憶系統。</td></tr></tbody></table>

> PS: For more information about Graphiti, please see its official website.

#### **Academic Articles**

<table><thead><tr><th width="250">工具</th><th>使用指南</th></tr></thead><tbody><tr><td>arXiv 論文搜尋</td><td>允許使用者從 arXiv 資料庫搜尋學術論文。</td></tr><tr><td>Google Scholar 搜尋</td><td>使用 Google Scholar 搜尋學術文章和引文。</td></tr></tbody></table>

#### **Web Search**

<table><thead><tr><th width="250">工具</th><th>使用指南</th></tr></thead><tbody><tr><td>Serper - 網頁內容擷取</td><td>從網頁 URL 提取可讀內容。</td></tr><tr><td>Serper - Google 搜尋</td><td>執行 Google 搜尋並返回摘要結果。</td></tr><tr><td>Serper - 專利搜尋</td><td>搜尋已發布的專利和相關文件。</td></tr><tr><td>Serper - 圖片搜尋</td><td>根據文字查詢搜尋圖片。</td></tr><tr><td>Serper - 論文搜尋</td><td>使用 Google Scholar 風格的來源查詢學術論文。</td></tr><tr><td>Serper - 新聞搜尋</td><td>根據文字查詢搜尋新聞。</td></tr><tr><td>Serper - 地圖資訊搜尋</td><td>根據文字查詢搜尋地圖。</td></tr></tbody></table>

> Note: For more information about Sperper, please see its official website.

#### **Code**

<table><thead><tr><th width="250">工具</th><th>使用指南</th></tr></thead><tbody><tr><td>執行 Python 程式碼</td><td>執行 Python 腳本或邏輯，以支援數學、資料解析或自動化等任務。</td></tr></tbody></table>

#### **Document Handling**

<table><thead><tr><th width="250">工具</th><th>使用指南</th></tr></thead><tbody><tr><td>預覽文件</td><td>在平台內以可讀格式顯示上傳的文件。</td></tr><tr><td>文件轉markdown</td><td>將文件轉換為 Markdown 格式。</td></tr></tbody></table>

#### **Other**

<table><thead><tr><th width="250">工具</th><th>使用指南</th></tr></thead><tbody><tr><td>取得目前時間</td><td>返回發出請求時的當前系統時間。</td></tr><tr><td>簡易數學式運算</td><td>在提示中執行簡單的算術運算。</td></tr><tr><td>動態思維鏈（Sequential Thinking）</td><td>將複雜問題分解為逐步思考，並可選擇修改或分支。適用於規劃、故障排除和結構化推理。</td></tr></tbody></table>

### Skill

<figure><img src="../.gitbook/assets/image (180).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (179).png" alt=""><figcaption></figcaption></figure>

By setting different skills, Agent can support more functions and task processing scenarios, such as data access, tool operation, process execution or specific task expansion. Users can configure corresponding skills according to their needs to improve the Agent's application flexibility and task processing capabilities.

### Agent collaboration

Through this function, users can establish cooperative relationships between multiple Agents and handle task content according to different divisions of responsibilities, thereby improving process flexibility and overall task processing efficiency.

<figure><img src="../.gitbook/assets/image (182).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (181).png" alt=""><figcaption></figcaption></figure>

### **Welcome Page**

Users can set their own default conversation content, allowing the Agent to provide directly clickable question directions before the conversation begins, helping users start interacting more quickly.

<figure><img src="../.gitbook/assets/image (178).png" alt=""><figcaption></figcaption></figure>

### **Prompt word template**

Users can link existing or favorited application templates (prompt word templates) to the Agent to speed up Q&A by filling in required fields.

<figure><img src="../.gitbook/assets/image (177).png" alt=""><figcaption></figcaption></figure>

### **File Processing**

**File Handling** settings allow the user to define how the Agent handles files uploaded in the workspace. This feature is particularly useful when the Agent needs to interpret, convert, or extract content from files such as PDFs, DOCX, or images.

<figure><img src="../.gitbook/assets/image (176).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="161">選項</th><th width="103">對 MCP 工具可見</th><th width="96">對 LLM 可見</th><th>說明</th><th>範例使用情境</th></tr></thead><tbody><tr><td>Do not process</td><td>X</td><td>X</td><td>檔案已上傳，但對 LLM 或 MCP 工具都不可見。不會被開啟或解讀。</td><td>– –</td></tr><tr><td>Process with Tool</td><td>O</td><td>X</td><td>檔案會傳遞給 MCP 工具進行處理，但不會傳遞給 LLM。</td><td>當您想從 CSV 或 PDF 中提取資料，但不需要 AI 生成的評論時很有用。</td></tr><tr><td>File to Image Conversion</td><td>X</td><td>O</td><td>檔案會被轉譯成圖片，僅對 LLM 可見，以供參考。</td><td>適用於掃描文件或視覺版面，其中圖表關係很重要。</td></tr><tr><td>Convert to Image &#x26; Tool</td><td>O</td><td>O</td><td>檔案會同時被轉譯為 LLM 參考和由 MCP 工具處理。</td><td>最適合需要同時解讀視覺版面和結構化資料的發票或表格。</td></tr></tbody></table>

### guardrail

Guardrails are a function used to control content output. They can check and restrict content during the process, helping to reduce risks related to personal data leakage, information security and legal compliance, and making the output content more consistent with usage specifications and management requirements.

<figure><img src="../.gitbook/assets/image (183).png" alt=""><figcaption></figcaption></figure>

## **Adaptation Preview**

Use this block to test Agent responses and adjust settings accordingly.

> Please note: Files uploaded or generated during the adaptation preview are only retained for 30 minutes.

<figure><img src="../.gitbook/assets/image (184).png" alt=""><figcaption></figcaption></figure>

### **Adjust Preview** How to upload files

* You can click the plus sign (+) in the dialog box to upload files.

<figure><img src="../.gitbook/assets/image (185).png" alt=""><figcaption></figcaption></figure>

* Also supports drag-and-drop file uploading method

<figure><img src="../.gitbook/assets/image (186).png" alt=""><figcaption></figcaption></figure>

## memory

The memory function can help users create reusable memory content for the Agent, so that the Agent can refer to preset background information, usage scenarios and processing procedures when performing tasks or responding to questions.

Users can view the created memory list on the Agent's memory page, and quickly identify the purpose of each memory through its activation status, name, description and usage context. Memory can be used to save specific task processes, judgment rules, preconditions, operating steps or precautions to help the Agent maintain consistent processing logic in subsequent interactions.

<figure><img src="../.gitbook/assets/image (187).png" alt=""><figcaption></figcaption></figure>

### build memory

<figure><img src="../.gitbook/assets/image (190).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (191).png" alt=""><figcaption></figcaption></figure>

1. Enter the Agent page. Click "Memory" in the submenu on the left.
2. Click the "Create" button in the upper right corner.
3. Fill in the basic information of memory:
 * Name: Enter the memory name.
 * Description: Enter memory description.
 * Applicable situations: Enter the usage situations where this memory is applicable.
 * Content: Enter detailed content, which can be formatted in Markdown format.
4. After confirming that the content is correct, click "Create" to complete the creation.

### View memory details

<figure><img src="../.gitbook/assets/image (189).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (188).png" alt=""><figcaption></figcaption></figure>

1. Enter the memory list.
2. Click on the memory name you want to view.
3. The system will open the details panel on the right.
4. Users can view the name, activation status, description, usage context and complete content of the memory. If the content is long, you can scroll up and down in the right panel to view it.

### Enable and disable memory

#### Memory enablement rules

The memory function includes the overall function switch and the single-stroke memory activation status.

<figure><img src="../.gitbook/assets/image (192).png" alt=""><figcaption></figcaption></figure>

If the switch is on, it means that this Agent can use the memory function. Users can still enable or disable different memories individually in the memory list.

If the switch is off, it means that this Agent does not use the memory function. Even if there are already created memories in the memory list, the Agent will not apply these memory contents.

#### Activating and deactivating single memory

<figure><img src="../.gitbook/assets/image (193).png" alt=""><figcaption></figcaption></figure>

In the memory list, the "Enabled" field is used to display whether a single memory is enabled. When the memory master switch is turned on, the activated single memory will be used as a reference for the Agent's response or task processing.

Users can disable temporarily unused memories as needed, retaining the content but not allowing the Agent to apply it; they can re-enable it if they need to use it again in the future.

## **Session Log**

Conversation records store all conversation records of this Agent. Administrators can filter records by title, user or date range. Records include processing procedures. When errors occur or responses are slow, administrators can review processing details to diagnose the problem.

<figure><img src="../.gitbook/assets/image (194).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (195).png" alt=""><figcaption></figcaption></figure>

## Permissions

The creator can grant access rights to other users through "Permissions" (please refer to role definition).

> Note: The creator is the default "manager", and each project can only have one owner.

<figure><img src="../.gitbook/assets/image (196).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">項目</th><th width="146">操作名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>編輯表格</td><td>允許使用者編輯表格的呈現方式</td></tr><tr><td>2</td><td>刷新</td><td>點擊後刷新列表</td></tr><tr><td>3</td><td>內容篩選</td><td>進階篩選指定內容</td></tr><tr><td>4</td><td>批次刪除</td><td>勾選項目後左上角的刪除按鈕便會顯示，可讓使用者刪除多個項目</td></tr><tr><td>5</td><td>搜尋欄位</td><td>搜尋 名稱</td></tr><tr><td>6</td><td>邀請</td><td>邀請組織 / 成員</td></tr><tr><td>7</td><td>動作</td><td>轉移您的角色或刪除選定的使用者</td></tr></tbody></table>

### **New member**

<figure><img src="../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (82).png" alt=""><figcaption></figcaption></figure>

1. Click "Add" to open the conversation box
2. The input box can search for organizations or users
3. Select the corresponding permissions
4. Enter keywords to jump out to the corresponding organization/user
5. You can click the level button on the right to confirm the level of the character.
6. After selecting the target organization/user, you can click the label to open the view menu and view all users within the organization level and role.
7. Click the "Add" button to complete the invitation

## **Web App**

Agents can be embedded into web pages to provide question and answer services, as shown below:

<figure><img src="../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

To embed an Agent into a website, use this feature to generate front-end embed code.

### **New Web App**

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

1. Enter the Web App in "Agent Function List"
2. Click "+" to open the _Create_ Web App dialog window
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multilingual label. Please refer to&#x20;
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to&#x20;
5. Click "Save" to complete
6. The new Web App will appear in the manifest. Use the Actions menu to Edit, Set Expiration, or Delete
7. Click the Web App name to access the information page and view Embed Code, settings _Application Language_, _Request and Tag Limits_, and more

> Note: Each Agent can have multiple API keys and matching embed code to independently manage expiration dates and usage limits for different Web App instances.

## API Key

API Key is an access key used to verify identity, allowing the system to identify the source of the request and apply corresponding permissions and usage quotas when calling the Agent API. Please keep your API Key safe to avoid leakage; if you suspect that the key has been leaked, it is recommended to immediately replace and update all integration settings that use the key.

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

### Add API Key

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

1. Enter the API Key in "Agent Function List"
2. Click "+" to open the _Create_ API Key dialog window
3. Enter the name of the API Key
4. Select whether to enable Rate Limit and set the value
5. If necessary, you can set the API Key expiration date
6. Click the "Save" button

> Please note: Please copy your ID and API key immediately after saving to avoid losing them.

### Copy Endpoint

Endpoint is the service entry location (URL) of Agent API. The system will send API requests to this location to perform the corresponding function. Please choose the correct Endpoint (such as test environment or production environment) according to the usage scenario to avoid sending requests to the wrong environment or causing connection failure.

Endpoint's copy button is located next to the search box. Click the copy button to copy the URL. Please pay attention to the environment in which you copy the URL.

<figure><img src="../.gitbook/assets/image (91).png" alt=""><figcaption></figcaption></figure>
