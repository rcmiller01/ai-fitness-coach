import os
import openai
import pyttsx3
import speech_recognition as sr

# Text to Speech
def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

# Speech to Text (Online Whisper)
def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]
