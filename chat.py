import os
import hashlib

from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


# ==========================================================
# DURAI AI ASSISTANT
# VERSION 10
# AUTOMATIC DOCUMENT RAG
# ==========================================================

DATA_FOLDER = "data"
CHROMA_FOLDER = "chroma_db"


# ==========================================================
# 1. Embeddings
# ==========================================================

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# ==========================================================
# 2. ChromaDB
# ==========================================================

vector_db = Chroma(
    persist_directory=CHROMA_FOLDER,
    embedding_function=embeddings
)


# ==========================================================
# 3. Llama
# ==========================================================

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


# ==========================================================
# 4. Text Splitter
# ==========================================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)


# ==========================================================
# 5. File Hash
# ==========================================================

def get_file_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:

            data = file.read(8192)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


# ==========================================================
# 6. Extract PDF Text
# ==========================================================

def extract_pdf(file_path):

    from pypdf import PdfReader

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

    return text


# ==========================================================
# 7. Read Document
# ==========================================================

def read_document(file_path):

    filename = os.path.basename(file_path)

    extension = os.path.splitext(
        filename
    )[1].lower()


    # PDF
    if extension == ".pdf":

        return extract_pdf(file_path)


    # Markdown
    elif extension == ".md":

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()


    # Text
    elif extension == ".txt":

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()


    else:

        return ""


# ==========================================================
# 8. Check Existing Document
# ==========================================================

def document_already_indexed(
    filename,
    file_hash
):

    try:

        result = vector_db.get(
            where={
                "source": filename
            }
        )

        ids = result.get(
            "ids",
            []
        )

        metadatas = result.get(
            "metadatas",
            []
        )


        if not ids:

            return False


        for metadata in metadatas:

            if metadata:

                if metadata.get(
                    "file_hash"
                ) == file_hash:

                    return True


    except Exception:

        return False


    return False


# ==========================================================
# 9. Delete Old Version of Document
# ==========================================================

def delete_old_document(filename):

    try:

        result = vector_db.get(
            where={
                "source": filename
            }
        )

        ids = result.get(
            "ids",
            []
        )

        if ids:

            vector_db.delete(
                ids=ids
            )

    except Exception:

        pass


# ==========================================================
# 10. Index One Document
# ==========================================================

def index_document(file_path):

    filename = os.path.basename(
        file_path
    )

    print(
        f"Checking document: {filename}"
    )


    # Calculate hash
    file_hash = get_file_hash(
        file_path
    )


    # Already indexed?
    if document_already_indexed(
        filename,
        file_hash
    ):

        print(
            f"Already indexed: {filename}"
        )

        return False


    # Read document
    text = read_document(
        file_path
    )


    if not text.strip():

        print(
            f"No readable text found: {filename}"
        )

        return False


    # Remove old version if it exists
    delete_old_document(
        filename
    )


    # Split into chunks
    chunks = text_splitter.split_text(
        text
    )


    documents = []

    for index, chunk in enumerate(
        chunks
    ):

        documents.append(
            Document(
                page_content=chunk,
                metadata={
                    "source": filename,
                    "file_hash": file_hash,
                    "chunk": index
                }
            )
        )


    # Add to Chroma
    if documents:

        vector_db.add_documents(
            documents=documents
        )


    print(
        f"Indexed: {filename}"
    )

    print(
        f"Chunks: {len(documents)}"
    )


    return True


# ==========================================================
# 11. Automatically Synchronize Data Folder
# ==========================================================

def sync_documents():

    os.makedirs(
        DATA_FOLDER,
        exist_ok=True
    )


    supported_extensions = [
        ".pdf",
        ".md",
        ".txt"
    ]


    files = os.listdir(
        DATA_FOLDER
    )


    indexed_count = 0


    for filename in files:

        extension = os.path.splitext(
            filename
        )[1].lower()


        if extension not in supported_extensions:

            continue


        file_path = os.path.join(
            DATA_FOLDER,
            filename
        )


        try:

            if index_document(
                file_path
            ):

                indexed_count += 1

        except Exception as error:

            print(
                f"Error indexing {filename}: {error}"
            )


    return indexed_count


# ==========================================================
# 12. Ask AI
# ==========================================================

def ask_ai(question):

    # Search all documents
    results = vector_db.similarity_search_with_score(
        question,
        k=8
    )


    if not results:

        return {
            "answer": (
                "I don't know based on the "
                "uploaded documents."
            ),
            "sources": [],
            "relevance": []
        }


    # ------------------------------------------------------
    # Build context
    # ------------------------------------------------------

    context_parts = []

    sources = []

    relevance = []


    for doc, score in results:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )


        context_parts.append(
            f"SOURCE: {source}\n\n"
            f"{doc.page_content}"
        )


        if source not in sources:

            sources.append(
                source
            )


        relevance.append(
            {
                "source": source,
                "score": round(
                    float(score),
                    4
                )
            }
        )


    context = "\n\n-------------------------\n\n".join(
        context_parts
    )


    # ------------------------------------------------------
    # Prompt
    # ------------------------------------------------------

    prompt = f"""
You are Durai AI Assistant.

You answer questions using the uploaded
knowledge base.

The knowledge base can contain ANY subject,
programming language, textbook, notes, PDF,
Markdown document, or study material.

IMPORTANT RULES:

1. Answer ONLY from the retrieved context.

2. Do not invent information.

3. Do not assume the user is asking about
   Python, C++, Java, or any specific language.

4. Identify the subject from the retrieved
   document content.

5. Do not mix information from unrelated
   documents.

6. If the retrieved context does not contain
   enough information to answer the question,
   say:

"I don't know based on the uploaded documents."

7. If the context contains programming code,
   explain it clearly.

8. If the user asks for code and the context
   contains the required concept, provide the
   appropriate code.

9. Give a clear and educational answer.

10. Mention the source document when useful.

==================================================
RETRIEVED CONTEXT
==================================================

{context}

==================================================
QUESTION
==================================================

{question}

==================================================
ANSWER
==================================================
"""


    # ------------------------------------------------------
    # LLM
    # ------------------------------------------------------

    response = llm.invoke(
        prompt
    )


    # ------------------------------------------------------
    # Return
    # ------------------------------------------------------

    return {
        "answer": response.content,
        "sources": sources,
        "relevance": relevance
    }