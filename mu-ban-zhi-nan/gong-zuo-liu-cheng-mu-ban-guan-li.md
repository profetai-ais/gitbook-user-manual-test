# 工作流程模板管理

## 簡介

流程模板用於工作流程助手，讓使用者可透過視覺化的方式設計，如何處理使用者在工作流程助手的對話中輸入的提示詞。

> **注意**：預設情況下，僅有 AI Studio 管理員可修改這些設定。

## **建立新工作流程模板**

> 流程的編輯操作 請見 [編輯工作流程](../agent-zhi-nan/bian-ji-gong-zuo-liu-cheng.md) 中的說明

## **建立新模板的方式**

#### **全新模板**

此選項將建立一個空白的流程模板。

<figure><img src="../.gitbook/assets/image (248).png" alt=""><figcaption></figcaption></figure>

1. 點擊右上角 "新增" 新增按鈕
2. 「名稱」欄位中輸入知識名稱後點擊右側按鈕建立多語言標籤，請參閱 [多國語言設定](gong-zuo-liu-cheng-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
3. 「描述」欄位中輸入知識描述後點擊右側按鈕建立多語言標籤，請參閱 [多國語言設定](gong-zuo-liu-cheng-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
4. 點選 "確定" 按鈕完成新增，新建立的流程將出現於模板列表中，點擊名稱可開啟編輯畫面

#### 多國語言設定

<figure><img src="../.gitbook/assets/image (249).png" alt=""><figcaption></figcaption></figure>

1. 點擊畫面的「地球」按鈕進行自動翻譯，使用者也可以手動編輯內容
2. 自動翻譯完成後點擊「確定」按鈕，儲存內容

> 注意：「模型」選單中的大語言模型選項請依實際安裝環境的配置為主，說明文件內呈現的選項僅供參考。

#### **從模板複製**

此選項讓使用者複製一個既有的工作流程模板到新的流程中編輯。

<figure><img src="../.gitbook/assets/image (251).png" alt=""><figcaption></figcaption></figure>

1. 從模板列表中選擇要複製的模板
2. 點擊複製按鈕
3. 新建立的流程將出現於模板列表中

#### **匯入模板**

此選項讓使用者從檔案匯入一個工作流程模板到新的流程中編輯。

<figure><img src="../.gitbook/assets/image (252).png" alt=""><figcaption></figcaption></figure>

1. 點擊右上方更多按鈕，選擇匯入檔案
2. 點擊 "檔案上傳區" 選擇要匯入的模板檔案 (副檔名為 `.pwflow` 的檔案)
3. 「名稱」欄位中輸入知識名稱後點擊右側按鈕建立多語言標籤，請參閱 [多國語言設定](gong-zuo-liu-cheng-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
4. 「描述」欄位中輸入知識描述後點擊右側按鈕建立多語言標籤，請參閱 [多國語言設定](gong-zuo-liu-cheng-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
5. 再點擊一次 "確定" 按鈕完成新增，新建立的流程將出現於模板列表中

## 權限

建立者可以透過「權限」授予其他使用者存取權限（角色定義請參考[權限功能介紹](../ru-men-zhi-nan/quan-xian-gong-neng-jie-shao.md) )。

> Note： 建立者是預設的「管理者」，每個項目只能有一個擁有者。

<figure><img src="../.gitbook/assets/image (253).png" alt=""><figcaption></figcaption></figure>

| 項目 | 操作名稱 | 說明                            |
| -- | ---- | ----------------------------- |
| 1  | 編輯表格 | 允許使用者編輯表格的呈現方式                |
| 2  | 刷新   | 點擊後刷新列表                       |
| 3  | 內容篩選 | 進階篩選指定內容                      |
| 4  | 批次刪除 | 勾選項目後左上角的刪除按鈕便會顯示，可讓使用者刪除多個項目 |
| 5  | 搜尋欄位 | 搜尋 名稱                         |
| 6  | 邀請   | 邀請組織 / 成員                     |
| 7  | 動作   | 轉移您的角色或刪除選定的使用者               |

### **新增成員**

<figure><img src="../.gitbook/assets/image (254).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (255).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (256).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (257).png" alt=""><figcaption></figcaption></figure>

1. 點擊「添加」開&#x555F;_&#x65B0;增成&#x54E1;_&#x5C0D;話方塊
2. 輸入框能搜尋組織或使用者
3. 選擇對應的權限
4. 輸入關鍵字跳出對應的組織/使用者
5. 可點選右邊的層級按鈕確認角色的層級
6. 選擇目標組織/使用者後，可點擊標籤打開檢視選單，檢視組織層級及角色內的所有使用者
7. 點擊「添加」按鈕，完成邀請
