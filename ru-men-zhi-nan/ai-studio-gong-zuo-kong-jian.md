---
description: 工作空間是使用者與 Agent 互動的地方。
---

# AI Studio 工作空間

介面主要由兩個部分組成：

* **對話記錄**：使用者可以建立新的對話，或快速存取先前的對話紀錄。
* **聊天區域**：與 Agent 進行對話的地方。

> 注意： 以下螢幕擷圖僅供參考。實際的對話紀錄、 Agent 及提示範本可能因您的環境而異。

## **對話記錄**

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

對話記錄區域分為兩個部分：

* **近期對話** ：已產生的對話串會儲存在此區域，點擊任何對話串即可在聊天區域中開啟。
* **近期 Agent**：曾經對話過的 Agent 會列在此處。

對話記錄區域可用的操作：

<table><thead><tr><th width="90">項目</th><th width="157">操作名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>探索</td><td>回到探索 Agent / 應用模板頁面</td></tr><tr><td>2</td><td>近期 Agent / 對話</td><td>近期使用的 Agent 與對話</td></tr><tr><td>3</td><td>建立</td><td>建立新對話</td></tr><tr><td>4</td><td>編輯</td><td>編輯所選對話紀錄的名稱</td></tr><tr><td>5</td><td>刪除</td><td>刪除所選對話紀錄</td></tr></tbody></table>

## **聊天區域**

<figure><img src="../.gitbook/assets/image (117).png" alt=""><figcaption></figcaption></figure>

<table data-first-column-sticky data-full-width="false"><thead><tr><th width="80">項目</th><th width="161">操作名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>參考來源</td><td>點擊以查看 Agent 回應中參考的來源，方便使用者進一步探索或驗證資訊</td></tr><tr><td>2</td><td>動作按鈕</td><td>由左至右：複製回應文字、相關提問、花費金額 / Token</td></tr><tr><td>3</td><td>加入</td><td>添加附加檔案，或使用提示詞模板</td></tr><tr><td>4</td><td>輸入框</td><td>使用者在此輸入提示。點擊送出按鈕將提示傳送給所有選取的 Agent 進行回應</td></tr></tbody></table>

> 補充說明：附件上傳入口的顯示可能因 Agent 設定而異。部分 Agent 或環境可由管理者控制是否顯示「檔案上傳（Upload File）」圖示；當此功能被關閉時，聊天輸入區將不會顯示附件入口，使用者亦無法在該會話中附加檔案。若您在工作區中未看到附件按鈕，請確認目前選取的 Agent 是否允許檔案附件功能，或洽詢系統管理員。

## **在聊天中使用提示範本**

<figure><img src="../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

1. 在提示輸入區按下「/」鍵，或者點擊「+」 的「提示詞模板」，即可顯示可用的提示範本清單
2. 從清單中點擊所需的提示範本
3. 輸入必要的參數，並點擊「Send Directly」取得 Agent 的回應；或點擊「Editing Prompt」在送出前修改內容

可用的提示範本類型：

<table><thead><tr><th width="176">範本類型</th><th>說明</th></tr></thead><tbody><tr><td>User Prompt</td><td> 從「探索」區域新增到個人收藏的提示範本，可在任何 Agent 對話中使用</td></tr><tr><td>Agent Prompt</td><td> 綁定到特定 Agent 的提示範本，只能在該 Agent 中使用</td></tr></tbody></table>

## **聊天會話檔案**

在與 Agent 進行會話時，會涉及兩種檔案。點擊「…」內的檔案圖示可進行**檢視**，並依權限執行**下載**或**刪除**等操作：

File Icon

* **參考檔案**：使用者作為提示附件上傳的檔案。
* **工作檔案**： Agent 在回應或輸出中產生的檔案。

下載與存取權限說明：

* 系統會依據知識庫 / 資料集的下載存取控管（Download access control）與使用者登入狀態判斷是否允許下載。
* 若使用者未被授權或未完成驗證，系統可能會阻擋下載、隱藏下載入口，或顯示權限不足提示。
* Agent 在回應中產生的「工作檔案」若來源涉及受控資料，同樣會套用相同的存取規則。

## **使用配額**

**使用配額** 區域讓使用者清楚了解在 **AI Studio 工作區** 中使用 AI 模型時的 Token 與成本消耗情況。Token 代表處理的最小資料單位，包括使用者輸入與模型輸出。此功能可幫助使用者即時追蹤與管理使用情況。

