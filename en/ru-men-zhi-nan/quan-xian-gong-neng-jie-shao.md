---
description: 本功能提供雙層級的權限控管，協助您彈性設定「誰能存取特定功能清單」以及「誰能操作裡面的單一項目」。
---

# Introduction to permission functions

## Permission structure

The first level: Function level (Feature/Function) is used to manage the use and management permissions of "a certain type of function", such as Agent list, knowledge base list, template list, etc. This layer determines whether you can enter the function, whether you can create a new project, whether you can manage the member list of the function, etc.

The second level: Project level (Item) is used to manage the permissions of "each individual project" within the function, such as an Agent, a knowledge base, and a template. This layer allows you to set member roles for a single project, deciding who can edit, who can only use, who can manage members, etc.

> Note: By default, only roles with administrative rights can enter the corresponding functions and perform management operations. If you cannot see certain functions or perform operations, please confirm with the administrator whether your permissions at the "function level" and "project level" have been authorized.

## **Agent function permission**

### **Agent List**

The following table describes what can be done at the "Agent List" level. You can think of the "Agent List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (121).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Create Agent</th><th>Manage Agent List Member</th><th>View all Agent</th><th>Edit all Agent</th></tr></thead><tbody><tr><td><strong>Agent Inventory Manager</strong></td><td>Actionable Agent List and Agent Fully functional characters</td><td>O</td><td>O</td><td>O⟬P H0030⟭<td>O</td></tr><tr><td><strong>Agent List collaborator </strong></td><td> is given permission to assist in managing Agents Role of Manifest Member</td><td>O</td><td>O</td><td>X⟬P H0046⟭<td>X</td></tr><tr><td><strong>Agent List users </strong></td><td> can create and edit their own Agents The role of</td><td>O</td><td>X</td>⟬PH006 1⟭X</td><td>X</td></tr></tbody></table>

### Agent

The following table describes what the "Agent" level can do. At this level, the "Agent Administrator" or "Agent Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Use in Workspace Agent</th><th>View in Agent list Agent</th><th>Manage Agent members</th><th>Edit Agent</th><th>Delete Agent</th></tr></thead><tbody><tr><td><strong>Agent Administrator </strong></td><td> has a complete Agent Control </td><td>O</td><td>O</td><td>O</td>⟬PH0 033⟭O</td><td>O</td></tr><tr><td><strong>Agent Collaborator</strong></td><td> can assist in managing Agent Adjustment of use and content of </td><td>O</td><td>O</td><td>O</td>⟬P H0051⟭O</td><td>X</td></tr><tr><td><strong>Agent User </strong></td><td> can only use Agent in the workspace The role of </td><td>O</td><td>X</td><td>X⟬PH006 8⟭<td>X</td><td>X</td></tr></tbody></table>



## Knowledge base list function permissions

### Knowledge base list

The following table describes what can be done at the Knowledge Base Inventory level. You can think of the "Knowledge Base List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Build Knowledge</th>⟬P H0009⟭Manage knowledge base members</th><th>View all knowledge</th><th>Edit all knowledge</th></tr></thead><tbody><tr><td><strong>Knowledge Base List Administrator</strong></td><td>A role that can operate all functions of the knowledge base and knowledge</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Knowledge Base List Collaborator</strong></td><td>Role assigned permission to assist in managing knowledge base members</td>⟬P H0041⟭O</td><td>O</td><td>X</td><td>X</td></tr><tr> <td><strong>Knowledge base list user </strong></td><td>A role that can create and edit their own knowledge </td><td>O</td><td>X</td><td>X</td><td>

### Knowledge

The following table describes what can be done at the "knowledge" level. At this level, "knowledge managers" or "knowledge collaborators" are usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role </th><th>Description </th><th>Available at Agent New knowledge</th><th>View knowledge in knowledge base list</th><th>Manage knowledge members</th><th>Edit knowledge</th><th>Delete Knowledge</th></tr></thead><tbody><tr><td><strong>Knowledge Manager⟬PH00 23⟭</td><td>Have complete knowledge control</td><td>O</td><td>O</td><td> O</td><td>O</td><td>O</td></tr><tr><td><strong>Knowledge Collaboration Author </strong></td><td> can assist in the content adjustment of management knowledge </td><td>O</td><td>O</td> <td>X</td><td>O</td><td> 058⟭Knowledge User</strong></td><td>A character who can only read knowledge</td><td>O</td><td>X</td><td>X</td><td>X</td><td>



## **MCP Function Permissions**

### **MCP List**

The following table describes what can be done at the "**MCP** Checklist" level. You can think of the "**MCP** List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (125).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Character</th><th> Description</th><th>Establish MCP</th><th>Manage MCP members⟬PH0 010⟭<th>View all MCPs</th><th>Edit all MCPs</th> </tr></thead><tbody><tr><td><strong>MCP Inventory Administrator</strong></td><td>A role that can operate the MCP inventory and all MCP functions</td><td>O</td>⟬PH002 7⟭O</td><td>O</td><td>O</td></tr><tr><td><strong>MCP Manifest collaborator </strong></td><td> is given the role of assisting in managing MCP manifest members </td><td>O</td>⟬PH004 3⟭O</td><td>X</td><td> List users </strong></td><td> can create and edit their own MCP roles </td><td>O</td>⟬P H0059⟭X</td><td>X</td><td>

