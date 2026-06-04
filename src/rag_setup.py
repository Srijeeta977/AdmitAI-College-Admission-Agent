from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

# Path to PDF folder
pdf_folder = "data"

documents = []

# Load all PDFs
for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, file)
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())

print(f"\nLoaded {len(documents)} pages from PDFs.")

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} text chunks.\n")

# Preview first chunk
print("Sample Chunk:\n")
print(chunks[0].page_content[:1000])