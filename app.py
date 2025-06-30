from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import subprocess
import uuid

app = FastAPI()

@app.post("/tts")
async def tts(request: Request):
    data = await request.json()
    text = data.get("text", "")
    if not text:
        return {"error": "No text provided"}
    out_path = f"/tmp/{uuid.uuid4()}.wav"

    # Run Coqui TTS
    subprocess.run([
        "tts",
        "--text", text,
        "--out_path", out_path,
        "--model_name", "tts_models/en/ljspeech/tacotron2-DDC"
    ])

    return FileResponse(out_path, media_type="audio/wav", filename="speech.wav")

