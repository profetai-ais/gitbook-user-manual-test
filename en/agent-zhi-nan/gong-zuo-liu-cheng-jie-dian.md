# Workflow node

## Introduction

The workflow system provides diverse node designs for building flexible, intelligent and modular assistants. Each node plays a different role in improving system logic, user interaction, and back-end integration.

<figure><img src="../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80"> project </th>Z XQPLACEHOLDER5QXZNode name</th><th>Use in workflow</th>ZXQPLACEH OLDER9QXZ</thead><tbody><tr><td>1ZXQPLAC EHOLDER14QXZ<td>Knowledge retrieval</td><td>Retrieve relevant information from internal knowledge base or document database. </td></tr><tr><td>2</td><td>LLM</td><td> uses a language model (e.g. GPT-5.2 Thinking/GPT-5.2 Instant/Gemini 3) Execute prompts to generate or reason results based on the current input. </td></tr><tr><td>3</td><td> responds to </td><td> defines what the user actually sees — Output and display the assistant's reply. </td></tr><tr><td>4</td><td> Annotation </td><td> Add internal annotations or callouts to the canvas — Not connected to actual logic. </td></tr><tr><td>5ZXQPLACEHOLDER 46QXZ<td>The variable node </td><td> retrieves, stores or converts the value of the previous step for use by subsequent nodes. </td></tr><tr><td>6</td>ZXQPLACE HOLDER55QXZ guardrail </td><td> can check and restrict content during the process, helping to reduce risks related to personal data leakage, information security and legal compliance, and making the output content more consistent with usage specifications and management needs. </td></tr><tr><td>7ZXQPLACEHOLDER62Q XZ<td>Classification</td><td> Automatically tag inputs or guide paths based on predefined logic or model-based classification. </td></tr><tr><td>8ZXQPLACEHOLDER 70QXZ<td> fork </td><td> describes the flow and sequence of data between nodes so that tasks can be automated. </td></tr><tr><td>9ZXQPLACEHOLDER 78QXZ<td> merges </td><td> to converge the output of different branches to the same node and transfer them to subsequent nodes for processing. </td></tr></tbody></table>

### **Knowledge Retrieval**

Retrieve relevant information from internal knowledge base or document database.

