---
description: 管理員可以建立與調整使用配額方案，以管理每位使用者可使用系統資源的頻率與數量。
---

# quota

## quota plan

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">項目</th><th width="170">名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>名稱</td><td>配額方案的顯示名稱（例如： <code>default</code>, <code>VVIP</code>, <code>Plan VIP</code>）。</td></tr><tr><td>2</td><td>用量重置週期</td><td>配額重置的頻率（例如：每天、每週、每小時）。</td></tr><tr><td>3</td><td>費用限制(USD)</td><td>每個重置週期內允許的最高花費（以美元計算）。<code>-1</code> 代表無限制。</td></tr><tr><td>4</td><td>建立者</td><td>建立此方案的管理員名稱。</td></tr><tr><td>5</td><td>修改日期</td><td>配額方案的修改時間。</td></tr><tr><td>6</td><td>描述</td><td>配額方案用途的內部註解或說明。</td></tr><tr><td>7</td><td>動作</td><td>編輯或刪除此方案的按鈕。</td></tr></tbody></table>

## **New quota plan**

Administrators can create a new usage quota plan by setting parameters such as name, description, cost limit, and reset period. These plans will control the frequency of users consuming paid resources (such as API tokens, model usage times) according to the limits set here.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Go to System Settings > Usage Quota Limits.
2. Select the Quota Plan tab.
3. Click the plus button to open the Add/Update Quota Plan form.
4. Name: Display name of the scheme.
5. Description: Optional internal remarks.
6. Cost Limit (USD): The amount allowed per reset cycle (-1 means no limit).
7. Usage Reset Cycle: Choose daily, weekly, or hourly.
8. Click OK to save the new quota plan.

## **Set default quota plan**

**Default Quota Plan** Defines the baseline usage limit for all newly created users unless otherwise manually assigned to a specific quota plan.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Go to the Set Default Quota Plan tab.
2. Click the Default User Quota Plan drop-down menu to see a list of available plans.
3. Select the desired scheme from the list (e.g. `預設`, `VVIP`, `超低配額`).

> Note: Administrators can create or update a plan in the Quota Plan tab before setting it as default.

## **Quota plan binding management**

**Quota Plan Binding Management** function allows administrators to manually assign exclusive usage quota plans to specific users, overriding the default settings.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Go to System Settings > User Quota Plan Binding Management.
2. Click "Create" to create a new binding.
3. On the left (Dataset), select the quota scheme to allocate (for example, `預設`, `VVIP`, `Plan 1`).
4. On the right (User) select one or more users from the drop-down list.
5. Click the "+" button to add users manually.
6. Click OK to confirm the assignment.

> Note: Once assigned, even if the default plan is modified later, the user will still execute according to the bound custom plan.

## **Quota adjustment record**

The **Quota Adjustment Record** page records all manual changes to user quota usage, especially operations from the **User Quota Plan Binding Management** tab.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

When the administrator clicks the **Refresh icon** on the **User Quota Plan Binding Management** tab, the system will pop up a window asking to enter the **Reason for Resetting Usage**. This field is required to complete the reset operation. After confirmation, the updated budget and reason will be displayed on the User Quota Adjustment Record page.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">項目</th><th width="220">欄位名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>使用者名稱</td><td>配額被手動調整的使用者名稱。</td></tr><tr><td>2</td><td>處理預算之前 (USD)</td><td>調整前的使用者預算（以美元計算）。</td></tr><tr><td>3</td><td>處理預算之後 (USD)</td><td>調整後的預算（以美元計算）。</td></tr><tr><td>4</td><td>重置用量原因</td><td>用來記錄手動更新或修正的原因。</td></tr><tr><td>5</td><td>建立日期</td><td>執行調整的日期。</td></tr></tbody></table>
