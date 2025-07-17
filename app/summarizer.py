from app.retriever import retrieve_context
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import os

MODEL_DIR = "app/model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)
summarizer_pipeline = pipeline("summarization", model=model, tokenizer=tokenizer)

def generate_summary_rag(text: str) -> str:
    if not text.strip():
        return "No input provided."
    context = retrieve_context(text)
    augmented_input = f"{context}\n\n{text}"
    summary = summarizer_pipeline(augmented_input, max_length=128, min_length=30, do_sample=False)
    return summary[0]['summary_text']


def generate_summary(text: str) -> str:
    if not text.strip():
        return "No input provided."

    summary = summarizer_pipeline(text, max_length=128, min_length=30, do_sample=False)
    return summary[0]['summary_text']
















# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# # Path to your local model
# MODEL_DIR = "app/model"

# # Load tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
# model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)

# # Create pipeline
# summarizer_pipeline = pipeline("summarization", model=model, tokenizer=tokenizer)

# def generate_summary(text: str) -> str:
#     if not text.strip():
#         return "No input provided."
#     summary = summarizer_pipeline(text, max_length=128, min_length=30, do_sample=False)
#     return summary[0]['summary_text']
