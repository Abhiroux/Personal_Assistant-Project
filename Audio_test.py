from ast import Store
from typing import Mapping
import pyttsx3
import speech_recognition as SR
from Assist import takeCommand
import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)
# print(voices[1].id)

def speak(str):
    engine.say(str)
    engine.runAndWait()
    pass

def takecmd():
    r= SR.Recognizer()
    with SR.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        str = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(str, language= 'eng-in')
    except Exception as e:
        print("say that again please")
        return None
    return query

# if __name__ == '__main__':
#     Store = takecmd().lower()
#     if 'hello' or 'Hii' in Store:
#         speak("Hi! Abhi! How are you")
#         mssg=takecmd().lower()
#         if 'I am fine' in mssg:
#             speak("Great!, Tell me how can i do for you")
#         elif 'I am not good' in mssg:
#             speak("Ooh Sorry!, I am gonna play some songs that will help you to feel better")
for voice in voices:
    print(voice)
    speak(voice.name)
            
            
    
        

