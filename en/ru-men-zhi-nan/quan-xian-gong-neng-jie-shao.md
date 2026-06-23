---
description: >-
  This function provides two-level permission control to help you flexibly set
  "who can access a specific function list" and "who can operate a single item
  in it."
---

# Introduction to permission functions

***

## Introduction to permission functions

### Permission structure

The first level: Function level (Feature/Function) is used to manage the use and management permissions of "a certain type of function", such as Agent list, knowledge base list, template list, etc. This layer determines whether you can enter the function, whether you can create a new project, whether you can manage the member list of the function, etc.

The second level: Project level (Item) is used to manage the permissions of "each individual project" within the function, such as an Agent, a knowledge base, and a template. This layer allows you to set member roles for a single project, deciding who can edit, who can only use, who can manage members, etc.

> Note: By default, only roles with administrative rights can enter the corresponding functions and perform management operations. If you cannot see certain functions or perform operations, please confirm with the administrator whether your permissions at the "function level" and "project level" have been authorized.

### **Agent function permission**

#### **Agent List**

The following table describes what can be done at the "Agent List" level. You can think of the "Agent List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th width="183">Role</th><th>Agent list manager</th><th>Agent list collaborator</th><th>Agent list user</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>Roles that can operate the Agent list and all Agent functions</td><td>Role given permission to assist in managing Agent inventory members</td><td>You can create and edit your own Agent role</td></tr><tr><td><strong>Create Agent</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Manage Agent List Members</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>View all Agents</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Edit all agents</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

#### Agent

The following table describes what the "Agent" level can do. At this level, the "Agent Administrator" or "Agent Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Agent administrator</th><th>Agent collaborator</th><th>Agent user</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>Have full Agent control</td><td>Can assist in managing Agent usage and content adjustment</td><td>Only Agent roles can be used in the workspace</td></tr><tr><td><strong>Using Agent in Workspace</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>View Agent in Agent List</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Manage Agent Members</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Edit Agent</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Delete Agent</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### Knowledge base list function permissions

#### Knowledge Base List

The following table describes what can be done at the Knowledge Base Inventory level. You can think of the "Knowledge Base List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (113).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Knowledge Base List Manager</th><th>Knowledge Base List Collaborators</th><th>Knowledge Base List Users</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>Roles that can operate the knowledge base and all functions of knowledge</td><td>A role assigned the authority to assist in the management of knowledge base members</td><td>Characters who can create and edit their own knowledge</td></tr><tr><td><strong>build knowledge</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Manage knowledge base members</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>View all knowledge</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Edit all knowledge</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

#### Knowledge

The following table describes what can be done at the "knowledge" level. At this level, "knowledge managers" or "knowledge collaborators" are usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>knowledge manager</th><th>knowledge collaborator</th><th>knowledge user</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>Have complete knowledge control</td><td>Content adjustments to assist in knowledge management</td><td>Characters who can only read knowledge</td></tr><tr><td><strong>New knowledge can be added to Agent</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>View knowledge in the knowledge base list</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Manage knowledge members</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Editorial knowledge</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>delete knowledge</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

#### **Knowledge Dataset**

By assigning users, groups, or organizations to a dataset, administrators can control which users can use the dataset in other functions, such as proxy settings, testing, or other knowledge-based functions.

After you save the permission settings, selected users, groups, or organizations will be able to access and use the dataset in supported features.

<figure><img src="../.gitbook/assets/image (286).png" alt=""><figcaption></figcaption></figure>

### **Skill Function Permission**

#### **Skill List**

The following table describes what can be done at the "**Skills** List" level. You can think of the "**Skills** List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (283).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Skills List Manager</th><th>Skills List Collaborators</th><th>Skill List User</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>A role with a list of operable skills and all functions of the skills</td><td>Roles given permission to assist in managing skill inventory members</td><td>You can create and edit characters with your own skills</td></tr><tr><td><strong>Build skills</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Management skills members</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>View all skills</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Edit all skills</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

#### **Skill**

The following table describes what can be done at the "MCP" level. At this level, the "MCP Administrator" or "MCP Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (285).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Skills Administrator</th><th>Skills Collaborator</th><th>Skill user</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>Have full skill control</td><td>Content adjustments to assist management skills</td><td>Characters who can only read skills</td></tr><tr><td><strong>New skills can be added to Agent</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>View skills in the Skills Inventory</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Set skill members</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Editing skills</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Delete skills</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### **MCP Function Permissions**

