---
description: "This page is used to centrally manage the keys (API Key) required by the system. Through this page, you can add, view and delete keys to ensure that system services can operate safely and correctly."
---
---
# Key management

## Page navigation

After entering the "Key Management" page, the screen will display the list of currently created keys. The field descriptions are as follows:

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="210">名稱</th><th>說明</th></tr></thead><tbody><tr><td>Type</td><td>密鑰類型（例如 SERPER、LiteLLM），代表此金鑰所對應的服務種類</td></tr><tr><td>Name</td><td>密鑰名稱，用於識別此 API Key 的用途</td></tr><tr><td>Key</td><td>API Key 值，為安全考量僅以遮罩方式顯示</td></tr><tr><td>Tenant ID</td><td>所屬租戶識別碼</td></tr><tr><td>Expire Date</td><td>密鑰到期時</td></tr><tr><td>Creator</td><td>建立者</td></tr><tr><td>Created Date</td><td>建立時間</td></tr><tr><td>Modified Date</td><td>最後更新時間</td></tr><tr><td>Actions</td><td>操作功能，目前提供刪除（垃圾桶圖示）</td></tr></tbody></table>

## Add new key

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

1. After clicking the "+" in the upper right corner, the setting window for adding a new key will open. Please complete the following settings in order:
2. Type: Select the key type.
3. Name: Enter the identification name of this API Key. It is recommended to fill in the specific purpose (for example: ) to facilitate subsequent management.
4. API Key: Enter the actual API key content.
 * Fields are hidden by default
 * You can switch to show/hide through the "eye" icon on the right
5. Confirm sending: After the setting is completed, click "Ok" to save the key; if not, click "Cancel" to cancel the operation.

## delete key

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

1. Click the trash can icon in the Actions column on the far right of the column
2. Click to confirm and then perform the deletion action. The key will be removed from the list immediately.

### **Notes**

* **The deleted key cannot be restored**
* If the API Key is being used by the system or process, deletion may cause related functions to not function properly.
* It is recommended to confirm that the key is no longer referenced by any service or process before deleting it.
