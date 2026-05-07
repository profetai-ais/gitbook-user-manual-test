---
description: "Click the knowledge card in the knowledge base page to enter the setting page."
---
---
# management knowledge

## **Page Navigation**

<figure><img src="../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">project</th><th width="180">Operation name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>return</td><td>Click to return to the knowledge base homepage</td></tr><tr><td>2</td><td>close</td><td>Click to minimize the menu area</td></tr><tr><td>3</td><td>Knowledge setting menu</td><td>Provides various knowledge settings and testing functions</td></tr><tr><td>4</td><td>Set input area</td><td>Open the corresponding operation page according to the menu item selected by the user</td></tr></tbody></table>

## **Basic settings**

Users can modify the name and description of knowledge through basic settings.

step:

1. Click the _Basic Settings_ item in the "Knowledge Settings Menu"
2. Edit the text in the Name or Description field
3. Click "Save" to complete the settings

> Note: The index model cannot be modified after it is selected when creating knowledge.

## **Dataset**

The data set setting page allows users to upload and manage files. The file types supported by AI Studio are:

* Long text content (such as TXT, Markdown, DOCX, HTML, JSONL, PDF that is not a pure image, etc.)
* Structured data (CSV, Excel, etc.)

<figure><img src="../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">project</th><th width="180">Operation name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>Edit table</td><td>Allows the user to edit the presentation of the table</td></tr><tr><td>2</td><td>refresh</td><td>Click to refresh the table</td></tr><tr><td>3</td><td>filter</td><td>Content can be filtered based on fields</td></tr><tr><td>4</td><td>my list</td><td>After turning it on, only the information you created will be displayed.</td></tr><tr><td>5</td><td>Batch download</td><td>Multiple items can be selected and downloaded in batches at one time</td></tr><tr><td>6</td><td>delete</td><td>After checking the data set in the list, a delete button will be displayed. Clicking it will delete the checked data set.</td></tr><tr><td>7</td><td>search</td><td>Users can enter keywords to filter</td></tr><tr><td>8</td><td>Add/Import</td><td>Upload the file, or create a blank dataset</td></tr><tr><td>9</td><td>operate</td><td>Users can edit or delete the corresponding data set</td></tr></tbody></table>

## **New data set**

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>

1. Click the _Dataset_ item in the "Knowledge Settings Menu"
2. Click the "Add/Import" button and select _Import file_
3. Click "Upload Area" to open the system window, select the file to be uploaded, and click _Next Page_ when finished.
4. In the data processing part, you can select the strategy for splitting the file content in the "File Processing" option on the left. Click _Generate Segmented Results_ and a preview of the split data will be displayed on the right. After confirming the processing method, click _Next Page_
5. Confirm the content again and click the "Upload" button to upload the file.
6. The page returns to the data set list. The data can be used after the file status bar displays "Complete".

### File upload restrictions

To ensure data processing performance and indexing quality, the data set has the following restrictions when importing files:

| project | limit |
| ---------- | -------------- |
| Maximum number of files imported at a time | Up to **100** files |
| Maximum size of a single file | 300MB |

Additional instructions:

* If any of the above limits is exceeded, the system will display a prompt message and prevent uploading. Please adjust the number of files or split the files and re-import them.
* If the file is a large file (such as a long PDF/DOCX), it is recommended to remove unnecessary images or appendix content first to avoid long processing time.

#### Download access control

The raw file download behavior of the dataset is affected by the "Dataset Access Permissions":

* Authorized users: can download/access original files in the data set list or data block view (subject to the operation buttons provided on the screen).
* Unauthorized users: When trying to download or access the original file, the system will block it and prompt insufficient permissions; some screens may not display the download entrance or set it to be inoperable.

If you need to authorize others to download/access the dataset file, the administrator can go to the "#Dataset Access Permissions" section at the bottom of this page, add organizations or users that can access the specified dataset, and save the settings.

#### Troubleshooting: Permission settings display abnormally

If the permission details are not displayed, the block is blank, or there is no content when expanded on the "Dataset Access Permissions" page, please try the following steps:

1. Click Refresh to reload the list, or switch to another menu and back.
2. Confirm that the target file/dataset is selected in the Dataset area on the left.
3. Confirm that the current account has permissions such as "AI Studio Administrator/Knowledge Base Administrator/Domain Expert/Collaborator" to manage the knowledge base; if not, please contact the administrator for assistance.

### Display of data set status information

Click the status icon to enter the location. For detailed operation methods, please refer to the page description.

&#x20;。

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

## **Data processing when adding new data sets**

Data processing after file upload supports the following two forms:

* **Direct Segmentation**: Apply user options for segmentation
* **QA segmentation**: Files with Q\&A ​​content are segmented by questions.

#### **Direct Segmentation**

