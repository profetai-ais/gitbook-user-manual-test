# 提示模板管理

## 簡介

提示模板用於簡化使用者詢問問題的方式。常被詢問的問題或是資訊取得的方式可模板化，讓使用者只需提供關鍵資訊，不用編寫提示詞便能取得高品質的回覆。企業可使用此功能提升回應一致性，確保生成式 AI 的回覆符合企業政策要求。

> 注意：預設情況下，僅有 AI Studio 管理員可修改這些設定。

## **新增提示模板**

<figure><img src="../.gitbook/assets/image (277).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (278).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (279).png" alt=""><figcaption></figcaption></figure>

1. 點選「新增」顯示建立提示詞模板視窗
2. 選擇提示模板類型
3. 「名稱」欄位中輸入知識名稱後點擊右側按鈕建立多語言標籤，請參閱 [多國語言設定](ti-shi-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
4. 「描述」欄位中輸入知識描述後點擊右側按鈕建立多語言標籤，請參閱 [多國語言設定](ti-shi-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
5. 建立「字段」
6. &#x20;在「提示詞設置」分頁中設置提示詞
7. 點擊 「確定」 完成新增

### 多國語言設定

<figure><img src="../.gitbook/assets/image (275).png" alt=""><figcaption></figcaption></figure>

1. 點擊畫面的「地球」按鈕進行自動翻譯，使用者也可以手動編輯內容
2. 自動翻譯完成後點擊「確定」按鈕，儲存內容

> 注意：「模型」選單中的大語言模型選項請依實際安裝環境的配置為主，說明文件內呈現的選項僅供參考。

### **提示模板的類型**

* **聊天提示：** 用於所有場景的模板。完成編輯後，可於「探索」頁面中的「應用模板」中收藏使用。
* **Agent 提示：** 專門與助手綁定的提示詞模板，不會出現在「探索」頁面中供人收藏。

### **字段說明**

<figure><img src="../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

_字段_ 可視為提示詞中的變數，讓使用者依實際場景提供提示詞中必要的資訊。字段有以下種類：

* **文本：** 單行輸入欄位，可設定文字長度。
* **多行文本：** 多行的輸入欄位，可設定文字長度。
* **列表：** 建立可讓使用者選擇的選項。
* **數字：** 數值的輸入欄位，可設定最大/最小值。
* **檔案上傳：**&#x5EFA;立可以讓使用者上傳檔案的欄位。

## 權限

建立者可以透過「權限」授予其他使用者存取權限（角色定義請參考 [權限功能介紹](../ru-men-zhi-nan/ji-chu-jie-mian-jie-shao.md) )。

> Note： 建立者是預設的「管理者」，每個項目只能有一個擁有者。

<figure><img src="../.gitbook/assets/image (281).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (282).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (283).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (284).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (285).png" alt=""><figcaption></figcaption></figure>

1. 點擊「添加」開&#x555F;_&#x65B0;增成&#x54E1;_&#x5C0D;話方塊
2. 輸入框能搜尋組織或使用者
3. 選擇對應的權限
4. 輸入關鍵字跳出對應的組織/使用者
5. 可點選右邊的層級按鈕確認角色的層級
6. 選擇目標組織/使用者後，可點擊標籤打開檢視選單，檢視組織層級及角色內的所有使用者
7. 點擊「添加」 按鈕，完成邀請
