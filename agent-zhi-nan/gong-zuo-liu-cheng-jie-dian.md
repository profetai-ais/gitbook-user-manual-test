# 工作流程節點

## 簡介

工作流程系統提供多樣化的節點設計，用於構建靈活、智慧且模組化的助手。每個節點在提升系統邏輯、使用者互動以及後端整合方面都扮演著不同的角色。

<figure><img src="../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">項目</th><th width="160">節點名稱</th><th>在工作流程中的用途</th></tr></thead><tbody><tr><td>1</td><td>知識檢索</td><td>從內部知識庫或文件資料庫中檢索相關資訊。</td></tr><tr><td>2</td><td>LLM</td><td>使用語言模型（例如 GPT-5.2 Thinking/GPT-5.2 Instant/Gemini 3）執行提示，根據當前輸入生成或推理結果。</td></tr><tr><td>3</td><td>回應</td><td>定義使用者實際看到的內容 — 輸出並顯示助手的回覆。</td></tr><tr><td>4</td><td>註解</td><td>在畫布上添加內部註解或標註 — 不與實際邏輯相連。</td></tr><tr><td>5</td><td>變數節點</td><td>擷取、儲存或轉換前一步驟的數值，以供後續節點使用。</td></tr><tr><td>6</td><td>護欄</td><td>可在流程中檢查與限制內容，協助降低個人資料外洩、資訊安全與法遵相關風險，讓輸出內容更符合使用規範與管理需求。</td></tr><tr><td>7</td><td>分類</td><td>根據預先定義的邏輯或基於模型的分類，自動為輸入加上標籤或引導路徑。</td></tr><tr><td>8</td><td>分叉</td><td>描述資料在各節點間的流向與順序，讓任務可被自動化執行。</td></tr><tr><td>9</td><td>合併</td><td>把不同分支的輸出收斂到同一個節點，統一交給後續節點處理。</td></tr></tbody></table>

### **知識檢索**

從內部知識庫或文件資料庫中檢索相關資訊。

<div align="center" data-with-frame="true"><figure><img src="../.gitbook/assets/image (28).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">項目</th><th width="160">功能名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>知識檢索</td><td>Input的內容（輸入「/」選擇query為使用者的問題）</td></tr><tr><td>2</td><td>知識庫參考</td><td>選擇所需的知識庫</td></tr><tr><td>3</td><td>檢索參數</td><td>參考「測試知識庫-檢索參數設定」</td></tr></tbody></table>

### **LLM**

使用語言模型（例如 GPT-5.2 Thinking/GPT-5.2 Instant/Gemini 3）執行提示，根據當前輸入生成或推理結果。



<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (29).png" alt="" width="188"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">項目</th><th width="160">功能名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>LLM名稱</td><td>輸入節點名稱，以利識別</td></tr><tr><td>2</td><td>LLM參數調整</td><td>參考 <a href="liao-tian-agent.md#can-shu">參數</a></td></tr><tr><td>3</td><td>模型</td><td>更換節點所使用的語言模型（與 2. 中的模型設定相同）</td></tr><tr><td>4</td><td>上下文</td><td>Input的內容（輸入「/」選擇query為使用者的問題）</td></tr><tr><td>5</td><td>使用節點檔案</td><td>允許LLM從前面節點取得哪些檔案</td></tr><tr><td>6</td><td>檔案處理</td><td>參考 <a href="https://www.notion.so/3509f9da96be81ef9413d427bc2132c7?pvs=21">檔案處理</a></td></tr><tr><td>7</td><td>啟用知識庫</td><td>參考 <a href="https://www.notion.so/3509f9da96be81d7b1bbe69f43f236d4?pvs=21">知識庫來源</a></td></tr><tr><td>8</td><td>Agent 協作</td><td>參考 <a href="liao-tian-agent.md#agent-xie-zuo">Agent 協作</a></td></tr><tr><td>9</td><td>技能</td><td>參考 <a href="liao-tian-agent.md#ji-neng">技能</a></td></tr><tr><td>10</td><td>參考記憶</td><td>啟用後，LLM在回覆時會參考在記憶庫的記憶，記憶的儲存方式可參考<a href="agent-memory.md"> Agent Memory</a></td></tr><tr><td>11</td><td>對話記憶</td><td>參考 <a href="liao-tian-agent.md#can-shu">參數</a> 內的對話記憶</td></tr><tr><td>12</td><td>工具</td><td>參考 <a href="liao-tian-agent.md#gong-ju">工具</a></td></tr></tbody></table>

### **回覆**

Response Node 用於定義 **Agent 的最終輸出內容**，負責將流程中整理完成的結果，回傳給使用者或作為後續系統輸出的回應。

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (30).png" alt="" width="246"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">項目</th><th width="160">功能名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>節點名稱</td><td>輸入節點名稱，以利識別</td></tr><tr><td>2</td><td>說明</td><td>可填寫此節點的用途說明</td></tr><tr><td>3</td><td>配置變數</td><td>輸入/以配置變數</td></tr></tbody></table>

### **註解**

在畫布上添加內部註解或標註 — 不與實際邏輯相連。

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (31).png" alt="" width="249"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">項目</th><th width="160">功能名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>節點名稱</td><td>輸入節點名稱，以利識別</td></tr><tr><td>2</td><td>備註</td><td>輸入備註內容以供後續識別</td></tr></tbody></table>

### **變數節點**

擷取、儲存或轉換前一步驟的數值，以供後續節點使用。

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (32).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">項目</th><th width="200">功能名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>變數（全域變數名稱）</td><td>用於選擇/指定要寫入的<strong>全域變數鍵值</strong>（例如：<code>global.age</code>），以便在後續流程節點中能以一致的名稱讀取與引用。</td></tr><tr><td>2</td><td>變數內容（變數值）</td><td>用於設定該全域變數的<strong>實際值（Value）</strong>，供後續節點直接取用。</td></tr></tbody></table>

### 護欄

根據預先定義的邏輯或基於模型的分類，自動為輸入加上標籤或引導路徑。

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (33).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">項目</th><th width="160">功能名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>配置變數</td><td>輸入/以配置變數</td></tr><tr><td>2</td><td>阻擋/遮罩</td><td>選擇護欄運作的模式</td></tr><tr><td>3</td><td>類別</td><td>依照不同的類型選擇阻擋/遮罩的內容</td></tr></tbody></table>

### **分類**

根據預先定義的邏輯或基於模型的分類，自動為輸入加上標籤或引導路徑。

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (34).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">項目</th><th width="160">功能名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>模型</td><td>更換節點所使用的語言模型</td></tr><tr><td>2</td><td>上下文</td><td>Input的內容（輸入「/」選擇query為使用者的問題）</td></tr><tr><td>3</td><td>類別</td><td>將問題分類</td></tr></tbody></table>

### 分叉

描述資料在各節點間的流向與順序，讓任務可被自動化執行。

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (35).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">項目</th><th width="160">功能名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>分支</td><td>檢視目前分支數量</td></tr><tr><td>2</td><td>分支狀態</td><td>檢視目前分支狀態</td></tr></tbody></table>

### 合併

把不同分支的輸出收斂到同一個節點，統一交給後續節點處理。

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (36).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">項目</th><th width="160">功能名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>等待</td><td>檢視等待的節點數量</td></tr><tr><td>2</td><td>輸入狀態</td><td>檢視目前輸入狀態</td></tr><tr><td>3</td><td>等待超時</td><td>設定等待超時</td></tr></tbody></table>
