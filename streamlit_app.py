import os
import streamlit as st

from chat import (
    ask_ai,
    sync_documents,
    index_document
)


# ==========================================================
# DURAI AI ASSISTANT
# VERSION 10
# AUTOMATIC DOCUMENT RAG
# ==========================================================


st.set_page_config(
    page_title="Durai AI Assistant",
    page_icon="🤖",
    layout="wide"
)


# ==========================================================
# Automatically sync documents
# ==========================================================

with st.spinner(
    "Checking knowledge base..."
):

    sync_documents()


# ==========================================================
# Session State
# ==========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("🤖 Durai AI")

    st.caption(
        "Automatic RAG Version 10"
    )

    st.divider()


    # ------------------------------------------------------
    # Upload
    # ------------------------------------------------------

    st.subheader(
        "📄 Add Document"
    )


    uploaded_file = st.file_uploader(
        "Upload PDF, Markdown or TXT",
        type=[
            "pdf",
            "md",
            "txt"
        ]
    )


    if uploaded_file is not None:

        os.makedirs(
            "data",
            exist_ok=True
        )


        save_path = os.path.join(
            "data",
            uploaded_file.name
        )


        # Save file
        with open(
            save_path,
            "wb"
        ) as file:

            file.write(
                uploaded_file.getbuffer()
            )


        # Automatically index it
        with st.spinner(
            "Adding document to knowledge base..."
        ):

            try:

                indexed = index_document(
                    save_path
                )


                if indexed:

                    st.success(
                        "✅ Document added "
                        "to knowledge base!"
                    )

                else:

                    st.info(
                        "Document is already "
                        "in the knowledge base."
                    )


            except Exception as error:

                st.error(
                    f"Error: {error}"
                )


    st.divider()


    # ------------------------------------------------------
    # Knowledge Base
    # ------------------------------------------------------

    st.subheader(
        "📚 Knowledge Base"
    )


    if os.path.exists(
        "data"
    ):

        files = os.listdir(
            "data"
        )


        documents = [
            file
            for file in files
            if file.lower().endswith(
                (
                    ".pdf",
                    ".md",
                    ".txt"
                )
            )
        ]


        if documents:

            for file in sorted(
                documents
            ):

                st.write(
                    "📄",
                    file
                )

        else:

            st.info(
                "No documents."
            )


    st.divider()


    # ------------------------------------------------------
    # RAG Information
    # ------------------------------------------------------

    st.subheader(
        "⚙️ RAG System"
    )

    st.write(
        "🔎 Retrieval: ChromaDB"
    )

    st.write(
        "📚 Documents: Automatic"
    )

    st.write(
        "🧩 Chunking: Automatic"
    )

    st.write(
        "🧠 Embeddings: nomic-embed-text"
    )

    st.write(
        "🤖 LLM: Llama 3.2"
    )


    st.divider()


    # ------------------------------------------------------
    # Clear Chat
    # ------------------------------------------------------

    if st.button(
        "🗑 Clear Chat"
    ):

        st.session_state.messages = []

        st.rerun()


# ==========================================================
# Main Page
# ==========================================================

st.title(
    "🤖 Durai AI Assistant"
)


st.write(
    "Ask questions from your complete knowledge base."
)


st.caption(
    "Upload any supported document — no code changes required."
)


st.divider()


# ==========================================================
# Previous Messages
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


        if message["role"] == "assistant":

            sources = message.get(
                "sources",
                []
            )


            relevance = message.get(
                "relevance",
                []
            )


            if sources:

                st.markdown(
                    "### 📚 Sources"
                )


                for source in sources:

                    st.write(
                        "📄",
                        source
                    )


            if relevance:

                with st.expander(
                    "🔎 Retrieval Details"
                ):

                    for item in relevance:

                        st.write(
                            f"📄 {item['source']} "
                            f"— distance: {item['score']}"
                        )


# ==========================================================
# Question
# ==========================================================

question = st.chat_input(
    "Ask anything about your documents..."
)


# ==========================================================
# Answer
# ==========================================================

if question:

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    with st.chat_message(
        "user"
    ):

        st.markdown(
            question
        )


    # AI response
    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "Searching your knowledge base..."
        ):

            try:

                result = ask_ai(
                    question
                )


                answer = result[
                    "answer"
                ]

                sources = result[
                    "sources"
                ]

                relevance = result[
                    "relevance"
                ]


                st.markdown(
                    answer
                )


                if sources:

                    st.markdown(
                        "### 📚 Sources"
                    )


                    for source in sources:

                        st.write(
                            "📄",
                            source
                        )


                if relevance:

                    with st.expander(
                        "🔎 Retrieval Details"
                    ):

                        for item in relevance:

                            st.write(
                                f"📄 {item['source']} "
                                f"— distance: {item['score']}"
                            )


            except Exception as error:

                answer = (
                    "An error occurred:\n\n"
                    f"`{error}`"
                )

                sources = []

                relevance = []

                st.error(
                    answer
                )


    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources,
            "relevance": relevance
        }
    )