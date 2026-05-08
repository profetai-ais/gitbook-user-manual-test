# Workflow node

## Introduction

The workflow system provides diverse node designs for building flexible, intelligent and modular assistants. Each node plays a different role in improving system logic, user interaction, and back-end integration.

<figure><img src="../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">project</th><th width="160">Node name</th><th>Use in workflow</th></tr></thead><tbody><tr><td>1</td><td>knowledge retrieval</td><td>Retrieve relevant information from internal knowledge base or document database.</td></tr><tr><td>2</td><td>LLM</td><td>Execute prompts using language models (e.g. GPT-5.2 Thinking/GPT-5.2 Instant/Gemini 3) to generate or reason results based on the current input.</td></tr><tr><td>3</td><td>respond</td><td>Define what the user actually sees—outputting and displaying the assistant's responses.</td></tr><tr><td>4</td><td>annotation</td><td>Add internal annotations or callouts to the canvas — not connected to actual logic.</td></tr><tr><td>5</td><td>variable node</td><td>Retrieve, store or convert the value of the previous step for use by subsequent nodes.</td></tr><tr><td>6</td><td>guardrail</td><td>Content can be checked and restricted during the process to help reduce risks related to personal data leakage, information security and legal compliance, and make the output content more consistent with usage specifications and management requirements.</td></tr><tr><td>7</td><td>Classification</td><td>Automatically label inputs or guide paths based on predefined logic or model-based classification.</td></tr><tr><td>8</td><td>bifurcation</td><td>Describe the flow and sequence of data between nodes so that tasks can be automated.</td></tr><tr><td>9</td><td>merge</td><td>Converge the outputs of different branches to the same node and hand them over to subsequent nodes for processing.</td></tr></tbody></table>

### **Knowledge retrieval**

Retrieve relevant information from internal knowledge base or document database.

<div align="center" data-with-frame="true"><figure><img src="../.gitbook/assets/image (28).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">project</th><th width="160">Function name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>knowledge retrieval</td><td>The content of Input (enter "/" to select query as the user's question)</td></tr><tr><td>2</td><td>Knowledge base reference</td><td>Select the required knowledge base</td></tr><tr><td>3</td><td>Retrieval parameters</td><td>Refer to "Testing Knowledge Base-Search Parameter Settings"</td></tr></tbody></table>

### **LLM**

Execute prompts using language models (e.g. GPT-5.2 Thinking/GPT-5.2 Instant/Gemini 3) to generate or reason results based on the current input.



<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (29).png" alt="" width="188"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">project</th><th width="160">Function name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>LLM name</td><td>Enter a node name for easy identification</td></tr><tr><td>2</td><td>LLM parameter adjustment</td><td>refer to <a href="liao-tian-agent.md#can-shu">parameter</a></td></tr><tr><td>3</td><td>Model</td><td>Change the language model used by the node (same as the model setting in 2.)</td></tr><tr><td>4</td><td>context</td><td>The content of Input (enter "/" to select query as the user's question)</td></tr><tr><td>5</td><td>Using node archives</td><td>Which files LLM is allowed to obtain from previous nodes</td></tr><tr><td>6</td><td>File processing</td><td>refer to <a href="https://www.notion.so/3509f9da96be81ef9413d427bc2132c7?pvs=21">File processing</a></td></tr><tr><td>7</td><td>Enable knowledge base</td><td>refer to <a href="https://www.notion.so/3509f9da96be81d7b1bbe69f43f236d4?pvs=21">Knowledge base sources</a></td></tr><tr><td>8</td><td>Agent collaboration</td><td>refer to <a href="liao-tian-agent.md#agent-xie-zuo">Agent collaboration</a></td></tr><tr><td>9</td><td>Skill</td><td>refer to <a href="liao-tian-agent.md#ji-neng">Skill</a></td></tr><tr><td>10</td><td>reference memory</td><td>After enabling, LLM will refer to the memory in the memory bank when replying. For the memory storage method, please refer to<a href="agent-memory.md"> Agent Memory</a></td></tr><tr><td>11</td><td>dialogue memory</td><td>refer to <a href="liao-tian-agent.md#can-shu">parameter</a> dialogue memory within</td></tr><tr><td>12</td><td>tool</td><td>refer to <a href="liao-tian-agent.md#gong-ju">tool</a></td></tr></tbody></table>

### **reply**

Response Node is used to define the final output content of the Agent and is responsible for transmitting the completed results in the process back to the user or as a response to subsequent system output.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (30).png" alt="" width="246"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">project</th><th width="160">Function name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>Node name</td><td>Enter a node name for easy identification</td></tr><tr><td>2</td><td>illustrate</td><td>You can fill in the purpose description of this node</td></tr><tr><td>3</td><td>Configuration variables</td><td>Enter/to configure variables</td></tr></tbody></table>

### **annotation**

Add internal annotations or callouts to the canvas — not connected to actual logic.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (31).png" alt="" width="249"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">project</th><th width="160">Function name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>Node name</td><td>Enter a node name for easy identification</td></tr><tr><td>2</td><td>Remark</td><td>Enter the remark content for subsequent identification</td></tr></tbody></table>

### **Variable Node**

Retrieve, store or convert the value of the previous step for use by subsequent nodes.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (32).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">project</th><th width="200">Function name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>Variable (global variable name)</td><td>Used to select/specify the<strong>Global variable key value</strong>(For example:<code>global.age</code>) so that it can be read and referenced with a consistent name in subsequent process nodes.</td></tr><tr><td>2</td><td>Variable content (variable value)</td><td>used to set this global variable<strong>Actual value (Value)</strong>, for subsequent nodes to access directly.</td></tr></tbody></table>

### guardrail

Automatically label inputs or guide paths based on predefined logic or model-based classification.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (33).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">project</th><th width="160">Function name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>Configuration variables</td><td>Enter/to configure variables</td></tr><tr><td>2</td><td>Block/Mask</td><td>Select guardrail operation mode</td></tr><tr><td>3</td><td>category</td><td>Select blocked/mask content according to different types</td></tr></tbody></table>

### **Classification**

Automatically label inputs or guide paths based on predefined logic or model-based classification.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (34).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">project</th><th width="160">Function name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>Model</td><td>Change the language model used by the node</td></tr><tr><td>2</td><td>context</td><td>The content of Input (enter "/" to select query as the user's question)</td></tr><tr><td>3</td><td>category</td><td>Classify problems</td></tr></tbody></table>

### bifurcation

Describe the flow and sequence of data between nodes so that tasks can be automated.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (35).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">project</th><th width="160">Function name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>branch</td><td>View the current number of branches</td></tr><tr><td>2</td><td>branch status</td><td>View current branch status</td></tr></tbody></table>

### merge

Converge the outputs of different branches to the same node and hand them over to subsequent nodes for processing.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (36).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">project</th><th width="160">Function name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>wait</td><td>View the number of waiting nodes</td></tr><tr><td>2</td><td>input status</td><td>View current input status</td></tr><tr><td>3</td><td>Wait timeout</td><td>Set wait timeout</td></tr></tbody></table>
