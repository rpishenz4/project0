import speech_recognition as sr 
import pyaudio
import os 
import time 
import playsound
from gtts import gTTS
"""
def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Say something...")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f"You said: {text}")
    return text 



tmp = get_audio()
"""
def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

print("Hello World")
speak("Hello World")