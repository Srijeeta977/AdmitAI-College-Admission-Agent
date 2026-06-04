# 🎓 AdmitAI – RAG Based College Admission Assistant

## Problem Statement

**Problem Statement No. 4 – College Admission Agent (RAG Based)**

The challenge is to develop an AI-powered College Admission Agent capable of assisting prospective students with admission-related queries. The system retrieves information from official admission documents and generates accurate, context-aware responses using Retrieval-Augmented Generation (RAG) and IBM Granite Models.

---

## Project Overview

AdmitAI is an intelligent admission assistance platform that simplifies the college admission process by providing instant answers to student queries regarding:

* Eligibility Criteria
* Admission Procedures
* Required Documents
* Course Information
* Fee Structure
* Important Deadlines
* Frequently Asked Questions

The solution combines IBM Granite foundation models, IBM watsonx.ai, LangFlow orchestration, LangChain, ChromaDB, and Streamlit to deliver reliable and document-grounded responses.

---

## Key Features

✅ Retrieval-Augmented Generation (RAG)

✅ IBM Granite 8B Code Instruct Integration

✅ IBM watsonx.ai Integration

✅ LangFlow Workflow Orchestration

✅ Admission Brochure Knowledge Base

✅ Semantic Search using Vector Embeddings

✅ Streamlit-Based Interactive User Interface

✅ Real-Time Question Answering

✅ Context-Aware Response Generation

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python 3.10

### AI & LLM

* IBM Granite 8B Code Instruct
* IBM watsonx.ai

### Orchestration

* LangFlow

### RAG Components

* LangChain
* ChromaDB
* Vector Embeddings
* Semantic Search
* Retrieval-Augmented Generation

### Knowledge Source

* Admission Brochure PDF

### Development Tools

* GitHub
* VS Code

---

## System Architecture

The system follows a Retrieval-Augmented Generation pipeline:

Student Query
→ Streamlit Interface
→ Retriever
→ ChromaDB Vector Database
→ Admission Knowledge Base
→ IBM Granite 8B Code Instruct
→ AI Generated Response

Architecture and workflow diagrams are available in the assets folder.

---

## Project Workflow

1. Admission brochure is loaded and processed.
2. Documents are split into chunks.
3. Chunks are converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. User submits a query through Streamlit.
6. Relevant information is retrieved.
7. IBM Granite model generates the final response.
8. Response is displayed to the user.

---

## LangFlow Implementation

The project includes visual AI workflows built using LangFlow.

Implemented Components:

* Chat Input
* Prompt Template
* IBM Granite Model
* Knowledge Base
* Knowledge Ingestion
* Chat Output

Workflow exports are available in the `langflow/` directory.

---

## Repository Structure

AdmitAI/

├── assets/

├── docs/

├── langflow/

├── screenshots/

├── src/

├── requirements.txt

└── README.md

---

## Documentation

Available under `docs/`

* Problem Statement PDF
* Project Presentation PPTX

---

## Screenshots

Available under `screenshots/`

* Streamlit Homepage
* ## Streamlit User Interface

![Streamlit UI](## Streamlit User Interface

![Streamlit Homepage](https://raw.githubusercontent.com/Srijeeta977/AdmitAI-College-Admission-Agent/main/screenshots/streamlit_homepage.png))
* Query Demonstrations
* LangFlow Workflow
* Knowledge Base Workflow
* IBM watsonx.ai Usage Statistics

---

## Installation

### Clone Repository

git clone <repository-url>

### Install Dependencies

pip install -r requirements.txt

### Run Application

streamlit run src/streamlit_app.py

---

## Results

* Successfully implemented RAG-based admission assistant.
* Successfully integrated IBM watsonx.ai.
* Successfully integrated IBM Granite 8B Code Instruct.
* Successfully implemented LangFlow orchestration.
* Successfully created document-grounded admission guidance.
* Successfully demonstrated semantic search and intelligent retrieval.

---

## Novelty & Uniqueness

* RAG-Based Admission Intelligence
* Document-Grounded Responses
* IBM Granite Powered Reasoning
* LangFlow Visual Orchestration
* Semantic Knowledge Retrieval
* Scalable and Enterprise-Ready Design

The solution functions as an intelligent admission advisor rather than a traditional FAQ chatbot.

---

## Future Scope

* Multi-College Admission Support
* Voice Assistant Integration
* Multilingual Support
* Personalized Course Recommendations
* Real-Time Admission Updates
* Automated Application Guidance
* AI-Powered Virtual Admission Counselor

---

## Authors

Developed as part of the IBM SkillsBuild Internship Project.

---

## License

This project is intended for educational and internship demonstration purposes.
