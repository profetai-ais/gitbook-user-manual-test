---
description: >-
  AI Studio 可讓 IT 人員串聯外部訂閱的大語言模型 (LLM) 服務，如 ChatGPT 或是
  Gemini，或是設定串接在自有算力上部署的地端大語言模型。
---

# Model

## **New large language model**

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. After entering, click "+Add" in the upper right corner to start setting.
2. Choose a service provider (for example: OpenAI / Azure / Gemini / Ollama / Claude)
3. Set content according to different service providers
 1. Name: Customizable, the name of the model that will be displayed in the system
 2. Model: Please enter the model to use

> Note: Please fill in manually, the system will not automatically list the options. (Example: `gpt-5`, ⟬`gpt-5`1⟭, ⟬`gpt-5`2⟭, ⟬`gpt-5`3⟭…etc.)
 >
 > For example, if it is mistakenly planted as ⟬`gpt-5`4⟭, an error message will appear during Agent testing:
 >
 > Received Model Group=gpt-6
 >
 > Available Model Group Fallbacks=None
 >
 > Mode: If you input the model yourself, you will need to select another mode (for example: Chat / Embedding)
 3. API basics: Please enter the API Key provided by the service provider

> Note: If the input is incorrect, the system will return an authorization error.
 >
 > * OpenAI: Please fill in the API prefix (Prefix). For example: `https://api.openai.com/v1`
 > * Gemini: No need to fill in the API Base URL, the system will automatically handle the routing.
 4. API Key: Please fill in the API Key
 5. Organization: Optional. Generally, Key can be left blank. Some OpenAI may need to fill in if short Key is used.
4. advanced settings
 1. If using **Cloud Model** → It is recommended to leave it blank and the system will automatically update the latest price.
 2. If you use **your own deployment model**→ you can evaluate whether to fill in the rate yourself.
5. Click Create to complete the settings.

## **Model setting content description**

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Setting Item⟬<table>4⟭⟬<table>5⟭Description⟬<table>6⟭⟬<table>7⟭Options⟬<table>8⟭⟬<table>9⟭⟬<table>1 0⟭⟬<table>11⟭⟬<table>12⟭⟬<table>13⟭Service name⟬<table>14⟭⟬<table>15⟭Service name of the provided model⟬<table>16⟭⟬<table>17⟭⟬<table>18⟭openai⟬<table>19⟭, ⟬<table>20⟭gemini⟬<table>21⟭, ⟬<table>22⟭ollama⟬<table>23⟭ (on-premises)⟬<table>24⟭⟬<table>25⟭⟬<table>26⟭⟬<table>27⟭Mode⟬<table> 28⟭⟬<table>29⟭Type of model⟬<table>30⟭⟬<table>31⟭⟬<table>32⟭chat⟬<table>33⟭, ⟬<table>34⟭embedding⟬<table>35⟭⟬<table>36⟭⟬<table>37⟭⟬<table>38⟭⟬<table>39⟭Model⟬<table>40⟭⟬<table>41⟭Service provides usable model ⟬<table>42⟭⟬<table>43⟭Example: ⟬<table>44⟭gpt-4.1⟬<table>45⟭, ⟬<table>46⟭gemini-2.0-flash⟬<table>47⟭ etc., depending on the settings during system installation ⟬<table>48⟭⟬<table>49⟭⟬<table>50⟭⟬<table>51⟭Name ⟬<table>52⟭⟬<table>53⟭ in AI Studio The name used to identify this model ⟬<table>54⟭⟬<table>55⟭ is by default the same as the model, and the user enters ⟬<table>56⟭⟬<table>57⟭⟬<table>58⟭⟬<table>59⟭Description⟬ <table>60⟭⟬<table>61⟭Model description⟬<table>62⟭⟬<table>63⟭User input⟬<table>64⟭⟬<table>65⟭⟬<table>66⟭⟬<table>67⟭API Key/API Basics ⟬<table>68⟭⟬<table>69⟭Service selection ⟬<table>70⟭openai⟬<table>71⟭ and ⟬<table>72⟭gemini⟬<table>73⟭ Enter the key and select ⟬<table>74⟭ollama⟬<table>75⟭ When entering the URL of the model API service ⟬<table>76⟭⟬<table>77⟭ the user inputs ⟬<table>78⟭⟬<table>79⟭⟬<table>80⟭⟬<table>81⟭custom price (Advanced settings)⟬<table>82⟭⟬<table>83⟭Whether to provide model service prices for calculating the cost of using generative AI⟬<table>84⟭⟬<table>85⟭User options⟬<table>86⟭⟬<table>87⟭⟬<table>88⟭⟬<table>89⟭Pricing model (Advanced Settings) How is the ⟬<table>90⟭⟬<table>91⟭ service priced? ⟬<table>92⟭⟬<table>93⟭Preset to mark per million ⟬<table>94⟭⟬<table>95⟭⟬<table>96⟭⟬<table>97⟭Enter cost (Advanced settings)⟬<table>98⟭⟬<table>99⟭Enter the amount value⟬<table>100⟭⟬<table>101⟭User input⟬<table>102⟭⟬<table>103⟭⟬<table>104⟭⟬<table>105⟭Output cost (Advanced settings)⟬<table>106⟭⟬<table>107⟭Enter the amount value⟬<table>108⟭⟬<table>109⟭User input⟬<table>110⟭⟬<table>111⟭⟬<table>112⟭⟬<table>113 ⟭Enable Status⟬<table>114⟭⟬<table>115⟭Enable/Stop Model⟬<table>116⟭⟬<table>117⟭User Options⟬<table>118⟭⟬<table>119⟭⟬<table>120⟭⟬<table>121⟭

> Note: The service name, mode and model cannot be changed after the model is created.
