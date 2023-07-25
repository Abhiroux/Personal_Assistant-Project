from ast import Store
from typing import Mapping
import pyttsx3
import speech_recognition as SR
from Assist import takeCommand
import pyaudio
engine = pyttsx3.init('sapi5')
import datetime
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

if __name__ == '__main__':
    query = takecmd().lower()
    if 'Good morning' in query:
        speak("Good Morning Abhishek")
        speak("Tell me how can I help you")
    # elif 'What day is today' in Store:
        # now=datetime.datetime.now()
        # speak(f"It's {now}")


# for voice in voices:
#     print(voice)
#     speak(voice.name)
            
            
    
        

