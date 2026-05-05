---
description: 聊天 Agent 可讓使用者直接與大型語言模型互動，適用於腦力激盪、資訊摘要、產生格式化文字內容等任務，且無須擔憂敏感資料外洩。
---

# Chat Agent

## **Create Agent**

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (155).png" alt=""><figcaption></figcaption></figure>

1. Click the "+ Create" button in the upper right corner of the screen
2. Select "Agent Type" in the pop-up window
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multilingual label. Please refer to [Multiple Language Settings](liao-tian-agent.md#duo-guo-yu-yan-she-ding)
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to [Multiple Language Settings](liao-tian-agent.md#duo-guo-yu-yan-she-ding)
5. Click the "Label" menu to select the label to be brought into this Agent
6. Click the "Model" menu to select the large language model used by this Agent
7. Click the "Save" button to complete the addition, and the system will automatically enter the Agent editing screen for the user to complete the settings.





### Multi-language setting <a href="#duo-guo-yu-yan-she-ding" id="duo-guo-yu-yan-she-ding"></a>

<figure><img src="../.gitbook/assets/image (157).png" alt=""><figcaption></figcaption></figure>

1. Click the "Earth" button on the screen for automatic translation. Users can also manually edit the content.
2. After automatic translation is completed, click the "OK" button to save the content.

> Note: The large language model options in the "Model" menu should be based on the configuration of the actual installation environment. The options presented in the documentation are for reference only.

## Chat Agent functional interface

<figure><img src="../.gitbook/assets/image (158).png" alt=""><figcaption></figcaption></figure>

The chat agent homepage is mainly divided into several parts, as shown below:

1. **Agent Function Options**: The function options area contains the following links, each link will open the corresponding setting page

| name | illustrate |
| --------- | ------------------- |
| Basic settings | Edit the Agent's home page |
| session log | Provide conversation history for this Agent |
| Member management | Manage access to this Agent |
| AI WEBAPP | Configure web embedding for this Agent |
| API Key | Provide credentials for third-party applications to securely call the API |

2. **Basic information**: You can view the Agent name, creation and editing time and personnel, and activation status
3. **Application Settings:** Provides settings related to Agent behavior based on Agent type

| name | illustrate |
| ---------- | --------------------------- |
| Inference parameters | Control how responses are generated |
| Knowledge base configuration | Select parameters and available knowledge sources |
| tool | Enable and configure available tools |
| Skill | Functions used to expand Agent capabilities |
| Agent collaboration | Allows Agents to connect in series and collaborate with other Agents to perform tasks |
| Agent welcome page | Set initial conversation content |
| prompt word template | Provides reusable prompt word templates for quick use |
| File handling | Control how uploaded files are processed |
| guardrail | Control content output |

4. **Adaptation Preview:** Allows users to test whether the Q&A results are as expected

## **Basic settings**

<figure><img src="../.gitbook/assets/image (159).png" alt=""><figcaption></figcaption></figure>

All types of Agent homepages share the **Basic Settings** section, which includes an **Enabled Status** switch and a **Settings** button for updating the Agent name and description. Clicking the Settings button will pop up the following dialog box:

1. **Agent Status**: Users can edit the activation status of Agent, and the status will change immediately when the switch is switched.
2. **Basic Settings Edit**: Can edit the most basic name, description and international language translation.

### Agent status settings

<figure><img src="../.gitbook/assets/image (160).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (161).png" alt=""><figcaption></figcaption></figure>

1. Click the status bar to open the interface
2. Click the Publish button
3. URL that can be copied in the workspace
4. After clicking the dialog button, the workspace dialog opens
5. Click the Unpublished button to unpublish

## **APP SETTINGS**

### **Inference Parameters**

The settings include two tabs: "**Parameters**" and "**System Prompt Words**".

#### **parameter**

Users can control the Agent's reply behavior by adjusting the items in the "**Parameters**" tab.

<figure><img src="../.gitbook/assets/image (163).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="98">Project</th><th width="112">Parameters</th><th width="238">Description</th><th>Scope and Value</th></tr></thead><tbody><tr><td>1</td><td>Model</td><td>Agent The default model selected when creating; can be changed here</td><td>n/a</td></tr>⟬PH0 024⟭<td>2</td><td>Temperature</td><td>Control the creativity of the reply. The higher the value, the more diverse and creative the responses; the lower the value, the more precise and consistent the responses</td><td>0–1</td></tr><tr><td>3</td><td>Top P</td><td> controls randomness and diversity. Lower values produce more conservative and predictable text; higher values produce more diverse results</td><td>0–1</td></tr><tr>⟬PH00 45⟭4</td><td>Maximum mark</td><td>Limit maximum output length</td><td>Set as required</td>⟬P H0053⟭<tr><td>5</td><td>Conversation Memory</td><td> Stores Q&A history to enhance coherence (may slow down responses Time) </td><td><code>0</code> represents a stateless response; <code>5-10</code> strikes a balance between consistency and performance. The more memories you have, the slower it becomes. </td></tr></tbody></table>

#### instruction

Users can use the "Commands" tab to define prompts to control the Agent's language, role, tone, etc.

<figure><img src="../.gitbook/assets/image (164).png" alt=""><figcaption></figcaption></figure>



* **Use template to add new prompt words**

Users can quickly add required application templates from templates.

<figure><img src="../.gitbook/assets/image (165).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (166).png" alt=""><figcaption></figcaption></figure>

1. Add directly from the blank space; or when prompted, use the mouse to select the location to be added.
2. Click the "Template" button to open the template list and select the type of template you want to add.
3. Generate corresponding templates. New templates will be generated by inverse selection. You can edit the templates according to your own needs.
4. Click the "Save" button to complete editing.



* **Input requirements to generate prompt words**

The prompt word generation function supports "rewriting existing content" or "generating from blank". The red box above can be filled in as the basis for rewriting, and the green input box below can fill in the generation guidelines to produce results.

<figure><img src="../.gitbook/assets/image (167).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

1. Select the dialog box below and enter your requirements for prompt words.
2. Press the Enter key on the keyboard or the generate button on the right and wait for AI to automatically generate the template.
3. It is automatically generated and can be edited according to your own needs.
4. Click the "Save" button to complete editing.

### knowledge base

#### Knowledge base sources

<figure><img src="../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>

#### Knowledge base parameters

<figure><img src="../.gitbook/assets/image (169).png" alt=""><figcaption></figcaption></figure>

### **tool**

Users can enable/disable tools accessible to Agent in settings.

<figure><img src="../.gitbook/assets/image (170).png" alt=""><figcaption></figcaption></figure>



#### **Session Memory**

<table><thead><tr><th width="250">Tools</th><th> says Ming</th></tr></thead><tbody><tr><td>KV Session short-term memory</td><td> enables precise, key-based storage and retrieval of temporary data during a session. Useful for tracking dynamic variables such as <code>Username</code>, <code>Selected Plan</code>. </td></tr><tr><td>graphiti - Added memory data </td><td>Storing episodic information (such as interactions or events) into the knowledge graph. </td></tr><tr><td>graphiti - Query memory node </td><td>Retrieve an entity summary or node-level memory representation. </td></tr><tr><td>graphiti - Query Memory Facts </td><td>Search for relevant facts and structured relationships in the memory graph. </td></tr><tr><td>graphiti - Delete Entity Relationship </td><td>Removes the defined relationship between entities from the graph. </td></tr><tr><td>graphiti - Delete event segment </td><td>Delete a specific event segment in the memory graph. </td></tr><tr><td>graphiti - Get Entity Relationships </td><td> Retrieve structured relationships related to a specific entity. </td></tr><tr><td>graphiti - Get a fragment of an event </td><td> Returns a recent memory episode to provide context for a conversation or decision-making. </td></tr><tr><td>graphiti - Clear Memory Graph </td><td>Resets the entire graph-based memory system. </td></tr></tbody></table>

> PS: For more information about Graphiti, please see its official website.

#### **Academic Articles**

<table><thead><tr><th width="250">Tools</th><th>Instructions South</th></tr></thead><tbody><tr><td>arXiv Paper Search </td><td> allows users to search for academic papers from the arXiv database. </td></tr><tr><td>Google Scholar Search</td><td>Search for scholarly articles and citations using Google Scholar. </td></tr></tbody></table>

#### **Web Search**

<table><thead><tr><th width="250">Tools</th><th>Usage Guide </th></tr></thead><tbody><tr><td>Serper - Web Content Extraction </td><td> Extracts readable content from web URLs. </td></tr><tr><td>Serper - Google Search </td><td>Performs a Google search and returns summary results. </td></tr><tr><td>Serper - Patent Search </td><td>Search for issued patents and related documents. </td></tr><tr><td>Serper - Image Search </td><td>Search for images based on text queries. </td></tr><tr><td>Serper - Paper Search </td><td> Search academic papers using Google Scholar-style sources. </td></tr><tr><td>Serper - News Search </td><td> Search for news based on text queries. </td></tr><tr><td>Serper - Map Information Search </td><td> Search maps based on text queries. </td></tr></tbody></table>

> Note: For more information about Sperper, please see its official website.

#### **Code**

<table><thead><tr><th width="250">Tools</th><th>Use Guide </th></tr></thead><tbody><tr><td>Execution Python code </td><td> executes Python scripts or logic to support tasks such as mathematics, data parsing, or automation. </td></tr></tbody></table>

#### **Document Handling**

<table><thead><tr><th width="250">Tools</th><th>Usage Guide</th></tr></thead><tbody><tr><td>Preview file </td><td>Displays the uploaded file in a readable format within the platform. </td></tr><tr><td>File to markdown</td><td>Convert the file to Markdown format. </td></tr></tbody></table>

#### **Other**

<table><thead><tr><th width="250">Tools</th><th>Usage Guide</th></tr></thead><tbody><tr><td>Get the current time </td><td>Returns the current system time when the request is made. </td></tr><tr><td>Easy Math </td><td>Perform simple arithmetic operations in the prompt. </td></tr><tr><td>Dynamic Thinking Chain (Sequential Thinking) </td><td>Decompose complex problems into step-by-step thinking, with the option to modify or branch. Good for planning, troubleshooting, and structured reasoning. </td></tr></tbody></table>

### Skill

<figure><img src="../.gitbook/assets/image (180).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (179).png" alt=""><figcaption></figcaption></figure>

By setting different skills, Agent can support more functions and task processing scenarios, such as data access, tool operation, process execution or specific task expansion. Users can configure corresponding skills according to their needs to improve the Agent's application flexibility and task processing capabilities.

### Agent collaboration

Through this function, users can establish cooperative relationships between multiple Agents and handle task content according to different divisions of responsibilities, thereby improving process flexibility and overall task processing efficiency.

<figure><img src="../.gitbook/assets/image (182).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (181).png" alt=""><figcaption></figcaption></figure>

### **Welcome Page**

Users can set their own default conversation content, allowing the Agent to provide directly clickable question directions before the conversation begins, helping users start interacting more quickly.

<figure><img src="../.gitbook/assets/image (178).png" alt=""><figcaption></figcaption></figure>

### **Prompt word template**

Users can link existing or favorited application templates (prompt word templates) to the Agent to speed up Q&A by filling in required fields.

<figure><img src="../.gitbook/assets/image (177).png" alt=""><figcaption></figcaption></figure>

### **File Processing**

**File Handling** settings allow the user to define how the Agent handles files uploaded in the workspace. This feature is particularly useful when the Agent needs to interpret, convert, or extract content from files such as PDFs, DOCX, or images.

<figure><img src="../.gitbook/assets/image (176).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="161">Option </th><th width="103"> Visible to MCP tools </th><th width="96"> to LLM Visible</th><th> Description</th><th>Example usage scenario</th></tr></thead><tbody><tr><td>Do not The process </td> <td> Will not be opened or interpreted. </td><td>– –</td></tr><tr><td>Process with Tool</td><td>O</td><td>X</td><td> files are passed to the MCP tool for processing, but not to LLM. </td><td> Useful when you want to extract material from a CSV or PDF, but don’t need AI-generated comments. </td></tr><tr><td>File to Image Conversion </td> <td> </td><td> is suitable for scanned documents or visual layouts where diagrammatic relationships are important. </td></tr><tr><td>Convert to Image &#x26; Tool</td><td>O</td><td>O</td><td> files are simultaneously translated into LLM references and processed by the MCP tool. </td><td> Best suited for invoices or forms that require interpretation of both visual layout and structured data. </td></tr></tbody></table>

### guardrail

Guardrails are a function used to control content output. They can check and restrict content during the process, helping to reduce risks related to personal data leakage, information security and legal compliance, and making the output content more consistent with usage specifications and management requirements.

<figure><img src="../.gitbook/assets/image (183).png" alt=""><figcaption></figcaption></figure>

## **Adaptation Preview**

Use this block to test Agent responses and adjust settings accordingly.

> Please note: Files uploaded or generated during the adaptation preview are only retained for 30 minutes.

<figure><img src="../.gitbook/assets/image (184).png" alt=""><figcaption></figcaption></figure>

### **Adjust Preview** How to upload files

* You can click the plus sign (+) in the dialog box to upload files.

<figure><img src="../.gitbook/assets/image (185).png" alt=""><figcaption></figcaption></figure>

* Also supports drag-and-drop file uploading method

<figure><img src="../.gitbook/assets/image (186).png" alt=""><figcaption></figcaption></figure>

## memory

The memory function can help users create reusable memory content for the Agent, so that the Agent can refer to preset background information, usage scenarios and processing procedures when performing tasks or responding to questions.

Users can view the created memory list on the Agent's memory page, and quickly identify the purpose of each memory through its activation status, name, description and usage context. Memory can be used to save specific task processes, judgment rules, preconditions, operating steps or precautions to help the Agent maintain consistent processing logic in subsequent interactions.

<figure><img src="../.gitbook/assets/image (187).png" alt=""><figcaption></figcaption></figure>

### build memory

<figure><img src="../.gitbook/assets/image (190).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (191).png" alt=""><figcaption></figcaption></figure>

1. Enter the Agent page. Click "Memory" in the submenu on the left.
2. Click the "Create" button in the upper right corner.
3. Fill in the basic information of memory:
 * Name: Enter the memory name.
 * Description: Enter memory description.
 * Applicable situations: Enter the usage situations where this memory is applicable.
 * Content: Enter detailed content, which can be formatted in Markdown format.
4. After confirming that the content is correct, click "Create" to complete the creation.

### View memory details

<figure><img src="../.gitbook/assets/image (189).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (188).png" alt=""><figcaption></figcaption></figure>

1. Enter the memory list.
2. Click the memory name you want to view.
3. The system will open the details panel on the right.
4. Users can view the name, activation status, description, usage context and complete content of the memory. If the content is long, you can scroll up and down in the right panel to view it.

### Enable and disable memory

#### Memory enablement rules

The memory function includes the overall function switch and the single-stroke memory activation status.

<figure><img src="../.gitbook/assets/image (192).png" alt=""><figcaption></figcaption></figure>

If the switch is on, it means that this Agent can use the memory function. Users can still enable or disable different memories individually in the memory list.

If the switch is off, it means that this Agent does not use the memory function. Even if there are already created memories in the memory list, the Agent will not apply these memory contents.

#### Activating and deactivating single memory

<figure><img src="../.gitbook/assets/image (193).png" alt=""><figcaption></figcaption></figure>

In the memory list, the "Enabled" field is used to display whether a single memory is enabled. When the memory master switch is turned on, the activated single memory will be used as reference content when the Agent responds or handles tasks.

Users can disable temporarily unused memories as needed, retaining the content but not allowing the Agent to apply it; they can re-enable it if they need to use it again in the future.

## **Session Log**

Conversation records store all conversation records of this Agent. Administrators can filter records by title, user or date range. Records include processing procedures. When errors occur or responses are slow, administrators can review processing details to diagnose the problem.

<figure><img src="../.gitbook/assets/image (194).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (195).png" alt=""><figcaption></figcaption></figure>

## Permissions

The creator can grant access rights to other users through "Permissions" (please refer to role definition).

> Note: The creator is the default "manager", and each project can only have one owner.

<figure><img src="../.gitbook/assets/image (196).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">Project</th><th width="146">Operation Name</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Edit table</td><td>Allows the user to edit the presentation of the table</td>⟬PH0 019⟭<tr><td>2</td><td>Refresh</td><td>Click to refresh the list </td></tr><tr><td>3</td><td>Content filtering</td> <td>Advanced filtering of specified content</td></tr><tr><td>4</td>⟬PH00 39⟭Batch deletion</td><td>After checking the items, the delete button in the upper left corner will be displayed, allowing the user to delete multiple items</td></tr><tr><td>5</td><td>Search field</td><td>Search Name</td></tr><tr><td>6</td><td>Invite</td><td>Invite Organization / Member</td></tr><tr><td>7</td><td>Action⟬PH00 64⟭<td>Transfer your role or remove selected users</td></tr></tbody></table>

### **New member**

<figure><img src="../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (82).png" alt=""><figcaption></figcaption></figure>

1. Click "Add" to open the conversation box
2. The input box can search for organizations or users
3. Select the corresponding permissions
4. Enter keywords to jump out to the corresponding organization/user
5. You can click the level button on the right to confirm the level of the character.
6. After selecting the target organization/user, you can click the label to open the view menu and view all users within the organization level and role.
7. Click the "Add" button to complete the invitation

## **Web App**

Agents can be embedded into web pages to provide question and answer services, as shown below:

<figure><img src="../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

To embed an Agent into a website, use this feature to generate front-end embed code.

### **New Web App**

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

1. Enter the Web App in "Agent Function List"
2. Click "+" to open the _Create_ Web App dialog window
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multilingual label. Please refer to&#x20;
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to&#x20;
5. Click "Save" to complete
6. The new Web App will appear in the manifest. Use the Actions menu to Edit, Set Expiration, or Delete
7. Click the Web App name to access the information page and view Embed Code, settings _Application Language_, _Request and Tag Limits_, and more

> Note: Each Agent can have multiple API keys and matching embed code to independently manage expiration dates and usage limits for different Web App instances.

## API Key

API Key is an access key used to verify identity, allowing the system to identify the source of the request and apply corresponding permissions and usage quotas when calling the Agent API. Please keep your API Key safe to avoid leakage; if you suspect that the key has been leaked, it is recommended to immediately replace and update all integration settings that use the key.

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

### Add API Key

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

1. Enter the API Key in "Agent Function List"
2. Click "+" to open the _Create_ API Key dialog window
3. Enter the name of the API Key
4. Select whether to enable Rate Limit and set the value
5. If necessary, you can set the API Key expiration date
6. Click the "Save" button

> Please note: Please copy your ID and API key immediately after saving to avoid losing them.

### Copy Endpoint

Endpoint is the service entry location (URL) of Agent API. The system will send API requests to this location to perform the corresponding function. Please choose the correct Endpoint (such as test environment or production environment) according to the usage scenario to avoid sending requests to the wrong environment or causing connection failure.

Endpoint's copy button is located next to the search box. Click the copy button to copy the URL. Please pay attention to the environment in which you copy the URL.

<figure><img src="../.gitbook/assets/image (91).png" alt=""><figcaption></figcaption></figure>
