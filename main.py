import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import AsyncOpenAI
from google import genai
app = FastAPI(title="Fisica Atomica")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def serve_chatbot():
    return FileResponse("charts.html")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)