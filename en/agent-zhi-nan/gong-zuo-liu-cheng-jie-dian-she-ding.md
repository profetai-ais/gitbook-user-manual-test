---
description: 本指南將逐步示範如何依據工作流程編輯器中的 UI 元素設定 LLM 節點。
---

# Workflow node settings



## Page introduction

<figure><img src="../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">Steps</th><th width="180">Blocks</th><th>Operating Instructions</th></tr></thead><tbody><tr><td>1</td><td>Node name </td><td> is LLM node naming is clear and descriptive (for example: 2. Industry trends). This helps organize processes visually and logically, especially in complex processes. <strong> Note: </strong> The node name must be unique to save the settings. </td></tr><tr><td>2</td><td>Node Description </td><td> Provide a short description for the LLM node (for example: including industry dynamics, policy changes, technology drivers and corporate behaviors). This helps organize processes visually and logically, especially in complex processes. </td></tr><tr><td>3</td><td>Model Selection</td><td>Select a language model from the drop-down menu (for example: gpt-5.2-thinking or gpt-5.2-instant). Make sure the model meets response quality and budget requirements. </td></tr><tr><td>4</td><td>Situation (input variables) </td><td> Set the input content that the LLM should refer to when inferring. Dynamic input can be passed using variables from other nodes or user input. Enter <code>/</code> in the situation window to see the available variables. ⚠️ To access variables such as <code>result</code>, <code>usage</code> or <code>execution_time</code> from previous nodes, these nodes must <strong> explicitly links </strong> to the current node, otherwise the context cannot parse the variables correctly. </td></tr><tr><td>5</td><td>Using node files </td><td>Which files are allowed to be obtained by LLM from the previous node Case </td></tr><tr><td>6</td><td>File Handling (optional) </td><td>Choose how to handle uploaded files. For more information, please refer to the <a href="liao-tian-agent.md#dang-an-chu-li">File Processing</a> chapter. </td></tr><tr><td>7</td><td>Knowledge Base </td><td>When enabled, the selected knowledge will be automatically queried during the conversation. </td></tr><tr><td>13</td><td>Inference Settings</td><td>Click the gear icon () next to the model selection area Customize model behavior, including: <br><em>1. Parameter adjustment </em>: Temperature, Top P, Max Tokens (please refer to the parameter table for more information). <br><em>2. System prompt words </em>: Write prompt words to define the role, task, tone, and tool behavior. </td></tr></tbody></table>

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">Steps</th><th width="180">Block</th><th>Operation Instructions Ming</th></tr></thead><tbody><tr><td>8</td><td>Agent Collaboration </td><td> allows Agents to connect in series and collaborate with other Agents to perform tasks. </td></tr><tr><td>9</td><td>Skills</td><td>By setting different skills, Agent can support more functions and task processing scenarios. </td></tr><tr><td>10</td><td>Reference Memory </td><td>When enabled, personal memory will be referenced during conversations. </td></tr><tr><td>11</td><td>Memory Settings (optional) </td><td> If multiple rounds of dialogue situations are required, please enable the memory function. Sets the memory window size when building multi-turn conversations or reasoning chains (recommended value: 3–5). <strong> Note: </strong> It is recommended to unify the number of session memory rounds to ensure process consistency and avoid information loss. ⚠️ A conversation refers to the pairing of a question (user prompt) and a response (assistant answer). </td></tr><tr><td>12</td><td>Tools (optional) </td><td>If the task requires functionality beyond the native capabilities of LLM, additional tools can be used (e.g. using <strong>Serper Search</strong> tool performs real-time web searches during generation). </td></tr></tbody></table>

## **How ​​to use Context and System Prompt**

When setting up the LLM node, both **Context** and **System Prompt** can contain instructions, but their purposes are different and have clear priorities:

### **Context**

> Purpose: Set dynamic input variables, which can be regarded as the "workspace" of the model - that is, the content currently referenced by the model.

**Note:**

* Use the **Context** field to pass in **query text**, **user input** or **preceding node data**.
* Supports using variables such as `${start.query}` or `${llm-nodeA.result}` to make responses more personal or contextual.
* Although you can put brief instructions here, the context field should be focused on **content** rather than rules of conduct.

### **System Prompt**

> Purpose: Define the behavior and role of the model, which can be regarded as the "permanent job description" of this node.

**Note:**

* Used to define who the model is, how it should act, and what it should accomplish.
* Commands in the system prompt word will take precedence over commands in the context.
* It is recommended to always clearly define:
 * **Role** (e.g. Product Manager, Analyst, Mentor)
 * **Task Objective** (e.g. writing a report, interpreting code)
 * **Tone** (e.g. formal, friendly)
 * **Tool usage rules** (if tools are attached)

### **File Handling**

The **File Handling** setting allows the user to define how the Assistant handles uploaded files in the workspace. This is especially useful when the assistant needs to interpret, convert or extract file content (e.g. PDF, DOCX, images) in a conversation.

<figure><img src="../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="143">Options</th><th width="120">MCP tool visible </th><th width="102">LLM Visible</th><th>Instructions</th><th>Example application scenarios</th></tr></thead><tbody><tr><td>Not processed</td><td>X</td><td>X</td><td>The file has been uploaded but the LLM and MCP tools are not visible and will not be opened or parsed. </td><td>– </td></tr><tr><td>Handle with tools only </td> <td>O</td><td>X</td><td>File passed to Processed by MCP tools but not provided to LLM. </td><td> is suitable for situations where data needs to be extracted from CSV or PDF but AI commentary is not required. </td></tr><tr><td>File to image</td><td> LLM Reference. </td><td> is suitable for scanning documents or visual materials that require reference to the layout structure. </td></tr><tr><td>Convert to image and tool processing</td>⟬P H0055⟭O</td><td>O</td><td>Also convert the file into a picture for LLM reference and passed to MCP tool for processing. </td><td> is suitable for invoices or forms that need to parse both visual structure and structured data. </td></tr></tbody></table>