### **MCP**

The following table describes what can be done at the "MCP" level. At this level, the "MCP Administrator" or "MCP Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role </th><th>Description </th><th>Available at Agent New MCP</th><th>View MCP in MCP list</th><th>Set MCP members</th><th>Edit MCP</th><th>Delete MCP</th></tr></thead><tbody><tr><td><strong>MCP Administrator </strong></td><td> has full MCP control </td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>MCP Collaborator </strong></td><td> can assist in managing content adjustments for MCP </td><td>O</td><td>O</td>⟬P H0049 ⟭ User </strong></td><td>can only read MCP roles </td><td>O</td><td>X⟬PH006 6⟭<td>X</td><td>X</td><td>



## **Workflow Template Function Permissions**

### **Workflow Template Checklist**

The following table describes what can be done at the "Workflow Template List" level. You can think of the "Workflow Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Build Workflow Template</th><th>Manage workflow member templates</th><th>View all workflow templates</th><th>Edit all workflow templates</th></tr></thead><tbody><tr><td><strong>Workflow Template Checklist Administrator</strong></td><td>Operable Workflow Template Checklist and Workflow The role of all template functions</td><td>O</td><td>O</td><td>O</td><td>O</td>⟬P H0033⟭<tr><td><strong>Workflow Template Manifest Collaborator</strong></td><td>Role assigned permission to assist in managing workflow template manifest members </td><td>O</td><td>O</td>⟬P H0045⟭X</td><td>X</td></tr>⟬PH0 050⟭<td><strong>Workflow template list user</strong></td><td>A role that can create and edit their own workflow templates</td>⟬PH0 057⟭O</td><td>X</td><td>X⟬PH00 62⟭<td>X</td></tr></tbody></table>

### Workflow template

The following table describes what can be done at the "Workflow Template" level. At this level, "workflow template administrators" or "workflow template collaborators" are usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (128).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Workflow templates are available in the workspace</th>⟬PH0 009⟭View the workflow template in the workflow list</th><th>Set workflow template members</th><th>Edit the workflow template</th><th>Delete the workflow Template</th></tr></thead><tbody><tr>⟬PH00 21⟭<strong>Workflow Template Administrator</strong></td><td>has complete Complete workflow template control</td><td>O</td><td>O⟬P H0030⟭<td>O</td><td>O</td><td> O</td></tr><tr><td><strong>Workflow template collaborator</strong></td><td>can assist in managing content adjustments to workflow templates⟬PH0 044⟭<td>O</td><td>O</td><td>X </td><td>O</td><td>X</td>⟬PH005 5⟭<tr><td><strong>Workflow Template User</strong></td><td>Role that can only read workflow templates</td><td>O⟬PH00 64⟭<td>X</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>



## **Prompt Word Template Function Permission**

### **Prompt word template list**

The following table describes what can be done at the "Prompt Word Template List" level. You can think of the "Prompt Word Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Create Prompt Word Template</th><th>Manage prompt word list template members</th><th>View all prompt word templates</th><th>Edit all prompt word templates</th></tr>⟬PH0 016⟭<tbody><tr><td><strong>Prompt word template list administrator</strong></td><td>Operable prompt word template list and prompt word template Fully functional characters</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Prompt Word Template List Collaborator</strong></td><td>Role given permission to assist in managing Prompt Word Template List members⟬P H0040⟭<td>O</td><td>O</td><td>X</td><td>X</td></tr>⟬PH0 050⟭<td><strong>Prompt word template list users</strong></td><td>A role that can create and edit their own prompt word templates</td>⟬PH00 57⟭O</td><td>X</td><td>X⟬PH00 62⟭<td>X</td></tr></tbody></table>

### prompt word template

The following table describes what can be done at the "prompt word template" level. At this level, the "prompt word template administrator" or "prompt word template collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Prompt word template can be used in the workspace</th><th>View prompt words in prompt word list list</th><th>Set prompt word template members</th><th>Edit prompt word template</th><th>Delete prompt word template⟬PH0 016⟭</tr></thead><tbody><tr><td><strong>Prompt word template administrator</strong></td><td>has complete prompt words Template control rights</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Prompt word template collaborator</strong></td><td>can assist in managing the content adjustment of the prompt word template</td> <td>O</td><td>O</td><td>X</td><td>O</td><td>X</td></tr> <tr><td><strong>Prompt word template user </strong></td><td>The role that can only read the prompt word template </td><td>O</td><td>X</td><td>X</td><td>X⟬P H0070⟭<td>X</td></tr></tbody></table>
