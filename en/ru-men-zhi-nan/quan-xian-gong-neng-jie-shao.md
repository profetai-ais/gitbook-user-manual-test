---
description: This function provides two-level permission control to help you flexibly set "who can access a specific function list" and "who can operate a single item in it."
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

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Create Agent</th><th>Manage Agent List Members</th><th>View All agents Fully functional roles</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Agent List collaborators</strong></td><td> are given permission to assist in managing Agents Role of List Member</td><td>O</td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Agent List users</strong></td><td> can create and edit their own Agents The role of </td><td>O</td><td>X</td><td>X</td><td>

### Agent

The following table describes what the "Agent" level can do. At this level, the "Agent Administrator" or "Agent Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Use Agent in Workspace</th><th>View Agent in Agent List</th><th>Manage Agent Member</th><th>Edit Agent</th><th>Delete Agent</th></tr></thead><tbody><tr><td><strong>Agent Administrator</strong></td><td>has a complete Agent Control</td><td>O</td><td>O</td><td>O</td>⟦3 3⟧O</td><td>O</td></tr><tr><td><strong>Agent Collaborators</strong></td><td> can assist in managing Agent Use and content adjustment</td><td>O</td><td>O</td><td>O</td> <td>O</td><td>X</td></tr><tr><td><strong>Agent User </strong></td><td> can only use Agent in the workspace The role of</td><td>O</td><td>X</td><td>X⟦6 8⟧<td>X</td><td>X</td></tr></tbody></table>



## Knowledge base list function permissions

### Knowledge base list

The following table describes what can be done at the Knowledge Base Inventory level. You can think of the "Knowledge Base List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Build Knowledge</th><th>Manage Knowledge Base Members⟦ 10⟧<th>View all knowledge</th><th>Edit all knowledge</th></tr></thead><tbody><tr> <td><strong>Knowledge base inventory administrator</strong></td><td>The role that can operate all functions of the knowledge base and knowledge⟦24 ⟧<td>O</td><td>O</td><td>O</td><td>O</td></tr><tr>⟦3 5⟧<strong>Knowledge Base Inventory Collaborators</strong></td><td>A role assigned permission to assist in managing knowledge base members⟦40 ⟧<td>O</td><td>O</td><td>X</td><td>X</td></tr><tr>⟦5 1⟧<strong>Knowledge base list user</strong></td><td>A role that can create and edit their own knowledge</td>⟦ 57⟧O</td><td>X</td><td>X</td><td>

### Knowledge

The following table describes what can be done at the "knowledge" level. At this level, "knowledge managers" or "knowledge collaborators" are usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Character </th><th>Description </th><th>Available in Agent New knowledge</th><th>View knowledge in knowledge base list</th><th>Manage knowledge members</th><th>Edit Knowledge</th><th>Delete Knowledge</th></tr></thead><tbody><tr><td><strong>Knowledge Management Administrator </strong></td><td>has complete knowledge control </td><td>O</td><td>O⟦30 ⟧<td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Know Knowledge collaborators</strong></td><td> can assist in the content adjustment of management knowledge</td><td>O</td><td> O</td><td>X</td><td>O</td><td> 58⟧Knowledge Users</strong></td><td>Characters who can only read knowledge</td><td>O</td>⟦65 ⟧X</td><td>X</td><td>X</td><td>



## **MCP Function Permissions**

### **MCP List**

The following table describes what can be done at the "**MCP** Checklist" level. You can think of the "**MCP** List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (125).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Create MCP</th><th>Manage MCP Members</th>⟦11 ⟧View all MCPs</th><th>Edit all MCPs</th></tr></thead><tbody><tr><td><strong>MCPs Inventory Administrator</strong></td><td>A role that can operate the MCP inventory and all MCP functions</td><td>O⟦2 6⟧<td>O</td><td>O</td><td>O</td></tr><tr><td><strong>MCP List collaborators</strong></td><td> are given the role of assisting in managing MCP list members</td><td>O⟦4 2⟧<td>O</td><td>X</td><td>X</td></tr><tr><td><strong>MCP List users</strong></td><td> can create and edit their own MCP roles</td><td>O </td><td>X</td><td>X</td><td>

### **MCP**

