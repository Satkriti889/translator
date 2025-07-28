import os
from fastapi import FastAPI, Request, Form, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


app = FastAPI()
templates = Jinja2Templates(directory="templates")

from agents.translator_agent import TranslatorAgent
from agents.vector_store import VectorStore

translator = TranslatorAgent()
vector_db = VectorStore()

class TranslationRequest(BaseModel):
    text: str
    direction: str = "en_to_ne"

@app.post("/api/translate")
async def api_translate(request: TranslationRequest):
    """Basic translation endpoint with caching"""
    try:
        similar = vector_db.search_similar(request.text, k=1)
        if similar:
            return {
                "translation": similar[0][1],
                "source": "cache",
                "direction": request.direction
            }

        if request.direction == "en_to_ne":
            translated_text = translator.translate_english_to_nepali(request.text)
        else:
            translated_text = translator.translate_nepali_to_english(request.text)

        if not translated_text:
            raise HTTPException(status_code=400, detail="Translation failed")

        vector_db.add_translation(request.text, translated_text)
        
        return {
            "translation": translated_text,
            "source": "gemini",
            "direction": request.direction
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def chat_interface(request: Request):
    """Basic web interface"""
    return templates.TemplateResponse("chat.html", {
        "request": request,
        "default_direction": "en_to_ne"
    })

@app.post("/translate", response_class=HTMLResponse)
async def web_translate(
    request: Request,
    text: str = Form(...),
    direction: str = Form("en_to_ne")
):
    """Web translation endpoint"""
    try:
        translation = await api_translate(TranslationRequest(
            text=text,
            direction=direction
        ))
        return templates.TemplateResponse("chat.html", {
            "request": request,
            "user_text": text,
            "translation": translation["translation"],
            "direction": direction
        })
    except HTTPException as e:
        return templates.TemplateResponse("chat.html", {
            "request": request,
            "error": e.detail,
            "user_text": text,
            "direction": direction
        })