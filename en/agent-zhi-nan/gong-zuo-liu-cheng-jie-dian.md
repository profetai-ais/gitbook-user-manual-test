# Workflow node

## Introduction

The workflow system provides diverse node designs for building flexible, intelligent and modular assistants. Each node plays a different role in improving system logic, user interaction, and back-end integration.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Node Name⟬<table>6⟭⟬<table>7⟭Use in Workflow⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Knowledge Retrieval⟬<table>16⟭⟬<table>17⟭Retrieve relevant information from internal knowledge base or document database. ⟬<table>18⟭⟬<table>19⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭⟬<table>23⟭LLM⟬<table>24⟭⟬<table>25⟭Use a language model (e.g. GPT-5.2 Thinking/GPT-5.2 Instant/Gemini 3) Execute prompts to generate or reason results based on the current input. ⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭3⟬<table>30⟭⟬<table>31⟭Response ⟬<table>32⟭⟬<table>33⟭Defines what the user actually sees—outputs and displays the assistant's reply. ⟬<table>34⟭⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭4⟬<table>38⟭⟬<table>39⟭Annotations ⟬<table>40⟭⟬<table>41⟭Add internal annotations or callouts to the canvas — not connected to actual logic. ⟬<table>42⟭⟬<table>43⟭⟬<table>44⟭⟬<table>45⟭5⟬<table>46⟭⟬<table>47⟭Variable node ⟬<table>48⟭⟬<table>49⟭Retrieve, store or convert the value of the previous step for use by subsequent nodes. ⟬<table>50⟭⟬<table>51⟭⟬<table>52⟭⟬<table>53⟭6⟬<table>54⟭⟬<table>55⟭Guardrail⟬<table>56⟭⟬ <table>57⟭ can check and restrict content during the process, helping to reduce risks related to personal data leakage, information security and legal compliance, and making the output content more consistent with usage specifications and management requirements. ⟬<table>58⟭⟬<table>59⟭⟬<table>60⟭⟬<table>61⟭7⟬<table>62⟭⟬<table>63⟭Classification⟬<table>64⟭⟬<table>65⟭Automatically label inputs or guide paths based on predefined logic or model-based classification. ⟬<table>66⟭⟬<table>67⟭⟬<table>68⟭⟬<table>69⟭8⟬<table>70⟭⟬<table>71⟭Fork ⟬<table>72⟭⟬<table>73⟭Describes the flow and sequence of data between nodes so that tasks can be automated. ⟬<table>74⟭⟬<table>75⟭⟬<table>76⟭⟬<table>77⟭9⟬<table>78⟭⟬<table>79⟭Merge ⟬<table>80⟭⟬<table>81⟭Converge the outputs of different branches to the same node and hand them over to subsequent nodes for processing. ⟬<table>82⟭⟬<table>83⟭⟬<table>84⟭⟬<table>85⟭

### **Knowledge retrieval**

Retrieve relevant information from internal knowledge base or document database.

