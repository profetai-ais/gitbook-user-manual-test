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

<table><thead><tr><th width="224">Status name</th><th>illustrate</th></tr></thead><tbody><tr><td>PENDING</td><td>Created, waiting to be queued/not yet dispatched</td></tr><tr><td>QUEUED</td><td>Already queued for execution</td></tr><tr><td>RUNNING</td><td>Executing</td></tr><tr><td>SUCCEEDED</td><td>Completed successfully</td></tr><tr><td>FAILED</td><td>Execution failed</td></tr><tr><td>STOPPED</td><td>to be stopped (aborted)</td></tr><tr><td>CANCELED</td><td>canceled</td></tr><tr><td>PAUSED</td><td>Paused</td></tr></tbody></table>

## Job page description

Click the name of the Task you want to view to open a pop-up window to browse the jobs below.

<figure><img src="../.gitbook/assets/image (231).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (232).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="101">project</th><th width="177">name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>Redo</td><td>Re-execute the job</td></tr><tr><td>2</td><td>continue </td><td>Continue the work progress of the Job</td></tr><tr><td>3</td><td>Details</td><td>View details</td></tr><tr><td>4</td><td>pause</td><td>Pause the work progress of the Job</td></tr><tr><td>3</td><td>Cancel</td><td>Cancel the work tasks of this Job</td></tr></tbody></table>
