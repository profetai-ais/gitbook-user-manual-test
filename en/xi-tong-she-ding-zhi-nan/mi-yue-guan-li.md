---
description: 本頁面用於集中管理系統所需的密鑰（API Key）。透過此頁可新增、檢視與刪除密鑰，確保系統服務能安全且正確地運作。
---

# Key management

## Page navigation

After entering the "Key Management" page, the screen will display the list of currently created keys. The field descriptions are as follows:

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="210">Name</th><th>Description</th></tr></thead><tbody><tr><td>Type</td><td>Key type (e.g. SERPER, LiteLLM), represents the service type corresponding to this key</td></tr><tr><td>Name</td><td>Key name, used to identify this API Key Purpose</td></tr><tr><td>Key</td><td>API Key Value, only displayed in mask mode for security reasons</td></tr><tr><td>Tenant ID</td><td>Tenant identification code</td></tr><tr><td>Expire Date</td><td>When key expires</td></tr><tr><td>Crea tor</td><td>Created by</td></tr><tr><td>Created Date</td><td>Establishment Time</td></tr><tr><td>Modified Date</td><td>Last updated</td></tr><tr><td>Actions </td><td> operation function, currently provides deletion (trash can icon) </td></tr></tbody></table>

## Add new key

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

1. After clicking the "+" in the upper right corner, the setting window for adding a new key will open. Please complete the following settings in order:
2. Type: Select the key type.
3. Name: Enter the identification name of this API Key. It is recommended to fill in the specific purpose (for example: `litellm api key`) to facilitate subsequent management.
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

* **刪除後的密鑰無法復原**
* 若該 API Key 正被系統或流程使用中，刪除後可能導致相關功能無法正常運作
* 建議在刪除前，先確認該金鑰已不再被任何服務或流程引用
