# Edit workflow

## **Page Navigation**

The figure below shows the workflow editing interface, including the following control items:

<figure><img src="../.gitbook/assets/image (234).png" alt=""><figcaption></figcaption></figure>

1. **Node List**: Workflow functional components provided by AI Studio; please refer to the [工作流程節點](gong-zuo-liu-cheng-jie-dian.md) page for detailed information on available nodes.
2. **Workflow function menu**: Provides functional operations of the editor; see the description below for details
3. **Workflow editing area**: You can drag and drop function nodes to this area to edit the workflow
4. **Editor Map**: Helps users quickly navigate to specific areas of the editor

<table><thead><tr><th width="183"> Workflow function menu items (from left to right as shown above) ZXQPLA CEHOLDER4QXZ<th>Description</th></tr></thead>ZXQPLACEHOLD ER9QXZ<tr><td>Previous step, next step</td><td>Return to the previous step, Or go back to the next step</td></tr><tr><td>HistoryZXQPLACEHO LDER18QXZ<td>Manage workflow edit history</td></tr>ZXQPLACEHOLDER22 QXZ<td>Export file</td><td>Export this workflow as file</td>ZXQP LACEHOLDER27QXZ<tr><td>Display mini map</td><td>Display Show or hide the minimap in the lower right corner of the screen</td></tr><tr><td>Reset viewZXQPL ACEHOLDER36QXZ<td>Center and display the entire workflow</td></tr>ZXQPLACEHOLDER4 0QXZ<td> folds </td><td> folds all nodes in the editor </td>ZXQPLA CEHOLDER45QXZ<tr><td>edit global variable </td><td>edit Global variables in workflow </td></tr><tr><td> scrapbook ZXQPLACEH OLDER54QXZ<td>Save selected nodes and access them at any time</td></tr>ZXQPLACEHOLDER58QX Z<td>Save </td><td>Save workflow changes</td>ZXQPLACEHO LDER63QXZ<tr><td>Test preview</td><td>Open chat window test work workflow (this button does not appear when editing from a workflow template) </td></tr></tbody></table>

## **Create/Edit Workflow**

> Note: It is recommended to open the workflow editor from the assistant settings so that you can use Test Preview directly for testing after editing.

<figure><img src="../.gitbook/assets/image (235).png" alt=""><figcaption></figcaption></figure>

Taking a blank workflow as an example, the screen default will contain a **"Start"** node. Clicking on this node will display several basic variables:

| Variable name | Description | Display information |
|-------------------------------- |---------------- |------------------------------------------------ |
| `(x)${{start}.{query}}` | User input prompt | _User input, for example: _ `summarize the attached document` |
| `(x)${{start}.{files}}` | List of files attached by the user in the chat input area | `metadata of the files in a JSON array` |
| `(x)${{start}.{time}}` | Current system time | `17:19:13` |
| `(x)${{start}.{date}}` | Current system date | `2025-06-06 Friday` |
| `(x)${{start}.{dateTime}}` | Current system date and time | `2025-06-06 Friday 17:19:13` |

The following is a simple example demonstrating basic workflow operations:

<figure><img src="../.gitbook/assets/image (236).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (237).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (238).png" alt=""><figcaption></figcaption></figure>

1. In the new workflow, click the "Start" node to view the basic variables
2. Drag and drop the "Reply" node from the node list to the editing area
3. Connect the output of the "Start" node to the input of the "Reply" node
4. This example will display the contents of basic variables. Click the "Reply" node to open the editing window and edit the assistant's reply content in the input area
5. Enter "/" to display the list of available workflow variables. Please refer to the table above to select the variables to be displayed in the reply.
6. After editing, click the "Save" button in the function menu, and then click "Test Preview" to test the workflow
7. Attach the file in the "Test Preview" chat area and enter the prompt before sending. You can instantly see the assistant's processing steps.
8. After the assistant completes processing, the user can expand the "Reply" item in the chat area to view the results of the workflow

You can follow this step to try using different nodes to create a workflow that meets your application needs!

### Example situation

#### Workflow node (Fork/Merge) news search assistant

Situational demonstration users send a query, and the system can search for information in parallel from multiple data sources at the same time, and automatically integrate the results and hand them over to AI to compile key content. Through the design of Fork and Merge, the efficiency of data collection and analysis can be greatly improved, making complex processes quick and clear.

{% file src="../.gitbook/assets/Understanding Fork & Merge Nodes_ A News Search Agent_2026-02-02_Video.mp4" %}

