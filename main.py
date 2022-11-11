import speech_recognition as sr 
import pyaudio


def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Say something...")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f"You said: {text}")
    return text 



get_audio()