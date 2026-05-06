---
description: >-
  This feature provides a two-level permission model, helping you flexibly
  control who can access specific feature libraries and who can manage
  individual items within them.
---

# Introduction to permission functions

## Permission Structure

**Level 1: Feature Level (Feature / Library)**

This level manages access and administrative permissions for a category of features, such as the Agent Library, Knowledge Base Library, Workflow Template Library, and more. It determines whether you can enter the feature, create new items, and manage the member list for that feature library.

**Level 2: Item Level (Item)**

This level manages permissions for each individual item within a feature, such as a specific Agent, Knowledge Base, or Workflow Template. It allows you to assign roles per item, deciding who can edit, who can only use it, and who can manage members.

> Note: By default, only roles with management permissions can access the corresponding feature and perform management actions. If you cannot see certain features or cannot perform specific actions, please check with your Admin to confirm whether you have been granted permissions at both the **feature level** and the **item level**.

## **Agent Feature Permissions**

### **Agent List**

The table below describes what actions can be performed at the **Agent List** level. You can think of the **Agent List** as a management scope: whether you can create items, manage members, or view/edit all items depends on the role assigned to you in this feature list.

<figure><img src="../.gitbook/assets/image (121).png" alt=""><figcaption></figcaption></figure>

| Role                        | Description                                                                 | Create Agent | Manage Agent List Members | View All Agents | Edit All Agents |
| --------------------------- | --------------------------------------------------------------------------- | ------------ | ------------------------- | --------------- | --------------- |
| **Agent List Admin**        | A role with full access to all functions in both the Agent List and Agents. | O            | O                         | O               | O               |
| **Agent List Collaborator** | A role granted permission to help manage members in the Agent List.         | O            | O                         | X               | X               |
| **Agent List User**         | A role that can create and edit their own Agents.                           | O            | X                         | X               | X               |

### Agent

The table below describes what actions can be performed at the **Agent** level. This level is typically managed by the **Agent Admin** or **Agent Collaborator**, who are responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>

| Role                   | Description                                               | Use Agent in Workspace | View Agent in Agent List | Manage Agent Members | Edit Agent |   |
| ---------------------- | --------------------------------------------------------- | ---------------------- | ------------------------ | -------------------- | ---------- | - |
| **Agent Admin**        | Has full control over the Agent.                          | O                      | O                        | O                    | O          | O |
| **Agent Collaborator** | Can help manage Agent usage and make content adjustments. | O                      | O                        | O                    | O          | X |
| **Agent User**         | A role that can only use the Agent in the workspace.      | O                      | X                        | X                    | X          | X |

## **Knowledge Base List Permissions**

### **Knowledge Base List**

The table below describes what actions can be performed at the **Knowledge Base List** level. You can think of the **Knowledge Base List** as a management scope: whether you can create items, manage members, or view/edit all items depends on the role assigned to you in this feature list.

<figure><img src="../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>

| Role                                 | Description                                                                             | Create Knowledge | Manage Knowledge Base Members | View All Knowledge | Edit All Knowledge |
| ------------------------------------ | --------------------------------------------------------------------------------------- | ---------------- | ----------------------------- | ------------------ | ------------------ |
| **Knowledge Base List Admin**        | A role with full access to all functions in both the Knowledge Base List and Knowledge. | O                | O                             | O                  | O                  |
| **Knowledge Base List Collaborator** | A role granted permission to help manage members in the Knowledge Base List.            | O                | O                             | X                  | X                  |
| **Knowledge Base List User**         | A role that can create and edit their own Knowledge.                                    | O                | X                             | X                  | X                  |

### Knowledge

The table below describes what actions can be performed at the **Knowledge** level. This level is typically managed by the **Knowledge Admin** or **Knowledge Collaborator**, who are responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>

| Role                       | Description                                   | Add Knowledge to Agent | View Knowledge in Knowledge Base List | Manage Knowledge Members | Edit Knowledge |   |
| -------------------------- | --------------------------------------------- | ---------------------- | ------------------------------------- | ------------------------ | -------------- | - |
| **Knowledge Admin**        | Has full control over the Knowledge.          | O                      | O                                     | O                        | O              | O |
| **Knowledge Collaborator** | Can help manage and update Knowledge content. | O                      | O                                     | X                        | O              | X |
| **Knowledge User**         | A role that can only read the Knowledge.      | O                      | X                                     | X                        | X              | X |

## **MCP Permissions**

### **MCP List**

The table below describes what actions can be performed at the **MCP List** level. You can think of the **MCP List** as a management scope: whether you can create items, manage members, or view/edit all items depends on the role assigned to you in this feature list.

<figure><img src="../.gitbook/assets/image (125).png" alt=""><figcaption></figcaption></figure>

