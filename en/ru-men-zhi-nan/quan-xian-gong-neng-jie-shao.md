---
description: "This function provides two-level permission control to help you flexibly set \"who can access a specific function list\" and \"who can operate a single item in it.\""
---
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

<table data-full-width="true"><thead><tr><th width="183">角色</th><th>Agent 清單管理員</th><th>Agent 清單協作者</th><th>Agent 清單使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>可操作 Agent 清單與 Agent 全部功能的角色</td><td>被賦予權限協助管理 Agent 清單成員的角色</td><td>可建立與編輯屬於自己的 Agent 的角色</td></tr><tr><td><strong>建立 Agent</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>管理 Agent 清單成員</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>檢視所有 Agent</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯所有 Agent</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### Agent

The following table describes what the "Agent" level can do. At this level, the "Agent Administrator" or "Agent Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>Agent 管理員</th><th>Agent 協作者</th><th>Agent 使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>擁有完整的 Agent 控制權</td><td>可協助管理 Agent 的使用與內容調整</td><td>僅能在工作空間使用 Agent 的角色</td></tr><tr><td><strong>在工作空間使用 Agent</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>在 Agent 清單檢視 Agent</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>管理 Agent 成員</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>編輯 Agent</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>刪除 Agent</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

## Knowledge base list function permissions

### Knowledge Base List

The following table describes what can be done at the Knowledge Base Inventory level. You can think of the "Knowledge Base List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>知識庫清單管理員</th><th>知識庫清單協作者</th><th>知識庫清單使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>可操作知識庫與知識全部功能的角色</td><td>被賦予權限協助管理知識庫成員的角色</td><td>可建立與編輯屬於自己的知識的角色</td></tr><tr><td><strong>建立知識</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>管理知識庫成員</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>檢視所有知識</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯所有知識</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### Knowledge

The following table describes what can be done at the "knowledge" level. At this level, "knowledge managers" or "knowledge collaborators" are usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>知識管理員</th><th>知識協作者</th><th>知識使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>擁有完整的知識控制權</td><td>可協助管理知識的內容調整</td><td>僅能讀取知識的角色</td></tr><tr><td><strong>可在 Agent 新增知識</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>在知識庫清單檢視知識</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>管理知識成員</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯知識</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>刪除知識</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

## **MCP Function Permissions**

### **MCP List**

The following table describes what can be done at the "**MCP** Checklist" level. You can think of the "**MCP** List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (125).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>MCP 清單管理員</th><th>MCP 清單協作者</th><th>MCP 清單使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>可操作MCP清單與MCP全部功能的角色</td><td>被賦予權限協助管理MCP清單成員的角色</td><td>可建立與編輯屬於自己的MCP的角色</td></tr><tr><td><strong>建立MCP</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>管理MCP成員</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>檢視所有MCP</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯所有MCP</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### **MCP**

The following table describes what can be done at the "MCP" level. At this level, the "MCP Administrator" or "MCP Collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>MCP 管理員</th><th>MCP 協作者</th><th>MCP 使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>擁有完整的MCP控制權</td><td>可協助管理MCP的內容調整</td><td>僅能讀取MCP的角色</td></tr><tr><td><strong>可在 Agent 新增MCP</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>在MCP清單清單檢視MCP</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>設定MCP成員</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯MCP</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>刪除MCP</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

## **Workflow Template Function Permissions**

### **Workflow Template Checklist**

The following table describes what can be done at the "Workflow Template List" level. You can think of the "Workflow Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>工作流程模板清單管理員</th><th>工作流程模板清單協作者</th><th>工作流程模板清單使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>可操作工作流程模板清單與工作流程全部模板功能的角色</td><td>被賦予權限協助管理工作流程模板清單成員的角色</td><td>可建立與編輯屬於自己的工作流程模板的角色</td></tr><tr><td><strong>建立工作流程模板</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>管理提工作流程成員模板</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>檢視所有工作流程模板</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯所有工作流程模板</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### Workflow template

The following table describes what can be done at the "Workflow Template" level. At this level, "workflow template administrators" or "workflow template collaborators" are usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (128).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>工作流程模板管理員</th><th>工作流程模板協作者</th><th>工作流程模板使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>擁有完整的工作流程模板控制權</td><td>可協助管理工作流程模板的內容調整</td><td>僅能讀取工作流程模板的角色</td></tr><tr><td><strong>可在工作空間使用工作流程模板</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>在工作流程清單清單檢視工作流程模板</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>設定工作流程模板成員</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯工作流程模板</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>刪除提工作流程模板</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

## **Prompt Word Template Function Permission**

### **Prompt word template list**

The following table describes what can be done at the "Prompt Word Template List" level. You can think of the "Prompt Word Template List" as a management scope: whether you can create projects, manage members, and view/edit all projects depends on the role you have been granted in this function list.

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>提示詞模板清單管理員</th><th>提示詞模板清單協作者</th><th>提示詞模板清單使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>可操作提示詞模板清單與提示詞模板全部功能的角色</td><td>被賦予權限協助管理提示詞模板清單成員的角色</td><td>可建立與編輯屬於自己的提示詞模板的角色</td></tr><tr><td><strong>建立提示詞模板</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>管理提示詞清單模板成員</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>檢視所有提示詞模板</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯所有提示詞模板</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### prompt word template

The following table describes what can be done at the "prompt word template" level. At this level, the "prompt word template administrator" or "prompt word template collaborator" is usually responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>提示詞模板管理員</th><th>提示詞模板協作者</th><th>提示詞模板使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>擁有完整的提示詞模板控制權</td><td>可協助管理提示詞模板的內容調整</td><td>僅能讀取提示詞模板的角色</td></tr><tr><td><strong>可在工作空間使用提示詞模板</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>在提示詞清單清單檢視提示詞</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>設定提示詞模板成員</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯提示詞模板</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>刪除提示詞模板</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>
