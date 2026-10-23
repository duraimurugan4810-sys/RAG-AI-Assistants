import os
import shutil

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ==================================================
# VERSION 10 - CREATE RAG DATABASE
# Supports Markdown and PDF
# ==================================================

DATA_FOLDER = "data"
CHROMA_FOLDER = "chroma_db"


print("=" * 60)
print("DURAI AI - CREATING RAG DATABASE")
print("=" * 60)


# ==================================================
# 1. Check data folder
# ==================================================

if not os.path.exists(DATA_FOLDER):

    print("ERROR: data folder does not exist.")

    exit()


# ==================================================
# 2. Load Markdown and PDF documents
# ==================================================

documents = []


for filename in os.listdir(DATA_FOLDER):

    file_path = os.path.join(
        DATA_FOLDER,
        filename
    )


    # ----------------------------------------------
    # Markdown
    # ----------------------------------------------

    if filename.lower().endswith(".md"):

        print(f"Loading: {filename}")

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                text = file.read()


            if text.strip():

                documents.append(
                    {
                        "text": text,
                        "source": filename
                    }
                )

        except Exception as e:

            print(
                f"ERROR reading {filename}: {e}"
            )


    # ----------------------------------------------
    # PDF
    # ----------------------------------------------

    elif filename.lower().endswith(".pdf"):

        print(f"Loading PDF: {filename}")

        try:

            from pypdf import PdfReader

            reader = PdfReader(file_path)

            text = ""


            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"


            if text.strip():

                documents.append(
                    {
                        "text": text,
                        "source": filename
                    }
                )

        except Exception as e:

            print(
                f"ERROR reading {filename}: {e}"
            )


# ==================================================
# 3. Check documents
# ==================================================

print()
print(
    f"Documents loaded: {len(documents)}"
)


if len(documents) == 0:

    print()
    print("ERROR: No documents were loaded.")

    exit()


# ==================================================
# 4. Split documents into chunks
# ==================================================

print()
print("Splitting documents into chunks...")


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)


chunks = []
metadatas = []


for document in documents:

    split_texts = text_splitter.split_text(
        document["text"]
    )


    for chunk in split_texts:

        if chunk.strip():

            chunks.append(chunk)

            metadatas.append(
                {
                    "source": document["source"]
                }
            )


print(
    f"Total chunks created: {len(chunks)}"
)


# ==================================================
# 5. Remove old Chroma database
# ==================================================

if os.path.exists(CHROMA_FOLDER):

    print()
    print("Removing old Chroma database...")

    try:

        shutil.rmtree(CHROMA_FOLDER)

    except PermissionError:

        print()
        print(
            "ERROR: ChromaDB is currently being used."
        )

        print(
            "Stop Streamlit/Python and run this again."
        )

        exit()


# ==================================================
# 6. Load embedding model
# ==================================================

print()
print("Loading embedding model...")


embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# ==================================================
# 7. Create Chroma database
# ==================================================

print()
print("Creating Chroma vector database...")


vector_db = Chroma.from_texts(
    texts=chunks,
    embedding=embeddings,
    metadatas=metadatas,
    persist_directory=CHROMA_FOLDER
)


# ==================================================
# 8. Finished
# ==================================================

print()
print("=" * 60)
print("RAG DATABASE CREATED SUCCESSFULLY!")
print("=" * 60)

print()
print(f"Documents: {len(documents)}")
print(f"Chunks: {len(chunks)}")
print(f"Database: {CHROMA_FOLDER}")

print()
print("Indexed documents:")

for document in documents:

    print(
        "  ✓",
        document["source"]
    )

print()
print("Your RAG knowledge base is ready.")