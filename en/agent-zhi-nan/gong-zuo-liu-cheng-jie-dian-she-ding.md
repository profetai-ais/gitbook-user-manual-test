---
description: This guide will demonstrate step-by-step how to configure LLM nodes based on UI elements in the workflow editor.
---

# Workflow node settings



## Page introduction

<figure><img src="../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">Steps</th><th width="180">Block </th><th>Operation Instructions</th>ZXQ PLACEHOLDER9QXZ</thead><tbody><tr>ZXQPLACEHOLDER 13QXZ1</td><td> node name </td><td> is LLM node naming is clear and descriptive (for example: 2. Industry trends). This helps organize processes visually and logically, especially in complex processes. <strong>Note: </strong> The node name must be unique to save the settings. </td></tr><tr><td>2</td><td> node description </td><td> is LLM Nodes provide brief descriptions (for example: including industry dynamics, policy changes, technology drivers and corporate behaviors). This helps organize processes visually and logically, especially in complex processes. </td></tr><tr><td>3ZXQPLACEHOLDER32QX Z<td>Model selection</td><td>Select a language model from the drop-down menu (for example: gpt-5.2-thinking or gpt-5.2-instant). Make sure the model meets response quality and budget requirements. </td></tr><tr><td>4</td><td> situation (input variable) </td><td> settings LLM Input that should be consulted when reasoning. Dynamic input can be passed using variables from other nodes or user input. Enter <code>/</code> in the situation window to see the available variables. ⚠️ To access variables such as <code>result</code>, <code>usage</code> or <code>execution_time</code> from previous nodes, these nodes must <strong> explicitly links </strong> to the current node, otherwise the context cannot resolve the variables correctly. </td></tr><tr><td>5ZXQPLACEHO LDER58QXZ<td> uses node files </td><td> allows LLM to obtain which files from the previous node Case</td></tr><tr><td>6ZXQPLACEH OLDER66QXZ<td>File processing (optional)</td><td>Choose how to process uploaded files. For more information, please refer to the <a href="liao-tian-agent.md#dang-an-chu-li"> file processing </a> chapter. </td></tr><tr><td>7ZXQPLACEHO LDER76QXZ<td>When the knowledge base </td><td> is enabled, the selected knowledge will be automatically queried during the conversation. </td></tr><tr><td>13</td><td>Inference setting </td><td>Click the gear icon next to the model selection area () Customize model behavior, including: <br><em>1. Parameter adjustment </em>: Temperature, Top P, Max Tokens (see parameter table for more information). <br><em>2. System prompt word </em>: Write a prompt word to define the role, task, tone and tool behavior. </td></tr></tbody></table>

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">Steps</th><th width="180">Block</th><th>Operation InstructionsZX QPLACEHOLDER8QXZ</tr></thead><tbody><tr><td>8</td><td>Agent Collaboration </td><td> allows Agents to connect in series and collaborate with other Agents to perform tasks. Agent Can support more functions and task processing scenarios. </td></tr><tr><td>10ZXQPLACEH OLDER30QXZ<td> Reference Memory </td><td> When enabled, the personal memory bank will be referenced during conversations. </td></tr><tr><td>11ZXQPLACEHOLDE R38QXZ<td>Memory settings (optional)</td><td>If multiple rounds of dialogue situations are required, please enable the memory function. Sets the memory window size when building multi-turn conversations or reasoning chains (recommended value: 3–5). <strong> Note: </strong> recommends unifying the number of session memory rounds to ensure process consistency and avoid information loss. ⚠️ A conversation refers to the pairing of a question (user prompt) and a response (assistant answer). </td></tr><tr><td>12</td><td>Tools (optional) </td><td>If the task requires beyond LLM Native capabilities with add-on tools (such as using the <strong>Serper Search</strong> tool to perform real-time web searches during the build process). </td></tr></tbody></table>

## **How ​​to use Context and System Prompt**

When setting up the LLM node, both **Context** and **System Prompt** can contain instructions, but their purposes are different and have clear priorities:

### **Context**

> Purpose: Set dynamic input variables, which can be regarded as the "workspace" of the model - that is, the content currently referenced by the model.

**Note:**

* Use the **Situation** field to pass in **query text**, **user input** or **preceding node data**.
* Supports using variables such as `${start.query}` or `${llm-nodeA.result}` to make responses more personal or contextual.
* Although you can put brief instructions here, the context field should be focused on **content**, not rules of conduct.

### **System Prompt**

> Purpose: Define the behavior and role of the model, which can be regarded as the "permanent job description" of this node.

**Note:**

* Used to define who the model **is**, **how it should act** and **what it should accomplish**.
* Commands in the system prompt word will **take precedence** over commands in the context.
* It is recommended to always clearly define:
  * **Role** (e.g. Product Manager, Analyst, Mentor)
  * **Task Objectives** (e.g. writing reports, interpreting code)
  * **Tone** (e.g.: formal, cordial)
  * **Tool usage rules** (if tools are attached)

### **File Handling**

The **File Handling** setting allows the user to define how the Assistant handles uploaded files in the workspace. This is especially useful when the assistant needs to interpret, convert or extract file content (e.g. PDF, DOCX, images) in a conversation.

<figure><img src="../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="143"> Options</th><th width="120">MCP Tool Visible</th><th width="102">LLM It can be seen that </th><th> describes </th><th> example application scenario </th></tr></thead><tbody>ZX QPLACEHOLDER16QXZ<td> not processed LLM and MCP tools are not visible and will not be opened or parsed. </td><td>– </td></tr><tr><td> Use tools only to handle </td> <td>O</td><td>X</td><td> file is transferred to Processed by MCP tools but not provided to LLM. </td><td> is suitable for situations where data needs to be extracted from CSV or PDF but AI commentary is not required. </td></tr><tr><td> file converted to picture </td>ZXQ PLACEHOLDER43QXZX</td><td>O</td><td>Convert file to image and only LLM Reference. </td><td> is suitable for scanning documents or visual materials that need to refer to the layout structure. </td></tr><tr><td> converted to image and tool processing </td>ZX QPLACEHOLDER55QXZO</td><td>O</td><td>Convert the file to a picture at the same time LLM reference and passed to MCP tool for processing. </td><td> is suitable for invoices or forms that need to parse visual structure and structured data at the same time. </td></tr></tbody></table>
