---
description: "Administrators can create and adjust usage quota plans to manage how often and how much system resources each user can use."
---
---
# quota

## quota plan

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">project</th><th width="170">name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>name</td><td>The display name of the quota plan (for example: <code>default</code>, <code>VVIP</code>, <code>Plan VIP</code>）。</td></tr><tr><td>2</td><td>Usage reset cycle</td><td>How often quotas are reset (for example: daily, weekly, hourly).</td></tr><tr><td>3</td><td>Fee Limit(USD)</td><td>Maximum allowed spend per reset period (in USD).<code>-1</code> Represents unlimited.</td></tr><tr><td>4</td><td>founder</td><td>The name of the administrator who created this scheme.</td></tr><tr><td>5</td><td>Modification date</td><td>The modification time of the quota plan.</td></tr><tr><td>6</td><td>describe</td><td>An internal note or description of the quota scheme's purpose.</td></tr><tr><td>7</td><td>action</td><td>Button to edit or delete this scenario.</td></tr></tbody></table>

## **New quota plan**

Administrators can create a new usage quota plan by setting parameters such as name, description, cost limit, and reset period. These plans will control the frequency of users consuming paid resources (such as API tokens, model usage times) according to the limits set here.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

1. Go to the Set Default Quota Plan tab.
2. Click the Default User Quota Plan drop-down menu to see a list of available plans.
3. Select the desired scenario from the list (e.g. , , ).

> Note: Administrators can create or update a plan in the Quota Plan tab before setting it as default.

## **Quota plan binding management**

**Quota Plan Binding Management** function allows administrators to manually assign exclusive usage quota plans to specific users, overriding the default settings.

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

1. Go to System Settings > User Quota Plan Binding Management.
2. Click "Create" to create a new binding.
3. On the left (Dataset), select the quota scheme to allocate (for example, , , ).
4. On the right (User) select one or more users from the drop-down list.
5. Click the "+" button to add users manually.
6. Click OK to confirm the assignment.

> Note: Once assigned, even if the default plan is modified later, the user will still execute according to the bound custom plan.

## **Quota Adjustment Record**

The **Quota Adjustment Record** page records all manual changes to user quota usage, especially operations from the **User Quota Plan Binding Management** tab.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

When the administrator clicks the **Refresh icon** on the **User Quota Plan Binding Management** tab, the system will pop up a window asking to enter the **Reason for Resetting Usage**. This field is required to complete the reset operation. After confirmation, the updated budget and reason will be displayed on the User Quota Adjustment Record page.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">project</th><th width="220">Field name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>username</td><td>The name of the user whose quota was manually adjusted.</td></tr><tr><td>2</td><td>Before processing budget (USD)</td><td>User budget before adjustment (in USD).</td></tr><tr><td>3</td><td>After processing budget (USD)</td><td>Adjusted budget (in U.S. dollars).</td></tr><tr><td>4</td><td>Reason for resetting usage</td><td>Used to record reasons for manual updates or corrections.</td></tr><tr><td>5</td><td>Creation date</td><td>The date the adjustment was performed.</td></tr></tbody></table>
