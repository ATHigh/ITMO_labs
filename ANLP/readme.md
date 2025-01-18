# The Ultimate CheatSheet RAG System

![Project Banner](https://github.com/ATHigh/ITMO_labs/blob/a3e436477f96150df8297ab9ee40dbd8243321a6/ANLP/rag_concepts-4499b260d1053838a3e361fb54f376ec.png)
<small>Image source: https://python.langchain.com/docs/concepts/rag/</small>

## Description
This repository contains an advanced Retrieval-Augmented Generation
(RAG) system designed to work with cheat sheets and structured datasets.
It integrates a conversational AI pipeline to retrieve and generate
accurate, context-aware answers.
The system supports various file formats, including PDFs, images, text, code
and LaTeX files, with enhanced preprocessing using OCR
and embeddings for efficient information retrieval.

As [knowledge base](https://www.kaggle.com/datasets/timoboz/data-science-cheat-sheets)
files connected with various topics were taken.

[Langchain](https://python.langchain.com/docs/tutorials/rag/#detailed-walkthrough) library was used as simple and user-friendly framework to make
RAG system.

Here you will find 2 ways of designed RAG system:
1) Using graph
2) Using chain for question-answering against an index.

## Used Tools

- **Vector store**: `FAISS`
- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2` (22.7M params)
- **Text2text model**: `google/flan-t5-large` (783M params)
- **PDF & image processing**: `PyMuPDFLoader` and `Tesseract OCR` for scanned pages or images.

## Example of Implementation and Workflow
![Example Implementation](https://github.com/ATHigh/ITMO_labs/blob/a3e436477f96150df8297ab9ee40dbd8243321a6/ANLP/test.png)

1. **Load** Documents and Extract Text
2. **Split** into smaller chunks
3. **Store**: using a VectorStore and Embeddings model.
4. **Retrieve**: Given a user input, relevant splits are retrieved from storage using a Retriever. 
5. **Generate**: A ChatModel / LLM produces an answer using a prompt that includes both the question with the retrieved data

## Validation

To validate the accurate answers of RAG system several questions were taken
according to the knowledge base. File QA_for_validation.csv consists of 20
questions with different types of answers. As a result:
- Average time for answer: **__~15.20 sec__**
- Accuracy: **__65%__** were pretty good

## TO DO:
- [ ] Enhance multi-modal capabilities for additional file types.
- [ ] Optimize embeddings for better retrieval accuracy.
- [ ] Integrate support for real-time user feedback.
- [ ] Add benchmarking tools for RAG evaluation (e.g., BLEU, ROUGE).
- [ ] Develop a user-friendly web interface for the system.