#### **MCP List**

The following table describes what can be done at the "**MCP** Checklist" level. You can think of the "**MCP** List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (115).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>MCP inventory manager</th><th>MCP manifest collaborator</th><th>MCP list user</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>Roles that can operate the MCP list and all MCP functions</td><td>Role assigned the authority to assist in managing MCP inventory members</td><td>You can create and edit your own MCP character</td></tr><tr><td><strong>Create MCP</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Manage MCP members</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>View all MCPs</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Edit all MCPs</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

#### **MCP**

The following table describes what can be done at the "MCP" level. At this level, the "MCP Administrator" or "MCP Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (116).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>MCP Administrator</th><th>MCP collaborator</th><th>MCP user</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>Have complete control of MCP</td><td>Can assist in managing MCP content adjustments</td><td>Only MCP characters can be read</td></tr><tr><td><strong>You can add an MCP to the Agent</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>View MCP in MCP list</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Set MCP members</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Edit MCP</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Delete MCP</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

#### MCP tools

By assigning users, groups, or organizations to a tool, administrators can control which users can use the tool in other functions, such as proxy settings, testing, or other tool-based features.

After you save permission settings, selected users, groups, or organizations will be able to access and use the tool within supported features.

<figure><img src="../.gitbook/assets/image (287).png" alt=""><figcaption></figcaption></figure>

### **Workflow Template Function Permissions**

#### **Workflow Template Checklist**

The following table describes what can be done at the "Workflow Template List" level. You can think of the "Workflow Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (117).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Workflow Template Checklist Manager</th><th>Workflow template checklist collaborators</th><th>Workflow template list users</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>List of operational workflow templates and roles of all workflow template functions</td><td>Role assigned to members who have permission to assist in managing workflow template inventory</td><td>Roles that can create and edit their own workflow templates</td></tr><tr><td><strong>Create workflow templates</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Management workflow member template</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>View all workflow templates</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Edit all workflow templates</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

#### Workflow template

The following table describes what can be done at the "Workflow Template" level. At this level, "workflow template administrators" or "workflow template collaborators" are usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (118).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Workflow template manager</th><th>Workflow template collaborators</th><th>Workflow template user</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>Have complete control over workflow templates</td><td>Can assist in managing content adjustments to workflow templates</td><td>Roles that can only read workflow templates</td></tr><tr><td><strong>Workflow templates available in workspaces</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>View workflow templates in the workflow list</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Set up workflow template members</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯工作流程模板</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Delete workflow template</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### **Prompt Word Template Function Permission**

#### **Prompt word template list**

The following table describes what can be done at the "Prompt Word Template List" level. You can think of the "Prompt Word Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (119).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Prompt word template list manager</th><th>Prompt Word Template Checklist Collaborators</th><th>Prompt word template list user</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>List of operable prompt word templates and roles of all functions of prompt word templates</td><td>Role assigned to members who have the authority to assist in managing prompt word template lists</td><td>Characters who can create and edit their own prompt word templates</td></tr><tr><td><strong>Create prompt word template</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Manage Prompt Word List Template Members</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>View all prompt word templates</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Edit all prompt word templates</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

#### prompt word template

The following table describes what can be done at the "prompt word template" level. At this level, the "prompt word template administrator" or "prompt word template collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (120).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Prompt word template manager</th><th>Prompt Word Template Collaborator</th><th>Prompt word template user</th></tr></thead><tbody><tr><td><strong>illustrate</strong></td><td>Have complete control over prompt word templates</td><td>Can assist in managing the content adjustment of prompt word templates</td><td>Only roles that can read prompt word templates</td></tr><tr><td><strong>Prompt word templates available in workspaces</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>View cue words in the cue word list</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Set prompt word template members</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Edit Prompt Word Template</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Delete prompt word template</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

## Model Function Permissions

The table below describes what each role can do at the model level. This layer is usually managed by Model Admins, who assign the appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (284).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Role</th><th>Model Collaborator</th><th>Model User</th></tr></thead><tbody><tr><td><strong>Description</strong></td><td>Role that can access models from the model list and use the model</td><td>Can only use models</td></tr><tr><td><strong>Use models in Agents within the workspace</strong></td><td>O</td><td>O</td></tr><tr><td><strong>Select models from the model list</strong></td><td>O</td><td>X</td></tr></tbody></table>
