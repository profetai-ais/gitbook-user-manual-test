---
description: "Click the knowledge card in the knowledge base page to enter the setting page."
---
---
# management knowledge

## **Page Navigation**

<figure><img src="../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">項目</th><th width="180">操作名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>返回</td><td>點擊後返回知識庫首頁</td></tr><tr><td>2</td><td>收起</td><td>點擊後將選單區域最小化</td></tr><tr><td>3</td><td>知識設定選單</td><td>提供各種知識設定與測試功能</td></tr><tr><td>4</td><td>設定輸入區</td><td>根據使用者所選選單項目開啟對應操作頁面</td></tr></tbody></table>

## **Basic settings**

Users can modify the name and description of knowledge through basic settings.

step:

1. Click the _Basic Settings_ item in the "Knowledge Settings Menu"
2. Edit the text in the Name or Description field
3. Click "Save" to complete the settings

> Note: The index model cannot be modified after it is selected when creating knowledge.

## **Dataset**

The data set setting page allows users to upload and manage files. The file types supported by AI Studio are:

* Long text content (such as TXT, Markdown, DOCX, HTML, JSONL, PDF that is not a pure image, etc.)
* Structured data (CSV, Excel, etc.)

<figure><img src="../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">項目</th><th width="180">操作名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>編輯表格</td><td>允許使用者編輯表格的呈現方式</td></tr><tr><td>2</td><td>刷新</td><td>點擊後重新整理表格</td></tr><tr><td>3</td><td>篩選</td><td>可依據欄位篩選內容</td></tr><tr><td>4</td><td>我的清單</td><td>開啟後，會只顯示你創建的資料</td></tr><tr><td>5</td><td>批次下載</td><td>可一次勾選多個項目批次下載</td></tr><tr><td>6</td><td>刪除</td><td>勾選列表中的數據集後將顯示刪除按鈕，點擊後將刪除已勾選的數據集</td></tr><tr><td>7</td><td>搜尋</td><td>使用者可輸入關鍵字篩選</td></tr><tr><td>8</td><td>新增/匯入</td><td>上傳檔案，或建立一個空白的數據集</td></tr><tr><td>9</td><td>操作</td><td>使用者可編輯或刪除對應的數據集</td></tr></tbody></table>

## **New data set**

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>

1. Click the _Dataset_ item in the "Knowledge Settings Menu"
2. Click the "Add/Import" button and select _Import file_
3. Click "Upload Area" to open the system window, select the file to be uploaded, and click _Next Page_ when finished.
4. In the data processing part, you can select the strategy for splitting the file content in the "File Processing" option on the left. Click _Generate Segmented Results_ and a preview of the split data will be displayed on the right. After confirming the processing method, click _Next Page_
5. Confirm the content again and click the "Upload" button to upload the file.
6. The page returns to the data set list. The data can be used after the file status bar displays "Complete".

### File upload restrictions

To ensure data processing performance and indexing quality, the data set has the following restrictions when importing files:

| project | limit |
| ---------- | -------------- |
| Maximum number of files imported at a time | Up to **100** files |
| Maximum size of a single file | 300MB |

Additional instructions:

* If any of the above limits is exceeded, the system will display a prompt message and prevent uploading. Please adjust the number of files or split the files and re-import them.
* If the file is a large file (such as a long PDF/DOCX), it is recommended to remove unnecessary images or appendix content first to avoid long processing time.

#### Download access control

The raw file download behavior of the dataset is affected by the "Dataset Access Permissions":

* Authorized users: can download/access original files in the data set list or data block view (subject to the operation buttons provided on the screen).
* Unauthorized users: When trying to download or access the original file, the system will block it and prompt insufficient permissions; some screens may not display the download entrance or set it to be inoperable.

If you need to authorize others to download/access the dataset file, the administrator can go to the "#Dataset Access Permissions" section at the bottom of this page, add organizations or users that can access the specified dataset, and save the settings.

#### Troubleshooting: Permission settings display abnormally

If the permission details are not displayed, the block is blank, or there is no content when expanded on the "Dataset Access Permissions" page, please try the following steps:

1. Click Refresh to reload the list, or switch to another menu and back.
2. Confirm that the target file/dataset is selected in the Dataset area on the left.
3. Confirm that the current account has permissions such as "AI Studio Administrator/Knowledge Base Administrator/Domain Expert/Collaborator" to manage the knowledge base; if not, please contact the administrator for assistance.

### Display of data set status information

Click the status icon to enter the location. For detailed operation methods, please refer to the page description.

&#x20;。

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

## **Data processing when adding new data sets**

Data processing after file upload supports the following two forms:

* **Direct Segmentation**: Apply user options for segmentation
* **QA segmentation**: Files with Q\&A ​​content are segmented by questions.

#### **Direct Segmentation**

