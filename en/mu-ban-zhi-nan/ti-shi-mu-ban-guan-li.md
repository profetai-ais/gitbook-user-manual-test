# Prompt template management

## Introduction

Prompt templates are used to simplify the way users ask questions. Frequently asked questions or methods of obtaining information can be templated, allowing users to only provide key information and obtain high-quality responses without writing prompt words. Enterprises can use this feature to improve response consistency and ensure that generative AI responses comply with enterprise policies.

> Note: By default, only AI Studio administrators can modify these settings.

## **New prompt template**

<figure><img src="../.gitbook/assets/image (277).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (278).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (279).png" alt=""><figcaption></figcaption></figure>

1. Click "Add" to display the window to create a prompt word template.
2. Select prompt template type
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multi-language label. Please refer to [多國語言設定](ti-shi-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multi-language label. Please refer to [多國語言設定](ti-shi-mu-ban-guan-li.md#duo-guo-yu-yan-she-ding)
5. Create "Field"
6. &#x20;Set prompt words in the "Prompt Word Settings" tab
7. Click "OK" to complete the addition.

### Multi-language settings

<figure><img src="../.gitbook/assets/image (275).png" alt=""><figcaption></figcaption></figure>

1. Click the "Earth" button on the screen for automatic translation. Users can also manually edit the content.
2. After automatic translation is completed, click the "OK" button to save the content.

> Note: The large language model options in the "Model" menu should be based on the configuration of the actual installation environment. The options presented in the documentation are for reference only.

### **Type of prompt template**

* **Chat Tips:** Templates for all scenarios. After completing the editing, you can save it for use in the "Application Templates" on the "Explore" page.
* **Agent Tips:** Prompt word templates specifically bound to the assistant will not appear in the "Explore" page for collection.

### **Field description**

<figure><img src="../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

_Field_ can be regarded as a variable in the prompt word, allowing the user to provide necessary information in the prompt word according to the actual scenario. Fields are of the following types:

* **Text:** Single line input field, the text length can be set.
* **Multi-line text:** Multi-line input field, the text length can be set.
* **List:** Create options that the user can choose from.
* **Number:** Numeric input field, where the maximum/minimum value can be set.
* **File Upload: **&#x5EFA; Set up a field that allows users to upload files.

## Permissions

The creator can grant access rights to other users through "Permissions" (please refer to [權限功能介紹](../ru-men-zhi-nan/ji-chu-jie-mian-jie-shao.md) for role definition).

> Note: The creator is the default "manager", and each project can only have one owner.

<figure><img src="../.gitbook/assets/image (281).png" alt=""><figcaption></figcaption></figure>

| Project | Operation Name | Description |
| -- | ---- | -------------------------- |
| 1 | Edit Table | Allows the user to edit the presentation of the table |
| 2 | Refresh | Refresh the list after clicking |
| 3 | Content filtering | Advanced filtering of specified content |
| 4 | Batch deletion | After checking the items, the delete button in the upper left corner will be displayed, allowing users to delete multiple items |
| 5 | Search field | Search name |
| 6 | Invite | Invite organizations/members |
| 7 | Actions | Transfer your role or delete selected users |

### **Add new member**

<figure><img src="../.gitbook/assets/image (282).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (283).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (284).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (285).png" alt=""><figcaption></figcaption></figure>

1. Click "Add" to open the conversation box
2. The input box can search for organizations or users
3. Select the corresponding permissions
4. Enter keywords to jump out of the corresponding organization/user
5. You can click the level button on the right to confirm the level of the character.
6. After selecting the target organization/user, you can click the label to open the view menu and view all users within the organization level and role.
7. Click the "Add" button to complete the invitation
