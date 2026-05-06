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

<table data-full-width="true"><thead><tr><th width="183">Role</th><th>Agent Inventory Administrator </th><th>Agent List of collaborators</th><th>Agent List User</th></tr></thead><tbody><tr><td><strong>Description</strong></td><td>Operable Agent The role </td><td>, which has all the functions of the list and Agent, is given the authority to help manage the Agent list members. The role </td><td> can create and edit its own Agent. The role of </td></tr><tr><td><strong> is created Agent</strong></td><td>O</td><td>O⟬PH003 4⟭<td>O</td></tr><tr><td><strong>Management Agent List member</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>View all Agent</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Edit All Agent</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### Agent

The following table describes what the "Agent" level can do. At this level, the "Agent Administrator" or "Agent Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Agent Administrator </th><th>Agent Collaborator</th><th>Agent User</th></tr></thead><tbody><tr><td><strong>Description</strong></td><td>has a complete Agent Control right </td><td> can help manage the use and content adjustment of Agent </td><td> Can only use Agent in the workspace The role of </td></tr><tr><td><strong> is used in the workspace Agent</strong></td><td>O</td><td>O⟬PH00 34⟭<td>O</td></tr><tr><td><strong>at Agent list view Agent</strong></td><td>O</td><td>O⟬PH004 6⟭<td>X</td></tr><tr><td><strong>Management Agent Member</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Edit Agent</strong></td><td>O</td><td>O⟬PH007 0⟭<td>X</td></tr><tr><td><strong>Delete Agent</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

## Knowledge base list function permissions

### Knowledge base list

The following table describes what can be done at the Knowledge Base Inventory level. You can think of the "Knowledge Base List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>KB List Administrator</th><th>KB List Collaborator</th> <th>Knowledge Base List Users</th></tr></thead>⟬PH00 13⟭<tr><td><strong>Description</strong></td> <td>A role that can operate the knowledge base and all functions of knowledge </td><td>A role that is given permission to assist in the management of knowledge base members </td><td>A role that can create and edit its own knowledge</td></tr><tr><td><strong>Build Knowledge⟬P H0029⟭</td><td>O</td><td>O⟬PH00 34⟭<td>O</td></tr><tr><td><strong>Manage Knowledge Base Members</strong></td><td>O⟬PH004 4⟭<td>O</td><td>X</td></tr><tr><td><strong>View all knowledge</strong></td> <td>O</td><td>X</td><td>X⟬P H0060⟭</tr><tr><td><strong>Edit all knowledge</strong></td><td>O</td><td>X⟬PH0 070⟭<td>X</td></tr></tbody></table>

### Knowledge

The following table describes what can be done at the "knowledge" level. At this level, "knowledge managers" or "knowledge collaborators" are usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Knowledge Manager</th><th> Knowledge Collaborator</th><th>Knowledge User</th></tr></thead><tbody><tr>⟬PH00 15⟭<strong> Description</strong></td><td>Have complete knowledge control rights</td><td>Can assist in knowledge management Content adjustment </td><td>Knowledge-only characters </td></tr><tr><td><strong> are available at Agent New knowledge</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>View knowledge in knowledge base list</strong></td><td>O</td><td>O</td><td>X</td></tr>⟬PH0 050⟭<td><strong>Management Knowledge Member</strong></td><td>O</td>⟬PH005 7 ⟭ </strong></td><td>O</td><td>O</td><td>X⟬PH007 2⟭</tr><tr><td><strong>Delete Knowledge</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

## **MCP Function Permissions**

### **MCP List**

The following table describes what can be done at the "**MCP** Checklist" level. You can think of the "**MCP** List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (125).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>MCP Inventory Administrator </th><th>MCP List of collaborators</th><th>MCP List User</th></tr></thead><tbody><tr><td><strong>Description</strong></td><td>A role that can operate the MCP inventory and all MCP functions </td><td>A role that is given the authority to assist in the management of MCP inventory members </td><td> You can create and edit your own MCP character</td></tr><tr><td><strong>Create MCP</strong></td> <td>O</td><td>O</td><td>O</td></tr><tr><td>⟬PH0 040⟭Manage MCP Members</strong></td><td>O</td><td>O</td><td>X</td> </tr><tr><td><strong>View all MCPs</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Edit all MCPs</strong>⟬PH0 066⟭<td>O</td><td>X</td><td>

### **MCP**

