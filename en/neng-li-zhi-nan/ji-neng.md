# Skill

## Introduction

By adding different Skills, Agents can perform more specific tasks, such as obtaining external information, connecting tools, processing specific processes, or completing operations that cannot be performed directly. You can configure the appropriate Skill for the Agent according to your needs, making it more flexible in responding and performing tasks, and more closely related to actual usage scenarios.

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

## Manually add skills

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

1. Go to the Skills tab
2. Click Add and select Create
3. Select a classified group, or click the + sign on the right to add a new group
4. The left side is the list directory. When you create a skill for the first time, there is a set of folders and Skill.md that cannot be deleted by default. However, you can add additional folders and files. For the new method, please refer to .
5. Fill in the file content according to the format
6. You can click Publish to complete the creation or initialize the entire draft.

> Please note: Saving does not mean publishing the content for online use

### Add folder or file

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

1. Click above the list on the left to choose to add a file or folder
2. Enter the name according to the selected type. Please note that when adding a new file, you need to add an additional file name extension.

### Edit/delete folder or file

<figure><img src="../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

1. Hover your mouse over the data you want to edit or delete
2. A button will appear on the right, which can be clicked and used according to the user's needs.

## Import skills

<figure><img src="../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

1. Go to the Skills tab
2. Click Add and select import skills
3. Select a classified group, or click the + sign on the right to add a new group
4. Import files in specified format (only supports **.zip, .md, .skill**)
5. Click Import to complete the creation

## Import Skills from SkillsMP

### Enable the SkillsMP Import Option

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

To display the SkillsMP import option in AIS, complete the following settings first:

1. Go to the official SkillsMP platform and apply for a personal or enterprise account.
2. Create an API Key from your SkillsMP account.
   1. Application URL: https://skillsmp.com/docs/api
3. Return to AIS and go to: System Settings → Key Management
4. Click Create.
5. In the Type field, select: SkillsMP
6. Paste the API Key obtained from SkillsMP into the designated field.
7. After the key is added successfully, the SkillsMP import option will be displayed in the system.

> Note:> &#x20;The SkillsMP import feature is only displayed after the API Key setup is completed. If the SkillsMP provider and its corresponding API Key have not been added in Key Management, the SkillsMP import option will not appear in the system.

#### Rate Limits

The SkillsMP API applies different rate limits depending on whether an API Key is used.

1. Without an API Key
   * Up to 50 requests per day
   * Up to 10 requests per minute
   * Supports keyword search only
2. With an API Key
   * Up to 500 requests per day
   * Up to 30 requests per minute
   * Supports keyword search
3. Wildcard Search Is Not Supported
   * The SkillsMP API does not support wildcard searches, such as \*.
4. Quota Usage Tracking
   * Each API response includes related response headers that can be used to track the current quota usage.

### Import Skills from SkillsMP in AIS

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (163).png" alt=""><figcaption></figcaption></figure>

After the SkillsMP API Key has been configured, you can import skills from SkillsMP in AIS.

1. Go to the Skills page.
2. Click Add, then select Import from SkillsMP.
3. Select a group for the imported skill.
4. Select the skill you want to import.
5. Click the + icon to import the selected skill.

## View security level

After each skill is imported, the system will automatically scan it and assign different security levels. Users can click on the icon to view detailed content.

<figure><img src="../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

### Security level determination

The current security level is determined based on inspection and evaluation based on the relevant specifications of **OWASP Top 10 for LLM**.

Reference:

## Use skills

There are two locations used:

* **Agent → Skill settings on the left**

<figure><img src="../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

* **Workflow → LLM Node → Skill Settings**

<figure><img src="../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>