| Role                      | Description                                                             | Create MCP | Manage MCP Members | View All MCPs | Edit All MCPs |
| ------------------------- | ----------------------------------------------------------------------- | ---------- | ------------------ | ------------- | ------------- |
| **MCP List Admin**        | A role with full access to all functions in both the MCP List and MCPs. | O          | O                  | O             | O             |
| **MCP List Collaborator** | A role granted permission to help manage members in the MCP List.       | O          | O                  | X             | X             |
| **MCP List User**         | A role that can create and edit their own MCPs.                         | O          | X                  | X             | X             |

### **MCP**

The table below describes what actions can be performed at the **MCP** level. This level is typically managed by the **MCP Admin** or **MCP Collaborator**, who are responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

| Role                 | Description                             | Add MCP to Agent | View MCP in MCP List | Manage MCP Members | Edit MCP |   |
| -------------------- | --------------------------------------- | ---------------- | -------------------- | ------------------ | -------- | - |
| **MCP Admin**        | Has full control over the MCP.          | O                | O                    | O                  | O        | O |
| **MCP Collaborator** | Can help manage and update MCP content. | O                | O                    | X                  | O        | X |
| **MCP User**         | A role that can only read the MCP.      | O                | O                    | X                  | O        | X |

## **Workflow Template Permissions**

### **Workflow Template List**

The table below describes what actions can be performed at the **Workflow Template List** level. You can think of the **Workflow Template List** as a management scope: whether you can create items, manage members, or view/edit all items depends on the role assigned to you in this feature list.

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

| Role                                    | Description                                                                                         | Create Workflow Template | Manage Workflow Template Members | View All Workflow Templates | Edit All Workflow Templates |
| --------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------ | -------------------------------- | --------------------------- | --------------------------- |
| **Workflow Template List Admin**        | A role with full access to all functions in both the Workflow Template List and Workflow Templates. | O                        | O                                | O                           | O                           |
| **Workflow Template List Collaborator** | A role granted permission to help manage members in the Workflow Template List.                     | O                        | O                                | X                           | X                           |
| **Workflow Template List User**         | A role that can create and edit their own Workflow Templates.                                       | O                        | X                                | X                           | X                           |

### Workflow Template

The table below describes what actions can be performed at the **Workflow Template** level. This level is typically managed by the **Workflow Template Admin** or **Workflow Template Collaborator**, who are responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (128).png" alt=""><figcaption></figcaption></figure>

| Role                               | Description                                           | Use Workflow Template in Workspace | View Workflow Template in Workflow Template List | Manage Workflow Template Members | Edit Workflow Template |   |
| ---------------------------------- | ----------------------------------------------------- | ---------------------------------- | ------------------------------------------------ | -------------------------------- | ---------------------- | - |
| **Workflow Template Admin**        | Has full control over the Workflow Template.          | O                                  | O                                                | O                                | O                      | O |
| **Workflow Template Collaborator** | Can help manage and update Workflow Template content. | O                                  | O                                                | X                                | O                      | X |
| **Workflow Template User**         | A role that can only read the Workflow Template.      | O                                  | X                                                | X                                | X                      | X |

## **Prompt Template Permissions**

### **Prompt Template List**

The table below describes what actions can be performed at the **Prompt Template List** level. You can think of the **Prompt Template List** as a management scope: whether you can create items, manage members, or view/edit all items depends on the role assigned to you in this feature list.

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

| Role                                  | Description                                                                                     | Create Prompt Template | Manage Prompt Template List Members | View All Prompt Templates | Edit All Prompt Templates |
| ------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------- | ----------------------------------- | ------------------------- | ------------------------- |
| **Prompt Template List Admin**        | A role with full access to all functions in both the Prompt Template List and Prompt Templates. | O                      | O                                   | O                         | O                         |
| **Prompt Template List Collaborator** | A role granted permission to help manage members in the Prompt Template List.                   | O                      | O                                   | X                         | X                         |
| **Prompt Template List User**         | A role that can create and edit their own Prompt Templates.                                     | O                      | X                                   | X                         | X                         |

### Prompt Template

The table below describes what actions can be performed at the **Prompt Template** level. This level is typically managed by the **Prompt Template Admin** or **Prompt Template Collaborator**, who are responsible for managing members and assigning appropriate permissions to collaborators or users.

<figure><img src="../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th>Role</th><th>Description</th><th>Use Prompt Template in Workspace</th><th>View Prompt Template in Prompt Template List</th><th width="128">Manage Prompt Template Members</th><th>Edit Prompt Template</th><th></th></tr></thead><tbody><tr><td><strong>Prompt Template Admin</strong></td><td>Has full control over the Prompt Template.</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Prompt Template Collaborator</strong></td><td>Can help manage and update Prompt Template content.</td><td>O</td><td>O</td><td>X</td><td>O</td><td>X</td></tr><tr><td><strong>Prompt Template User</strong></td><td>A role that can only read the Prompt Template.</td><td>O</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>
