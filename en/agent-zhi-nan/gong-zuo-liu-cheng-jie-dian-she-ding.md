---
description: 本指南將逐步示範如何依據工作流程編輯器中的 UI 元素設定 LLM 節點。
---

# Workflow node settings



## Page introduction

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Steps⟬<table>4⟭⟬<table>5⟭Blocks⟬<table>6⟭⟬<table>7⟭Operating Instructions⟬<table>8 ⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Node name ⟬<table>16⟭⟬<table>17⟭ is LLM node naming is clear and descriptive (for example: 2. Industry trends). This helps organize processes visually and logically, especially in complex processes. ⟬<table>18⟭ Note: ⟬<table>19⟭ The node name must be unique to save the settings. ⟬<table>20⟭⟬<table>21⟭⟬<table>22⟭⟬<table>23⟭2⟬<table>24⟭⟬<table>25⟭Node Description ⟬<table>26⟭⟬<table>27⟭ Provide a short description for the LLM node (for example: including industry dynamics, policy changes, technology drivers and corporate behaviors). This helps organize processes visually and logically, especially in complex processes. ⟬<table>28⟭⟬<table>29⟭⟬<table>30⟭⟬<table>31⟭3⟬<table>32⟭⟬<table>33⟭Model Selection⟬<table>34⟭⟬<table>35⟭Select a language model from the drop-down menu (for example: gpt-5.2-thinking or gpt-5.2-instant). Make sure the model meets response quality and budget requirements. ⟬<table>36⟭⟬<table>37⟭⟬<table>38⟭⟬<table>39⟭4⟬<table>40⟭⟬<table>41⟭Situation (input variables) ⟬<table>42⟭⟬<table>43⟭ Set the input content that the LLM should refer to when inferring. Dynamic input can be passed using variables from other nodes or user input. Enter ⟬<table>44⟭/⟬<table>45⟭ in the situation window to see the available variables. ⚠️ To access variables such as ⟬<table>46⟭result⟬<table>47⟭, ⟬<table>48⟭usage⟬<table>49⟭ or ⟬<table>50⟭execution_time⟬<table>51⟭ from previous nodes, these nodes must ⟬<table>52⟭ explicitly links ⟬<table>53⟭ to the current node, otherwise the context cannot parse the variables correctly. ⟬<table>54⟭⟬<table>55⟭⟬<table>56⟭⟬<table>57⟭5⟬<table>58⟭⟬<table>59⟭Using node files ⟬<table>60⟭⟬<table>61⟭Which files are allowed to be obtained by LLM from the previous node Case ⟬<table>62⟭⟬<table>63⟭⟬<table>64⟭⟬<table>65⟭6⟬<table>66⟭⟬<table>67⟭File Handling (optional) ⟬<table>68⟭⟬<table>69⟭Choose how to handle uploaded files. For more information, please refer to the ⟬<table>70⟭File Processing⟬<table>71⟭ chapter. ⟬<table>72⟭⟬<table>73⟭⟬<table>74⟭⟬<table>75⟭7⟬<table>76⟭⟬<table>77⟭Knowledge Base ⟬<table>78⟭⟬<table>79⟭When enabled, the selected knowledge will be automatically queried during the conversation. ⟬<table>80⟭⟬<table>81⟭⟬<table>82⟭⟬<table>83⟭13⟬<table>84⟭⟬<table>85⟭Inference Settings⟬<table>86⟭⟬<table>87⟭Click the gear icon () next to the model selection area Customize model behavior, including: ⟬<table>88⟭⟬<table>89⟭1. Parameter adjustment ⟬<table>90⟭: Temperature, Top P, Max Tokens (please refer to the parameter table for more information). ⟬<table>91⟭⟬<table>92⟭2. System prompt words ⟬<table>93⟭: Write prompt words to define the role, task, tone, and tool behavior. ⟬<table>94⟭⟬<table>95⟭⟬<table>96⟭⟬<table>97⟭

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Steps⟬<table>4⟭⟬<table>5⟭Block⟬<table>6⟭⟬<table>7⟭Operation Instructions Ming⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭8⟬<table>14⟭⟬<table>15⟭Agent Collaboration ⟬<table>16⟭⟬<table>17⟭ allows Agents to connect in series and collaborate with other Agents to perform tasks. ⟬<table>18⟭⟬<table>19⟭⟬<table>20⟭⟬<table>21⟭9⟬<table>22⟭⟬<table>23⟭Skills⟬<table>24⟭⟬<table>25⟭By setting different skills, Agent can support more functions and task processing scenarios. ⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭10⟬<table>30⟭⟬<table>31⟭Reference Memory ⟬<table>32⟭⟬<table>33⟭When enabled, personal memory will be referenced during conversations. ⟬<table>34⟭⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭11⟬<table>38⟭⟬<table>39⟭Memory Settings (optional) ⟬<table>40⟭⟬<table>41⟭ If multiple rounds of dialogue situations are required, please enable the memory function. Sets the memory window size when building multi-turn conversations or reasoning chains (recommended value: 3–5). ⟬<table>42⟭ Note: ⟬<table>43⟭ It is recommended to unify the number of session memory rounds to ensure process consistency and avoid information loss. ⚠️ A conversation refers to the pairing of a question (user prompt) and a response (assistant answer). ⟬<table>44⟭⟬<table>45⟭⟬<table>46⟭⟬<table>47⟭12⟬<table>48⟭⟬<table>49⟭Tools (optional) ⟬<table>50⟭⟬<table>51⟭If the task requires functionality beyond the native capabilities of LLM, additional tools can be used (e.g. using ⟬<table>52⟭Serper Search⟬<table>53⟭ tool performs real-time web searches during generation). ⟬<table>54⟭⟬<table>55⟭⟬<table>56⟭⟬<table>57⟭