## Clipboard Copy / Paste

The workflow supports quick copying and pasting of node settings, which is suitable for creating multiple similar nodes or moving existing logic across processes.

<figure><img src="../.gitbook/assets/image (239).png" alt=""><figcaption></figcaption></figure>

How to use:

* Select one or more nodes on the canvas
* Use copy/paste operations
* After pasting, the nodes will appear in the canvas with the same settings, and you can fine-tune the differences.

Additional behavioral instructions:

* Copy and paste across workflows: Nodes can be copied and pasted from process A to process B to speed up the assembly process.
* Batch operation: You can select multiple nodes at one time and copy and paste them, retaining the node settings.
* Naming conflict handling: If the node name or variable name is repeated after pasting, the system may require the name to be adjusted before saving (please follow the prompts to correct it).

> Note: If "output variables of other nodes" are referenced in the node settings, it may not be parsed after being pasted into a new process due to the lack of upstream node links. It is recommended to check whether the connections and variable references are complete before pasting.

## Local Storage temporary storage synchronization mechanism

In order to avoid loss of edits when the browser is refreshed or closed for abnormal reasons, the editor will temporarily store part of the draft status in the local storage (Local Storage) and synchronize it between multiple pages.

<figure><img src="../.gitbook/assets/image (240).png" alt=""><figcaption></figcaption></figure>

## History

The history record can store every content that the user clicks to save. The user can view the historical editing record and return to an older version through restore.

> Note: You need to click the save button in the upper right corner before the content will be recorded in the history.

<figure><img src="../.gitbook/assets/image (241).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (242).png" alt=""><figcaption></figcaption></figure>

&#x20;![](<../.gitbook/assets/image (243).png>)

1. Click "History" in the workflow function menu
2. The left side of the pop-up window is a real-time preview
3. On the right is the version record. You can switch to different versions by clicking on the card.
   1. The maximum number of historical records stored is 21. When the 22nd record is saved, the oldest record will be deleted.
   2. If you want to save a certain historical record, please click the pushpin icon to save the fixed version. The selected pushpin can only store a maximum of 20 records.
4. Click on the version you want to switch to
5. Click "Revert" to apply to the workflow

## Edit global variables (Global Variables)

Global variables can be regarded as "constants/settings shared by this workflow" and are suitable for placing content that will be reused by multiple nodes, such as company policies, tone specifications, fixed formats, reply template fragments, API parameter default values, etc. Through centralized management, repeated modifications in multiple nodes can be avoided.

<figure><img src="../.gitbook/assets/image (244).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (245).png" alt=""><figcaption></figcaption></figure>

1. Click "Edit Global Variables" in the workflow function menu
2. Add or edit variable content in the pop-up window
3. When finished, click "Save" to apply to the workflow.

### Add/edit variables

* Name: An identifying name for reference, only numbers and English letters are allowed.
* Content: Variable value ontology, which can be multi-line text (such as specifications, templates, paragraphs).

> Note: If the variable name is changed, the system will synchronously update the reference in the workflow (it is recommended that the actual screen prompts prevail). If you have manually copied and pasted variables into node content in "plain text", such text does not belong to the variable reference range and needs to be updated by yourself.

### Reference global variables in nodes

Enter / in the node settings (such as the LLM node's Context or other input field) to insert available global variables from the variable list. After insertion, the system will present it in the form of a variable expression, and the latest content will be automatically brought in later.

<figure><img src="../.gitbook/assets/image (246).png" alt=""><figcaption></figcaption></figure>

### Reference global variables in System Prompt

When you want multiple LLM nodes to share a consistent role, tone, or output specification, it is recommended to write the specification into a global variable and directly reference the variable in the System Prompt of each node.

Advantages: When the specification is updated, it only needs to be changed once and it can be applied to all referenced nodes.

> Note: If you see a prompt such as "Variable cannot be resolved/reference failed" when saving, please confirm:

1. Variable names do not contain special symbols or reserved words
2. This node field supports variable reference
3. The variable has been saved successfully

>

### Example situation

#### Global Variables Language Translation Assistant

Scenario demonstration: By setting global variables once, you can simultaneously control the output behavior of all AI nodes in the entire workflow, such as output language. Users can quickly switch between Chinese, English or other languages ​​without modifying each node one by one, ensuring that the overall output is consistent, which is especially suitable for multi-lingual or multinational application scenarios.

{% file src="../.gitbook/assets/Understanding Global Variables A Localization Agent_2026-02-04_Video.mp4" %}

