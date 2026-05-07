---
description: 工作流程 Agent 讓使用者以建立流程的方式，設計 Agent 可如何透過 AI Studio 提供的功能元件完成使用者的複雜任務。
---

# Workflow Agent

## **Create Workflow Agent**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click the "+ Create" button in the upper right corner of the screen
2. Select "Agent Type" as _Workflow_ in the pop-up window
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multilingual label. Please refer to [Multiple Language Settings](gong-zuo-liu-cheng-agent.md#duo-guo-yu-yan-she-ding)
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to [Multiple Language Settings](gong-zuo-liu-cheng-agent.md#duo-guo-yu-yan-she-ding)
5. Click the "Workflow Template" menu to select a workflow template
6. Click the "Save" button to complete the addition, and the system will automatically enter the Agent editing screen for the user to complete the settings.

### Multi-language settings

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click the "Earth" button on the screen for automatic translation. Users can also manually edit the content.
2. After automatic translation is completed, click the "OK" button to save the content.

> Note: The workflow template options in the workflow menu should be based on the configuration of the actual installation environment. The options presented in the documentation are for reference only.

## Workflow Agent functional interface

Workflow Agent's homepage can be divided into several main areas, as follows:

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. **Agent function options:** Provides links to Agent function settings

The function options area contains the following function links. After clicking, the corresponding setting page will appear:

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Name⟬<table>4⟭⟬<table>5⟭Description⟬<table>6⟭⟬ <table>7⟭⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭Basic Settings⟬<table>12⟭⟬<table>13⟭Edit Agent's homepage⟬<table>14⟭⟬<table>15⟭⟬<table>16⟭⟬<table>17⟭Process Settings⟬<table>18⟭⟬<table>19⟭Edit Agent The workflow of ⟬<table>20⟭⟬<table>21⟭⟬<table>22⟭⟬<table>23⟭Session Log⟬<table>24⟭⟬<table>25⟭ provides this Agent Conversation record⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭Member Management⟬<table>30⟭⟬<table>31⟭Manage this Agent Access rights⟬<table>32⟭⟬<table>33⟭⟬<table>34⟭⟬<table>35⟭AI WEBAPP⟬<table>36⟭⟬<table>37⟭ Set this Agent Web page embedding ⟬<table>38⟭⟬<table>39⟭⟬<table>40⟭⟬<table>41⟭API Key⟬<table>42⟭⟬<table>43⟭ provides secure calling API for third-party applications Voucher for ⟬<table>44⟭⟬<table>45⟭⟬<table>46⟭⟬<table>47⟭

2. **Basic information**: Editable Agent name, description and activation status
3. **Application Settings:** Provides settings related to Agent behavior based on Agent type

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Name⟬<table>4⟭⟬<table>5⟭Description⟬<table>6⟭⟬<table>7⟭⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭Welcome page⟬<table>12⟭⟬<table>13⟭Setting Agent Question setting⟬<table>14⟭⟬<table>15⟭⟬<table>16⟭⟬<table>17⟭Prompt word template⟬<table>18⟭⟬<table>19⟭Add existing prompt word template for subsequent use⟬<table>20⟭⟬<table> 21⟭⟬<table>22⟭⟬<table>23⟭File processing method⟬<table>24⟭⟬<table>25⟭Control the processing method of uploaded files⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭

4. **Adaptation Preview:** Allows users to test whether the Q&A results are as expected

## **Basic settings**

All types of Agent homepages share the Basic Settings section, which includes an Enabled Status switch and a Settings button for updating the Agent name and description. Clicking the Settings button will pop up the following dialog box:

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. **Agent Status**: Users can edit the activation status of Agent, and the status will change immediately when the switch is switched.
2. **Basic Settings Edit**: Can edit the most basic name, description and international language translation.

### Agent status settings

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click the status bar to open the interface
2. Click the Publish button
3. URL that can be copied in the workspace
4. After clicking the dialog button, the workspace dialog opens
5. Click the Unpublished button to unpublish

## **APP SETTINGS**

Provides settings related to Agent behavior based on Agent type. The application settings of _Workflow Agent_ will be described below.

### **Prompt word template**

The application template (prompt word template) that has been created or collected can be bound to the Agent. When using it, you only need to fill in the necessary information to speed up the question and answer process.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

### **Welcome Page**

Users can set their own default conversation content, allowing the Agent to provide directly clickable question directions before the conversation begins, helping users start interacting more quickly.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

## **Adaptation Preview**

Users can test Agent behavior and response content in this area, and adjust Agent configuration based on the responses.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

## Workflow settings

"Workflow Settings" in the Agent function options is used to edit the Agent's workflow. Clicking it will open the editing screen of the workflow bound to this Agent.

> For screen descriptions and operations of process editing, please see [Edit Workflow](bian-ji-gong-zuo-liu-cheng.md)

## **Session Log**

The conversation log provides all conversation records of this Agent. Administrators can filter the records by title, user, and conversation time interval.

The processing flow is also retained in the log record; when an error occurs in a conversation or performance is poor, managers can review the processing flow of each reply to discover the reason.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

## Permissions

The creator can grant access rights to other users through "Permissions" (for role definition, please refer to [Permission Function Introduction] (../ru-men-zhi-nan/quan-xian-gong-neng-jie-shao.md)).

> Note: The creator is the default "owner", and each project can only have one owner.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Operation Name⟬<table>6⟭⟬<table>7⟭ says Ming⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Edit form⟬P H0016⟭⟬<table>17⟭Allows users to edit the presentation of tables⟬<table>18⟭⟬<table>19⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭⟬<table>23⟭Refresh⟬<table>24⟭⟬<table>25⟭Click to refresh the list⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭3⟬<table>30⟭⟬ <table>31⟭Content Filtering⟬<table>32⟭⟬<table>33⟭Advanced Filtering Specified Content⟬<table>34⟭⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭4⟬<table>38⟭⟬<table>39⟭Status switching⟬<table>40⟭⟬<table>41⟭Quickly switch status by single or multiple selections on the form⟬<table>42⟭⟬<table>43⟭⟬<table>44⟭⟬ <table>45⟭5⟬<table>46⟭⟬<table>47⟭Batch deletion⟬<table>48⟭⟬<table>49⟭After checking the items, the delete button in the upper left corner will be displayed, allowing the user to delete multiple items Item⟬<table>50⟭⟬<table>51⟭⟬<table>52⟭⟬<table>53⟭6⟬<table>54⟭⟬<table>55⟭Search field⟬<table>56⟭⟬<table>57⟭Search Name⟬<table>58⟭⟬<table>59⟭⟬<table>60⟭⟬<table>61⟭7⟬<table>62⟭⟬<table>63⟭Invite⟬<table>64⟭⟬<table>65⟭Invite Organization / Member⟬<table>66⟭⟬<table>67⟭⟬<table>68⟭⟬<table>69⟭8⟬<table>70⟭⟬<table> 71⟭Enabled status⟬<table>72⟭⟬<table>73⟭User permission enabled status⟬<table>74⟭⟬<table>75⟭⟬ <table>76⟭⟬<table>77⟭9⟬<table>78⟭⟬<table>79⟭Action⟬<table>80⟭⟬<table>8 1⟭Transfer your role or delete selected users⟬<table>82⟭⟬<table>83⟭⟬<table>84⟭⟬<table>85⟭

### **New member**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

&#x20;

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click "Invite" to open the conversation box
2. The input box can search for organizations or users
3. Select the corresponding permissions
4. Enter keywords to jump out to the corresponding organization/user
5. You can click the level button on the right to confirm the level of the character.
6. After selecting the target organization/user, you can click the label to open the view menu and view all users within the organization level and role.
7. Click the "Add" button to complete the invitation

## **Web App**

Agents can be embedded into web pages to provide question and answer services, as shown in the figure below:

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

If users want to embed Agent into a web page, they need to use this function to create code embedded in the front end of the web page.

### **New AI WEBAPP**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Enter the Web App in "Agent Function List"
2. Click "+" to open the _Create_ Web App dialog box
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multilingual label. Please refer to [Multiple Language Settings](gong-zuo-liu-cheng-agent.md#duo-guo-yu-yan-she-ding)
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to [Multiple Language Settings](gong-zuo-liu-cheng-agent.md#duo-guo-yu-yan-she-ding)
5. Click "Save" to complete
6. The new Web App will appear in the manifest. Use the Actions menu to Edit, Set Expiration, or Delete
7. Click the Web App name to access the information page and view Embed Code, settings _Application Language_, _Request and Tag Limits_, and more

> Note: Each Agent can have multiple API keys and matching embed code to independently manage expiration dates and usage limits for different Web App instances.

## API Key

API Key is an access key used to verify identity, allowing the system to identify the source of the request and apply corresponding permissions and usage quotas when calling the Agent API. Please keep your API Key safe to avoid leakage; if you suspect that the key has been leaked, it is recommended to immediately replace and update all integration settings that use the key.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

### Add API Key

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Enter the API Key in "Agent Function List"
2. Click "+" to open the _Create_ API Key dialog window
3. Enter the name of the API Key
4. Select whether to enable Rate Limit and set the value
5. Click the "Save" button

> Please note: Please copy your ID and API key immediately after saving to avoid losing them.

### Copy Endpoint

Endpoint is the service entry location (URL) of Agent API. The system will send API requests to this location to perform the corresponding function. Please choose the correct Endpoint (such as test environment or production environment) according to the usage scenario to avoid sending requests to the wrong environment or causing connection failure.

Endpoint's copy button is located next to the search box. Click the copy button to copy the URL. Please pay attention to the environment in which you copy the URL.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>
