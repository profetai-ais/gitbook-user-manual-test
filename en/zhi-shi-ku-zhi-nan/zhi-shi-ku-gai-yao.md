# Knowledge Base Summary

## Introduction

AI Studio's "knowledge base" feature provides application developers with an easy-to-use interface to easily manage personal or team knowledge and can be seamlessly integrated into AI assistants. Developers can upload internal documents, frequently asked questions (FAQs), and standard operating instructions and process them into structured data that can be queried by large language models (LLMs).

Compared with the static pre-training data set built into the AI ​​model, the content in the knowledge base can be updated in real time, ensuring that LLM can access the latest information at any time and avoid problems caused by outdated or missing data.

When LLM receives a user query, the system will use Hybrid Search to search for the most relevant content in the knowledge base. Hybrid Search combines the following signal sources at the same time and combines the ranking results:

* Full-text Search: Use database full-text index (Postgres) to find paragraphs that highly match the query terms
* Vector Search: Use semantic similarity to find content that is consistent with the concept of the question but may not contain the same words.
* Chunk Summary Index: Use paragraph summary/key index to help locate key paragraphs in long documents to improve the focus of recall

The system will return highly relevant content fragments (Chunks) and provide them to LLM as context to generate more accurate and traceable answers. This method ensures that LLM not only relies on pre-trained knowledge, but also combines the latest internal documents and database content, reducing response bias caused by outdated or omitted data.

<figure><img src="../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

## **Main Advantages**

* **No data leakage**: Important corporate knowledge files are retained within the corporate environment and will not flow out of the internal network.
* **Real-time updates**: The knowledge base can be updated at any time to ensure that the model has the latest information.
* **Accuracy**: By retrieving relevant documents, LLM can generate answers based on actual information, reducing the risk of hallucination.
* **Flexibility**: Developers can customize the content of the knowledge base according to actual needs and define the required knowledge scope.

You only need to prepare text content, such as:

* Long text content (TXT, Markdown, DOCX, HTML, JSONL, even PDF files)
* Structured data (CSV, Excel, etc.)

Simply upload the file to the **Knowledge Base** and the data processing will be completed automatically.

## **Application Scenario**

If you want to create an AI customer service assistant based on the existing knowledge base and product files, you only need to upload the relevant files to the knowledge base of AI Studio, and then create the AI ​​assistant.

Traditionally, it may take weeks to develop a complete AI customer service chatbot from original text training, and it is difficult to effectively maintain and continuously improve. In AI Studio, the entire process only takes three minutes, and you can start collecting user feedback immediately.

## Knowledge and Datasets

In AI Studio, the knowledge base is composed of multiple **data sets**, and each **data set** can contain multiple data chunks (Chunks). You can integrate your entire knowledge base into your application as search context, from uploaded archives or content synced from other data sources.
