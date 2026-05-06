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

<figure><img src="../.gitbook/assets/image (121).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>說明</th><th>建立 Agent</th><th>管理 Agent 清單成員</th><th>檢視所有 Agent</th><th>編輯所有 Agent</th></tr></thead><tbody><tr><td><strong>Agent 清單管理員</strong></td><td>可操作 Agent 清單與 Agent 全部功能的角色</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Agent 清單協作者</strong></td><td>被賦予權限協助管理 Agent 清單成員的角色</td><td>O</td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>Agent 清單使用者</strong></td><td>可建立與編輯屬於自己的 Agent 的角色</td><td>O</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>

### Agent

以下表格描述的是「Agent」層級可以做的事情。這一層通常由「Agent 管理員」或「Agent 協作者」負責管理成員，將適合的權限分配給協作者或使用者。

<figure><img src="../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>說明</th><th width="96">在工作空間使用 Agent</th><th width="98">在 Agent 清單檢視 Agent</th><th width="87">管理 Agent 成員</th><th width="92">編輯 Agent</th><th>刪除 Agent</th></tr></thead><tbody><tr><td><strong>Agent 管理員</strong></td><td>擁有完整的 Agent 控制權</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>Agent 協作者</strong></td><td>可協助管理 Agent 的使用與內容調整</td><td>O</td><td>O</td><td>O</td><td>O</td><td>X</td></tr><tr><td><strong>Agent 使用者</strong></td><td>僅能在工作空間使用 Agent 的角色</td><td>O</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>

## 知識庫清單功能權限

### 知識庫清單

以下表格描述的是「知識庫清單」層級可以做的事情。你可以把「知識庫清單」當成一個管理範圍：能不能建立項目、能不能管理成員、能不能檢視/編輯所有項目，取決於你在此功能清單被授予的角色。

<figure><img src="../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>說明</th><th>建立知識</th><th>管理知識庫成員</th><th>檢視所有知識</th><th>編輯所有知識</th></tr></thead><tbody><tr><td><strong>知識庫清單管理員</strong></td><td>可操作知識庫與知識全部功能的角色</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>知識庫清單協作者</strong></td><td>被賦予權限協助管理知識庫成員的角色</td><td>O</td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>知識庫清單使用者</strong></td><td>可建立與編輯屬於自己的知識的角色</td><td>O</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>

### 知識

以下表格描述的是「知識」層級可以做的事情。這一層通常由「知識管理員」或「知識協作者」負責管理成員，將適合的權限分配給協作者或使用者。

<figure><img src="../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>說明</th><th width="93">可在 Agent 新增知識</th><th width="93">在知識庫清單檢視知識</th><th width="100">管理知識成員</th><th width="93">編輯知識</th><th>刪除知識</th></tr></thead><tbody><tr><td><strong>知識管理員</strong></td><td>擁有完整的知識控制權</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>知識協作者</strong></td><td>可協助管理知識的內容調整</td><td>O</td><td>O</td><td>X</td><td>O</td><td>X</td></tr><tr><td><strong>知識使用者</strong></td><td>僅能讀取知識的角色</td><td>O</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>

## **MCP 功能權限**

### **MCP 清單**

以下表格描述的是「**MCP** 清單」層級可以做的事情。你可以把「**MCP** 清單」當成一個管理範圍：能不能建立項目、能不能管理成員、能不能檢視/編輯所有項目，取決於你在此功能清單被授予的角色。

<figure><img src="../.gitbook/assets/image (125).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>說明</th><th>建立MCP</th><th>管理MCP成員</th><th>檢視所有MCP</th><th>編輯所有MCP</th></tr></thead><tbody><tr><td><strong>MCP 清單管理員</strong></td><td>可操作MCP清單與MCP全部功能的角色</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>MCP 清單協作者</strong></td><td>被賦予權限協助管理MCP清單成員的角色</td><td>O</td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>MCP 清單使用者</strong></td><td>可建立與編輯屬於自己的MCP的角色</td><td>O</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>

### **MCP**

以下表格描述的是「MCP」層級可以做的事情。這一層通常由「MCP 管理員」或「MCP 協作者」負責管理成員，將適合的權限分配給協作者或使用者。

