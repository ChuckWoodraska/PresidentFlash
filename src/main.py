from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger
from src.game_logic import GameLogic
import os

app = FastAPI(root_path="/president-flash")
game_logic = GameLogic()

# Setup templates
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def startup_event():
    logger.info("Application starting up...")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    logger.info("Generating new question")
    question_data = game_logic.generate_question()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "question": question_data["question"],
        "options": question_data["options"],
        "correct_answer": question_data["correct_answer"]
    })

@app.post("/check", response_class=HTMLResponse)
async def check_answer(request: Request, answer: str = Form(...), correct_answer: str = Form(...)):
    is_correct = answer == correct_answer
    logger.info(f"Answer checked: {answer} (Correct: {correct_answer}) - Result: {is_correct}")

    question_data = game_logic.generate_question()
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "question": question_data["question"],
        "options": question_data["options"],
        "correct_answer": question_data["correct_answer"],
        "last_result": "Correct!" if is_correct else f"Incorrect. The answer was {correct_answer}."
    })
