---
description: 本頁面用於集中管理系統所需的密鑰（API Key）。透過此頁可新增、檢視與刪除密鑰，確保系統服務能安全且正確地運作。
---

# Key management

## Page navigation

After entering the "Key Management" page, the screen will display the list of currently created keys. The field descriptions are as follows:

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Name⟬<table>4⟭⟬<table>5⟭Description⟬<table>6⟭⟬<table>7⟭⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭Type⟬<table>12⟭⟬<table>13⟭Key type (e.g. SERPER, LiteLLM), represents the service type corresponding to this key⟬<table>14⟭⟬<table>15⟭⟬<table>16⟭⟬<table>17⟭Name⟬<table>18⟭⟬<table>19⟭Key name, used to identify this API Key Purpose⟬<table>20⟭⟬<table>21⟭⟬<table>22⟭⟬<table>23⟭Key⟬<table>24⟭⟬<table>25⟭API Key Value, only displayed in mask mode for security reasons⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭Tenant ID⟬<table>30⟭⟬<table>31⟭Tenant identification code⟬<table>32⟭⟬<table>33⟭⟬<table>34⟭⟬<table>35⟭Expire Date⟬<table>36⟭⟬<table>37⟭When key expires⟬<table>38⟭⟬<table>39⟭⟬<table>40⟭⟬<table>41⟭Crea tor⟬<table>42⟭⟬<table>43⟭Created by⟬<table>44⟭⟬<table>45⟭⟬<table>46⟭⟬<table>47⟭Created Date⟬<table>48⟭⟬<table>49⟭Establishment Time⟬<table>50⟭⟬<table>51⟭⟬<table>52⟭⟬<table>53⟭Modified Date⟬<table>54⟭⟬<table>55⟭Last updated⟬<table>56⟭⟬<table>57⟭⟬<table>58⟭⟬<table>59⟭Actions ⟬<table>60⟭⟬<table>61⟭ operation function, currently provides deletion (trash can icon) ⟬<table>62⟭⟬<table>63⟭⟬<table>64⟭⟬<table>65⟭

## Add new key

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. After clicking the "+" in the upper right corner, the setting window for adding a new key will open. Please complete the following settings in order:
2. Type: Select the key type.
3. Name: Enter the identification name of this API Key. It is recommended to fill in the specific purpose (for example: `litellm api key`) to facilitate subsequent management.
4. API Key: Enter the actual API key content.
 * Fields are hidden by default
 * You can switch to show/hide through the "eye" icon on the right
5. Confirm sending: After the setting is completed, click "Ok" to save the key; if not, click "Cancel" to cancel the operation.

## delete key

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click the trash can icon in the Actions column on the far right of the column
2. Click to confirm and then perform the deletion action. The key will be removed from the list immediately.

### **Notes**

* **The deleted key cannot be restored**
* If the API Key is being used by the system or process, deletion may cause related functions to not function properly.
* It is recommended to confirm that the key is no longer referenced by any service or process before deleting it.
