# Workflow template management

## Introduction

Process templates are used in workflow assistants, allowing users to visually design how to handle prompt words entered by users in the dialog of workflow assistants.

> **Note**: By default, only AI Studio administrators can modify these settings.

## **Create a new workflow template**

> For process editing operations, please see the instructions in [編輯工作流程](../agent-zhi-nan/bian-ji-gong-zuo-liu-cheng.md)

## **How ​​to create a new template**

#### **New template**

This option will create a blank process template.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click the "Add" button in the upper right corner
2. Enter the knowledge name in the "Name" field and click the button on the right to create a multilingual label. Please refer to [多國語言設定](gong-zuo-liu-cheng-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
3. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to [多國語言設定](gong-zuo-liu-cheng-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
4. Click the "OK" button to complete the addition. The newly created process will appear in the template list. Click the name to open the editing screen.

#### Multi-language settings

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click the "Earth" button on the screen for automatic translation. Users can also manually edit the content.
2. After automatic translation is completed, click the "OK" button to save the content.

> Note: The large language model options in the "Model" menu should be based on the configuration of the actual installation environment. The options presented in the documentation are for reference only.

#### **Copy from template**

This option allows users to copy an existing workflow template into a new process for editing.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Select the template to copy from the list of templates
2. Click the copy button
3. The newly created process will appear in the template list

#### **Import template**

This option allows users to import a workflow template from a file into a new process for editing.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click the More button on the upper right and select Import File
2. Click the "File Upload Area" to select the template file to be imported (the file with the file extension `.pwflow`)
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multilingual label. Please refer to [多國語言設定](gong-zuo-liu-cheng-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to [多國語言設定](gong-zuo-liu-cheng-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
5. Click the "OK" button again to complete the addition, and the newly created process will appear in the template list

## Permissions

The creator can grant access rights to other users through "Permissions" (please refer to [權限功能介紹](../ru-men-zhi-nan/quan-xian-gong-neng-jie-shao.md) for role definition).

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