<div align="center" data-with-frame="true"><figure><img src="../.gitbook/assets/image .png" alt="" width="375"><figcaption></figcaption></figure></div>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Function Name⟬<table>6⟭⟬<table>7⟭Description⟬<table>8⟭⟬<table>9⟭⟬<table>10 ⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Knowledge retrieval⟬<table>16⟭⟬<table>17⟭Input content (enter "/" to select query as the user's question)⟬<table>18⟭⟬<table>19⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭⟬<table>23⟭Knowledge Library Reference ⟬<table>24⟭⟬<table>25⟭ Select the required knowledge base ⟬<table>26⟭⟬<table>27⟭⟬<table> 28⟭⟬<table>29⟭3⟬<table>30⟭⟬<table>31⟭Search parameters⟬<table>32⟭⟬<table>33⟭ Refer to "Testing Knowledge Base - Search Parameter Settings"⟬<table>34⟭⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭

### **LLM**

Execute prompts using language models (e.g. GPT-5.2 Thinking/GPT-5.2 Instant/Gemini 3) to generate or reason results based on the current input.



<div data-with-frame="true"><figure><img src="../.gitbook/assets/image .png" alt="" width="188"><figcaption></figcaption></figure></div>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Function Name⟬<table> 6⟭⟬<table>7⟭Description⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1 ⟬<table>14⟭⟬<table>15⟭LLM name ⟬<table>16⟭⟬<table>17⟭Enter the node name to facilitate identification ⟬<table>18⟭⟬<table> 19⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭⟬<table>23⟭LLM parameter adjustment⟬<table>24⟭⟬<table>25⟭Reference ⟬<table>26⟭Parameters⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭⟬<table>30⟭⟬<table>31 ⟭3⟬<table>32⟭⟬<table>33⟭Model ⟬<table>34⟭⟬<table>35⟭Replace the language model used by the node (with 2. The model settings in are the same)⟬<table>36⟭⟬<table>37⟭⟬<table>38⟭⟬<table>39⟭4⟬<table>40⟭⟬<table>41⟭Context⟬<table> 42⟭⟬<table>43⟭Input content (enter "/" to select query as the user's question)⟬<table>44⟭⟬<table>45⟭⟬<table>46⟭⟬P H0047⟭5⟬<table>48⟭⟬<table>49⟭Use node files⟬<table>50⟭⟬<table>51⟭Allow LLM to obtain which files from previous nodes⟬<table> 52⟭⟬<table>53⟭⟬<table>54⟭⟬<table>55⟭6⟬<table>56⟭⟬<table>57⟭File Processing⟬<table>58⟭⟬<table>59⟭Reference ⟬<table>60⟭File Processing⟬<table>61⟭⟬<table>62⟭⟬<table>63⟭⟬<table>64⟭⟬<table>65⟭7⟬<table>66⟭⟬<table>67⟭Enable Knowledge Base⟬<table>68⟭⟬<table>69⟭Reference ⟬<table>70⟭Knowledge Base Source⟬<table>71⟭⟬<table>72⟭⟬<table>73⟭⟬<table>74⟭⟬<table>75⟭8⟬<table>76⟭⟬<table>77⟭Agent Collaboration⟬<table>78⟭⟬<table>79⟭Reference ⟬<table>80⟭Agent Collaboration⟬<table>81⟭⟬<table>82⟭⟬<table>83⟭⟬<table>84⟭⟬<table>85⟭9⟬<table>86⟭⟬<table>87⟭Skills⟬<table>88⟭⟬<table>89⟭Reference ⟬<table>90⟭Skills⟬<table>91⟭⟬<table>92⟭⟬<table>93⟭⟬<table>94⟭⟬<table>95⟭10⟬<table>96⟭⟬<table>97⟭Reference Memory⟬<table>98⟭⟬<table>99⟭After enabled, LLM will refer to the memory in the memory bank when replying. For the memory storage method, please refer to ⟬<table>100⟭ Agent Memory⟬<table>101⟭⟬<table>102⟭⟬<table>103⟭⟬<table>104⟭⟬<table>105⟭11⟬<table>106⟭⟬<table>107⟭Conversation Memory⟬<table>108⟭⟬<table>109⟭Reference ⟬<table>110⟭ Parameters ⟬<table>111⟭ Dialogue memory within ⟬<table>112⟭⟬<table>113⟭⟬<table>114⟭⟬<table>115⟭12⟬<table>116⟭⟬<table>117⟭Tools⟬<table>118⟭⟬<table>119⟭Reference ⟬<table>120⟭Tools⟬<table>121⟭⟬<table>122⟭⟬<table>123⟭⟬<table>124⟭⟬<table>125⟭

### **reply**

Response Node is used to define the final output content of the Agent and is responsible for transmitting the completed results in the process back to the user or as a response to subsequent system output.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image .png" alt="" width="246"><figcaption></figcaption></figure></div>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Function Name⟬<table>6⟭⟬<table>7⟭Description⟬<table>8⟭⟬<table>9⟭ ⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Node name⟬<table>16⟭⟬<table>17⟭Enter the node name for easy identification⟬<table>18⟭⟬ <table>19⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭⟬<table>23⟭Description⟬<table>24⟭⟬<table>25⟭You can fill in the purpose description of this node⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭3⟬<table>30⟭⟬<table>31⟭Configuration variables⟬<table>32⟭⟬<table>33⟭Enter/to configure variables⟬<table>34⟭⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭

### **annotation**

Add internal annotations or callouts to the canvas — not connected to actual logic.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image .png" alt="" width="249"><figcaption></figcaption></figure></div>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Function Name⟬<table>6⟭⟬<table>7 ⟭Description⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Node Name⟬<table>16⟭⟬<table>17⟭Enter the node name to facilitate identification of ⟬<table>18⟭⟬<table>19⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭ ⟬<table>23⟭Remarks⟬<table>24⟭⟬<table>25⟭Enter the remark content for subsequent identification⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭

### **Variable Node**

Retrieve, store or convert the value of the previous step for use by subsequent nodes.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image .png" alt="" width="375"><figcaption></figcaption></figure></div>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Function Name⟬<table>6⟭ ⟬<table>7⟭Description⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Variable (global variable name) ⟬<table>16⟭⟬<table>17⟭ is used to select/specify the ⟬<table>18⟭global variable key value to be written. ⟬<table>19⟭ (for example: ⟬<table>20⟭global.age⟬<table>21⟭) so that it can be read and referenced with a consistent name in subsequent process nodes. ⟬<table>22⟭⟬<table>23⟭⟬<table>24⟭⟬<table>25⟭2⟬<table>26⟭⟬<table>27⟭Variable content (variable value)⟬P H0028⟭⟬<table>29⟭ is used to set the ⟬<table>30⟭actual value (Value) ⟬<table>31⟭ of the global variable, which can be directly accessed by subsequent nodes. ⟬<table>32⟭⟬<table>33⟭⟬<table>34⟭⟬<table>35⟭

### guardrail

Automatically label inputs or guide paths based on predefined logic or model-based classification.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image .png" alt="" width="375"><figcaption></figcaption></figure></div>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Function Name⟬<table>6⟭⟬<table>7⟭Description⟬<table>8⟭⟬<table>9⟭⟬P H0010⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Configuration variables⟬<table>16⟭⟬<table>17⟭Enter/to configure variables⟬<table>18⟭⟬<table>19 ⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭⟬<table>23⟭Block/Mask⟬<table>2 4⟭⟬<table>25⟭Select the guardrail operation mode⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬P H0029⟭3⟬<table>30⟭⟬<table>31⟭Category⟬<table>32⟭⟬<table>33⟭Select the content to block/mask according to different types⟬<table>34⟭⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭

### **Classification**

Automatically label inputs or guide paths based on predefined logic or model-based classification.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image .png" alt="" width="375"><figcaption></figcaption></figure></div>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>05⟭Function Name⟬<table>6⟭⟬<table>7⟭Description⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15⟭Module Type ⟬<table>16⟭⟬<table>17⟭Replace the language model used by the node ⟬<table>18⟭⟬<table>19⟭⟬ <table>20⟭⟬<table>21⟭2⟬<table>22⟭⟬<table>23⟭Context⟬<table>24⟭⟬<table>25⟭Input content (enter "/" to select query as the user's question)⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭3⟬<table>30⟭⟬<table>31⟭Category⟬<table>32 ⟭⟬<table>33⟭Categorize the problem ⟬<table>34⟭⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭

### bifurcation

Describe the flow and sequence of data between nodes so that tasks can be automated.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image .png" alt="" width="375"><figcaption></figcaption></figure></div>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Function Name⟬<table>6⟭⟬<table> 7⟭Description⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭1⟬<table>14⟭⟬<table>15 ⟭Branch⟬<table>16⟭⟬<table>17⟭View the current number of branches⟬<table>18⟭⟬<table>19⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭ ⟬<table>23⟭Branch status⟬<table>24⟭⟬<table>25⟭View current branch status⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭

### merge

Converge the outputs of different branches to the same node and hand them over to subsequent nodes for processing.

<div data-with-frame="true"><figure><img src="../.gitbook/assets/image .png" alt="" width="375"><figcaption></figcaption></figure></div>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Project⟬<table>4⟭⟬<table>5⟭Function Name⟬<table>6⟭⟬<table>7⟭Description⟬<table>8⟭⟬<table>9 P H0019⟭⟬<table>20⟭⟬<table>21⟭2⟬<table>22⟭⟬<table>23⟭Input status⟬<table>24⟭⟬<table>25⟭View current input status⟬<table>26⟭⟬<table>27⟭⟬<table>28⟭⟬<table>29⟭3⟬<table>30⟭⟬<table>31⟭Waiting timeout⟬<table>32⟭⟬<table>33⟭Set waiting timeout⟬<table>34⟭⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭
