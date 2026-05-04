---
description: Work management is used to centrally manage and track various jobs (Jobs) being executed by Agent, and clearly understand the status, responsibility and progress changes of each job.
---

# work management

## Introduction

<figure><img src="../.gitbook/assets/image (230).png" alt=""><figcaption></figcaption></figure>

When a user puts forward a request, the system will break it down into executable work items and create corresponding Tasks in the Job Manager; each Task will contain a clear job, description, current status (for example: pending, in progress, completed, failed/needs intervention), creation and update time, related inputs and outputs, and necessary execution records to facilitate user backtracking and verification.

## Task status introduction

There are 8 types of status in total:

<table><thead><tr><th width="224">Status Name</th><th>Description</th></tr></thead><tbody><tr>⟦1 1⟧PENDING</td><td> Created, waiting to be queued/not yet dispatched</td></tr>⟦16 ⟧<td>QUEUED</td><td> Already queued for execution </td></tr><tr>⟦2 3⟧RUNNING</td><td>Executing</td></tr><tr><td>SUCCEED ED</td><td>Completed successfully</td></tr><tr><td>FAILED</td>⟦3 7⟧Execution failed</td></tr><tr><td>STOPPED</td><td>Stopped (aborted )</td></tr><tr><td>CANCELED</td><td>Canceled</td>⟦5 1⟧<tr><td>PAUSED</td><td>Paused</td></tr></tbody></table>

## Job page description

Click the name of the Task you want to view to open a pop-up window to browse the jobs below.

<figure><img src="../.gitbook/assets/image (231).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (232).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="101">Project</th><th width="177">Name</th><th>Description</th></tr>⟦ 10⟧<tbody><tr><td>1</td><td>Redo</td><td>Reexecute Job</td></tr><tr><td>2</td><td>Continue </td><td>Continue Job Work progress</td></tr><tr><td>3</td><td>Detailed information</td><td> View details</td></tr><tr><td>4</td><td>Pause</td><td>Pause Job's work progress</td></tr><tr><td>3</td><td>Cancel</td><td>Cancel this Job's work task</td></tr></tbody></table>
