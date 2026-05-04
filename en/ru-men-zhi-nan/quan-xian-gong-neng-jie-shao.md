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

<table data-full-width="true"><thead><tr><th> Role</th><th>Description</th><th>Creation Agent</th><th>Manage Agent List Members</th><th>View All Agent</th><th>Edit All Agent</th></tr></thead><tbody><tr><td><strong>Agent List Administrator </strong></td><td> Operational Agent List and Agent Fully functional roles EHOLDER30QXZ<td>O</td></tr><tr><td><strong>Agent List collaborator </strong></td><td> is granted permission to assist in managing Agent Roles of list members EHOLDER46QXZ<td>X</td></tr><tr><td><strong>Agent List user </strong></td><td> can create and edit their own Agent The role of </td><td>O</td><td>X</td>ZXQPLACEHOLDER61Q XZX</td><td>X</td></tr></tbody></table>

### Agent

The following table describes what the "Agent" level can do. At this level, the "Agent Administrator" or "Agent Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th> Role </th><th> Description </th><th> used in workspace Agent</th><th>View in Agent List Agent</th><th>Manage Agent Member</th><th>Edit Agent</th><th>Delete Agent</th></tr></thead><tbody><tr><td><strong>Agent Administrator </strong></td><td> has a complete Agent Control </td><td>O</td><td>O</td><td>O</td>ZXQPLACEHO LDER33QXZO</td><td>O</td></tr><tr><td><strong>Agent Collaborator </strong></td><td> can assist in managing Agent Use and content adjustment of </td><td>O</td><td>O</td><td>O</td>ZXQPLAC EHOLDER51QXZO</td><td>X</td></tr><tr><td><strong>Agent User </strong></td><td> can only use Agent in the workspace The role of </td><td>O</td><td>X</td><td>XZXQPLACEHOLDER68Q XZ<td>X</td><td>X</td></tr></tbody></table>



## Knowledge base list function permissions

### Knowledge Base List

The following table describes what can be done at the Knowledge Base Inventory level. You can think of the "Knowledge Base List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Description</th><th>Build Knowledge</th>ZXQP LACEHOLDER9QXZManage knowledge base members</th><th>View all knowledge</th><th>Edit all knowledge</th></tr></thead>ZXQPLACE HOLDER17QXZ<tr><td><strong>Knowledge Base List AdministratorZXQPLACEHOL DER21QXZ</td><td>The role that can operate the knowledge base and all functions of knowledge</td>ZXQPLA CEHOLDER25QXZO</td><td>O</td>ZXQPLACEHOLDER2 9QXZO</td><td>O</td></tr>ZXQPLA CEHOLDER34QXZ<td><strong>Knowledge Base List Collaborators</strong>ZXQPLACEH OLDER38QXZ<td> has been given the role </td><td>OZX with permission to assist in managing knowledge base members. QPLACEHOLDER42QXZ<td>O</td><td>XZXQPLACEHOL DER46QXZ<td>X</td></tr><tr>ZX QPLACEHOLDER51QXZ<strong>Knowledge Base List User</strong></td>ZXQPL ACEHOLDER55QXZ can create and edit characters with their own knowledge </td><td>OZXQPLACEHOLDER58QX Z<td>X</td><td>X</td>ZXQPLACE HOLDER63QXZX</td></tr></tbody></table>

### Knowledge

The following table describes what can be done at the "knowledge" level. At this level, "knowledge managers" or "knowledge collaborators" are usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th> Role </th><th> Description </th><th> is available on Agent Add new knowledge </th><th>View knowledge in the knowledge base list</th><th>Manage knowledge members</th><th>Edit knowledge</th>ZXQPLACEHOLDER15Q XZ Delete Knowledge </th></tr></thead><tbody><tr><td><strong> Knowledge Manager </strong>ZXQPLACEH OLDER24QXZ<td> has complete knowledge control </td><td>OZXQPLACE HOLDER28QXZ<td>O</td><td>OZXQPLACEHOLDER32 QXZ<td>O</td><td>O</td>ZXQPL ACEHOLDER37QXZ<tr><td><strong>Knowledge CollaboratorZXQPLACEHOL DER41QXZ</td><td> can assist in the content adjustment of management knowledge</td>ZXQPLACEH OLDER45QXZO</td><td>O</td>ZXQPLACEHOLDER49Q XZX</td><td>O</td><td>XZXQPL ACEHOLDER54QXZ</tr><tr><td>ZXQPLACEHOLDER58 QXZKnowledge user</strong></td><td>Character who can only read knowledgeZXQPLACEHOLD ER62QXZ<td>O</td><td>X</td>Z XQPLACEHOLDER67QXZX</td><td>X</td>ZXQPLACEH OLDER71QXZX</td></tr></tbody></table>



