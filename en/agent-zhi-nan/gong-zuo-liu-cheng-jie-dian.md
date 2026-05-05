# Workflow node

## Introduction

The workflow system provides diverse node designs for building flexible, intelligent and modular assistants. Each node plays a different role in improving system logic, user interaction, and back-end integration.

<figure><img src="../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">Project</th><th width="160">Node Name</th><th>Use in Workflow</th>⟬PH00 09⟭</thead><tbody><tr><td>1</td><td>Knowledge Retrieval</td><td>Retrieve relevant information from internal knowledge base or document database. </td></tr><tr><td>2</td><td>LLM</td><td>Use a language model (e.g. GPT-5.2 Thinking/GPT-5.2 Instant/Gemini 3) Execute prompts to generate or reason results based on the current input. </td></tr><tr><td>3</td><td>Response </td><td>Defines what the user actually sees—outputs and displays the assistant's reply. </td></tr><tr><td>4</td><td>Annotations </td><td>Add internal annotations or callouts to the canvas — not connected to actual logic. </td></tr><tr><td>5</td><td>Variable node </td><td>Retrieve, store or convert the value of the previous step for use by subsequent nodes. </td></tr><tr><td>6</td><td>Guardrail</td><td> can check and restrict content during the process, helping to reduce risks related to personal data leakage, information security and legal compliance, and making the output content more consistent with usage specifications and management requirements. </td></tr><tr><td>7</td><td>Classification</td><td>Automatically label inputs or guide paths based on predefined logic or model-based classification. </td></tr><tr><td>8</td><td>Fork </td><td>Describes the flow and sequence of data between nodes so that tasks can be automated. </td></tr><tr><td>9</td><td>Merge </td><td>Converge the outputs of different branches to the same node and hand them over to subsequent nodes for processing. </td></tr></tbody></table>

### **Knowledge retrieval**

Retrieve relevant information from internal knowledge base or document database.

<div align="center" data-with-frame="true"><figure><img src="../.gitbook/assets/image (28).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Project</th>⟬PH00 05⟭Function Name</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Knowledge retrieval</td><td>Input content (enter "/" to select query as the user's question)⟬PH0 018⟭</tr><tr><td>2</td><td>Knowledge Library Reference </td><td> Select the required knowledge base </td></tr>⟬PH00 28⟭<td>3</td><td>Search parameters</td><td> Refer to "Testing Knowledge Base - Search Parameter Settings"</td></tr></tbody></table>

### **LLM**