<figure><img src="../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>說明</th><th width="91">可在 Agent 新增MCP</th><th width="93">在MCP清單清單檢視MCP</th><th width="83">設定MCP成員</th><th width="87">編輯MCP</th><th>刪除MCP</th></tr></thead><tbody><tr><td><strong>MCP 管理員</strong></td><td>擁有完整的MCP控制權</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>MCP 協作者</strong></td><td>可協助管理MCP的內容調整</td><td>O</td><td>O</td><td>X</td><td>O</td><td>X</td></tr><tr><td><strong>MCP 使用者</strong></td><td>僅能讀取MCP的角色</td><td>O</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>

## **工作流程模板 功能權限**

### **工作流程模板清單**

以下表格描述的是「工作流程模板清單」層級可以做的事情。你可以把「工作流程模板清單」當成一個管理範圍：能不能建立項目、能不能管理成員、能不能檢視/編輯所有項目，取決於你在此功能清單被授予的角色。

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>說明</th><th>建立工作流程模板</th><th>管理提工作流程成員模板</th><th>檢視所有工作流程模板</th><th>編輯所有工作流程模板</th></tr></thead><tbody><tr><td><strong>工作流程模板清單管理員</strong></td><td>可操作工作流程模板清單與工作流程全部模板功能的角色</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>工作流程模板清單協作者</strong></td><td>被賦予權限協助管理工作流程模板清單成員的角色</td><td>O</td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>工作流程模板清單使用者</strong></td><td>可建立與編輯屬於自己的工作流程模板的角色</td><td>O</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>

### 工作流程模板

以下表格描述的是「工作流程模板」層級可以做的事情。這一層通常由「工作流程模板管理員」或「工作流程模板協作者」負責管理成員，將適合的權限分配給協作者或使用者。

<figure><img src="../.gitbook/assets/image (128).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>說明</th><th width="93">可在工作空間使用工作流程模板</th><th width="104">在工作流程清單清單檢視工作流程模板</th><th width="98">設定工作流程模板成員</th><th width="82">編輯工作流程模板</th><th>刪除提工作流程模板</th></tr></thead><tbody><tr><td><strong>工作流程模板管理員</strong></td><td>擁有完整的工作流程模板控制權</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>工作流程模板協作者</strong></td><td>可協助管理工作流程模板的內容調整</td><td>O</td><td>O</td><td>X</td><td>O</td><td>X</td></tr><tr><td><strong>工作流程模板使用者</strong></td><td>僅能讀取工作流程模板的角色</td><td>O</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>

## **提示詞模板 功能權限**

### **提示詞模板清單**

以下表格描述的是「提示詞模板清單」層級可以做的事情。你可以把「提示詞模板清單」當成一個管理範圍：能不能建立項目、能不能管理成員、能不能檢視/編輯所有項目，取決於你在此功能清單被授予的角色。

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>說明</th><th width="99">建立提示詞模板</th><th width="107">管理提示詞清單模板成員</th><th width="108">檢視所有提示詞模板</th><th>編輯所有提示詞模板</th></tr></thead><tbody><tr><td><strong>提示詞模板清單管理員</strong></td><td>可操作提示詞模板清單與提示詞模板全部功能的角色</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>提示詞模板清單協作者</strong></td><td>被賦予權限協助管理提示詞模板清單成員的角色</td><td>O</td><td>O</td><td>X</td><td>X</td></tr><tr><td><strong>提示詞模板清單使用者</strong></td><td>可建立與編輯屬於自己的提示詞模板的角色</td><td>O</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>

### 提示詞模板

以下表格描述的是「提示詞模板」層級可以做的事情。這一層通常由「提示詞模板管理員」或「提示詞模板協作者」負責管理成員，將適合的權限分配給協作者或使用者。

<figure><img src="../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>角色</th><th>說明</th><th width="103">可在工作空間使用提示詞模板</th><th width="94">在提示詞清單清單檢視提示詞</th><th width="95">設定提示詞模板成員</th><th width="85">編輯提示詞模板</th><th>刪除提示詞模板</th></tr></thead><tbody><tr><td><strong>提示詞模板管理員</strong></td><td>擁有完整的提示詞模板控制權</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td><strong>提示詞模板協作者</strong></td><td>可協助管理提示詞模板的內容調整</td><td>O</td><td>O</td><td>X</td><td>O</td><td>X</td></tr><tr><td><strong>提示詞模板使用者</strong></td><td>僅能讀取提示詞模板的角色</td><td>O</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></tbody></table>
