---
description: 本功能提供雙層級的權限控管，協助您彈性設定「誰能存取特定功能清單」以及「誰能操作裡面的單一項目」。
---

# 權限功能介紹

## 權限架構

第一層：功能層級（Feature / Function） 用來管理「某一類功能」的使用與管理權限，例如 Agent 清單、知識庫清單、模板清單....等。這一層決定你能不能進入該功能、能不能建立新項目、能不能管理該功能的成員名單等。

第二層：項目層級（Item） 用來管理功能內「每一個單獨項目」的權限，例如某一個 Agent、某一個知識庫、某一個模板。這一層讓你可以針對單一項目設定成員角色，決定誰能編輯、誰只能使用、誰可以管理成員等。

> 注意：預設情況下，只有具備管理權限的角色可以進入對應功能與進行管理操作。若你無法看到某些功能或無法執行操作，請向管理員確認你在「功能層級」與「項目層級」的權限是否已被授權。

## **Agent 功能權限**

### **Agent 清單**

以下表格描述的是「Agent 清單」層級可以做的事情。你可以把「Agent 清單」當成一個管理範圍：能不能建立項目、能不能管理成員、能不能檢視/編輯所有項目，取決於你在此功能清單被授予的角色。

<figure><img src="../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th width="183">角色</th><th>Agent 清單管理員</th><th>Agent 清單協作者</th><th>Agent 清單使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>可操作 Agent 清單與 Agent 全部功能的角色</td><td>被賦予權限協助管理 Agent 清單成員的角色</td><td>可建立與編輯屬於自己的 Agent 的角色</td></tr><tr><td><strong>建立 Agent</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>管理 Agent 清單成員</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>檢視所有 Agent</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯所有 Agent</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### Agent

以下表格描述的是「Agent」層級可以做的事情。這一層通常由「Agent 管理員」或「Agent 協作者」負責管理成員，將適合的權限分配給協作者或使用者。

<figure><img src="../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>Agent 管理員</th><th>Agent 協作者</th><th>Agent 使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>擁有完整的 Agent 控制權</td><td>可協助管理 Agent 的使用與內容調整</td><td>僅能在工作空間使用 Agent 的角色</td></tr><tr><td><strong>在工作空間使用 Agent</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>在 Agent 清單檢視 Agent</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>管理 Agent 成員</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>編輯 Agent</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>刪除 Agent</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

## 知識庫清單功能權限

### 知識庫清單

以下表格描述的是「知識庫清單」層級可以做的事情。你可以把「知識庫清單」當成一個管理範圍：能不能建立項目、能不能管理成員、能不能檢視/編輯所有項目，取決於你在此功能清單被授予的角色。

<figure><img src="../.gitbook/assets/image (113).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>知識庫清單管理員</th><th>知識庫清單協作者</th><th>知識庫清單使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>可操作知識庫與知識全部功能的角色</td><td>被賦予權限協助管理知識庫成員的角色</td><td>可建立與編輯屬於自己的知識的角色</td></tr><tr><td><strong>建立知識</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>管理知識庫成員</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>檢視所有知識</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯所有知識</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### 知識

以下表格描述的是「知識」層級可以做的事情。這一層通常由「知識管理員」或「知識協作者」負責管理成員，將適合的權限分配給協作者或使用者。

<figure><img src="../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>知識管理員</th><th>知識協作者</th><th>知識使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>擁有完整的知識控制權</td><td>可協助管理知識的內容調整</td><td>僅能讀取知識的角色</td></tr><tr><td><strong>可在 Agent 新增知識</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>在知識庫清單檢視知識</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>管理知識成員</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯知識</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>刪除知識</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### **知識數據集**

透過將使用者、群組或組織指派給資料集，管理員可以控制哪些使用者可以在其他功能（例如代理設定、測試或其他基於知識的功能）中使用該資料集。

儲存權限設定後，選定的使用者、群組或組織將能夠在受支援的功能中存取和使用該資料集。

<figure><img src="../.gitbook/assets/image (286).png" alt=""><figcaption></figcaption></figure>

## **技能 功能權限**

### **技能清單**

以下表格描述的是「**技能** 清單」層級可以做的事情。你可以把「**MCP** 清單」當成一個管理範圍：能不能建立項目、能不能管理成員、能不能檢視/編輯所有項目，取決於你在此功能清單被授予的角色。

<figure><img src="../.gitbook/assets/image (283).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>技能 清單管理員</th><th>技能 清單協作者</th><th>技能 清單使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>可操作技能清單與技能全部功能的角色</td><td>被賦予權限協助管理技能清單成員的角色</td><td>可建立與編輯屬於自己的技能的角色</td></tr><tr><td><strong>建立技能</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>管理技能成員</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>檢視所有技能</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯所有技能</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### **技能**

以下表格描述的是「MCP」層級可以做的事情。這一層通常由「MCP 管理員」或「MCP 協作者」負責管理成員，將適合的權限分配給協作者或使用者。

<figure><img src="../.gitbook/assets/image (285).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>技能 管理員</th><th>技能 協作者</th><th>技能 使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>擁有完整的技能控制權</td><td>可協助管理技能的內容調整</td><td>僅能讀取技能的角色</td></tr><tr><td><strong>可在 Agent 新增技能</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>在技能清單清單檢視技能</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>設定技能成員</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯技能</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>刪除技能</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