When the original content does not have a clear question and answer structure, or users want to quickly create data segments, the "direct segmentation" mode can be enabled. The system will automatically divide paragraphs according to the settings.

<table><thead><tr><th width="180">處理方式</th><th>說明</th></tr></thead><tbody><tr><td>自動</td><td>系統預設根據輸入內容長度與語言結構自動分段，適合快速上手、無需自訂規則的情境。當未指定切分方式時，系統會以斷行、句號等常見符號進行初步分段。</td></tr><tr><td>Token 分段</td><td>依據設定的分段 token 長度切分文本。建議單段長度控制在 100–1000 tokens 範圍內，避免語意破碎或截斷上下文。</td></tr><tr><td>自訂規則</td><td>提供更細緻的控制，除了段落長度（建議 100–1000）與重疊範圍（如 100 tokens）的設定外，還增加分隔符選項控制分段。</td></tr><tr><td>Regex 分段</td><td>透過特定字元（如 <code>\\n</code>、<code>。</code>、<code>,</code>、<code>;</code>）切分文本；可多種符號組合使用，適合一般自然語言處理場景。</td></tr></tbody></table>

<table><thead><tr><th width="180">處理方式的選項</th><th width="200">適用的分段處理方式</th><th>說明</th></tr></thead><tbody><tr><td>理想長度分段</td><td>Token 分段、自訂規則</td><td>可設定每個段落的目標長度（以 token 為單位）；數值越小分段越細，但上下文連結可能減弱；數值越大，則需搭配重疊範圍以保語境一致。</td></tr><tr><td>重疊範圍</td><td>Token 分段、自訂規則</td><td>定義每段與前一段重複的 token 數量（如 100），提升語境延續性。建議值介於 1 到理想長度 - 1 之間；適合處理多輪對話、技術文檔等高語境需求內容。</td></tr><tr><td>自訂分隔符</td><td>自訂規則</td><td>設定辨識分段點的符號，以分號區隔。例：設定 <code>;; ;'';</code> 會在文中出現 <code>;</code>、<code>(空格)</code>、<code>''</code> 時產生分段。</td></tr><tr><td>規則</td><td>Regex 分段</td><td>使用者自訂分段的 Regex 語法，可點擊下方預設的分段範例進行編輯：<code>.+\\n?</code> (換行分段)、<code>[^。]+。?</code> (中文句號分段)。</td></tr><tr><td>移除最後的換行符</td><td>Regex 分段</td><td>是否自動移除段尾空行 <code>\\n$</code> 符號。</td></tr></tbody></table>

> Recommendation: Use Token segmentation + overlapping range to effectively keep the semantics and context intact and avoid the statement being cut off causing information fragmentation and loss.

#### **QA Segmentation**

When processing question-and-answer document content (such as FAQs, customer service records, interview transcripts, etc.), you can improve structural recognition and semantic clarity through QA segmentation settings. The system provides the following parameters to help identify and segment questions and answer blocks.

<table><thead><tr><th width="200">選項</th><th>說明</th></tr></thead><tbody><tr><td>問題前綴</td><td>指定問題開頭的識別字串（如 <code>Q:</code>、<code>問題：</code>），系統將以此標記為新問題段落的起始點。</td></tr><tr><td>回答前綴</td><td>指定回答開頭的識別字串（如 <code>A:</code>、<code>回答：</code>），用來標記與問題對應的解答內容。</td></tr><tr><td>移除前綴</td><td>啟用後將自動移除問題與回答段落開頭的標記字串（如 <code>Q:</code>、<code>A:</code>）。</td></tr><tr><td>前綴表達式</td><td>支援使用正則表達式（Regex）進行問題與回答前綴的識別，適用於格式不固定或大量資料轉換的場景。例如：<code>^Q[0-9]*:</code> 可匹配多個問題編號。</td></tr><tr><td>移除最後一個換行符</td><td>啟用後將自動清除每段 QA 區塊結尾的多餘換行符。</td></tr></tbody></table>

## **View/Edit Dataset**

Clicking on a file name in the file list will open the _data block_ view page, allowing users to browse the indexed data content and edit it as needed.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">項目</th><th width="180">選項</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>資料塊 標籤頁</td><td>顯示該檔案被切分後產生的資料塊</td></tr><tr><td>2</td><td>參考檔案 標籤頁</td><td>顯示與資料塊關聯的所有檔案，包括被用作切分的原始檔案與作為參考資料的檔案</td></tr><tr><td>3</td><td>返回</td><td>點擊後返回資料集首頁</td></tr><tr><td>4</td><td>搜尋欄</td><td>允許使用者輸入文字搜尋相關的資料塊</td></tr><tr><td>5</td><td>新增/匯入</td><td>點擊後可手動新增資料塊</td></tr><tr><td>6</td><td>編輯</td><td>點擊後顯示資料塊的 <em>編輯</em> 與 <em>刪除</em> 操作選項</td></tr></tbody></table>

