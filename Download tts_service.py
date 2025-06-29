import edge_tts
import asyncio
import os

OUTPUT_FILE = "mia_output.mp3"

EMOTIONAL_PRESETS = {
    "joy": {"rate": "+5%", "pitch": "+3%"},
    "sad": {"rate": "-5%", "pitch": "-4%"},
    "romantic": {"rate": "-2%", "pitch": "+2%"},
    "calm": {"rate": "-1%", "pitch": "-1%"},
    "anxious": {"rate": "+3%", "pitch": "+1%"},
    "stressed": {"rate": "+5%", "pitch": "-2%"},
    "tired": {"rate": "-6%", "pitch": "-3%"},
    "default": {"rate": "0%", "pitch": "0%"}
}

async def speak_text(text: str, emotion: str = "default", voice: str = "en-US-JennyNeural", outfile: str = OUTPUT_FILE):
    preset = EMOTIONAL_PRESETS.get(emotion, EMOTIONAL_PRESETS["default"])
    ssml = f"""<speak>
        <voice name='{voice}'>
            <prosody rate='{preset["rate"]}' pitch='{preset["pitch"]}'>
                {text}
            </prosody>
        </voice>
    </speak>"""
    communicate = edge_tts.Communicate(ssml, voice=voice, ssml=True)
    await communicate.save(outfile)
    return outfile

def speak(text: str, emotion: str = "default"):
    asyncio.run(speak_text(text, emotion))
    os.system(f"start {OUTPUT_FILE}" if os.name == "nt" else f"xdg-open {OUTPUT_FILE}")