## **MCP 功能權限**

### **MCP 清單**

以下表格描述的是「**MCP** 清單」層級可以做的事情。你可以把「**MCP** 清單」當成一個管理範圍：能不能建立項目、能不能管理成員、能不能檢視/編輯所有項目，取決於你在此功能清單被授予的角色。

<figure><img src="../.gitbook/assets/image (115).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>MCP 清單管理員</th><th>MCP 清單協作者</th><th>MCP 清單使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>可操作MCP清單與MCP全部功能的角色</td><td>被賦予權限協助管理MCP清單成員的角色</td><td>可建立與編輯屬於自己的MCP的角色</td></tr><tr><td><strong>建立MCP</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>管理MCP成員</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>檢視所有MCP</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯所有MCP</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### **MCP**

以下表格描述的是「MCP」層級可以做的事情。這一層通常由「MCP 管理員」或「MCP 協作者」負責管理成員，將適合的權限分配給協作者或使用者。

<figure><img src="../.gitbook/assets/image (116).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>MCP 管理員</th><th>MCP 協作者</th><th>MCP 使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>擁有完整的MCP控制權</td><td>可協助管理MCP的內容調整</td><td>僅能讀取MCP的角色</td></tr><tr><td><strong>可在 Agent 新增MCP</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>在MCP清單清單檢視MCP</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>設定MCP成員</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯MCP</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>刪除MCP</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### MCP 工具

透過將使用者、群組或組織指派給工具，管理員可以控制哪些使用者可以在其他功能（例如代理設定、測試或其他基於工具的功能）中使用該工具。

儲存權限設定後，選定的使用者、群組或組織將能夠在受支援的功能中存取和使用該工具。

<figure><img src="../.gitbook/assets/image (287).png" alt=""><figcaption></figcaption></figure>

## **工作流程模板 功能權限**

### **工作流程模板清單**

以下表格描述的是「工作流程模板清單」層級可以做的事情。你可以把「工作流程模板清單」當成一個管理範圍：能不能建立項目、能不能管理成員、能不能檢視/編輯所有項目，取決於你在此功能清單被授予的角色。

<figure><img src="../.gitbook/assets/image (117).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>工作流程模板清單管理員</th><th>工作流程模板清單協作者</th><th>工作流程模板清單使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>可操作工作流程模板清單與工作流程全部模板功能的角色</td><td>被賦予權限協助管理工作流程模板清單成員的角色</td><td>可建立與編輯屬於自己的工作流程模板的角色</td></tr><tr><td><strong>建立工作流程模板</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>管理提工作流程成員模板</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>檢視所有工作流程模板</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯所有工作流程模板</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### 工作流程模板

以下表格描述的是「工作流程模板」層級可以做的事情。這一層通常由「工作流程模板管理員」或「工作流程模板協作者」負責管理成員，將適合的權限分配給協作者或使用者。

<figure><img src="../.gitbook/assets/image (118).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>工作流程模板管理員</th><th>工作流程模板協作者</th><th>工作流程模板使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>擁有完整的工作流程模板控制權</td><td>可協助管理工作流程模板的內容調整</td><td>僅能讀取工作流程模板的角色</td></tr><tr><td><strong>可在工作空間使用工作流程模板</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>在工作流程清單清單檢視工作流程模板</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>設定工作流程模板成員</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯工作流程模板</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>刪除提工作流程模板</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

## **提示詞模板 功能權限**

### **提示詞模板清單**

以下表格描述的是「提示詞模板清單」層級可以做的事情。你可以把「提示詞模板清單」當成一個管理範圍：能不能建立項目、能不能管理成員、能不能檢視/編輯所有項目，取決於你在此功能清單被授予的角色。

<figure><img src="../.gitbook/assets/image (119).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>提示詞模板清單管理員</th><th>提示詞模板清單協作者</th><th>提示詞模板清單使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>可操作提示詞模板清單與提示詞模板全部功能的角色</td><td>被賦予權限協助管理提示詞模板清單成員的角色</td><td>可建立與編輯屬於自己的提示詞模板的角色</td></tr><tr><td><strong>建立提示詞模板</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>管理提示詞清單模板成員</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>檢視所有提示詞模板</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯所有提示詞模板</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>

### 提示詞模板

以下表格描述的是「提示詞模板」層級可以做的事情。這一層通常由「提示詞模板管理員」或「提示詞模板協作者」負責管理成員，將適合的權限分配給協作者或使用者。

<figure><img src="../.gitbook/assets/image (120).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>提示詞模板管理員</th><th>提示詞模板協作者</th><th>提示詞模板使用者</th></tr></thead><tbody><tr><td><strong>說明</strong></td><td>擁有完整的提示詞模板控制權</td><td>可協助管理提示詞模板的內容調整</td><td>僅能讀取提示詞模板的角色</td></tr><tr><td><strong>可在工作空間使用提示詞模板</strong></td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>在提示詞清單清單檢視提示詞</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>設定提示詞模板成員</strong></td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>編輯提示詞模板</strong></td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>刪除提示詞模板</strong></td><td>O</td><td>X</td><td>X</td></tr></tbody></table>
