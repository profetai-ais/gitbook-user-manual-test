---
description: "Workflow Agent allows users to create processes and design how the Agent can complete the user's complex tasks through the functional components provided by AI Studio."
---
---
# Workflow Agent

## **Create Workflow Agent**

<figure><img src="../.gitbook/assets/image (200).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (201).png" alt=""><figcaption></figcaption></figure>

1. Click the "+ Create" button in the upper right corner of the screen
2. In the pop-up window, select "Agent Type" as _Workflow_
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multilingual label. Please refer to 
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to 
5. Click the "Workflow Template" menu to select a workflow template
6. Click the "Save" button to complete the addition, and the system will automatically enter the Agent editing screen for the user to complete the settings.

### Multi-language settings

<figure><img src="../.gitbook/assets/image (198).png" alt=""><figcaption></figcaption></figure>

1. Click the "Earth" button on the screen for automatic translation. Users can also manually edit the content.
2. After automatic translation is completed, click the "OK" button to save the content.

> Note: The workflow template options in the workflow menu should be based on the configuration of the actual installation environment. The options presented in the documentation are for reference only.

## Workflow Agent functional interface

Workflow Agent's homepage can be divided into several main areas, as follows:

<figure><img src="../.gitbook/assets/image (203).png" alt=""><figcaption></figcaption></figure>

1. **Agent function options:** Provides links to Agent function settings

The function options area contains the following function links. After clicking, the corresponding setting page will appear:

<table><thead><tr><th width="250">名稱</th><th>說明</th></tr></thead><tbody><tr><td>基礎設置</td><td>編輯 Agent 的主頁</td></tr><tr><td>流程設置</td><td>編輯 Agent 的工作流程</td></tr><tr><td>會話日誌</td><td>提供此 Agent 的對話紀錄</td></tr><tr><td>成員管理</td><td>管理此 Agent 的存取權限</td></tr><tr><td>AI WEBAPP</td><td>設定此 Agent 的網頁嵌入</td></tr><tr><td>API Key</td><td>提供第三方應用安全呼叫 API 的憑證</td></tr></tbody></table>

2. **Basic information**: Editable Agent name, description and activation status
3. **Application Settings:** Provides settings related to Agent behavior based on Agent type

<table><thead><tr><th width="250">名稱</th><th>說明</th></tr></thead><tbody><tr><td>歡迎頁面</td><td>設定Agent 問題設定</td></tr><tr><td>提示詞模板</td><td>加入現有提示詞模板供後續使用</td></tr><tr><td>檔案處理方式</td><td>控制上傳檔案的處理方式</td></tr></tbody></table>

4. **Adaptation Preview:** Allows users to test whether the Q&A results are as expected

## **Basic settings**

All types of Agent homepages share the Basic Settings section, which includes an Enabled Status switch and a Settings button for updating the Agent name and description. Clicking the Settings button will pop up the following dialog box:

<figure><img src="../.gitbook/assets/image (204).png" alt=""><figcaption></figcaption></figure>

1. **Agent Status**: Users can edit the activation status of Agent, and the status will change immediately when the switch is switched.
2. **Basic Settings Edit**: Can edit the most basic name, description and international language translation.

### Agent status settings

<figure><img src="../.gitbook/assets/image (205).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (206).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (207).png" alt=""><figcaption></figcaption></figure>

1. Click the status bar to open the interface
2. Click the Publish button
3. URL that can be copied in the workspace
4. After clicking the dialog button, the workspace dialog opens
5. Click the Unpublished button to unpublish

## **APP SETTINGS**

Provides settings related to Agent behavior based on Agent type. The application settings of _Workflow Agent_ will be described below.

### **Prompt word template**

The application template (prompt word template) that has been created or collected can be bound to the Agent. When using it, you only need to fill in the necessary information to speed up the question and answer process.

<figure><img src="../.gitbook/assets/image (208).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (210).png" alt=""><figcaption></figcaption></figure>

### **Welcome Page**

Users can set their own default conversation content, allowing the Agent to provide directly clickable question directions before the conversation begins, helping users start interacting more quickly.

<figure><img src="../.gitbook/assets/image (209).png" alt=""><figcaption></figcaption></figure>

## **Adaptation Preview**

Users can test Agent behavior and response content in this area, and adjust Agent configuration based on the responses.

<figure><img src="../.gitbook/assets/image (211).png" alt=""><figcaption></figcaption></figure>

## Workflow settings

"Workflow Settings" in the Agent function options is used to edit the Agent's workflow. Clicking it will open the editing screen of the workflow bound to this Agent.