The following table describes what can be done at the "MCP" level. At this level, the "MCP Administrator" or "MCP Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>MCP Administrator </th><th>MCP Collaborator</th><th>MCP User</th></tr></thead><tbody><tr>⟬PH00 15⟭<strong> Description</strong></td><td>Have complete MCP control rights </td><td>can assist in managing MCP content adjustments </td><td>Read only Take the role of MCP</td></tr><tr><td><strong> available at Agent New MCP</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>View MCP</strong>⟬PH00 in MCP list 42⟭<td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Set MCP Member</strong></td><td>O</td>⟬PH00 57 ⟭X</td><td> P</strong></td><td>O</td><td>O</td><td>X⟬PH00 72⟭</tr><tr><td><strong>Delete MCP</strong></td><td>O </td><td>X</td><td>

## **Workflow Template Function Permissions**

### **Workflow Template Checklist**

The following table describes what can be done at the "Workflow Template List" level. You can think of the "Workflow Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Workflow Template Checklist Administrator</th><th>Workflow Template Checklist Collaborator</th><th>Workflow Template List Users</th></tr></thead><tbody><tr><td><strong>Description</strong></td><td>A role that can operate the workflow template list and all workflow template functions</td><td>A role that is given permission to assist in managing the workflow template list members</td><td>Can create and edit self- Role of your own workflow template</td></tr><tr><td>⟬PH00 28⟭Create a workflow template</strong></td><td>O</td>⟬PH0 033⟭O</td><td>O</td></tr><tr><td><strong>Management Workflow Member Template</strong></td>⟬PH004 3⟭O</td><td>O</td><td>X</td></tr><tr><td><strong>View all workflow templates</strong></td><td>O</td><td>X</td>⟬PH005 9⟭X</td></tr><tr><td><strong>Edit all jobs Operation process template</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### Workflow template

The following table describes what can be done at the "Workflow Template" level. At this level, "workflow template administrators" or "workflow template collaborators" are usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (128).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Workflow Process Template Administrator</th><th>Workflow Template Collaborator</th><th>Workflow Template User</th></tr></thead><tbody><tr><td>⟬P H0016⟭Description</strong></td><td>Have complete control over the workflow template</td><td>Can assist in managing the content adjustment of workflow templates </td><td>A role that can only read workflow templates </td></tr><tr><td><strong>Can use workflows in the workspace Template</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>In workflow clearing Single List View Workflow Template</strong></td><td>O</td><td>O </td><td>X</td></tr><tr><td>⟬PH0 052⟭Set Workflow Template Members</strong></td><td>O</td>⟬PH005 7⟭X</td><td>X</td></tr><tr><td>⟬P H0064⟭Edit Workflow Template</strong></td><td>O</td>⟬PH006 9⟭O</td><td>X</td></tr><tr><td><strong>Delete workflow template</strong></td><td>O</td>⟬PH0 081⟭X</td><td>X</td></tr></tbody></table>

## **Prompt Word Template Function Permission**

### **Prompt word template list**

The following table describes what can be done at the "Prompt Word Template List" level. You can think of the "Prompt Word Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Prompt Word Template List Administrator</th><th>Prompt Word Template List Collaborator</th> <th>Prompt word template list user</th></tr></thead>⟬PH00 13⟭<tr><td><strong>Description</strong></td>⟬P H0019⟭A role that can operate the prompt word template list and all functions of the prompt word template</td><td>A role that is given permission to assist in managing prompt word template list members</td><td>Can create and edit their own prompts The role of the indicator template</td></tr><tr><td><strong> Create prompt word template</strong></td><td>O</td><td>O</td><td>O</td></tr><tr>⟬PH0 039⟭<strong>Manage prompt word list template members</strong></td><td> O</td><td>O</td><td>X</td>⟬PH0 049⟭<tr><td><strong>View all prompt word templates</strong>⟬P H0054⟭<td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Edit all mentions Signal word template</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### prompt word template

The following table describes what can be done at the "prompt word template" level. At this level, the "prompt word template administrator" or "prompt word template collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Character</th><th>Tips Word Template Administrator</th><th>Prompt Word Template Collaborator</th><th>Prompt Word Template Use User</th></tr></thead><tbody><tr><td>⟬P H0016⟭ Description</strong></td><td>Have complete control over the prompt word template</td> <td> can assist in managing the content adjustment of prompt word templates </td><td>A role that can only read prompt word templates </td></tr><tr><td><strong>can use prompt word templates in the workspace </strong></td><td>O</td><td>O</td>⟬P H0035⟭O</td></tr><tr><td><strong> in prompt word list List view prompt words</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td>⟬PH005 2⟭Set prompt word template members</strong></td><td>O</td><td> X</td><td> 0064⟭Edit prompt word template</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Delete prompt word template</strong></td><td>O</td>⟬PH00 81⟭X</td><td>X</td></tr></tbody></table>
