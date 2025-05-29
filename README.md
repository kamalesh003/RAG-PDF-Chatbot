# 🤖 RAG PDF Chatbot

A lightweight Retrieval-Augmented Generation (RAG) chatbot that allows users to upload a PDF, process it using chunked vector embeddings (FAISS), and query the document using natural language. This project uses:

* **Flan-T5 Small** as the language model
* **FAISS** for efficient document vector similarity search
* **LangChain** for orchestrating retrieval and generation
* **Gradio** for the web interface
* **Hugging Face Spaces** for public deployment

---

## 🚀 Features

* Upload any PDF file and get insights instantly
* Uses vector embeddings for semantic search
* Fast and efficient QA using Flan-T5
* Clean, modern Gradio UI
* Ready for deployment on Hugging Face Spaces

---

## 🧠 Architecture

```text
     ┌────────────┐
     │ Upload PDF │
     └────┬───────┘
          │
          ▼
      ┌─────────────┐
      │PyMuPDFLoader│
      └────┬────────┘
           ▼
  ┌────────────────────────┐
  │Text Splitter(Recursive)│
  └────────┬───────────────┘
           ▼
   ┌────────────────────┐
   │  FAISS Vector Store │
   └────────┬───────────┘
            ▼
   ┌────────────────────────┐
   │ Retrieval + Prompting  │◄───── User Question
   └────────┬───────────────┘
            ▼
   ┌───────────────────────┐
   │  Flan-T5 (Text2Text)  │
   └────────┬──────────────┘
            ▼
     Answer with Sources
```

---

## 🧩 Tech Stack

* `transformers`
* `langchain`
* `faiss-cpu`
* `PyMuPDF`
* `gradio`
* `sentence-transformers`

---

## 📦 Installation

```bash
# Clone the repo
$ git clone https://github.com/yourusername/rag-pdf-chatbot.git
$ cd rag-pdf-chatbot

# Install dependencies
$ pip install -r requirements.txt

# Optional: Download model weights locally (optional for Spaces)
$ transformers-cli download google/flan-t5-small
```

---

## 🛠️ Usage (Locally)

```bash
python app.py
```

Visit `http://localhost:7860` in your browser.

---

## 🌍 Public Deployment (Hugging Face Spaces)

This app is deployed on Hugging Face Spaces. [Click here to try it live](https://huggingface.co/spaces/higher5fh/pdf-chatbot).

To deploy it yourself:

1. Create a new Space (type: Gradio)
2. Upload all project files
3. Include `requirements.txt` and `app.py`
4. The Space will automatically launch

---

## 📁 Project Structure

```
rag-pdf-chatbot/
├── app.py                  # Gradio UI + interface
├── config.py               # Model and pipeline configuration
├── utils.py                # PDF processing and question answering
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

---

## 🔐 Security

* This project does not store any PDFs or user data.
* Runs entirely in memory.



## ❤️ Acknowledgments

* [LangChain](https://github.com/langchain-ai/langchain)
* [HuggingFace Transformers](https://huggingface.co/docs/transformers)
* [Gradio](https://gradio.app)
* [Sentence-Transformers](https://www.sbert.net/)
* [FAISS](https://github.com/facebookresearch/faiss)

---


