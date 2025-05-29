from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEmbeddings

# --- Config ---
LLM_MODEL_NAME = "google/flan-t5-small"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50
MAX_INPUT_TOKENS = 512
MAX_NEW_TOKENS = 150
TOP_K = 2

# --- Load tokenizer and model ---
tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(LLM_MODEL_NAME)
gen_pipeline = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=MAX_NEW_TOKENS,
    truncation=True,
)
llm = HuggingFacePipeline(pipeline=gen_pipeline)

# --- Load embeddings ---
embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

# --- Prompt template ---
prompt_template = """Use the following extracted parts of a document to answer the question.
Provide a concise, precise, and accurate answer. If you don't know, say "I don't know".
Context:
{context}
Question:
{question}
Answer:"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"],
)
