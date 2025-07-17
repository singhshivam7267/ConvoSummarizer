# ConvoSummarizer


## 🧠 RAG-Enhanced Text Summarization App

This is a FastAPI-based application that summarizes input text using a fine-tuned Pegasus model. It supports both:

- ✨ **Standard Summarization** (without context)
- 🔍 **RAG (Retrieval-Augmented Generation)** — retrieves relevant knowledge from a context base (`context_chunks.txt`)

---

## 📦 Project Structure

```

project-root/
├── app/
│   ├── model/                    # Fine-tuned Pegasus model (tokenizer + model)
│   ├── summarizer.py            # Summary generation logic (RAG + fallback)
│   ├── retriever.py             # FAISS-based context retrieval
│   ├── context\_chunks.txt       # Static knowledge base
│   ├── main.py                  # FastAPI backend
│   └── templates/
│       └── home.html            # UI template
├── requirements.txt
└── README.md

````

---

## 🔧 Installation

1. **Clone the repository** and navigate into it:
   ```bash
   git clone <your-repo-url>
   cd your-repo-name
````

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Build FAISS Index from context\_chunks.txt

To enable RAG-based summarization, you need to embed and index your context first.

You can do this in a one-time script or at FastAPI startup.

### 🔨 Option 1: One-time script (`scripts/build_index.py`)

```python
# scripts/build_index.py
from app.retriever import build_knowledge_base

with open("app/context_chunks.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

build_knowledge_base(lines)
print("✅ FAISS index built and ready.")
```

Run it:

```bash
python scripts/build_index.py
```

---

## 🚀 Run FastAPI App

```bash
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 🧪 How It Works

### 1. `generate_summary(text)`

* Uses the Pegasus model to summarize input without external context.

### 2. `generate_summary_rag(text)`

* Retrieves top-3 similar context chunks from FAISS (built from `context_chunks.txt`)
* Appends them to input before summarizing.

```python
# summarizer.py
def generate_summary_rag(text: str) -> str:
    context = retrieve_context(text)
    augmented_input = f"{context}\n\n{text}"
    return summarizer_pipeline(augmented_input)[0]['summary_text']
```

---

## 🧠 retrieve\_context(query)

* FAISS index is created from static chunks.
* Finds top-k relevant items for a given query using sentence-transformer embeddings.

```python
def retrieve_context(query: str, top_k: int = 3):
    ...
    D, I = index.search(query_embedding, top_k)
    return "\n".join([documents[i] for i in I[0]])
```

---

## 🌐 UI Behavior

* User enters input in the form
* Selects **"Use RAG"** checkbox (optional)
* Summary output appears in styled UI box


## 🛠 Technologies Used

* 🤗 [Transformers (Pegasus)](https://huggingface.co/transformers/)
* 🧠 [Sentence-Transformers](https://www.sbert.net/)
* 🧬 [FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss)
* ⚡ [FastAPI](https://fastapi.tiangolo.com/)
* 🌐 HTML/CSS (Jinja2 templates)

---
