---
description: Administrators can create and adjust usage quota plans to manage the frequency and amount of system resources that each user can use.
---

# Quota

## Quota Plan

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80"> project ZXQPLACEHOLDER 4QXZ<th width="170">Name</th><th>Description</th>ZXQPLACEH OLDER9QXZ</thead><tbody><tr><td>1ZX QPLACEHOLDER14QXZ<td> name </td><td> The display name of the quota scheme (for example: <code>default</code>, <code>VVIP</code>, <code>Plan VIP</code>). </td></tr><tr><td>2ZXQPLACEHOLDE R28QXZ<td>Usage reset period</td><td>The frequency of quota reset (for example: daily, weekly, hourly). </td></tr><tr><td>3ZXQPLACEHOLDER3 6QXZ<td>Fees Limit (USD)</td><td>Maximum spend (in USD) allowed during each reset period. <code>-1</code> stands for unlimited. </td></tr><tr><td>4</td><td> Created by </td><td> The name of the administrator who created this plan. </td></tr><tr><td>5</td><td> modification date </td><td> modification time of the quota plan. </td></tr><tr><td>6</td><td> An internal note or explanation describing the purpose of the </td><td> quota scheme. </td></tr><tr><td>7</td><td> Action </td><td> Button to edit or delete this plan. </td></tr></tbody></table>

## **New quota plan**

Administrators can create a new usage quota plan by setting parameters such as name, description, cost limit, and reset period. These plans will control the frequency of users consuming paid resources (such as API tokens, model usage times) according to the limits set here.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

1. Go to System Settings > Usage Quota Limits.
2. Select the Quota Plan tab.
3. Click the plus button to open the Add/Update Quota Plan form.
4. Name: Display name of the scheme.
5. Description: Optional internal remarks.
6. Cost Limit (USD): The amount allowed per reset cycle (-1 represents no limit).
7. Usage Reset Cycle: Choose daily, weekly or hourly.
8. Click OK to save the new quota plan.

## **Set default quota plan**

**Default Quota Plan** Defines the baseline usage limit for all newly created users unless otherwise manually assigned to a specific quota plan.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

1. Go to the Set Default Quota Plan tab.
2. Click the Default User Quota Plan drop-down menu to view the list of available plans.
3. Select the desired scheme from the list (e.g. `預設`, `VVIP`, `超低配額`).

> Note: Administrators can create or update a plan in the Quota Plan tab before setting it as default.

## **Quota plan binding management**

**Quota Plan Binding Management** function allows administrators to manually assign exclusive usage quota plans to specific users, overriding the default settings.

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

1. Go to System Settings > User Quota Plan Binding Management.
2. Click "Create" to create a new binding.
3. On the left (Dataset), select the quota scheme to be allocated (for example, `預設`, `VVIP`, `Plan 1`).
4. Select one or more users from the drop-down list on the right (User).
5. Click the "+" button to add users manually.
6. Click OK to confirm the assignment.

> Note: Once assigned, even if the default plan is modified later, the user will still execute according to the bound custom plan.

## **Quota adjustment record**

The **Quota Adjustment Record** page records all manual changes to user quota usage, especially operations from the **User Quota Plan Binding Management** tab.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

When the administrator clicks the **Refresh icon** on the **User Quota Plan Binding Management** tab, the system will pop up a window asking to enter the **Reason for Resetting Usage**. This field is required to complete the reset operation. After confirmation, the updated budget and reason will be displayed on the User Quota Adjustment Record page.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80"> project ZXQPLACEHOLDER4Q XZ<th width="220">Field name</th><th>Description</th>ZXQPLACEHO LDER9QXZ</thead><tbody><tr><td>1ZXQPL ACEHOLDER14QXZ<td>Username</td><td>Username whose quota is manually adjusted. </td></tr><tr><td>2</td><td>Before processing the budget (USD)</td><td> User budget before adjustment in USD. </td></tr><tr><td>3</td><td>After processing the budget (USD)</td><td>Adjusted budget in US dollars. </td></tr><tr><td>4</td><td> reset usage reason </td><td> is used to record the reason for manual update or correction. </td></tr><tr><td>5</td><td> Creation date </td><td> Date when adjustment is performed. </td></tr></tbody></table>
