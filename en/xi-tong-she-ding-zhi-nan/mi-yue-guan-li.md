---
description: "This page is used to centrally manage the keys (API Key) required by the system. Through this page, you can add, view and delete keys to ensure that system services can operate safely and correctly."
---
---
# Key management

## Page navigation

After entering the "Key Management" page, the screen will display the list of currently created keys. The field descriptions are as follows:

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="210">name</th><th>illustrate</th></tr></thead><tbody><tr><td>Type</td><td>Key type (such as SERPER, LiteLLM), representing the type of service corresponding to this key</td></tr><tr><td>Name</td><td>Key name identifying the purpose of this API Key</td></tr><tr><td>Key</td><td>API Key value, only displayed in mask mode for security reasons</td></tr><tr><td>Tenant ID</td><td>Tenant identification code</td></tr><tr><td>Expire Date</td><td>when key expires</td></tr><tr><td>Creator</td><td>founder</td></tr><tr><td>Created Date</td><td>Setup time</td></tr><tr><td>Modified Date</td><td>Last updated</td></tr><tr><td>Actions</td><td>Operation function, currently provides deletion (trash can icon)</td></tr></tbody></table>

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
