from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fake_model import async_batch_model
from fake_model import stream_model
from pathlib import Path
from fastapi.responses import FileResponse
import asyncio
from fake_model import batch_model

app = FastAPI()

@app.get("/health")
def health():
	return {"status": "ok"}

@app.get("/batch")
async def batch():
	result = await asyncio.to_thread(batch_model)
	return {"result": result}

@app.get("/stream")
def stream():
	return StreamingResponse(stream_model(), media_type="text/plain")

@app.get("/")
def home():
	return FileResponse(Path(__file__).parent / "index.html")
