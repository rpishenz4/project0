import speech_recognition as sr 
import pyttsx3
import os 
import time 
import playsound
from gtts import gTTS
from datetime import datetime


'''
def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Say something...")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f"You said: {text}")
    return text 



tmp = get_audio()
'''

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
                
        #listens for the user's input
        audio2 = r.listen(source)
            
        # Using google to recognize audio
        MyText = r.recognize_google(audio)
        MyText = MyText.lower()

        print("Did you say ",MyText)
        speak(MyText)


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

listen()
speak("I am sorry anthony. I will be nice to you from now on")
#task("time")