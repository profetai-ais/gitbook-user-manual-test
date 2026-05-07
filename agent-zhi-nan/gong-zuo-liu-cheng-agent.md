---
description: 工作流程 Agent 讓使用者以建立流程的方式，設計 Agent 可如何透過 AI Studio 提供的功能元件完成使用者的複雜任務。
---

# 工作流程 Agent

## **建立工作流程 Agent**

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (188).png" alt=""><figcaption></figcaption></figure>

1. 點擊畫面靠右上方的「 + 建立」按鈕
2. 在彈出視窗中選擇「 Agent 類型」為 _工作流程_
3. 在「名稱」欄位中輸入知識名稱後點擊右側按鈕建立多語言標籤，請參閱 [多國語言設定](gong-zuo-liu-cheng-agent.md#duo-guo-yu-yan-she-ding)
4. 在「描述」欄位中輸入知識描述後點擊右側按鈕建立多語言標籤，請參閱 [多國語言設定](gong-zuo-liu-cheng-agent.md#duo-guo-yu-yan-she-ding)
5. 點擊「Workflow Template」選單選擇工作流程模板
6. 點擊「儲存」按鈕完成新增，系統自動進入 Agent 編輯畫面讓使用者完成設定

### 多國語言設定

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption></figcaption></figure>

1. 點擊畫面的「地球」按鈕進行自動翻譯，使用者也可以手動編輯內容
2. 自動翻譯完成後點擊「確定」按鈕，儲存內容

> 注意：工作流程選單中的工作流程模板選項請依實際安裝環境的配置為主，說明文件內呈現的選項僅供參考。

## 工作流程 Agent 功能介面

工作流程 Agent 的首頁可分為幾個主要區域，如下所示：

<figure><img src="../.gitbook/assets/image (190).png" alt=""><figcaption></figcaption></figure>

1.  **Agent 功能選項：** 提供 Agent 功能設定的連結

    功能選項區包含以下功能連結，點擊後畫面呈現對應的設定頁面：

<table><thead><tr><th width="250">名稱</th><th>說明</th></tr></thead><tbody><tr><td>基礎設置</td><td>編輯 Agent 的主頁</td></tr><tr><td>流程設置</td><td>編輯 Agent 的工作流程</td></tr><tr><td>會話日誌</td><td>提供此 Agent 的對話紀錄</td></tr><tr><td>成員管理</td><td>管理此 Agent 的存取權限</td></tr><tr><td>AI WEBAPP</td><td>設定此 Agent 的網頁嵌入</td></tr><tr><td>API Key</td><td>提供第三方應用安全呼叫 API 的憑證</td></tr></tbody></table>

2. **基本資訊**：可編輯 Agent 名稱、描述和啟用狀態
3. **應用設置：** 根據 Agent 類型提供 Agent 行為的相關設定

<table><thead><tr><th width="250">名稱</th><th>說明</th></tr></thead><tbody><tr><td>歡迎頁面</td><td>設定Agent 問題設定</td></tr><tr><td>提示詞模板</td><td>加入現有提示詞模板供後續使用</td></tr><tr><td>檔案處理方式</td><td>控制上傳檔案的處理方式</td></tr></tbody></table>

4. **調適預覽：** 讓使用者測試問答結果是否如預期

## **基本設定**

所有類型的 Agent 首頁都共享 基本設定 區塊，其中包括 啟用狀態 的開關，以及用於更新 Agent 名稱和描述的 設定 按鈕。點擊設定按鈕會彈出以下對話方塊：

<figure><img src="../.gitbook/assets/image (191).png" alt=""><figcaption></figcaption></figure>

1. **Agent 狀態**：使用者可編輯 Agent 的啟用狀態，切換開關時會立即改變狀態。
2. **基本設定編輯**：能編輯最基本的名稱、描述及國際語言翻譯。

### Agent 狀態設定

<figure><img src="../.gitbook/assets/image (191).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (192).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (193).png" alt=""><figcaption></figcaption></figure>

1. 點擊狀態攔，打開介面
2. 點擊發布按鈕
3. 可複製在工作空間的網址
4. 點擊對話按鈕後，打開工作空間對話
5. 點擊未發佈按鈕可取消發佈

## **應用設置**

根據 Agent 類型提供 Agent 行為的相關設定，以下將說明 _工作流程 Agent_ 的應用設置。

### **提示詞模板**

可將已建立或已收藏的應用模板（提示詞模板）與 Agent 綁定，使用時僅需填入必要資訊，加快問答流程。

<figure><img src="../.gitbook/assets/image (194).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (196).png" alt=""><figcaption></figcaption></figure>

### **歡迎頁面**

使用者可自行設定預設的對話內容，讓 Agent 在對話開始前提供可直接點選的提問方向，幫助使用者更快速開始互動。

<figure><img src="../.gitbook/assets/image (195).png" alt=""><figcaption></figcaption></figure>

## **調適預覽**

使用者可在此區域測試 Agent 行為與回覆內容，根據回覆調整 Agent 的配置。

<figure><img src="../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>

## 工作流程設定

Agent 功能選項中的「工作流程設定」用於編輯 Agent 的工作流程，點擊後即開啟與此 Agent 綁定的工作流程的編輯畫面。

> 流程編輯的畫面說明與操作，請見[編輯工作流程](bian-ji-gong-zuo-liu-cheng.md)

## **會話日誌**

會話日誌提供此 Agent 所有的對話紀錄，管理人員可依標題、使用者與對話時間區間篩選紀錄。

日誌記錄裡也保留了處理流程；當對話出現錯誤或效能不佳時，管理人員可檢視每個回覆產生的處理流程來發掘原因。

<figure><img src="../.gitbook/assets/image (198).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (199).png" alt=""><figcaption></figcaption></figure>

## 權限

建立者可以透過「權限」授予其他使用者存取權限（角色定義請參考[權限功能介紹](../ru-men-zhi-nan/quan-xian-gong-neng-jie-shao.md))。

> Note： 建立者是預設的「擁有者」，每個項目只能有一個擁有者。

<figure><img src="../.gitbook/assets/image (201).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="99">項目</th><th width="132">操作名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>編輯表格</td><td>允許使用者編輯表格的呈現方式</td></tr><tr><td>2</td><td>刷新</td><td>點擊後刷新列表</td></tr><tr><td>3</td><td>內容篩選</td><td>進階篩選指定內容</td></tr><tr><td>4</td><td>狀態切換</td><td>在表格上單選或多選快速切換狀態</td></tr><tr><td>5</td><td>批次刪除</td><td>勾選項目後左上角的刪除按鈕便會顯示，可讓使用者刪除多個項目</td></tr><tr><td>6</td><td>搜尋欄位</td><td>搜尋 名稱</td></tr><tr><td>7</td><td>邀請</td><td>邀請組織 / 成員</td></tr><tr><td>8</td><td>啟用狀態</td><td>使用者權限啟用狀態</td></tr><tr><td>9</td><td>動作</td><td>轉移您的角色或刪除選定的使用者</td></tr></tbody></table>

### **新增成員**

<figure><img src="../.gitbook/assets/image (202).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (203).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (204).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (205).png" alt=""><figcaption></figcaption></figure>

1. 點擊「邀請」開&#x555F;_&#x65B0;增成&#x54E1;_&#x5C0D;話方塊
2. 輸入框能搜尋組織或使用者
3. 選擇對應的權限
4. 輸入關鍵字跳出對應的組織/使用者
5. 可點選右邊的層級按鈕確認角色的層級
6. 選擇目標組織/使用者後，可點擊標籤打開檢視選單，檢視組織層級及角色內的所有使用者
7. 點擊「添加」按鈕，完成邀請

## **Web App**

Agent 可被嵌入至網頁提供問答服務，例如下圖所示：

<figure><img src="../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

使用者若想將 Agent 嵌入到網頁裡使用，便需要利用此功能建立嵌入網頁前端的程式碼。

### **新增 AI WEBAPP**

<figure><img src="../.gitbook/assets/image (206).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (207).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (208).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (209).png" alt=""><figcaption></figcaption></figure>

1. 進入 「 Agent 功能清單」 中的 Web App
2. 點擊 「+」 開啟 _建立_ Web App 對話方塊
3. 「名稱」欄位中輸入知識名稱後點擊右側按鈕建立多語言標籤，請參閱 [多國語言設定](gong-zuo-liu-cheng-agent.md#duo-guo-yu-yan-she-ding)
4. 「描述」欄位中輸入知識描述後點擊右側按鈕建立多語言標籤，請參閱 [多國語言設定](gong-zuo-liu-cheng-agent.md#duo-guo-yu-yan-she-ding)
5. 點擊 「儲存」 完成
6. 新的 Web App 將出現在清單中。使用 「動作」 選單進行 「編輯」、「設定到期日」 或 「刪除」
7. 點擊 Web App 名稱以存取資訊頁面，並檢視 「嵌入程式碼」、設定 _應用程式語言_、_請求與標記限制_ 等

> Note：每個 Agent 可以有多個 API 金鑰和相符的嵌入程式碼，以獨立管理不同 Web App 實例的到期日和使用限制。

## API Key

API Key 是用於驗證身分的存取金鑰，讓系統在呼叫 Agent API 時，能辨識請求來源並套用對應的權限與使用配額。請妥善保管您的 API Key，避免外流；若您懷疑金鑰已被洩漏，建議立即更換並更新所有已使用該金鑰的整合設定。

<figure><img src="../.gitbook/assets/image (210).png" alt=""><figcaption></figcaption></figure>

### 新增 API Key

<figure><img src="../.gitbook/assets/image (211).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (212).png" alt=""><figcaption></figcaption></figure>

1. 進入 「 Agent 功能清單」 中的 API Key
2. 點擊 「+」 開啟 _建立_ API Key 對話視窗
3. 輸入API Key 的名稱
4. 選擇是否要啟用 Rate Limit 並且設定數值
5. 點擊「儲存」 按鈕

> 請注意 : 儲存後請立即複製您的ID和API金鑰，以免遺失。

### 複製 Endpoint

Endpoint 是 Agent API 的服務入口位置（URL）。系統會將 API 請求送往此位置以執行對應的功能。請依使用情境選擇正確的 Endpoint（例如測試環境或正式環境），避免將請求送往錯誤環境或導致連線失敗。

Endpoint的複製按鈕位於搜尋框旁邊，點擊複製按鈕即可複製URL。請留意複製URL時所在的環境。

<figure><img src="../.gitbook/assets/image (213).png" alt=""><figcaption></figcaption></figure>
