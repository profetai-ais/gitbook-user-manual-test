# tag management

## Introduction

The tag management function helps users classify and manage items in the system through tags. Users can add different labels to each item to quickly identify, filter and find target items in the list. Users can centrally view, create, edit or delete tags here, and confirm the functional module to which each tag belongs.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

## Create tags

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Enter the "Tag Management" page in "System Settings".
2. Click the "Add" button in the upper right corner.
3. Enter the label name, or click the button on the right to create a multi-language label, please refer to [ 多國語言設定](biao-qian-guan-li.md#duo-guo-yu-yan-she-ding)
4. Select the function module to which this label belongs.
5. After confirming that the content is correct, click Save or Create. After the creation is completed, the tag will appear in the tag management list.

### Multi-language settings

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click the "Earth" button on the screen for automatic translation. Users can also manually edit the content.
2. After automatic translation is completed, click the "OK" button to save the content.

> Note: The large language model options in the "Model" menu should be based on the configuration of the actual installation environment. The options presented in the documentation are for reference only.

### Things to note

* Tags are mainly used to classify, filter and manage projects. It is recommended that users confirm the naming rules before creating tags to avoid tags with similar meanings but different names in the same module, making subsequent management difficult.
* Tags with duplicate names cannot be created under the same functional module; tags with the same name can be used under different functional modules. For example, Agent and Knowledge Base can each have labels with the same name in the future, but they will belong to different functional modules.
* Tag names support multiple languages, and the search will be based on the current system language. If the user switches languages, the display or search results may be different depending on the language setting.

## Delete tag

When a user deletes a label that has been used by other data, the system will display a deletion confirmation window and provide two processing methods:

* **Replace other tags**

If "Replace other tags" is selected, the user needs to specify a new tag as the replacement target. After confirmation, all data that originally referenced this tag will be changed to reference the new tag. This action cannot be undone after it is completed.

* **No replacement, delete all associations**

If you select "Don't replace, delete all associations", the system will remove all data associations with this label. The original data itself will not be deleted, but the tag will no longer remain on the data. This action cannot be undone after it is completed.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Enter the "Tag Management" page.
2. Find the tag you want to delete and click the delete icon on the right side of the column.
3. Choose processing method:
 * Select "Replace with other label" and specify the new label to replace it with.
 * Or select "Don't replace, delete all associations".
4. Click "Continue".
5. The system will display the confirmation window again based on your selection. After confirming that the content is correct, click "Replace" or "Delete" to complete the operation.

### Things to note

* After deleting a label or replacing a label association, the action cannot be undone. Before executing, please confirm whether the tag is still used by other data, and confirm whether it needs to be replaced with other tags first.
* If you select "Replace other tags", all data that references the original tag will be changed to reference the new tag. If you select "Don't replace, delete all associations", all data that references the original tag will have the tag association removed.
* Deleting a label will only remove the label itself or its associations. It will not delete the feature modules or other data to which the label has been applied.
