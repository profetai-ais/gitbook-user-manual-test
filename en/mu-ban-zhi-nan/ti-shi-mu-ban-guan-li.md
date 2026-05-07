# Prompt template management

## Introduction

Prompt templates are used to simplify the way users ask questions. Frequently asked questions or methods of obtaining information can be templated, allowing users to only provide key information and obtain high-quality responses without writing prompt words. Enterprises can use this feature to improve response consistency and ensure that generative AI responses comply with enterprise policies.

> Note: By default, only AI Studio administrators can modify these settings.

## **New prompt template**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click "Add" to display the window to create a prompt word template.
2. Select prompt template type
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multilingual label. Please refer to [多國語言設定](ti-shi-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to [多國語言設定](ti-shi-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
5. Create "Field"
6. &#x20;Set prompt words in the "Prompt Word Settings" tab
7. Click "OK" to complete the addition

### Multi-language settings

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click the "Earth" button on the screen for automatic translation. Users can also manually edit the content.
2. After automatic translation is completed, click the "OK" button to save the content.

> Note: The large language model options in the "Model" menu should be based on the configuration of the actual installation environment. The options presented in the documentation are for reference only.

### **Prompt template type**

* **Chat Tips:** Templates for all scenarios. After completing the editing, you can save it for use in the "Application Templates" on the "Explore" page.
* **Agent Tips:** Prompt word templates specifically bound to the assistant will not appear in the "Explore" page for collection.

### **Field Description**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

_Field_ can be regarded as a variable in the prompt word, allowing the user to provide necessary information in the prompt word according to the actual scenario. Fields are of the following types:

* **Text:** Single line input field, the text length can be set.
* **Multi-line text:** Multi-line input field, the text length can be set.
* **List:** Create options that the user can choose from.
* **Number:** Numeric input field, where the maximum/minimum value can be set.
* **File Upload:**&#x5EFA;Establish a field that allows users to upload files.

## Permissions

The creator can grant access rights to other users through "Permissions" (please refer to [權限功能介紹](../ru-men-zhi-nan/ji-chu-jie-mian-jie-shao.md) for role definition).

> Note: The creator is the default "manager", and each project can only have one owner.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

| 項目 | 操作名稱 | 說明 |
| -- | ---- | ----------------------------- |
| 1 | 編輯表格 | 允許使用者編輯表格的呈現方式 |
| 2 | 刷新 | 點擊後刷新列表 |
| 3 | 內容篩選 | 進階篩選指定內容 |
| 4 | 批次刪除 | 勾選項目後左上角的刪除按鈕便會顯示，可讓使用者刪除多個項目 |
| 5 | 搜尋欄位 | 搜尋 名稱 |
| 6 | 邀請 | 邀請組織 / 成員 |
| 7 | 動作 | 轉移您的角色或刪除選定的使用者 |

### **New member**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click "Add" to open the conversation box
2. The input box can search for organizations or users
3. Select the corresponding permissions
4. Enter keywords to jump out to the corresponding organization/user
5. You can click the level button on the right to confirm the level of the character.
6. After selecting the target organization/user, you can click the label to open the view menu and view all users within the organization level and role.
7. Click the "Add" button to complete the invitation