> For screen description and operation of process editing, please see 

## **Session Log**

The conversation log provides all conversation records of this Agent. Administrators can filter the records by title, user, and conversation time interval.

The processing flow is also retained in the log record; when an error occurs in a conversation or performance is poor, managers can review the processing flow of each reply to discover the reason.

<figure><img src="../.gitbook/assets/image (212).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (213).png" alt=""><figcaption></figcaption></figure>

## Permissions

The creator can grant access rights to other users through "Permissions" (please refer to for role definition).

> Note: The creator is the default "owner", and each project can only have one owner.

<figure><img src="../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="99">項目</th><th width="132">操作名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>編輯表格</td><td>允許使用者編輯表格的呈現方式</td></tr><tr><td>2</td><td>刷新</td><td>點擊後刷新列表</td></tr><tr><td>3</td><td>內容篩選</td><td>進階篩選指定內容</td></tr><tr><td>4</td><td>狀態切換</td><td>在表格上單選或多選快速切換狀態</td></tr><tr><td>5</td><td>批次刪除</td><td>勾選項目後左上角的刪除按鈕便會顯示，可讓使用者刪除多個項目</td></tr><tr><td>6</td><td>搜尋欄位</td><td>搜尋 名稱</td></tr><tr><td>7</td><td>邀請</td><td>邀請組織 / 成員</td></tr><tr><td>8</td><td>啟用狀態</td><td>使用者權限啟用狀態</td></tr><tr><td>9</td><td>動作</td><td>轉移您的角色或刪除選定的使用者</td></tr></tbody></table>

### **New member**

<figure><img src="../.gitbook/assets/image (216).png" alt=""><figcaption></figcaption></figure>

&#x20;

<figure><img src="../.gitbook/assets/image (217).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (218).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (219).png" alt=""><figcaption></figcaption></figure>

1. Click "Invite" to open the conversation box
2. The input box can search for organizations or users
3. Select the corresponding permissions
4. Enter keywords to jump out to the corresponding organization/user
5. You can click the level button on the right to confirm the level of the character.
6. After selecting the target organization/user, you can click the label to open the view menu and view all users within the organization level and role.
7. Click the "Add" button to complete the invitation

## **Web App**

Agents can be embedded into web pages to provide question and answer services, as shown in the figure below:

<figure><img src="../.gitbook/assets/image (221).png" alt=""><figcaption></figcaption></figure>

If users want to embed Agent into a web page, they need to use this function to create code embedded in the front end of the web page.

### **New AI WEBAPP**

<figure><img src="../.gitbook/assets/image (222).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (223).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (224).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (225).png" alt=""><figcaption></figcaption></figure>

1. Enter the Web App in "Agent Function List"
2. Click "+" to open the _Create_ Web App dialog box
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multi-language label. Please refer to 
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to 
5. Click "Save" to complete
6. The new Web App will appear in the manifest. Use the Actions menu to Edit, Set Expiration, or Delete
7. Click the Web App name to access the information page and view Embed Code, settings _Application Language_, _Request and Tag Limits_, and more

> Note: Each Agent can have multiple API keys and matching embed code to independently manage expiration dates and usage limits for different Web App instances.

## API Key

API Key is an access key used to verify identity, allowing the system to identify the source of the request and apply corresponding permissions and usage quotas when calling the Agent API. Please keep your API Key safe to avoid leakage; if you suspect that the key has been leaked, it is recommended to immediately replace and update all integration settings that use the key.

<figure><img src="../.gitbook/assets/image (226).png" alt=""><figcaption></figcaption></figure>

### Add API Key

<figure><img src="../.gitbook/assets/image (227).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (228).png" alt=""><figcaption></figcaption></figure>

1. Enter the API Key in "Agent Function List"
2. Click "+" to open the _Create_ API Key dialog window
3. Enter the name of the API Key
4. Select whether to enable Rate Limit and set the value
5. Click the "Save" button

> Please note: Please copy your ID and API key immediately after saving to avoid losing them.

### Copy Endpoint

Endpoint is the service entry location (URL) of Agent API. The system will send API requests to this location to perform the corresponding function. Please choose the correct Endpoint (such as test environment or production environment) according to the usage scenario to avoid sending requests to the wrong environment or causing connection failure.

Endpoint's copy button is located next to the search box. Click the copy button to copy the URL. Please pay attention to the environment in which you copy the URL.

<figure><img src="../.gitbook/assets/image (229).png" alt=""><figcaption></figcaption></figure>
