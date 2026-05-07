---
description: 管理員可以建立與調整使用配額方案，以管理每位使用者可使用系統資源的頻率與數量。
---

# quota

## quota plan

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Name⟬<table>6⟭⟬<table>7⟭Description⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Name⟬<table>16⟭⟬<table>17⟭The display name of the quota plan (for example: ⟬<table>18⟭default⟬<table>19⟭, ⟬<table>20⟭VVIP⟬<table>21⟭, ⟬<table>22⟭Plan VIP⟬<table>23⟭). ⟬<table>24⟭⟬<table>25⟭⟬<table>26⟭⟬<table>27⟭2⟬<table>28⟭⟬<table>29⟭Usage reset period ⟬<table>30⟭⟬<table>31⟭How often the quota is reset (for example: daily, weekly, hourly). ⟬<table>32⟭⟬<table>33⟭⟬<table>34⟭⟬<table>35⟭3⟬<table>36⟭⟬<table>37⟭Fee Limit (USD) ⟬<table>38⟭⟬<table>39⟭Maximum spend (in USD) allowed per reset cycle. ⟬<table>40⟭-1⟬<table>41⟭ represents unlimited. ⟬<table>42⟭⟬<table>43⟭⟬<table>44⟭⟬<table>45⟭4⟬<table>46⟭⟬<table>47⟭ Created by ⟬<table>48⟭⟬<table>49⟭The name of the administrator who created this scheme. ⟬<table>50⟭⟬<table>51⟭⟬<table>52⟭⟬<table>53⟭5⟬<table>54⟭⟬<table>55⟭Modification Date ⟬<table>56⟭⟬<table>57⟭Modification time of the quota plan. ⟬<table>58⟭⟬<table>59⟭⟬<table>60⟭⟬<table>61⟭6⟬<table>62⟭⟬<table>63⟭ An internal note or explanation describing the purpose of the ⟬<table>64⟭⟬<table>65⟭ quota scheme. ⟬<table>66⟭⟬<table>67⟭⟬<table>68⟭⟬<table>69⟭7⟬<table>70⟭⟬<table>71⟭Actions⟬<table>72⟭⟬<table>73⟭Button to edit or delete this scenario. ⟬<table>74⟭⟬<table>75⟭⟬<table>76⟭⟬<table>77⟭

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
3. Select the desired scheme from the list (e.g. `預設`, ⟬`預設`1⟭, ⟬`預設`2⟭).

> Note: Administrators can create or update a plan in the Quota Plan tab before setting it as default.

## **Quota plan binding management**

**Quota Plan Binding Management** function allows administrators to manually assign exclusive usage quota plans to specific users, overriding the default settings.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Go to System Settings > User Quota Plan Binding Management.
2. Click "Create" to create a new binding.
3. On the left (Dataset), select the quota scheme to allocate (for example, `預設`, ⟬`預設`1⟭, ⟬`預設`2⟭).
4. On the right (User) select one or more users from the drop-down list.
5. Click the "+" button to add users manually.
6. Click OK to confirm the assignment.

> Note: Once assigned, even if the default plan is modified later, the user will still execute according to the bound custom plan.

## **Quota adjustment record**

The **Quota Adjustment Record** page records all manual changes to user quota usage, especially operations from the **User Quota Plan Binding Management** tab.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

When the administrator clicks the **Refresh icon** on the **User Quota Plan Binding Management** tab, the system will pop up a window asking to enter the **Reason for Resetting Usage**. This field is required to complete the reset operation. After confirmation, the updated budget and reason will be displayed on the User Quota Adjustment Record page.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Item⟬<table>4⟭⟬<table>5⟭Field name⟬<table>6⟭⟬<table>7⟭Description⟬<table>8⟭⟬<table> 9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Username⟬<table>16⟭⟬<table>17⟭The username whose quota is manually adjusted. ⟬<table>18⟭⟬<table>19⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭⟬<table>23⟭Before budget processing (USD) ⟬<table>24⟭⟬<table>25⟭User budget in USD before adjustment. ⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭3⟬<table>30⟭⟬<table>31⟭After budget processing (USD) ⟬<table>32⟭⟬<table>33⟭Adjusted budget in USD. ⟬<table>34⟭⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭4⟬<table>38⟭⟬<table>39⟭Reset usage reason ⟬<table>40⟭⟬<table>41⟭ is used to record the reason for manual update or correction. ⟬<table>42⟭⟬<table>43⟭⟬<table>44⟭⟬<table>45⟭5⟬<table>46⟭⟬<table>47⟭Establishment Date ⟬<table>48⟭⟬<table>49⟭The date the adjustment was performed. ⟬<table>50⟭⟬<table>51⟭⟬<table>52⟭⟬<table>53⟭
