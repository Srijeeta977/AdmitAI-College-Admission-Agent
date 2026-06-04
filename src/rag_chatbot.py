from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from ibm_watsonx_ai.foundation_models import ModelInference

# IBM Credentials
API_KEY = "qO2Od-_wFbqYk-z-rHUsjx2n9bfkrIPBuD--nIZJCcv5"
PROJECT_ID = "f5320c3b-1459-4518-80fb-5ddec4e556f2"
URL = "https://au-syd.ml.cloud.ibm.com"

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load Vector Database
vector_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

# IBM Watsonx Model
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

print("\n🎓 AdmitAI - RAG Based College Admission Assistant")
print("Type 'exit' to quit.\n")

while True:
    question = input("Student: ")

    if question.lower() == "exit":
        break

    # Retrieve relevant chunks
    docs = vector_db.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are AdmitAI, a professional AI-powered college admission assistant.

Rules:
- Answer ONLY from the provided context.
- Do NOT make up information.
- If answer is not present in context, reply ONLY:
"The information is not available in the current admission database."
- Keep answers concise and professional.
- Avoid repetition.
- Do not explain your thinking process.

Context:
{context}

Student Question:
{question}

Answer:
"""

    response = model.generate_text(prompt=prompt)

    print("\nAdmitAI:\n")
    print(response)
    print("\n")