## **MCP Function Permissions**

### **MCP List**

The following table describes what can be done at the "**MCP** Checklist" level. You can think of the "**MCP** List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (125).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th> role</th>ZXQPLACEHOLDE R5QXZ Description </th><th> Create MCP</th><th>Manage MCP member ZXQPLACEHOLDER1 0QXZ<th>View all MCP</th><th>Edit all MCP</th>ZXQPLACEHOL DER15QXZ</thead><tbody><tr><td><strong>MCP List administrator </strong></td><td> is a role that can operate the MCP list and all functions of the MCP </td><td>O</td><td>OZXQPLACE HOLDER28QXZ<td>O</td><td>O</td></tr><tr><td><strong>MCP Manifest collaborator </strong></td><td> is given the role of </td><td>O</td><td>ZXQPLACE with permission to assist in managing MCP manifest members. HOLDER44QXZ<td>X</td><td>X</td></tr><tr><td><strong>MCP List user </strong></td><td> can create and edit his own MCP role </td><td>O</td>ZXQPLACEHOLDER59QX ZX</td><td>X</td><td>X</td></tr></tbody></table>

### **MCP**

The following table describes what can be done at the "MCP" level. At this level, the "MCP Administrator" or "MCP Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th> Role </th><th> Description </th><th> is available on Agent Added MCP</th><th> in MCP listView MCP</th><th>Set MCP members</th><th>Edit MCPZXQPLACEHOLDER14QX Z<th> Delete MCP Administrator </strong></td><td> has full MCP control </td>Z XQPLACEHOLDER27QXZO</td><td>O</td>ZXQPLACEHOLDER 31QXZO</td><td>O</td><td>OZXQPLAC EHOLDER36QXZ</tr><tr><td><strong>MCP Collaborator </strong></td><td> can help manage content adjustments for MCP ZXQPLACEHOLDER44QX Z<td>O</td><td>O</td>ZXQPLACEHOLDE R49QXZX</td><td>O</td><td>XZXQPLA CEHOLDER54QXZ</tr><tr><td><strong>MCP User </strong></td><td> can only read the MCP role ZXQPLACEHOLDER6 2QXZ<td>O</td><td>X</td>ZXQ PLACEHOLDER67QXZX</td><td>X</td>ZXQPLACEHO LDER71QXZX</td></tr></tbody></table>



## **Workflow template function permissions**

### **Workflow Template List**

The following table describes what can be done at the "Workflow Template List" level. You can think of the "Workflow Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th> roleZXQPLACEHOLDER4 QXZ<th>Instructions</th><th>Create workflow template</th>ZXQPL ACEHOLDER9QXZManage workflow member templates</th><th>View all workflow templatesZXQPLACEHOLDER12QX Z<th>Edit all workflow templates</th></tr></thead>ZXQ PLACEHOLDER17QXZ<tr><td><strong>Workflow template list administrator</strong></td><td>Role of operational workflow template list and workflow full template functionZXQPLACEHOLDE R24QXZ<td>O</td><td>O</td>ZXQPLA CEHOLDER29QXZO</td><td>O</td>ZXQPLACEHOLDER33QX Z<tr><td><strong>Workflow Template ChecklistCollaborator</strong>Z XQPLACEHOLDER38QXZ<td> is given the role of </td>ZXQPLACEHOLD with permission to assist in managing workflow template inventory members ER41QXZO</td><td>O</td><td>XZXQP LACEHOLDER46QXZ<td>X</td></tr>ZXQPLACEHOLDER50Q XZ<td><strong>Workflow template list user</strong></td>Z XQPLACEHOLDER55QXZA role that can create and edit its own workflow template</td><td>OZXQPLACEHOLDE R58QXZ<td>X</td><td>X</td>ZXQPLA CEHOLDER63QXZX</td></tr></tbody></table>

### Workflow template