When the original content does not have a clear question and answer structure, or users want to quickly create data segments, the "direct segmentation" mode can be enabled. The system will automatically divide paragraphs according to the settings.

<table><thead><tr><th width="180">Processing method</th><th>illustrate</th></tr></thead><tbody><tr><td>automatic</td><td>The system is preset to automatically segment the input content according to the length and language structure, which is suitable for situations where you can get started quickly without customizing rules. When the segmentation method is not specified, the system will perform preliminary segmentation using common symbols such as line breaks and periods.</td></tr><tr><td>Token segmentation</td><td>Split the text according to the set segment token length. It is recommended that the length of a single paragraph be controlled within the range of 100–1000 tokens to avoid semantic fragmentation or truncation of context.</td></tr><tr><td>Custom rules</td><td>Provides more detailed control. In addition to setting the paragraph length (recommended 100–1000) and overlapping range (such as 100 tokens), it also adds separator options to control segmentation.</td></tr><tr><td>Regex segmentation</td><td>By specific characters (such as <code>\\n</code>、<code>。</code>、<code>,</code>、<code>;</code>) to segment text; it can be used in combination with a variety of symbols and is suitable for general natural language processing scenarios.</td></tr></tbody></table>

<table><thead><tr><th width="180">Processing options</th><th width="200">Applicable segmentation methods</th><th>illustrate</th></tr></thead><tbody><tr><td>ideal length segment</td><td>Token segmentation and custom rules</td><td>You can set the target length of each paragraph (in tokens); the smaller the value, the thinner the segments, but the contextual link may be weakened; the larger the value, the more overlapping ranges are needed to ensure consistent context.</td></tr><tr><td>Overlapping range</td><td>Token segmentation and custom rules</td><td>Define the number of tokens (such as 100) that each paragraph repeats with the previous paragraph to improve context continuity. The recommended value is between 1 and the ideal length - 1; suitable for handling high-context content such as multi-turn conversations, technical documents, etc.</td></tr><tr><td>Custom separator</td><td>Custom rules</td><td>Set the symbol for identifying segment points, separated by semicolons. Example: Setting <code>;; ;'';</code> will appear in the text <code>;</code>、<code>(space)</code>、<code>''</code> segmentation occurs.</td></tr><tr><td>rule</td><td>Regex segmentation</td><td>User-defined segmented Regex syntax can be edited by clicking on the default segmented example below:<code>.+\\n?</code> (line break segmentation),<code>[^。]+。?</code> (Chinese period segmentation).</td></tr><tr><td>Remove final newline character</td><td>Regex segmentation</td><td>Whether to automatically remove blank lines at the end of paragraphs <code>\\n$</code> symbol.</td></tr></tbody></table>

> Recommendation: Use Token segmentation + overlapping range to effectively keep the semantics and context intact and avoid the statement being cut off causing information fragmentation and loss.

#### **QA Segmentation**

When processing question-and-answer document content (such as FAQs, customer service records, interview transcripts, etc.), you can improve structural recognition and semantic clarity through QA segmentation settings. The system provides the following parameters to help identify and segment questions and answer blocks.

