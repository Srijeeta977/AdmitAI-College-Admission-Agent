import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from ibm_watsonx_ai.foundation_models import ModelInference

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AdmitAI",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM HEADER ----------------

st.markdown("""
# 🎓 AdmitAI
### Intelligent RAG-Based College Admission Assistant
""")

st.markdown("---")

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.header("📘 About Project")

    st.write("""
AdmitAI is an AI-powered College Admission Assistant built using:

- IBM Watsonx AI
- Retrieval-Augmented Generation (RAG)
- ChromaDB
- LangChain
- Streamlit
- Sentence Transformers
""")

    st.success("✅ IBM Cloud Integrated")
    st.success("✅ RAG Enabled")
    st.success("✅ Resume Ready Project")

# ---------------- IBM CREDENTIALS ----------------

API_KEY = "qO2Od-_wFbqYk-z-rHUsjx2n9bfkrIPBuD--nIZJCcv5"
PROJECT_ID = "f5320c3b-1459-4518-80fb-5ddec4e556f2"
URL = "https://au-syd.ml.cloud.ibm.com"

# ---------------- LOAD VECTOR DATABASE ----------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

# ---------------- IBM MODEL ----------------

parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 150,
    "temperature": 0.2
}

model = ModelInference(
    model_id="meta-llama/llama-3-3-70b-instruct",
    params=parameters,
    credentials={
        "apikey": API_KEY,
        "url": URL
    },
    project_id=PROJECT_ID
)

# ---------------- CHAT INTERFACE ----------------

# ---------------- CHAT HISTORY ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY OLD MESSAGES ----------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------------- USER INPUT ----------------

user_question = st.chat_input(
    "Ask your admission-related question..."
)

# ---------------- PROCESS USER MESSAGE ----------------

if user_question:

    # Show user message instantly
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):
        st.markdown(user_question)

    # AI response area
    with st.chat_message("assistant"):

        with st.spinner("AdmitAI is analyzing documents..."):

            # Retrieve relevant docs
            docs = vector_db.similarity_search(user_question, k=3)

            context = "\n\n".join(
                [doc.page_content for doc in docs]
            )

            prompt = f"""
You are AdmitAI, an intelligent AI-powered college admission assistant.

Rules:
- Answer ONLY from the provided context.
- Do NOT make up information.
- If answer is unavailable, reply:
"The information is not available in the current admission database."
- Keep responses professional and concise.
- Avoid repetition.

Context:
{context}

Student Question:
{user_question}

Answer:
"""

            # Generate AI response
            response = model.generate_text(
                prompt=prompt
            )

            # Display response
            st.markdown(response)

            # Optional expandable source context
            with st.expander("📄 Retrieved Context"):
                st.write(context)

    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })