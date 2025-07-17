# app.main:app --host 127.0.0.1 --port 8000
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.summarizer import generate_summary_rag
from app.retriever import build_knowledge_base

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def load_context():
    # Load and preprocess your context
    with open("data/context_chunks.txt", "r", encoding="utf-8") as f:
        context_data = f.read().split("\n\n")  # Separate chunks by double newline
    build_knowledge_base(context_data)

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "summary": ""})

# @app.post("/summarize/", response_class=HTMLResponse)
# async def summarize(request: Request, dialogue: str = Form(...)):
#     summary = generate_summary_rag(dialogue)
#     return templates.TemplateResponse("index.html", {
#         "request": request,
#         "summary": summary,
#         "original": dialogue
#     })

@app.post("/summarize/", response_class=HTMLResponse)
async def summarize(request: Request, dialogue: str = Form(...), use_rag: str = Form(None)):
    try:
        if use_rag:
            summary = generate_summary_rag(dialogue)
        else:
            from app.summarizer import generate_summary  # fallback
            summary = generate_summary(dialogue)
    except Exception as e:
        summary = f"An unexpected error occurred: {str(e)}"
        
    # if use_rag:
    #     summary = generate_summary_rag(dialogue)
    # else:
    #     from app.summarizer import generate_summary  # fallback
    #     summary = generate_summary(dialogue)

    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "summary": summary,
        "original": dialogue,
        "use_rag": use_rag
    })




# from fastapi import FastAPI, Request, Form
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from app.summarizer import generate_summary

# app = FastAPI()

# # Mount templates and static
# templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# async def homepage(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request, "summary": ""})

# @app.post("/summarize/", response_class=HTMLResponse)
# async def summarize(request: Request, dialogue: str = Form(...)):
#     summary = generate_summary(dialogue)
#     return templates.TemplateResponse("index.html", {"request": request, "summary": summary, "original": dialogue})
