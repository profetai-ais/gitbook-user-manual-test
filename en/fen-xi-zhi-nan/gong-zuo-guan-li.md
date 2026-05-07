---
description: "Work management is used to centrally manage and track various jobs (Jobs) being executed by Agent, and clearly understand the status, responsibility and progress changes of each job."
---
---
# work management

## Introduction

<figure><img src="../.gitbook/assets/image (230).png" alt=""><figcaption></figcaption></figure>

When a user puts forward a request, the system will break it down into executable work items and create corresponding Tasks in the Job Manager; each Task will contain a clear job, description, current status (for example: pending, in progress, completed, failed/needs intervention), creation and update time, related inputs and outputs, and necessary execution records to facilitate user backtracking and verification.

## Task status introduction

There are 8 types of status in total:

<table><thead><tr><th width="224">狀態名稱</th><th>說明</th></tr></thead><tbody><tr><td>PENDING</td><td>已建立，等待進入佇列/尚未派送</td></tr><tr><td>QUEUED</td><td>已在佇列中等待執行</td></tr><tr><td>RUNNING</td><td>執行中</td></tr><tr><td>SUCCEEDED</td><td>成功完成</td></tr><tr><td>FAILED</td><td>執行失敗</td></tr><tr><td>STOPPED</td><td>被停止（中止）</td></tr><tr><td>CANCELED</td><td>被取消</td></tr><tr><td>PAUSED</td><td>暫停中</td></tr></tbody></table>

## Job page description

Click the name of the Task you want to view to open a pop-up window to browse the jobs below.

<figure><img src="../.gitbook/assets/image (231).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (232).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="101">項目</th><th width="177">名稱</th><th>說明</th></tr></thead><tbody><tr><td>1</td><td>重做</td><td>重新執行 Job</td></tr><tr><td>2</td><td>繼續 </td><td>繼續 Job 的工作進度</td></tr><tr><td>3</td><td>詳細資訊</td><td>查看詳細資訊</td></tr><tr><td>4</td><td>暫停</td><td>暫停 Job 的工作進度</td></tr><tr><td>3</td><td>取消</td><td>取消這個 Job 的工作任務</td></tr></tbody></table>
