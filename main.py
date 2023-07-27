import pyttsx3
import datetime
from intent_classification.intent_classification import IntentClassifier
intent_classifier = IntentClassifier()
from assistant_functions.weather import get_weather
from assistant_functions.assitant_functions import *
import speech_recognition as sr

engine = pyttsx3.init('sapi5')              #sapi5 is a microsoft speech API for voice recognition
voices = engine.getProperty('voices')       #Assiging voices that available in device

engine.setProperty('voice',voices[1].id)    #Voice setting

def speak(audio):                           
    '''defining speak() function that will speak\say the given text/string '''
    engine.say(audio)
    engine.runAndWait()
    pass

def takeCommand():
    ''' it takes voice input form the user and returns that input as a stirng'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f": {query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "none"
    return query


class Assistant:
    def __init__(self, name): 
        self.name = name

    def reply(self, text):
        intent = intent_classifier.predict(text)
        replies = {
            'weather' : get_weather,
            'greeting': get_Greetings,
            'leaving': Leave,
            'app_open': Open_exe(text),
            'assist_intro': AssistantIntro,
            'open spotify':openSpotify,
            'well_being': well_being(text),
            'play_music': play_music
        }
        reply_func = replies[intent]
        if callable(reply_func):
            try:
                print(f"Assistant: {reply_func()}")
                speak(reply_func())
            except Exception as e:
                print(f"Error: {e}")

    def wishMe(self):                             
        '''defining wishMe() for Assistant to greet according to time'''
        hour = int(datetime.datetime.now().hour)
        if hour>=3 and hour<12:
            speak("Good Morning!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!")

    def main(self):
        self.wishMe()
        while True:
            said = takeCommand()
            self.reply(said)


assistant = Assistant("Shirley")
assistant.main()
