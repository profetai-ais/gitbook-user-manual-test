---
description: 「配置」模組主要用於管理系統的預設行為設定，包含 GPT 預設配置與 default system prompt 等相關項目。
---

# Configuration

## **Related Questions**

The related question function uses LLM's replied content to generate related questions, allowing users to click to perform Q&A. Administrators can change the settings for generating related questions.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. In the left menu of AI Studio, expand the "Settings" item and select "System Settings"
2. In the pagination, select "Related Questions"
3. Click the gear-shaped icon on the right side of the _model title_ to open the "Inference Parameters" window, select the model for translation and adjust the generation parameters. For parameter details, please see [Inference Parameters](pei-zhi.md#tui-li-can-shu)
4. If you want to edit translation prompts, you can enter them in the "Prompt Words" text field, or click "Default Template" to use the default translation prompts.
5. Click the "Save" button at the bottom right to save changes

> Note: If you enter the prompt words yourself, you need LLM to produce a JSON syntax data structure so that the assistant can generate related questions. For the format, please refer to the content of the default template.

## generate title

Used to automatically generate titles based on user input. The system recognizes the input language and generates a short, topical title.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. In the left menu of AI Studio, expand the "Settings" item and select "System Settings"
2. In the pagination, select "Generate title"
3. Click the gear-shaped icon on the right side of the _model title_ to open the "Inference Parameters" window, select the model for translation and adjust the generation parameters. For parameter details, please see [Inference Parameters](pei-zhi.md#tui-li-can-shu)
4. If you want to edit translation prompts, you can enter them in the "Prompt Words" text field, or click "Default Template" to use the default translation prompts.
5. Click the "Save" button at the bottom right to save changes

> Note: If you enter the prompt words by yourself, you need LLM to produce a JSON syntax data structure so that the assistant can generate the title. For the format, please refer to the content of the default template.

## **Memory Language Model**

Used to set the language model used for Personalization-related content located in the avatar in the upper right corner of the screen. You can select the appropriate language according to the actual use situation, such as English or Chinese.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. In the left menu of AI Studio, expand the "Settings" item and select "System Settings"
2. In the pagination, select "Memory Language Model"
3. Click the gear-shaped icon on the right side of the _model title_ to open the "Inference Parameters" window, select the model for translation and adjust the generation parameters. For parameter details, please see [Inference Parameters](pei-zhi.md#tui-li-can-shu)

## **Memory Vector Model**

Used to set the Personalization located in the avatar in the upper right corner of the screen, and the embedding model used when vectorizing the Memory content and writing it to the database.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. In the left menu of AI Studio, expand the "Settings" item and select "System Settings"
2. In the paging, select "Memory Vector Model"
3. Click the gear-shaped icon on the right side of the _model title_ to open the "Inference Parameters" window, select the model for translation and adjust the generation parameters. For parameter details, please see [Inference Parameters](pei-zhi.md#tui-li-can-shu)

## **Memory Constraints**

Used to set "Personalization" located in the avatar in the upper right corner of the screen, memory usage rules and restrictions, such as under what circumstances the memory should be used, retained or deleted.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. In the left menu of AI Studio, expand the "Settings" item and select "System Settings"
2. In the paging, select Remember Constraints
3. Click the gear-shaped icon on the right side of the _model title_ to open the "Inference Parameters" window, select the model for translation and adjust the generation parameters. For parameter details, please see [Inference Parameters](pei-zhi.md#tui-li-can-shu)
4. If you want to edit the prompt word, you can enter it in the "Prompt Word" text field, or click "Default Template" to use the default translation prompt word.
5. Click the Save button to save the settings.

## Voice settings

Rules and restrictions for translation when using the speech-to-text feature in the workspace.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. In the left menu of AI Studio, expand the "Settings" item and select "System Settings"
2. In the tab, select "Voice Settings"
3. Click the gear-shaped icon on the right side of the _model title_ to open the "Inference Parameters" window, select the model for translation and adjust the generation parameters. For parameter details, please see [Inference Parameters](pei-zhi.md#tui-li-can-shu)
4. If you want to edit the prompt word, you can enter it in the "Prompt Word" text field, or click "Default Template" to use the default translation prompt word.
5. Click the Save button to save the settings.

## **Skill Scan Settings**

Used to control whether to enable the scanning mechanism when uploading skills. When enabled, the system will scan when skills are uploaded; when disabled, the system will not scan when uploading.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. In the left menu of AI Studio, expand the "Settings" item and select "System Settings"
2. In the tab, select "Skill Scan Settings"
3. Toggle switch to enable/disable features
4. Click the gear-shaped icon on the right side of the _model title_ to open the "Inference Parameters" window, select the model for translation and adjust the generation parameters. For parameter details, please see [Inference Parameters](pei-zhi.md#tui-li-can-shu)
5. Click the "Save" button at the bottom right to save changes

## Command override settings

The command rewriting setting can automatically organize the original commands entered by the user into clearer, structured and executable prompt words. While retaining the original meaning, the system will remove vague and repetitive content, supplement necessary format, tone, length or language restrictions, and organize multi-step requirements into clear action instructions so that subsequent models can more accurately understand and perform tasks.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. In the left menu of AI Studio, expand the "Settings" item and select "System Settings"
2. In the tab, select "Command Override Settings"
3. Click the gear-shaped icon on the right side of the _model title_ to open the "Inference Parameters" window, select the model for translation and adjust the generation parameters. For parameter details, please see [Inference Parameters](pei-zhi.md#tui-li-can-shu)
4. If you want to edit the prompt word, you can enter it in the "Prompt Word" text field, or click "Default Template" to use the default translation prompt word.
5. Click the Save button to save the settings.

## Canvas settings

**Canvas Settings** can determine whether the user needs to enable canvas-related functions, and automatically dispatch to the appropriate processing flow according to the request content. When the requirement involves charts, flow charts, relationship diagrams, interactive UI or web application descriptions, the system will give priority to the canvas design function for processing; if it includes HTML generation requirements, it will also be handed over to the program editing function through the designated process. If the request does not fall within the scope of visualization or web application, maintain the normal response process to avoid unnecessary activation of the canvas function.

<figure><img src="../.gitbook/assets/image .png" alt=""><figcaption></figcaption></figure>

1. In the left menu of AI Studio, expand the "Settings" item and select "System Settings"
2. In the pagination, select Canvas Settings
3. Toggle switch to enable/disable features
4. Select the skills required to use this canvas
5. If you want to edit the prompt word, you can enter it in the "Prompt Word" text field, or click "Default Template" to use the default translation prompt word.
6. Click the "Save" button at the bottom right to save changes

## **Inference Parameters**

<figure><img src="../.gitbook/assets/image .png" alt="" width="494"><figcaption></figcaption></figure>

<table>⟬<table>1⟭⟬<table>2⟭⟬<table>3⟭Name⟬<table>4⟭⟬<table>5⟭Description⟬<table>6⟭⟬<table>07⟭⟬<table>8⟭⟬<table>9⟭⟬<table>10⟭⟬<table>11⟭Temperature⟬<table>12⟭⟬<table>13⟭Control how creative your answers can be. A high value indicates that the answer is more creative and varied; a low value indicates that the answer is more precise and stable. ⟬<table>14⟭⟬<table>15⟭⟬<table>16⟭⟬<table>17⟭Top P⟬<table>18⟭⟬<table>19⟭Control the randomness and diversity of answers. The smaller the number, the more conservative and predictable the generated text will be; the larger the number, the more diverse the generated text will be. ⟬<table>20⟭⟬<table>21⟭top P＝0.5⟬<table>22⟭, only the words with the sum of the top 50% probability that are most likely to appear in the system are considered, and words with low probability of occurrence are excluded. ⟬<table>23⟭⟬<table>24⟭⟬<table>25⟭⟬<table>26⟭Max Tokens⟬<table>27⟭⟬<table>28⟭Limit the maximum length of the assistant output. ⟬<table>29⟭⟬<table>30⟭⟬<table>31⟭⟬<table>32⟭