## **How ​​to use Context and System Prompt**

When setting up the LLM node, both **Context** and **System Prompt** can contain instructions, but their purposes are different and have clear priorities:

### **Context**

> Purpose: Set dynamic input variables, which can be regarded as the "workspace" of the model - that is, the content currently referenced by the model.

**Note:**

* Use the **Context** field to pass in **query text**, **user input** or **preceding node data**.
* Supports using variables such as `${start.query}` or ⟬`${start.query}`1⟭ to make responses more personal or contextual.
* Although you can put brief instructions here, the context field should be focused on **content** rather than rules of conduct.

### **System Prompt**

> Purpose: Define the behavior and role of the model, which can be regarded as the "permanent job description" of this node.

**Note:**

* Used to define who the model is, how it should act, and what it should accomplish.
* Commands in the system prompt word will take precedence over commands in the context.
* It is recommended to always clearly define:
 * **Role** (e.g. Product Manager, Analyst, Mentor)
 * **Task Objective** (e.g. writing a report, interpreting code)
 * **Tone** (e.g. formal, friendly)
 * **Tool usage rules** (if tools are attached)

### **File Handling**

The **File Handling** setting allows the user to define how the Assistant handles uploaded files in the workspace. This is especially useful when the assistant needs to interpret, convert or extract file content (e.g. PDF, DOCX, images) in a conversation.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Options⟬<table>4⟭⟬<table>5⟭MCP tool visible ⟬<table>6⟭⟬<table>7⟭LLM Visible⟬<table>8⟭⟬<table>9⟭Instructions⟬<table>10⟭⟬<table>11⟭Example application scenarios⟬<table>12⟭⟬<table>13⟭⟬<table>14⟭⟬<table>15⟭⟬ <table>16⟭⟬<table>17⟭Not processed⟬<table>18⟭⟬<table>19⟭X⟬<table>20⟭⟬<table>21⟭X⟬<table>22⟭⟬<table>23⟭The file has been uploaded but the LLM and MCP tools are not visible and will not be opened or parsed. ⟬<table>24⟭⟬<table>25⟭– ⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭Handle with tools only ⟬<table>30⟭ ⟬<table>31⟭O⟬<table>32⟭⟬<table>33⟭X⟬<table>34⟭⟬<table>35⟭File passed to Processed by MCP tools but not provided to LLM. ⟬<table>36⟭⟬<table>37⟭ is suitable for situations where data needs to be extracted from CSV or PDF but AI commentary is not required. ⟬<table>38⟭⟬<table>39⟭⟬<table>40⟭⟬<table>41⟭File to image⟬<table>42⟭⟬<table>43⟭ LLM Reference. ⟬<table>48⟭⟬<table>49⟭ is suitable for scanning documents or visual materials that require reference to the layout structure. ⟬<table>50⟭⟬<table>51⟭⟬<table>52⟭⟬<table>53⟭Convert to image and tool processing⟬<table>54⟭⟬P H0055⟭O⟬<table>56⟭⟬<table>57⟭O⟬<table>58⟭⟬<table>59⟭Also convert the file into a picture for LLM reference and passed to MCP tool for processing. ⟬<table>60⟭⟬<table>61⟭ is suitable for invoices or forms that need to parse both visual structure and structured data. ⟬<table>62⟭⟬<table>63⟭⟬<table>64⟭⟬<table>65⟭
