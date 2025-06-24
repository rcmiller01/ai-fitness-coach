from fastapi import APIRouter, UploadFile
from app.services.voice_service import transcribe_audio, speak_text

router = APIRouter()

@router.post("/listen")
async def listen_voice(file: UploadFile):
    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    text = transcribe_audio(file_path)
    return {"message": text}

@router.get("/speak")
def speak(message: str):
    speak_text(message)
    return {"status": "spoken", "text": message}
