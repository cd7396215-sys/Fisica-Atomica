import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

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
    # Asegúrate de que charts.html esté en la raíz de tu proyecto junto a main.py
    if os.path.exists("charts.html"):
        return FileResponse("charts.html")
    raise HTTPException(status_code=404, detail="Archivo charts.html no encontrado")

# Nota: Quitamos el bloque uvicorn.run de abajo ya que Vercel levanta la app automáticamente