<table><thead><tr><th width="200">Options</th><th>illustrate</th></tr></thead><tbody><tr><td>question prefix</td><td>Specifies an identifying string that begins the question (e.g. <code>Q:</code>、<code>question:</code>), the system will use this mark as the starting point of the new question paragraph.</td></tr><tr><td>answer prefix</td><td>Specify the identification string that begins the answer (e.g. <code>A:</code>、<code>answer:</code>), used to mark the answer content corresponding to the question.</td></tr><tr><td>remove prefix</td><td>When enabled, markup strings at the beginning of question and answer paragraphs (e.g. <code>Q:</code>、<code>A:</code>）。</td></tr><tr><td>prefix expression</td><td>Supports the use of regular expressions (Regex) to identify question and answer prefixes, which is suitable for scenarios where the format is not fixed or a large amount of data is converted. For example:<code>^Q[0-9]*:</code> Can match multiple issue numbers.</td></tr><tr><td>Remove last newline character</td><td>When enabled, extra newlines at the end of each QA block will be automatically removed.</td></tr></tbody></table>

## **View/Edit Dataset**

Clicking on a file name in the file list will open the _data block_ view page, allowing users to browse the indexed data content and edit it as needed.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">project</th><th width="180">Options</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>Data block tab</td><td>Display the data blocks generated after the file is split</td></tr><tr><td>2</td><td>Reference Archives Tab</td><td>Displays all files associated with the data block, including original files used for segmentation and files used as reference files</td></tr><tr><td>3</td><td>return</td><td>Click to return to the homepage of the data set</td></tr><tr><td>4</td><td>search bar</td><td>Allows users to enter text to search for relevant blocks of data</td></tr><tr><td>5</td><td>Add/Import</td><td>Click to manually add data blocks</td></tr><tr><td>6</td><td>edit</td><td>Click to display the data block <em>edit</em> and <em>delete</em> Operation options</td></tr></tbody></table>

## **Edit data block content**

Users can optimize the content of data blocks to improve the accuracy of data referenced when LLM generates responses, such as adding possible question expressions to Q\&A ​​type data blocks.

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>

1. Click the "Edit" button of the data block and select _Edit_
2. Click the "Edit" button in the upper right corner of the pop-up window to open the editing interface field
3. Click the "+" button to the right of the _Question_ title to add a question
4. After entering the question content, click the "✔️" button on the upper right side of the interface to save the changes.

## **Create Reference File**

When AI Studio generates a reply by quoting the content of the data set, it can add relevant files as reference sources, such as providing specific pages and pictures of PDF or PPT, etc.

<figure><img src="../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

1. Click on the "Reference Files" tab
2. Click the "+Create" button to open the system window, select the file to upload, and click _Confirm_ after completion.
3. Confirm that the file has been uploaded correctly in the _Reference File List_ and click the "Data Block" tab after confirmation.
4. Click the "Edit" button of the data block and select _Edit_
5. Click "Linked Files" on the left
6. Click the "+Create" button to open the new file window
7. After clicking "File Menu" to select the reference file, click _Confirm_ to complete the creation of the additional reference file.

## **test**

After creating a data set, users can use the Test function to ask questions and see which data blocks were referenced when generating responses. They can also score the search results by adjusting the search parameters, thereby optimizing the data content to improve the accuracy of the cited data.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

&#x20;

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

1. Click the _Test_ item in the "Knowledge Settings Menu"
2. Click the _gear button_ to the right of the "Search text" heading to open search parameter settings
3. It is generally recommended to check "Enable Rating" below
4. Click the "LLM Scoring Model" menu to select the model you want to use
5. Adjust the "Score Threshold" setting to filter the score requirements of search results. Only results that meet the score requirements will be displayed as relevant information in _Rating Results_
6. Click the "Confirm" button to save the parameter settings
7. Enter the content/question you want to query in the "Search text" and click the _Query_ button to submit
8. Search results will be listed in "Recall Results" and sorted by recall score.
9. Click on any _recall result_ to view the complete information content, and click the Index tab to view the index used by the system to retrieve that data block

## knowledge rights

The creator can grant access rights to other users through "Knowledge Permissions" (please refer to for role definition).

> Note: The creator is the default "manager", and each project can only have one owner.

<figure><img src="../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="80">project</th><th width="180">Operation name</th><th>illustrate</th></tr></thead><tbody><tr><td>1</td><td>Edit table</td><td>Allows the user to edit the presentation of the table</td></tr><tr><td>2</td><td>refresh</td><td>Refresh list after click</td></tr><tr><td>3</td><td>Content filtering</td><td>Advanced filtering of specific content</td></tr><tr><td>4</td><td>Status switching</td><td>Quickly switch status by selecting single or multiple selections on the table</td></tr><tr><td>5</td><td>Batch delete</td><td>After checking the items, the delete button in the upper left corner will be displayed, allowing users to delete multiple items.</td></tr><tr><td>6</td><td>search field</td><td>Search name</td></tr><tr><td>7</td><td>invite</td><td>Invite organizations/members</td></tr><tr><td>9</td><td>action</td><td>Transfer your role or remove selected users</td></tr></tbody></table>

### **New member**

<figure><img src="../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (76).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (77).png" alt=""><figcaption></figcaption></figure>

1. Click "Add" to open the conversation box
2. The input box can search for organizations or users
3. Select the corresponding permissions
4. Enter keywords to jump out to the corresponding organization/user
5. You can click the level button on the right to confirm the level of the character.
6. After selecting the target organization/user, you can click the label to open the view menu and view all users within the organization level and role.
7. Click the "Add" button to complete the invitation

## **Dataset access rights**

AI Studio provides data set access rights management, allowing enterprises to control the scope of information that different departments or users can reference when using generative AI based on information security requirements.

Access rights can be granted to organizations or individual users; if granted to an organization, all users in the organization have access to the data. For information on organization and related member settings, please refer to the Domain Twin Portal Operation Manual.

<figure><img src="../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

1. Click the _Dataset Access Permissions_ item in the "Knowledge Settings Menu"
2. Click the button to add permissions to the dataset batch
3. In the "Dataset" area, select the file for which you want to set permissions
4. Click the "Organization" tab in the right area and check the organizational level to which permissions are to be granted.
5. Click the "Users" tab in the right area to select the user to whom permissions are to be granted.
6. Search for the user you want to add in the "User Menu". After selecting, click the "+" button next to the menu to add a user.
7. After completing the changes to the organization and users, click the "Save" button in the upper right corner to retain the settings.
