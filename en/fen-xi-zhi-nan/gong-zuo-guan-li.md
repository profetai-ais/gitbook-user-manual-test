---
description: 工作管理用於集中管理與追蹤 Agent 執行中的各項工作（Jobs）清楚掌握每個工作的狀態、責任歸屬與進度變化。
---

# work management

## Introduction

<figure><img src="../.gitbook/assets/image (230).png" alt=""><figcaption></figcaption></figure>

When a user puts forward a request, the system will break it down into executable work items and create corresponding Tasks in the Job Manager; each Task will contain a clear job, description, current status (for example: pending, in progress, completed, failed/needs intervention), creation and update time, related inputs and outputs, and necessary execution records to facilitate user backtracking and verification.

## Task status introduction

There are 8 types of status in total:

<table><thead><tr><th width="224">Status Name</th><th>Description</th></tr></thead><tbody><tr><td>PENDING</td><td> Created, waiting to be queued/not yet dispatched</td></tr><tr><td>QUEUED</td><td>Already queued for execution </td></tr>⟬P H0022⟭<td>RUNNING</td><td>Executing</td></tr><tr><td>SU CCEEDED</td><td>Completed successfully</td></tr><tr><td>FAILED</td> <td>Execution failed</td></tr><tr><td>STOPPED</td><td> was stopped (aborted) </td></tr><tr><td>CANCELED</td><td>Canceled</td></tr><tr><td>PAUSED</td><td>Paused</td></tr></tbody></table>

## Job page description

Click the name of the Task you want to view to open a pop-up window to browse the jobs below.

<figure><img src="../.gitbook/assets/image (231).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (232).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="101">Project</th><th width="177">Name</th><th>Description</th> </tr></thead><tbody><tr><td>1</td><td>Redo </td><td>Redo Job</td></tr><tr><td>2</td><td>Continue </td><td>Continue Job Work progress of</td></tr><tr><td>3</td><td>Detailed information</td><td> View details</td></tr><tr><td>4</td><td>Pause</td><td>Pause Job's work progress</td></tr><tr><td>3</td><td>Cancel</td><td>Cancel this Job Work tasks</td></tr></tbody></table>