> 注意： 預設情況下，配額使用會每日自動重置。

<figure><img src="../.gitbook/assets/image (113).png" alt=""><figcaption></figcaption></figure>

使用明細會顯示在 **兩個位置**，各自有不同用途：

<table data-full-width="false"><thead><tr><th width="83">項目</th><th width="121">顯示區域</th><th width="122">位置</th><th width="276">顯示指標</th><th>用途</th></tr></thead><tbody><tr><td>1</td><td>每日配額總覽</td><td>側邊欄左下角</td><td>- <strong>Quota Plan</strong>：目前預算與已花費金額（例如 0.01 / 10.00 USD）<br>- <strong>Usage</strong>：當日配額使用百分比視覺化</td><td>提供所有會話的每日使用概況</td></tr><tr><td>2</td><td>會話層級 Token 明細</td><td>每個 AI 回應下方（滑鼠懸停圖示顯示）</td><td>- <strong>Total Input Tokens</strong>：包含提示、系統指令、上下文<br>- <strong>Total Output Tokens</strong>：AI 生成的回應<br>- <strong>Total Tokens</strong>：輸入與輸出 Token 總和<br>- <strong>Total Usage Cost</strong>：依當前模型價格計算的成本</td><td>提供每次互動的詳細成本拆解</td></tr></tbody></table>

## 畫布

畫布功能可協助使用者將 AI 產生的內容呈現在右側工作區中，方便後續查看、編輯與整理。當使用者與 AI 對話並產生較長篇幅或較複雜的內容時，可透過畫布以更清楚的版面呈現，例如文件、表格、圖表、程式碼或其他視覺化內容。

畫布適用於需要長時間檢視與調整內容的情境，例如撰寫文件、整理報告、分析資料、檢視圖表，或在對話過程中持續修改同一份內容。使用者可在左側與 AI 進行討論，並於右側查看或維護畫布內容，降低在聊天訊息中反覆尋找內容的成本。

### 調用畫布

<figure><img src="../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (116).png" alt=""><figcaption></figcaption></figure>

1. 點擊左下角+號，選擇畫布，功能會出現在輸入框中。
2. 在聊天視窗中輸入需求，請 AI 產生文件、表格、圖表或其他內容。
3. 當系統產生可使用畫布呈現的內容時，畫面中會顯示畫布卡片。
4. 點選畫布卡片後，系統會將內容開啟於右側畫布工作區，使用者可在畫布中查看完整內容。
5. 若內容需要調整，可繼續透過聊天視窗請 AI 修改，或依系統支援情況直接編輯畫布內容，修改後的內容會顯示於畫布中，方便使用者持續檢視與整理。

### 注意事項

Canvas 適合用於較長、較複雜，或需要反覆查看與修改的內容。若只是簡短文字回覆，系統可能會直接顯示於聊天視窗中，不一定會開啟 Canvas。

不同內容類型可支援的操作方式可能不同，例如文件、表格、圖表或程式碼的呈現與編輯方式可能有所差異。若 Canvas 內容由 AI 產生，建議使用者在採用前再次確認內容是否正確，必要時可請 AI 進一步修正或補充。

## 語音轉文字

語音聽寫功能可協助使用者透過語音輸入文字內容。使用者只需開啟麥克風並開始說話，系統即可將語音內容轉換為文字，減少手動輸入的時間，提升資料填寫或文字輸入的效率。

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

1. 進入 Agent 對話頁面，點選文字輸入框旁的麥克風圖示。
2. 若系統跳出麥克風權限提示，請允許系統使用麥克風。
3. 開始清楚說出需輸入的內容。
4. 語音錄製完成後，點選「確認」按鈕。
5. 轉譯完成後，文字內容將顯示於輸入欄位中。請確認文字內容是否正確，若有錯字或語意不完整，可手動修改後再送出。

### 注意事項

為提升語音辨識準確度，建議在安靜的環境中使用此功能，並以清楚、穩定的語速說話。若周圍噪音較多、語速過快，或發音不清楚，可能會影響系統辨識結果。

語音轉譯需要一段處理時間，請於點選確認按鈕後等待系統完成轉譯。轉譯產生的文字可能出現錯字、漏字或標點符號不完整的情況，送出前請務必再次確認內容。