Execute prompts using language models (e.g. GPT-5.2 Thinking/GPT-5.2 Instant/Gemini 3) to generate or reason results based on the current input.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (29).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Project</th><th width="160">Function Name⟬PH000 6⟭<th>Description</th></tr></thead><tbody><tr><td>1 </td><td>LLM name </td><td>Enter the node name to facilitate identification </td>⟬PH00 19⟭<tr><td>2</td><td>LLM parameter adjustment</td><td>Reference <a href="liao-tian-agent.md#can-shu">Parameters</a></td></tr><tr><td>3</td><td>Model </td><td>Replace the language model used by the node (with 2. The model settings in are the same)</td></tr><tr><td>4</td><td>Context⟬PH00 42⟭<td>Input content (enter "/" to select query as the user's question)</td></tr><tr>⟬P H0047⟭5</td><td>Use node files</td><td>Allow LLM to obtain which files from previous nodes⟬PH00 52⟭</tr><tr><td>6</td><td>File Processing</td><td>Reference <a href="https://www.notion.so/3509f9da96be81ef9413d427bc2132c7?pvs=21">File Processing</a></td></tr><tr><td>7</td><td>Enable Knowledge Base</td><td>Reference <a href="https://www.notion.so/3509f9da96be81d7b1bbe69f43f236d4?pvs=21">Knowledge Base Source</a></td></tr><tr><td>8</td><td>Agent Collaboration</td><td>Reference <a href="liao-tian-agent.md#agent-xie-zuo">Agent Collaboration</a></td></tr><tr><td>9</td><td>Skills</td><td>Reference <a href="liao-tian-agent.md#ji-neng">Skills</a></td></tr><tr><td>10</td>⟬PH0 097⟭Reference Memory</td><td>After enabled, LLM will refer to the memory in the memory bank when replying. For the memory storage method, please refer to <a href="agent-memory.md"> Agent Memory</a></td></tr><tr><td>11</td><td>Conversation Memory</td><td>Reference <a href="liao-tian-agent.md#can-shu"> Parameters </a> Dialogue memory within </td></tr><tr><td>12</td><td>Tools</td><td>Reference <a href="liao-tian-agent.md#gong-ju">Tools</a></td></tr></tbody></table>

### **reply**

Response Node is used to define the final output content of the Agent and is responsible for transmitting the completed results in the process back to the user or as a response to subsequent system output.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (30).png" alt="" width="246"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Project</th><th width="160">Function Name</th><th>Description</th></tr> </thead><tbody><tr><td>1</td><td>Node name</td><td>Enter the node name for easy identification</td></tr><tr><td>2</td><td>Description</td><td>You can fill in the purpose description of this node</td></tr>⟬PH0 028⟭<td>3</td><td>Configuration variables</td><td>Enter/to configure variables</td></tr></tbody></table>

### **annotation**

Add internal annotations or callouts to the canvas — not connected to actual logic.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (31).png" alt="" width="249"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Project</th><th width="160">Function Name</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Node Name</td><td>Enter the node name to facilitate identification of </td></tr><tr><td>2</td> <td>Remarks</td><td>Enter the remark content for subsequent identification</td></tr></tbody></table>

### **Variable Node**

Retrieve, store or convert the value of the previous step for use by subsequent nodes.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (32).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Project</th><th width="200">Function Name</th> <th>Description</th></tr></thead><tbody><tr><td>1⟬PH0 014⟭<td>Variable (global variable name) </td><td> is used to select/specify the <strong>global variable key value to be written. </strong> (for example: <code>global.age</code>) so that it can be read and referenced with a consistent name in subsequent process nodes. </td></tr><tr><td>2</td><td>Variable content (variable value)⟬P H0028⟭<td> is used to set the <strong>actual value (Value) </strong> of the global variable, which can be directly accessed by subsequent nodes. </td></tr></tbody></table>

### guardrail

Automatically label inputs or guide paths based on predefined logic or model-based classification.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (33).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Project</th><th width="160">Function Name</th><th>Description</th></tr>⟬P H0010⟭<tbody><tr><td>1</td><td>Configuration variables</td><td>Enter/to configure variables</td></tr><tr><td>2</td><td>Block/Mask⟬PH002 4⟭<td>Select the guardrail operation mode</td></tr><tr>⟬P H0029⟭3</td><td>Category</td><td>Select the content to block/mask according to different types</td></tr></tbody></table>

### **Classification**

Automatically label inputs or guide paths based on predefined logic or model-based classification.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (34).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Project</th>⟬PH0 005⟭Function Name</th><th>Description</th></tr>⟬PH0 010⟭<tbody><tr><td>1</td><td>Module Type </td><td>Replace the language model used by the node </td></tr><tr><td>2</td><td>Context</td><td>Input content (enter "/" to select query as the user's question)</td>⟬PH0 027⟭<tr><td>3</td><td>Category</td><td>Categorize the problem </td></tr></tbody></table>

### bifurcation

Describe the flow and sequence of data between nodes so that tasks can be automated.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (35).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Project</th><th width="160">Function Name</th>⟬PH000 7⟭Description</th></tr></thead><tbody><tr><td>1</td><td>Branch</td><td>View the current number of branches</td></tr><tr><td>2</td> <td>Branch status</td><td>View current branch status</td></tr></tbody></table>

### merge

Converge the outputs of different branches to the same node and hand them over to subsequent nodes for processing.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (36).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Project</th><th width="160">Function Name</th><th>Description</th>⟬PH0009 P H0019⟭<tr><td>2</td><td>Input status</td><td>View current input status</td></tr>⟬PH0 028⟭<td>3</td><td>Waiting timeout</td><td>Set waiting timeout</td></tr></tbody></table>
