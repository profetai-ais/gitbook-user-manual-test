---
description: 工作管理用於集中管理與追蹤 Agent 執行中的各項工作（Jobs）清楚掌握每個工作的狀態、責任歸屬與進度變化。
---

# 工作管理

## 簡介

<figure><img src="../.gitbook/assets/image (230).png" alt=""><figcaption></figcaption></figure>

當使用者提出需求後，系統會將其拆解為可執行的工作項目，並在 Job Manager 中建立對應的 Task；每個 Task 會包含清楚的 Job、描述、目前狀態（例如：待處理、進行中、已完成、失敗/需介入）、建立與更新時間、相關輸入與產出、以及必要的執行紀錄，方便使用者回溯與核對。

## 任務狀態介紹

狀態 (Status) 總共有8種：

<table><thead><tr><th width="224">狀態名稱</th><th>說明</th></tr></thead><tbody><tr><td>PENDING</td><td>已建立，等待進入佇列/尚未派送</td></tr><tr><td>QUEUED</td><td>已在佇列中等待執行</td></tr><tr><td>RUNNING</td><td>執行中</td></tr><tr><td>SUCCEEDED</td><td>成功完成</td></tr><tr><td>FAILED</td><td>執行失敗</td></tr><tr><td>STOPPED</td><td>被停止（中止）</td></tr><tr><td>CANCELED</td><td>被取消</td></tr><tr><td>PAUSED</td><td>暫停中</td></tr></tbody></table>

## Job頁面說明

點擊想要查看的 Task 名稱可打開彈出視窗瀏覽底下的 Job。

<figure><img src="../.gitbook/assets/image (231).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (232).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="101">項目</th><th width="177">名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>重做</td><td>重新執行 Job</td></tr><tr><td>2</td><td>繼續 </td><td>繼續 Job 的工作進度</td></tr><tr><td>3</td><td>詳細資訊</td><td>查看詳細資訊</td></tr><tr><td>4</td><td>暫停</td><td>暫停 Job 的工作進度</td></tr><tr><td>3</td><td>取消</td><td>取消這個 Job 的工作任務</td></tr></tbody></table>
