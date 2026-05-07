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
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multi-language label. Please refer to 
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to 
5. Create "Field"
6. &#x20;Set prompt words in the "Prompt Word Settings" tab
7. Click "OK" to complete the addition

### Multi-language settings

<figure><img src="../.gitbook/assets/image (275).png" alt=""><figcaption></figcaption></figure>

1. Click the "Earth" button on the screen for automatic translation. Users can also manually edit the content.
2. After automatic translation is completed, click the "OK" button to save the content.

> Note: The large language model options in the "Model" menu should be based on the configuration of the actual installation environment. The options presented in the documentation are for reference only.

### **Prompt template type**

* **Chat Tips:** Templates for all scenarios. After completing the editing, you can save it for use in the "Application Templates" on the "Explore" page.
* **Agent Tips:** Prompt word templates specifically bound to the assistant will not appear in the "Explore" page for collection.

### **Field Description**

<figure><img src="../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

_Field_ can be regarded as a variable in the prompt word, allowing the user to provide necessary information in the prompt word according to the actual scenario. Fields are of the following types:

* **Text:** Single line input field, the text length can be set.
* **Multi-line text:** Multi-line input field, the text length can be set.
* **List:** Create options that the user can choose from.
* **Number:** Numeric input field, where the maximum/minimum value can be set.
* **File Upload:**&#x5EFA;Establish a field that allows users to upload files.

## Permissions

The creator can grant access rights to other users through "Permissions" (for role definition, please refer to ).

> Note: The creator is the default "manager", and each project can only have one owner.

<figure><img src="../.gitbook/assets/image (281).png" alt=""><figcaption></figcaption></figure>

| project | Operation name | illustrate |
| -- | ---- | ----------------------------- |
| 1 | Edit table | Allows the user to edit the presentation of the table |
| 2 | refresh | Refresh list after click |
| 3 | Content filtering | Advanced filtering of specific content |
| 4 | Batch delete | After checking the items, the delete button in the upper left corner will be displayed, allowing users to delete multiple items. |
| 5 | search field | Search name |
| 6 | invite | Invite organizations/members |
| 7 | action | Transfer your role or remove selected users |

### **New member**

<figure><img src="../.gitbook/assets/image (282).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (283).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (284).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (285).png" alt=""><figcaption></figcaption></figure>

1. Click "Add" to open the conversation box
2. The input box can search for organizations or users
3. Select the corresponding permissions
4. Enter keywords to jump out to the corresponding organization/user
5. You can click the level button on the right to confirm the level of the character.
6. After selecting the target organization/user, you can click the label to open the view menu and view all users within the organization level and role.
7. Click the "Add" button to complete the invitation