<div align="center" data-with-frame="true"><figure><img src="../.gitbook/assets/image (28).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80"> project </th>ZXQPLA CEHOLDER5QXZFunction name</th><th>Description</th></tr>ZXQPLACEH OLDER10QXZ<tbody><tr><td>1</td>ZXQPLACEHOL DER15QXZ Knowledge retrieval </td><td>Input content (enter "/" to select query as the user's question) </td>Z XQPLACEHOLDER19QXZ<tr><td>2</td><td>Knowledge Base Refer to </td><td> to select the required knowledge base </td></tr>ZXQPLACEHOLDE R28QXZ<td>3</td><td> retrieval parameter </td>ZXQPLACEHOLD ER33QXZ refer to "Testing Knowledge Base - Search Parameter Settings" </td></tr></tbody></table>

### **LLM**

Execute prompts using language models (e.g. GPT-5.2 Thinking/GPT-5.2 Instant/Gemini 3) to generate or reason results based on the current input.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (29).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Item</th><th width="160">Function nameZXQPLACEHOLDER6 QXZ<th>Description</th></tr></thead><tbody><tr>ZXQPLACEHOLDER 13QXZ1</td><td>LLM name</td><td>Enter the node name to facilitate identification </td>ZXQPLACEHOLDE R19QXZ<tr><td>2</td><td>LLM parameter adjustment </td><td> reference <a href="liao-tian-agent.md#can-shu"> parameters</a></td></tr><tr>ZXQPLAC EHOLDER31QXZ3</td><td> model </td><td> replaces the language model used by the node (with 2. The model settings in are the same) </td></tr><tr><td>4</td><td>ContextZXQPL Contents of ACEHOLDER42QXZ<td>Input (enter "/" to select query as the user's question) </td></tr><tr>ZXQPLACEHOLDE R47QXZ5</td><td> uses the node file </td><td> to allow LLM to obtain which files </td>ZXQPLACE from the previous node HOLDER53QXZ<tr><td>6</td><td>File processing</td><td>Reference <a href="https://www.notion.so/3509f9da96be81ef9413d427bc2132c7?pvs=21"> file processing</a></td></tr><tr>ZX QPLACEHOLDER65QXZ7</td><td>Enable knowledge base</td><td>Reference <a href="https://www.notion.so/3509f9da96be81d7b1bbe69f43f236d4?pvs=21"> Knowledge Base Source </a></td></tr><tr><td>8</td><td>Agent Collaboration </td><td> Reference <a href="liao-tian-agent.md#agent-xie-zuo">Agent Collaboration</a></td></tr><tr>ZXQPLACEHOL DER85QXZ9</td><td>Skills</td><td>Reference <a href="liao-tian-agent.md#ji-neng">Skills</a></td></tr><tr><td>10ZXQPLAC EHOLDER96QXZ<td> Reference memory </td><td> When enabled, LLM will refer to the memory in the memory bank when replying. For the storage method of memory, please refer to <a href="agent-memory.md"> Agent Memory</a></td></tr><tr>ZXQPLACEHOL DER105QXZ11</td><td>Dialogue Memory</td><td>Reference <a href="liao-tian-agent.md#can-shu"> parameters</a> Dialogue memory within </td></tr><tr><td> 12</td><td>Tools</td><td>Reference <a href="liao-tian-agent.md#gong-ju">Tools</a></td></tr></tbody></table>

### **reply**

Response Node is used to define the final output content of the Agent and is responsible for transmitting the completed results in the process back to the user or as a response to subsequent system output.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (30).png" alt="" width="246"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80"> project </th>ZXQ PLACEHOLDER5QXZFunction name</th><th>Description</th></tr>ZX QPLACEHOLDER10QXZ<tbody><tr><td>1</td>Z XQPLACEHOLDER15QXZNode name</td><td>Enter the node name to facilitate identification </td>ZXQPLA CEHOLDER19QXZ<tr><td>2</td><td>DescriptionZXQ PLACEHOLDER24QXZ<td> can fill in the usage description of this node </td></tr>ZXQPLACEHOLD ER28QXZ<td>3</td><td> configuration variable </td>ZXQPLAC EHOLDER33QXZ input/to configure the variable </td></tr></tbody></table>

### **Note**

Add internal annotations or callouts to the canvas — not connected to actual logic.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (31).png" alt="" width="249"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Item</th><th width="160">Function name</th>ZXQPLACEHOLDER7QX ZDescription</th></tr></thead><tbody><tr><td>1</td>ZXQPLACEHOLDER1 5QXZNode name</td><td>Enter the node name to facilitate identification </td></tr><tr><td>2ZXQPLACEHOLDER22 QXZ<td>Remarks</td><td>Enter the remarks for subsequent identification</td></tr></tbody></table>

### **Variable Node**

Retrieve, store or convert the value of the previous step for use by subsequent nodes.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (32).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Item</th><th width="200">Function nameZXQPLA CEHOLDER6QXZ<th>Description</th></tr></thead><tbody>ZXQPLACEHOLDER1 2QXZ<td>1</td><td> variable (global variable name) </td><td> is used to select/specify the variable to be written <strong> global variable key value </strong> (for example: <code>global.age</code>) so that it can be read and referenced with a consistent name in subsequent process nodes. </td></tr><tr><td>2</td><td> The variable content (variable value) </td><td> is used to set the <strong> actual value (Value) </strong> of the global variable for direct access by subsequent nodes. </td></tr></tbody></table>

### Guardrail

Automatically label inputs or guide paths based on predefined logic or model-based classification.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (33).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80"> project </th>ZXQP LACEHOLDER5QXZFunction name</th><th>Description</th></tr>ZXQP LACEHOLDER10QXZ<tbody><tr><td>1</td>ZXQP LACEHOLDER15QXZConfigure variable </td><td>Enter/to configure variable </td>ZXQPLACEHOLD ER19QXZ<tr><td>2</td><td>Block/MaskZXQPLAC EHOLDER24QXZ<td> Select the guardrail operation mode </td></tr>ZXQPLACEHOLDER28QX Z<td>3</td><td> Category</td>ZXQPLACEHOLDER33 QXZ chooses to block/mask content according to different types </td></tr></tbody></table>

### **Classification**

Automatically label inputs or guide paths based on predefined logic or model-based classification.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (34).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80"> project </th>ZXQPL ACEHOLDER5QXZFunction name</th><th>Description</th></tr>ZXQPLA CEHOLDER10QXZ<tbody><tr><td>1</td>ZXQPLAC EHOLDER15QXZ model </td><td> Replace the language model used by the node </td>ZXQPLACEHOLDER 19QXZ<tr><td>2</td><td>ContextZXQPLACEHOLD Contents of ER24QXZ<td>Input (enter "/" to select query as the user's question) </td></tr>ZXQP LACEHOLDER28QXZ<td>3</td><td>Category</td>ZXQ PLACEHOLDER33QXZ classifies the problem as </td></tr></tbody></table>

### Forks

Describe the flow and sequence of data between nodes so that tasks can be automated.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (35).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80">Item</th><th width="160">Function name</th>ZXQPLACEHOLDER7Q XZ Description ER15QXZ branch </td><td> View the current number of branches </td></tr><tr><td>2ZXQPLACEHOLDER22 QXZ<td> branch status </td><td> View current branch status </td></tr></tbody></table>

### Merge

Converge the outputs of different branches to the same node and hand them over to subsequent nodes for processing.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image (36).png" alt="" width="375"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="80"> project </th>ZX QPLACEHOLDER5QXZFunction name</th><th>Description</th></tr>Z XQPLACEHOLDER10QXZ<tbody><tr><td>1ZXQPLACEHOLDER14QX Z<td> is waiting for </td><td> View the number of waiting nodes </td>ZXQPLAC EHOLDER19QXZ<tr><td>2</td><td>Enter status Z XQPLACEHOLDER24QXZ<td>View current input status</td></tr>ZXQPLACEHOLD ER28QXZ<td>3</td><td>wait timeout</td>ZXQPLA CEHOLDER33QXZ Set wait timeout </td></tr></tbody></table>
