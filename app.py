import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma

print("=" * 50)
print("Loading PDF...")
print("=" * 50)

import os

pdf_folder = "data"

documents = []

pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith(".pdf")]

print("\nLoading PDFs...\n")

for pdf in pdf_files:

    print(f"Loading: {pdf}")

    loader = PyPDFLoader(os.path.join(pdf_folder, pdf))

    documents.extend(loader.load())

print(f"\nTotal PDFs Loaded : {len(pdf_files)}")
print(f"Total Pages Loaded : {len(documents)}")
print(f"Total Pages : {len(documents)}")

print("=" * 50)
print("Splitting PDF into Chunks...")
print("=" * 50)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Total Chunks : {len(chunks)}")

print("=" * 50)
print("Creating Embeddings...")
print("=" * 50)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

print("Embeddings Model Loaded Successfully!")

print("=" * 50)
print("Creating Vector Database...")
print("=" * 50)

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

print("Vector Database Created Successfully!")
print("=" * 50)
print("Loading Llama 3.2...")
print("=" * 50)

llm = ChatOllama(
    model="llama3.2:3b"
)

print("Llama Loaded Successfully!")

print("=" * 50)

while True:

    question = input("\nAsk your question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    docs = vector_db.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question only using the information below.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    print("\n" + "=" * 60)
    print("Answer\n")
    print(response.content)
    print("=" * 60)

print("\n")
print("=" * 50)
print("Answer")
print("=" * 50)
print(response.content)