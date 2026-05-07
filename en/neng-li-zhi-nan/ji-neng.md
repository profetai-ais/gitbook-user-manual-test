# Skill

## Introduction

By adding different Skills, Agents can perform more specific tasks, such as obtaining external information, connecting tools, processing specific processes, or completing operations that cannot be performed directly. You can configure the appropriate Skill for the Agent according to your needs, making it more flexible in responding and performing tasks, and more closely related to actual usage scenarios.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

## Manually add skills

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Go to the Skills tab
2. Click Add and select Create
3. Select a classified group, or click the + sign on the right to add a new group
4. The left side is the list directory. When you create a skill for the first time, there is a set of folders and Skill.md that cannot be deleted by default. However, you can add additional folders and files. For the new method, please refer to [Add a new folder or file] (ji-neng.md#xin-zeng-zi-liao-jia-huo-dang-an)
5. Fill in the file content according to the format
6. You can click Publish to complete the creation or initialize the entire draft.

> Please note: Saving does not mean publishing the content for online use

### Add folder or file

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click above the list on the left to choose to add a file or folder
2. Enter the name according to the selected type. Please note that when adding a new file, you need to add an additional file name extension.

### Edit/delete folder or file

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Hover your mouse over the data you want to edit or delete
2. A button will appear on the right, which can be clicked and used according to the user's needs.

## Import skills

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Go to the Skills tab
2. Click Add and select import skills
3. Select a classified group, or click the + sign on the right to add a new group
4. Import files in specified format (only supports **.zip, .md, .skill**)
5. Click Import to complete the creation

## View security level

After each skill is imported, the system will automatically scan it and assign different security levels. Users can click on the icon to view detailed content.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

### Security level determination

The current security level is determined based on inspection and evaluation based on the relevant specifications of **OWASP Top 10 for LLM**.

Reference: [https://genai.owasp.org/llm-top-10/](https://genai.owasp.org/llm-top-10/)

## Use skills

There are two locations used:

* **Agent → Skill settings on the left**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

* **Workflow → LLM Node → Skill Settings**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>