## **Edit data block content**

Users can optimize the content of data blocks to improve the accuracy of data referenced when LLM generates responses, such as adding possible question expressions to Q\&A ​​type data blocks.

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>

1. Click the "Edit" button of the data block and select _Edit_
2. Click the "Edit" button in the upper right corner of the pop-up window to open the editing interface field
3. Click the "+" button to the right of the _Question_ title to add a question
4. After entering the question content, click the "✔️" button on the upper right side of the interface to save the changes.

## **Create Reference File**

When AI Studio generates a reply by quoting the content of the data set, it can add relevant files as reference sources, such as providing specific pages and pictures of PDF or PPT, etc.

<figure><img src="../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

1. Click on the "Reference Files" tab
2. Click the "+Create" button to open the system window, select the file to upload, and click _Confirm_ after completion.
3. Confirm that the file has been uploaded correctly in the _Reference File List_ and click the "Data Block" tab after confirmation.
4. Click the "Edit" button of the data block and select _Edit_
5. Click "Linked Files" on the left
6. Click the "+Create" button to open the new file window
7. After clicking "File Menu" to select the reference file, click _Confirm_ to complete the creation of the additional reference file.

## **test**

After creating a data set, users can use the Test function to ask questions and see which data blocks were referenced when generating responses. They can also score the search results by adjusting the search parameters, thereby optimizing the data content to improve the accuracy of the cited data.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

&#x20;

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

1. Click the _Test_ item in the "Knowledge Settings Menu"
2. Click the _gear button_ to the right of the "Search text" heading to open search parameter settings
3. It is generally recommended to check "Enable Rating" below
4. Click the "LLM Scoring Model" menu to select the model you want to use
5. Adjust the "Score Threshold" setting to filter the score requirements of search results. Only results that meet the score requirements will be displayed as relevant information in _Rating Results_
6. Click the "Confirm" button to save the parameter settings
7. Enter the content/question you want to query in the "Search text" and click the _Query_ button to submit
8. Search results will be listed in "Recall Results" and sorted by recall score.
9. Click on any _recall result_ to view the complete information content, and click the Index tab to view the index used by the system to retrieve that data block

## knowledge rights

The creator can grant access rights to other users through "Knowledge Permissions" (please refer to for role definition).

> Note: The creator is the default "manager", and each project can only have one owner.

<figure><img src="../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">項目</th><th width="180">操作名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>編輯表格</td><td>允許使用者編輯表格的呈現方式</td></tr><tr><td>2</td><td>刷新</td><td>點擊後刷新列表</td></tr><tr><td>3</td><td>內容篩選</td><td>進階篩選指定內容</td></tr><tr><td>4</td><td>狀態切換</td><td>在表格上單選或多選快速切換狀態</td></tr><tr><td>5</td><td>批次刪除</td><td>勾選項目後左上角的刪除按鈕便會顯示，可讓使用者刪除多個項目</td></tr><tr><td>6</td><td>搜尋欄位</td><td>搜尋 名稱</td></tr><tr><td>7</td><td>邀請</td><td>邀請組織 / 成員</td></tr><tr><td>9</td><td>動作</td><td>轉移您的角色或刪除選定的使用者</td></tr></tbody></table>

### **New member**

<figure><img src="../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (76).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (77).png" alt=""><figcaption></figcaption></figure>

1. Click "Add" to open the conversation box
2. The input box can search for organizations or users
3. Select the corresponding permissions
4. Enter keywords to jump out to the corresponding organization/user
5. You can click the level button on the right to confirm the level of the character.
6. After selecting the target organization/user, you can click the label to open the view menu and view all users within the organization level and role.
7. Click the "Add" button to complete the invitation

## **Dataset access rights**

AI Studio provides data set access rights management, allowing enterprises to control the scope of information that different departments or users can reference when using generative AI based on information security requirements.

Access rights can be granted to organizations or individual users; if granted to an organization, all users in the organization have access to the data. For information on organization and related member settings, please refer to the Domain Twin Portal Operation Manual.

<figure><img src="../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

1. Click the _Dataset Access Permissions_ item in the "Knowledge Settings Menu"
2. Click the button to add permissions to the dataset batch
3. In the "Dataset" area, select the file for which you want to set permissions
4. Click the "Organization" tab in the right area and check the organizational level to which permissions are to be granted.
5. Click the "Users" tab in the right area to select the user to whom permissions are to be granted.
6. Search for the user you want to add in the "User Menu". After selecting, click the "+" button next to the menu to add a user.
7. After completing the changes to the organization and users, click the "Save" button in the upper right corner to retain the settings.
