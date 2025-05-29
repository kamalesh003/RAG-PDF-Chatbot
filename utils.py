import tempfile
import os
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from config import (
    tokenizer,
    llm,
    embedding_model,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K,
    MAX_INPUT_TOKENS,
    PROMPT,
)

qa_chain = None

def truncate_context(text, max_tokens=MAX_INPUT_TOKENS):
    tokens = tokenizer.encode(text, truncation=True, max_length=max_tokens)
    return tokenizer.decode(tokens, skip_special_tokens=True)

def create_qa_chain(llm, retriever):
    return RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={
            "prompt": PROMPT,
            "document_variable_name": "context"
        },
    )

def process_pdf(pdf_file):
    global qa_chain
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(pdf_file)
        tmp_path = tmp.name

    loader = PyMuPDFLoader(tmp_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    split_docs = splitter.split_documents(docs)

    vectordb = FAISS.from_documents(split_docs, embedding_model)
    retriever = vectordb.as_retriever(search_kwargs={"k": TOP_K})

    qa_chain = create_qa_chain(llm, retriever)

    os.remove(tmp_path)
    return "✅ PDF processed and indexed. Ready for questions."

def answer_question(question):
    global qa_chain
    if qa_chain is None:
        return "⚠️ Please upload and process a PDF first."
    try:
        result = qa_chain.invoke({"question": question})
        answer = truncate_context(result.get("answer", "⚠️ No answer found."))
        sources = result.get("sources", "No sources.")
        return f"🧠 **Answer:**\n{answer.strip()}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

