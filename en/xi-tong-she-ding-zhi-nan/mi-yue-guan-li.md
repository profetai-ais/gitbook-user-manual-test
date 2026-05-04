---
description: This page is used to centrally manage the keys (API Key) required by the system. Through this page, you can add, view and delete keys to ensure that system services can operate safely and correctly.
---

# Key management

## Page Navigation

After entering the "Key Management" page, the screen will display the list of currently created keys. The field descriptions are as follows:

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="210">Name</th><th>Description</th>ZXQPL ACEHOLDER7QXZ</thead><tbody><tr><td>Type</td><td> key type (e.g. SERPER, LiteLLM), represents the service type corresponding to this key </td></tr><tr><td>Name</td><td> key name, used to identify this API Key Use of </td></tr><tr><td>Key</td><td>API Key Value, for security reasons only displayed in mask mode </td></tr><tr><td>Tenant ID</td><td> tenant identification code </td></tr><tr><td>Expire Date</td><td> key expires when </td></tr><tr><td>Crea tor</td><td>Created</td></tr><tr><td>Created Date</td><td> Creation Time</td></tr><tr><td>Modified Date</td><td>Last updated</td></tr><tr><td>Actions </td><td> operation function currently provides deletion (trash can icon) </td></tr></tbody></table>

## Add new key

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

1. After clicking the "+" in the upper right corner, the setting window for adding a new key will open. Please complete the following settings in order:
2. Type: Select the key type.
3. Name: Enter the identification name of this API Key. It is recommended to fill in the specific purpose (for example: `litellm api key`) to facilitate subsequent management.
4. API Key: Enter the actual API key content.
   * The field is hidden by default
   * You can switch to show/hide through the "eye" icon on the right
5. Confirm sending: After the setting is completed, click "Ok" to save the key; if not, click "Cancel" to cancel the operation.

## Delete key

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

1. Click the trash can icon in the Actions column on the far right of the column
2. Click Confirm and then perform the deletion action. The key will be immediately removed from the list.

### **Notes**

* **The deleted key cannot be restored**
* If the API Key is being used by the system or process, deletion may cause related functions to not function properly.
* It is recommended to confirm that the key is no longer referenced by any service or process before deleting it.
