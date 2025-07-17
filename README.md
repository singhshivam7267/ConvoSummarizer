# ConvoSummarizer


## 🧠 RAG-Enhanced Text Summarization App

This is a FastAPI-based application that summarizes input text using a fine-tuned Pegasus model. It supports both:

 <img width="1000" height="850" alt="image" src="https://github.com/user-attachments/assets/d06d58b5-624a-4f2f-9176-7c7b02f5469c" />
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



## 🔧 Installation

1. **Clone the repository** and navigate into it:
   ```bash
   git clone <your-repo-url>
   cd your-repo-name

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

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

