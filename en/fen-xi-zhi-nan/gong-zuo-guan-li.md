---
description: 工作管理用於集中管理與追蹤 Agent 執行中的各項工作（Jobs）清楚掌握每個工作的狀態、責任歸屬與進度變化。
---

# work management

## Introduction

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

When a user puts forward a request, the system will break it down into executable work items and create corresponding Tasks in the Job Manager; each Task will contain a clear job, description, current status (for example: pending, in progress, completed, failed/needs intervention), creation and update time, related inputs and outputs, and necessary execution records to facilitate user backtracking and verification.

## Task status introduction

There are 8 types of status in total:

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Status Name⟬<table>4⟭⟬<table>5⟭Description⟬<table>6⟭⟬<table>7⟭⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭PENDING⟬<table>12⟭⟬<table>13⟭ Created, waiting to be queued/not yet dispatched⟬<table>14 ⟭⟬<table>15⟭⟬<table>16⟭⟬<table>17⟭QUEUED⟬<table>18⟭⟬<table>19⟭Already queued for execution ⟬<table>20⟭⟬<table>21⟭⟬P H0022⟭⟬<table>23⟭RUNNING⟬<table>24⟭⟬<table>25⟭Executing⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭SU CCEEDED⟬<table>30⟭⟬<table>31⟭Completed successfully⟬<table>32⟭⟬<table>33⟭⟬<table>34⟭⟬<table>35⟭FAILED⟬<table>36⟭ ⟬<table>37⟭Execution failed⟬<table>38⟭⟬<table>39⟭⟬<table>40⟭⟬<table>41⟭STOPPED⟬<table>42⟭⟬<table>43⟭ was stopped (aborted) ⟬<table>44⟭⟬<table>45⟭⟬<table>46⟭⟬<table>47⟭CANCELED⟬<table>48⟭⟬<table>49⟭Canceled⟬<table>50⟭⟬<table>51 ⟭⟬<table>52⟭⟬<table>53⟭PAUSED⟬<table>54⟭⟬<table>55⟭Paused⟬<table>56⟭⟬<table>57⟭⟬<table>58⟭⟬<table>59⟭

## Job page description

Click the name of the Task you want to view to open a pop-up window to browse the jobs below.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Name⟬<table>6⟭⟬<table>7⟭Description⟬<table>8⟭ ⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Redo ⟬<table>16⟭⟬<table>17⟭Redo Job⟬<table>18⟭⟬<table>19⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭⟬<table>23⟭Continue ⟬<table>24⟭⟬<table>25⟭Continue Job Work progress of⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭3⟬<table>30⟭⟬<table>31⟭Detailed information⟬<table>32⟭⟬<table>33⟭ View details⟬<table>34⟭⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭4⟬<table>38⟭⟬<table>39⟭Pause⟬<table>40⟭⟬<table>41⟭Pause Job's work progress⟬<table>42⟭⟬<table>43⟭⟬<table>44⟭⟬<table>45⟭3⟬<table>46⟭⟬<table>47⟭Cancel⟬<table>48⟭⟬<table>49⟭Cancel this Job Work tasks⟬<table>50⟭⟬<table>51⟭⟬<table>52⟭⟬<table>53⟭
