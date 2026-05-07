---
description: 聊天 Agent 可讓使用者直接與大型語言模型互動，適用於腦力激盪、資訊摘要、產生格式化文字內容等任務，且無須擔憂敏感資料外洩。
---

# Chat Agent

## **Create Agent**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click the "+ Create" button in the upper right corner of the screen
2. Select "Agent Type" in the pop-up window
3. Enter the knowledge name in the "Name" field and click the button on the right to create a multilingual label. Please refer to [Multiple Language Settings](liao-tian-agent.md#duo-guo-yu-yan-she-ding)
4. Enter the knowledge description in the "Description" field and click the button on the right to create a multilingual label. Please refer to [Multiple Language Settings](liao-tian-agent.md#duo-guo-yu-yan-she-ding)
5. Click the "Label" menu to select the label to be brought into this Agent
6. Click the "Model" menu to select the large language model used by this Agent
7. Click the "Save" button to complete the addition, and the system will automatically enter the Agent editing screen for the user to complete the settings.





### Multi-language setting <a href="#duo-guo-yu-yan-she-ding" id="duo-guo-yu-yan-she-ding">⟬<a href="#duo-guo-yu-yan-she-ding" id="duo-guo-yu-yan-she-ding">1⟭

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click the "Earth" button on the screen for automatic translation. Users can also manually edit the content.
2. After automatic translation is completed, click the "OK" button to save the content.

> Note: The large language model options in the "Model" menu should be based on the configuration of the actual installation environment. The options presented in the documentation are for reference only.

## Chat Agent functional interface

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

The chat agent homepage is mainly divided into several parts, as shown below:

1. **Agent Function Options**: The function options area contains the following links, each link will open the corresponding setting page | name | illustrate | | --------- | ------------------- | | Basic settings | Edit the Agent's home page | | session log | Provide conversation history for this Agent | | Member management | Manage access to this Agent | | AI WEBAPP | Configure web embedding for this Agent | | API Key | Provide credentials for third-party applications to securely call the API | 2. **Basic information**: You can view the Agent name, creation and editing time and personnel, and activation status
3. **Application Settings:** Provides settings related to Agent behavior based on Agent type | name | illustrate | | ---------- | --------------------------- | | Inference parameters | Control how responses are generated | | Knowledge base configuration | Select parameters and available knowledge sources | | tool | Enable and configure available tools | | Skill | Functions used to expand Agent capabilities | | Agent collaboration | Allows Agents to connect in series and collaborate with other Agents to perform tasks | | Agent welcome page | Set initial conversation content | | prompt word template | Provides reusable prompt word templates for quick use | | File handling | Control how uploaded files are processed | | guardrail | Control content output | 4. **Adaptation Preview:** Allows users to test whether the Q&A results are as expected

## **Basic settings**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

All types of Agent homepages share the **Basic Settings** section, which includes an **Enabled Status** switch and a **Settings** button for updating the Agent name and description. Clicking the Settings button will pop up the following dialog box:

1. **Agent Status**: Users can edit the activation status of Agent, and the status will change immediately when the switch is switched.
2. **Basic Settings Edit**: Can edit the most basic name, description and international language translation.

### Agent status settings

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Parameters⟬<table>6⟭⟬<table>7⟭Description⟬<table>8⟭⟬<table>9⟭Scope and Value⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭⟬<table>14⟭⟬<table>15⟭1⟬<table>16⟭⟬<table>17⟭Model⟬<table>18⟭⟬<table>19⟭Agent The default model selected when creating; can be changed here⟬<table>20⟭⟬<table>21⟭n/a⟬<table>22⟭⟬<table>23⟭⟬<table>24⟭⟬<table>25⟭2⟬<table>26⟭⟬<table>27⟭Temperature⟬<table>28⟭⟬<table>29⟭Control the creativity of the reply. The higher the value, the more diverse and creative the responses; the lower the value, the more precise and consistent the responses⟬<table>30⟭⟬<table>31⟭0–1⟬<table>32⟭⟬<table>33⟭⟬<table>34⟭⟬<table>35⟭3⟬<table>36⟭⟬<table>37⟭Top P⟬<table>38⟭⟬<table>39⟭ controls randomness and diversity. Lower values produce more conservative and predictable text; higher values produce more diverse results⟬<table>40⟭⟬<table>41⟭0–1⟬<table>42⟭⟬<table>43⟭⟬<table>44⟭⟬<table> 45⟭4⟬<table>46⟭⟬<table>47⟭Maximum mark⟬<table>48⟭⟬<table>49⟭Limit maximum output length⟬<table>50⟭⟬<table>51⟭Set as required⟬<table>52⟭⟬P H0053⟭⟬<table>54⟭⟬<table>55⟭5⟬<table>56⟭⟬<table>57⟭Conversation Memory⟬<table>58⟭⟬<table>59⟭ Stores Q&A history to enhance coherence (may slow down responses Time) ⟬<table>60⟭⟬<table>61⟭⟬<table>62⟭0⟬<table>63⟭ represents a stateless response; ⟬<table>64⟭5-10⟬<table>65⟭ strikes a balance between consistency and performance. The more memories you have, the slower it becomes. ⟬<table>66⟭⟬<table>67⟭⟬<table>68⟭⟬<table>69⟭

#### instruction

Users can use the "Commands" tab to define prompts to control the Agent's language, role, tone, etc.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>



* **Use template to add new prompt words**

Users can quickly add required application templates from templates.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Add directly from the blank space; or when prompted, use the mouse to select the location to be added.
2. Click the "Template" button to open the template list and select the type of template you want to add.
3. Generate corresponding templates. New templates will be generated by inverse selection. You can edit the templates according to your own needs.
4. Click the "Save" button to complete editing.



* **Input requirements to generate prompt words**

The prompt word generation function supports "rewriting existing content" or "generating from blank". The red box above can be filled in as the basis for rewriting, and the green input box below can fill in the generation guidelines to produce results.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Select the dialog box below and enter your requirements for prompt words.
2. Press the Enter key on the keyboard or the generate button on the right and wait for AI to automatically generate the template.
3. It is automatically generated and can be edited according to your own needs.
4. Click the "Save" button to complete editing.

### knowledge base

#### Knowledge base sources

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

#### Knowledge base parameters

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

### **tool**

Users can enable/disable tools accessible to Agent in settings.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>



#### **Session Memory**

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Tools⟬<table>4⟭⟬<table>5⟭ says Ming⟬<table>6⟭⟬<table>7⟭⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭KV Session short-term memory⟬<table>12⟭⟬<table>13⟭ enables precise, key-based storage and retrieval of temporary data during a session. Useful for tracking dynamic variables such as ⟬<table>14⟭Username⟬<table>15⟭, ⟬<table>16⟭Selected Plan⟬<table>17⟭. ⟬<table>18⟭⟬<table>19⟭⟬<table>20⟭⟬<table>21⟭graphiti - Added memory data ⟬<table>22⟭⟬<table>23⟭Storing episodic information (such as interactions or events) into the knowledge graph. ⟬<table>24⟭⟬<table>25⟭⟬<table>26⟭⟬<table>27⟭graphiti - Query memory node ⟬<table>28⟭⟬<table>29⟭Retrieve an entity summary or node-level memory representation. ⟬<table>30⟭⟬<table>31⟭⟬<table>32⟭⟬<table>33⟭graphiti - Query Memory Facts ⟬<table>34⟭⟬<table>35⟭Search for relevant facts and structured relationships in the memory graph. ⟬<table>36⟭⟬<table>37⟭⟬<table>38⟭⟬<table>39⟭graphiti - Delete Entity Relationship ⟬<table>40⟭⟬<table>41⟭Removes the defined relationship between entities from the graph. ⟬<table>42⟭⟬<table>43⟭⟬<table>44⟭⟬<table>45⟭graphiti - Delete event segment ⟬<table>46⟭⟬<table>47⟭Delete a specific event segment in the memory graph. ⟬<table>48⟭⟬<table>49⟭⟬<table>50⟭⟬<table>51⟭graphiti - Get Entity Relationships ⟬<table>52⟭⟬<table>53⟭ Retrieve structured relationships related to a specific entity. ⟬<table>54⟭⟬<table>55⟭⟬<table>56⟭⟬<table>57⟭graphiti - Get a fragment of an event ⟬<table>58⟭⟬<table>59⟭ Returns a recent memory episode to provide context for a conversation or decision-making. ⟬<table>60⟭⟬<table>61⟭⟬<table>62⟭⟬<table>63⟭graphiti - Clear Memory Graph ⟬<table>64⟭⟬<table>65⟭Resets the entire graph-based memory system. ⟬<table>66⟭⟬<table>67⟭⟬<table>68⟭⟬<table>69⟭

> PS: For more information about Graphiti, please see its official website.

#### **Academic Articles**

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Tools⟬<table>4⟭⟬<table>5⟭Instructions South⟬<table>6⟭⟬<table>7⟭⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭arXiv Paper Search ⟬<table>12⟭⟬<table>13⟭ allows users to search for academic papers from the arXiv database. ⟬<table>14⟭⟬<table>15⟭⟬<table>16⟭⟬<table>17⟭Google Scholar Search⟬<table>18⟭⟬<table>19⟭Search for scholarly articles and citations using Google Scholar. ⟬<table>20⟭⟬<table>21⟭⟬<table>22⟭⟬<table>23⟭

#### **Web Search**

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Tools⟬<table>4⟭⟬<table>5⟭Usage Guide ⟬<table>6⟭⟬<table>7⟭⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭Serper - Web Content Extraction ⟬<table>12⟭⟬<table>13⟭ Extracts readable content from web URLs. ⟬<table>14⟭⟬<table>15⟭⟬<table>16⟭⟬<table>17⟭Serper - Google Search ⟬<table>18⟭⟬<table>19⟭Performs a Google search and returns summary results. ⟬<table>20⟭⟬<table>21⟭⟬<table>22⟭⟬<table>23⟭Serper - Patent Search ⟬<table>24⟭⟬<table>25⟭Search for issued patents and related documents. ⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭Serper - Image Search ⟬<table>30⟭⟬<table>31⟭Search for images based on text queries. ⟬<table>32⟭⟬<table>33⟭⟬<table>34⟭⟬<table>35⟭Serper - Paper Search ⟬<table>36⟭⟬<table>37⟭ Search academic papers using Google Scholar-style sources. ⟬<table>38⟭⟬<table>39⟭⟬<table>40⟭⟬<table>41⟭Serper - News Search ⟬<table>42⟭⟬<table>43⟭ Search for news based on text queries. ⟬<table>44⟭⟬<table>45⟭⟬<table>46⟭⟬<table>47⟭Serper - Map Information Search ⟬<table>48⟭⟬<table>49⟭ Search maps based on text queries. ⟬<table>50⟭⟬<table>51⟭⟬<table>52⟭⟬<table>53⟭

> Note: For more information about Sperper, please see its official website.

#### **Code**

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Tools⟬<table>4⟭⟬<table>5⟭Use Guide ⟬<table>6⟭⟬<table>7⟭⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭Execution Python code ⟬<table>12⟭⟬<table>13⟭ executes Python scripts or logic to support tasks such as mathematics, data parsing, or automation. ⟬<table>14⟭⟬<table>15⟭⟬<table>16⟭⟬<table>17⟭

#### **Document Handling**

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Tools⟬<table>4⟭⟬<table>5⟭Usage Guide⟬<table>6⟭⟬<table>7 ⟭⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭Preview file ⟬<table>12⟭⟬<table>13⟭Displays the uploaded file in a readable format within the platform. ⟬<table>14⟭⟬<table>15⟭⟬<table>16⟭⟬<table>17⟭File to markdown⟬<table>18⟭⟬<table>19⟭Convert the file to Markdown format. ⟬<table>20⟭⟬<table>21⟭⟬<table>22⟭⟬<table>23⟭

#### **Other**

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Tools⟬<table>4⟭⟬<table>5⟭Usage Guide⟬<table>6⟭⟬<table>7 ⟭⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭Get the current time ⟬<table>12⟭⟬<table>13⟭Returns the current system time when the request is made. ⟬<table>14⟭⟬<table>15⟭⟬<table>16⟭⟬<table>17⟭Easy Math ⟬<table>18⟭⟬<table>19⟭Perform simple arithmetic operations in the prompt. ⟬<table>20⟭⟬<table>21⟭⟬<table>22⟭⟬<table>23⟭Dynamic Thinking Chain (Sequential Thinking) ⟬<table>24⟭⟬<table>25⟭Decompose complex problems into step-by-step thinking, with the option to modify or branch. Good for planning, troubleshooting, and structured reasoning. ⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭

### Skill

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

By setting different skills, Agent can support more functions and task processing scenarios, such as data access, tool operation, process execution or specific task expansion. Users can configure corresponding skills according to their needs to improve the Agent's application flexibility and task processing capabilities.

### Agent collaboration

Through this function, users can establish cooperative relationships between multiple Agents and handle task content according to different divisions of responsibilities, thereby improving process flexibility and overall task processing efficiency.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

### **Welcome Page**

Users can set their own default conversation content, allowing the Agent to provide directly clickable question directions before the conversation begins, helping users start interacting more quickly.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

### **Prompt word template**

Users can link existing or favorited application templates (prompt word templates) to the Agent to speed up Q&A by filling in required fields.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

### **File Processing**

**File Handling** settings allow the user to define how the Agent handles files uploaded in the workspace. This feature is particularly useful when the Agent needs to interpret, convert, or extract content from files such as PDFs, DOCX, or images.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Option ⟬<table>4⟭⟬<table>5⟭ Visible to MCP tools ⟬<table>6⟭⟬<table>7⟭ to LLM Visible⟬<table>8⟭⟬<table>9⟭ Description⟬<table>10⟭⟬<table>11⟭Example usage scenario⟬<table>12⟭⟬<table>13⟭⟬<table>14⟭⟬<table>15⟭⟬<table>16⟭⟬<table>17⟭Do not The process ⟬<table>18 ⟭ ⟬ <table>19 ⟭ Will not be opened or interpreted. ⟬<table>24⟭⟬<table>25⟭– –⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭Process with Tool⟬<table>30⟭⟬<table>31⟭O⟬<table>32⟭⟬<table>33⟭X⟬<table>34⟭⟬<table>35⟭ files are passed to the MCP tool for processing, but not to LLM. ⟬<table>36⟭⟬<table>37⟭ Useful when you want to extract material from a CSV or PDF, but don’t need AI-generated comments. ⟬<table>38⟭⟬<table>39⟭⟬<table>40⟭⟬<table>41⟭File to Image Conversion ⟬<table>42 ⟭ ⟬ <table>43 ⟭ ⟬<table>48⟭⟬<table>49⟭ is suitable for scanned documents or visual layouts where diagrammatic relationships are important. ⟬<table>50⟭⟬<table>51⟭⟬<table>52⟭⟬<table>53⟭Convert to Image &#x26; Tool⟬<table>54⟭⟬<table>55⟭O⟬<table>56⟭⟬<table>57⟭O⟬<table>58⟭⟬<table>59⟭ files are simultaneously translated into LLM references and processed by the MCP tool. ⟬<table>60⟭⟬<table>61⟭ Best suited for invoices or forms that require interpretation of both visual layout and structured data. ⟬<table>62⟭⟬<table>63⟭⟬<table>64⟭⟬<table>65⟭

### guardrail

Guardrails are a function used to control content output. They can check and restrict content during the process, helping to reduce risks related to personal data leakage, information security and legal compliance, and making the output content more consistent with usage specifications and management requirements.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

## **Adaptation Preview**

Use this block to test Agent responses and adjust settings accordingly.

> Please note: Files uploaded or generated during the adaptation preview are only retained for 30 minutes.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

### **Adjust Preview** How to upload files

* You can click the plus sign (+) in the dialog box to upload files.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

* Also supports drag-and-drop file uploading method

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

## memory

The memory function can help users create reusable memory content for the Agent, so that the Agent can refer to preset background information, usage scenarios and processing procedures when performing tasks or responding to questions.

Users can view the created memory list on the Agent's memory page, and quickly identify the purpose of each memory through its activation status, name, description and usage context. Memory can be used to save specific task processes, judgment rules, preconditions, operating steps or precautions to help the Agent maintain consistent processing logic in subsequent interactions.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

### build memory

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Enter the Agent page. Click "Memory" in the submenu on the left.
2. Click the "Create" button in the upper right corner.
3. Fill in the basic information of memory:
 * Name: Enter the memory name.
 * Description: Enter memory description.
 * Applicable situations: Enter the usage situations where this memory is applicable.
 * Content: Enter detailed content, which can be formatted in Markdown format.
4. After confirming that the content is correct, click "Create" to complete the creation.

### View memory details

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Enter the memory list.
2. Click the memory name you want to view.
3. The system will open the details panel on the right.
4. Users can view the name, activation status, description, usage context and complete content of the memory. If the content is long, you can scroll up and down in the right panel to view it.

### Enable and disable memory

#### Memory enablement rules

The memory function includes the overall function switch and the single-stroke memory activation status.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

If the switch is on, it means that this Agent can use the memory function. Users can still enable or disable different memories individually in the memory list.

If the switch is off, it means that this Agent does not use the memory function. Even if there are already created memories in the memory list, the Agent will not apply these memory contents.

#### Activating and deactivating single memory

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

In the memory list, the "Enabled" field is used to display whether a single memory is enabled. When the memory master switch is turned on, the activated single memory will be used as reference content when the Agent responds or handles tasks.

Users can disable temporarily unused memories as needed, retaining the content but not allowing the Agent to apply it; they can re-enable it if they need to use it again in the future.

## **Session Log**

Conversation records store all conversation records of this Agent. Administrators can filter records by title, user or date range. Records include processing procedures. When errors occur or responses are slow, administrators can review processing details to diagnose the problem.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

## Permissions

The creator can grant access rights to other users through "Permissions" (please refer to role definition).

> Note: The creator is the default "manager", and each project can only have one owner.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Operation Name⟬<table>6 ⟭⟬<table>7⟭Description⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬ <table>14⟭⟬<table>15⟭Edit table⟬<table>16⟭⟬<table>17⟭Allows the user to edit the presentation of the table⟬<table>18⟭⟬<table>19⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭⟬<table>23⟭Refresh⟬<table>24⟭⟬<table>25⟭Click to refresh the list ⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭3⟬<table>30⟭⟬<table>31⟭Content filtering⟬<table>32⟭ ⟬<table>33⟭Advanced filtering of specified content⟬<table>34⟭⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭4⟬<table>38⟭⟬<table> 39⟭Batch deletion⟬<table>40⟭⟬<table>41⟭After checking the items, the delete button in the upper left corner will be displayed, allowing the user to delete multiple items⟬<table>42⟭⟬ <table>43⟭⟬<table>44⟭⟬<table>45⟭5⟬<table>46⟭⟬<table>47⟭Search field⟬<table>48⟭⟬<table>49⟭Search Name⟬<table>50⟭⟬<table>51⟭⟬<table>52⟭⟬<table>53⟭6⟬<table>54⟭⟬<table>55⟭Invite⟬<table>56⟭⟬<table>57⟭Invite Organization / Member⟬<table>58⟭⟬<table>59⟭⟬<table>60⟭⟬<table>61⟭7⟬<table>62⟭⟬<table>63⟭Action⟬<table> 64⟭⟬<table>65⟭Transfer your role or remove selected users⟬<table>66⟭⟬<table>67⟭⟬<table>68⟭⟬<table>69⟭

### **New member**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. Click "Add" to open the conversation box
2. The input box can search for organizations or users
3. Select the corresponding permissions
4. Enter keywords to jump out to the corresponding organization/user
5. You can click the level button on the right to confirm the level of the character.
6. After selecting the target organization/user, you can click the label to open the view menu and view all users within the organization level and role.
7. Click the "Add" button to complete the invitation

## **Web App**

Agents can be embedded into web pages to provide question and answer services, as shown below:

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

To embed an Agent into a website, use this feature to generate front-end embed code.

### **New Web App**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

### Add API Key

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>
