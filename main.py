import speech_recognition as sr 
#import pyaudio
import os 
import time 
import playsound
from gtts import gTTS
from datetime import datetime


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



def task(text):
    speak(f"Searching for command: {text}")
    if text == "time":
        timenow = datetime.now()
        curr_time = timenow.strftime("%H:%M:%S")
        speak(curr_time)
    else:
        speak("No command found please try again")


speak("Fuck you Tim")
#task("time")