The following table describes what can be done at the "Workflow Template" level. At this level, "workflow template administrators" or "workflow template collaborators" are usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (128).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th> role</th>ZXQPLA CEHOLDER5QXZ Description</th><th> Workflow template </th>ZXQPLACEHOLDER9QX can be used in the workspace View the workflow template </th><th> in the workflow list and set the workflow template member </th>ZXQPLACEHOLDER 13QXZEdit workflow template </th><th>Delete and submit workflow template </th></tr>Z XQPLACEHOLDER18QXZ<tbody><tr><td><strong>Workflow Template administrator </strong></td><td> has complete control over the workflow template </td>ZXQP LACEHOLDER27QXZO</td><td>O</td><td>OZXQPL ACEHOLDER32QXZ<td>O</td><td>O</td>ZXQPLAC EHOLDER37QXZ<tr><td><strong>Workflow template collaborator</strong>Z XQPLACEHOLDER42QXZ<td> can assist in managing the content adjustment of workflow templates</td><td>OZXQPLAC EHOLDER46QXZ<td>O</td><td>X</td>ZXQPLACEH OLDER51QXZO</td><td>X</td></tr>ZXQPLACEHOL DER56QXZ<td><strong>Workflow template user</strong></td>ZXQPLA CEHOLDER61QXZ can only read the role </td><td>O</td>ZXQPLACEHOLDER6 of the workflow template 5QXZX</td><td>X</td><td>XZXQPLACEHOLDER70 QXZ<td>X</td></tr></tbody></table>



## **Prompt Word Template Function Permission**

### **Prompt word template list**

The following table describes what can be done at the "Prompt Word Template List" level. You can think of the "Prompt Word Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th> roleZXQPLACEHOLDER4 QXZ<th> Description</th><th>Create prompt word template</th>ZXQPL ACEHOLDER9QXZManage prompt word list template members</th><th>View all prompt word templatesZXQPLACEHOLDER12QX Z<th>Edit all prompt word templates</th></tr></thead>ZXQ PLACEHOLDER17QXZ<tr><td><strong>Prompt word template list administratorZXQPLA CEHOLDER21QXZ</td><td>The role of the list of operable prompt word templates and the full function of the prompt word templateZXQPLACEHOLDER2 4QXZ<td>O</td><td>O</td>ZXQPLAC EHOLDER29QXZO</td><td>O</td></tr> <tr><td><strong> prompt word template list collaborator </strong>ZXQ PLACEHOLDER38QXZ<td> is given the role of </td>ZXQPLACEHOLDER with permission to assist in managing prompt word template list members 41QXZO</td><td>O</td><td>XZXQPL ACEHOLDER46QXZ<td>X</td></tr>ZXQPLACEHOLDER50QX Z<td><strong> prompt word template list user </strong></td>ZX QPLACEHOLDER55QXZ can create and edit its own prompt word template character </td><td>OZXQPLACEHOLDER 58QXZ<td>X</td><td>X</td>ZXQPLA CEHOLDER63QXZX</td></tr></tbody></table>

### Prompt word template

The following table describes what can be done at the "prompt word template" level. At this level, the "prompt word template administrator" or "prompt word template collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th> role</th>ZXQPL ACEHOLDER5QXZ Description</th><th>You can use the prompt word template </th>ZXQPLACEHOLDER9Q in the workspace XZ View the prompt word </th><th> in the prompt word list list and set the prompt word template member </th>ZXQPLACEHOLDER13Q XZ edit prompt word template </th><th> delete prompt word template </th></tr>ZXQPLA CEHOLDER18QXZ<tbody><tr><td><strong>Prompt word template administrator Z XQPLACEHOLDER23QXZ</td><td> has complete control over the prompt word template</td>ZXQPLACEHO LDER27QXZO</td><td>O</td><td>OZXQPLACEHO LDER32QXZ<td>O</td><td>O</td>ZXQPLACEHOL DER37QXZ<tr><td><strong> prompt word template collaborator </strong>ZXQPL ACEHOLDER42QXZ<td> can assist in managing the content adjustment of prompt word templates</td><td>OZXQPLACEHOL DER46QXZ<td>O</td><td>X</td>ZXQPLACEHOLD ER51QXZO</td><td>X</td></tr>ZXQPLACEHOLDE R56QXZ<td><strong> prompt word template user </strong></td>ZXQPLACE HOLDER61QXZ can only read the role of prompt word template </td><td>O</td>ZXQPLACEHOLDER65Q XZX</td><td>X</td><td>XZXQPLACEHOLDER70Q XZ<td>X</td></tr></tbody></table>