The following table describes what can be done at the "MCP" level. At this level, the "MCP Administrator" or "MCP Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Character </th><th>Description </th><th>Available in Agent Added MCP</th><th>View MCP</th><th> in MCP list and set MCP members</th><th>edit Edit MCP</th><th>Delete MCP</th></tr></thead><tbody><tr><td><strong>MCP Administrators</strong></td><td>have full MCP control</td><td>O</td><td>O⟦30 ⟧<td>O</td><td>O</td><td>O</td></tr><tr><td><strong>MCP Collaborators </strong></td><td> can help manage content adjustments for MCP </td><td>O</td><td>O⟦4 8⟧<td> User</strong></td><td>can only read MCP characters</td><td>O</td><td>X </td><td>X</td><td>X</td><td>



## **Workflow Template Function Permissions**

### **Workflow Template Checklist**

The following table describes what can be done at the "Workflow Template List" level. You can think of the "Workflow Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Create workflow template</th><th>Manage workflow member template Board</th><th>View all workflow templates</th><th>Edit all workflow templates</th></tr></thead>⟦17 ⟧<tr><td><strong>Workflow Template List Administrator</strong></td><td>Operationable Workflow Template List and Workflow Characters with all template functions</td><td>O</td><td>O</td><td>O</td><td>O</td>⟦33 ⟧<tr><td><strong>Workflow template checklist collaborators</strong></td><td> are given permission to assist in managing workflow template checklist Single-member roles</td><td>O</td><td>O</td><td>X</td><td>X</td></tr>⟦5 0⟧<td><strong>Workflow template list. Users</strong></td><td> can create and edit their own workflow templates. Color</td><td>O</td><td>X</td><td>X</td><td>

### Workflow template

The following table describes what can be done at the "Workflow Template" level. At this level, a "workflow template administrator" or a "workflow template collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (128).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Workflow templates are available in the workspace</th><th>In the workflow list List View Workflow Template</th><th>Set Workflow Template Members</th><th>Edit Workflow Template</th><th>Delete Mention Workflow Template</th></tr></thead><tbody><tr><td><strong>Workflow Template Administrator</strong></td><td> Have complete control over workflow templates</td><td>O</td><td>O</td><td>O</td><td>O</td>⟦ 35⟧O</td></tr><tr><td><strong>Workflow template collaborators</strong></td><td> can assist in managing workflow templates Board content adjustment</td><td>O</td><td>O</td><td>X</td><td>O</td><td>X</td> </tr><tr><td><strong>Workflow template user </strong></td><td>A role that can only read the workflow template </td>⟦ 63⟧O</td><td>X</td><td>X</td><td>X</td><td>



## **Prompt Word Template Function Permission**

### **Prompt word template list**

The following table describes what can be done at the "Prompt Word Template List" level. You can think of the "Prompt Word Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Create Prompt Word Template</th><th>Manage Prompt Word List Template Member</th><th>View all prompt word templates</th><th>Edit all prompt word templates</th></tr></thead>⟦17 ⟧<tr><td><strong>Prompt word template list administrator</strong></td><td>Operable prompt word template list and prompt word template Fully functional characters</td><td>O</td><td>O</td><td>O</td><td>O</td></tr> <tr><td><strong>Prompt word template list collaborators </strong></td><td> are given permission to assist in managing the prompt word template list. Role of Member</td><td>O</td><td>O</td><td>X</td><td>X</td></tr>⟦50 ⟧<td><strong>Prompt word template list users</strong></td><td>A role that can create and edit their own prompt word templates⟦ 56⟧<td>O</td><td>X</td><td>X</td><td>

### prompt word template

The following table describes what can be done at the "prompt word template" level. At this level, the "prompt word template administrator" or "prompt word template collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>The prompt word template can be used in the workspace </th><th>In the prompt word list List view prompt words</th><th>Set prompt word template members</th><th>Edit prompt word template</th><th>Delete prompt word template Board</th></tr></thead><tbody><tr><td><strong>Prompt Word Template Administrator</strong></td><td>Has Complete Prompt word template control rights</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O </td></tr><tr><td><strong>Prompt word template collaborators</strong></td><td> can help manage the content of the prompt word template Adjust </td><td>O</td><td>O</td><td>X</td><td>O</td><td>X</td>⟦5 5⟧<tr><td><strong>Prompt word template user</strong></td><td>The role that can only read the prompt word template</td>⟦63 ⟧O</td><td>X</td><td>X</td><td>X</td><td>
