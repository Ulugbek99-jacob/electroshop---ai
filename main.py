import os
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq

app = FastAPI()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class Question(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "AI API is running!"}

@app.post("/chat")
def chat(question: Question):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": question.message}]
    )
    return {"reply": response.choices[0].message.content}
