from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()

class Question(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "AI API ishlayapti!"}

@app.post("/chat")
def chat(question: Question):
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": question.message}]
    )
    return {"reply": response.message.content}