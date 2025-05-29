import gradio as gr
from utils import process_pdf, answer_question

# --- Gradio UI ---
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 RAG PDF Chatbot (Flan-T5 Small + FAISS + LangChain)")

    with gr.Row():
        pdf_input = gr.File(label="📄 Upload PDF", type="binary")
        upload_btn = gr.Button("📥 Process PDF")
    upload_output = gr.Textbox(label="📌 Status")

    question_input = gr.Textbox(label="💬 Ask a Question", placeholder="e.g., What are the key insights in section 2?")
    ask_btn = gr.Button("🔍 Get Answer")
    answer_output = gr.Textbox(label="🧠 Response", lines=10)

    upload_btn.click(process_pdf, inputs=pdf_input, outputs=upload_output)
    ask_btn.click(answer_question, inputs=question_input, outputs=answer_output)

# --- Launch ---
demo.launch(server_name="0.0.0.0", server_port=7860)
