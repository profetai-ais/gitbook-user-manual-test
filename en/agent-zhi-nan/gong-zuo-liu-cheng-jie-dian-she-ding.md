---
description: "This guide will demonstrate step-by-step how to configure LLM nodes based on UI elements in the workflow editor."
---
---
# Workflow node settings



## Page introduction

<figure><img src="../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">step</th><th width="180">block</th><th>Operating Instructions</th></tr></thead><tbody><tr><td>1</td><td>Node name</td><td>Name your LLM nodes clearly and descriptively (e.g. 2. Industry Trends). This helps organize processes visually and logically, especially in complex processes.<strong>Notice:</strong> Node names must be unique to store settings.</td></tr><tr><td>2</td><td>Node description</td><td>Provide a brief description for the LLM node (for example: including industry dynamics, policy changes, technology drivers and corporate behaviors). This helps organize processes visually and logically, especially in complex processes.</td></tr><tr><td>3</td><td>Model selection</td><td>Select a language model from the drop-down menu (for example: gpt-5.2-thinking or gpt-5.2-instant). Make sure the model meets response quality and budget requirements.</td></tr><tr><td>4</td><td>Situation (input variables)</td><td>Sets the input that the LLM should refer to when inferring. Dynamic input can be passed using variables from other nodes or user input. Enter in context window <code>/</code> Available variables can be viewed. ⚠️ To access the data from the previous node <code>result</code>、<code>usage</code> or <code>execution_time</code> variables, these nodes must <strong>explicit link</strong> to the current node, otherwise the context cannot resolve the variables correctly.</td></tr><tr><td>5</td><td>Using node archives</td><td>Which files LLM is allowed to obtain from previous nodes</td></tr><tr><td>6</td><td>File processing (optional)</td><td>Choose what to do with uploaded files. For more information please refer to <a href="liao-tian-agent.md#dang-an-chu-li">File processing</a> chapter.</td></tr><tr><td>7</td><td>knowledge base</td><td>When enabled, selected knowledge will be automatically queried during conversations.</td></tr><tr><td>13</td><td>reasoning setting</td><td>Click the gear icon () next to the model selection area to customize model behavior, including:<br><em>1. Parameter adjustment</em>: Temperature, Top P, Max Tokens (please refer to the parameter table for more information).<br><em>2. System prompt words</em>: Write prompt words to define roles, tasks, tone, and tool behavior.</td></tr></tbody></table>

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">step</th><th width="180">block</th><th>Operating Instructions</th></tr></thead><tbody><tr><td>8</td><td>Agent collaboration</td><td>Let Agents connect in series and collaborate with other Agents to perform tasks.</td></tr><tr><td>9</td><td>Skill</td><td>By setting different skills, Agent can support more functions and task processing scenarios.</td></tr><tr><td>10</td><td>reference memory</td><td>When enabled, personal memory will be referenced during conversations.</td></tr><tr><td>11</td><td>Memory settings (optional)</td><td>If you need multiple rounds of dialogue situations, please enable the memory function. Sets the memory window size when building multi-turn conversations or reasoning chains (recommended value: 3–5).<strong>Notice:</strong> It is recommended to unify the number of session memory rounds to ensure process consistency and avoid information loss. ⚠️ A conversation refers to the pairing of a question (user prompt) and a response (assistant answer).</td></tr><tr><td>12</td><td>Tools (optional)</td><td>If the task requires functionality beyond the native capabilities of LLM, additional tools can be used (e.g. using <strong>Serper Search</strong> The tool performs real-time web searches during the build process).</td></tr></tbody></table>

## **How ​​to use Context and System Prompt**

When setting up the LLM node, both **Context** and **System Prompt** can contain instructions, but their purposes are different and have clear priorities:

### **Context**

> Purpose: Set dynamic input variables, which can be regarded as the "workspace" of the model - that is, the content currently referenced by the model.

**Note:**

* Use the **Context** field to pass in **query text**, **user input** or **preceding node data**.
* Supports using variables such as or to make responses more personal or contextual.
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

<table><thead><tr><th width="143">Options</th><th width="120">MCP tools visible</th><th width="102">LLM visible</th><th>illustrate</th><th>Example application scenarios</th></tr></thead><tbody><tr><td>Not processed</td><td>X</td><td>X</td><td>The file has been uploaded but is not visible to LLM and MCP tools and will not be opened or parsed.</td><td>– </td></tr><tr><td>Handle with tools only</td><td>O</td><td>X</td><td>Archives are passed to MCP tools for processing but are not provided to LLM.</td><td>Ideal for situations where data needs to be extracted from CSV or PDF but AI commentary is not required.</td></tr><tr><td>Convert files to images</td><td>X</td><td>O</td><td>Convert archives to images and for LLM reference only.</td><td>Suitable for scanned documents or visual materials that require reference to layout structure.</td></tr><tr><td>Convert to image and tool processing</td><td>O</td><td>O</td><td>At the same time, the file is converted into a picture for reference by LLM and passed to the MCP tool for processing.</td><td>Suitable for invoices or forms that need to parse both visual structure and structured data.</td></tr></tbody></table>
