import pyttsx3
engine = pyttsx3.init('sapi5')              #sapi5 is a microsoft speech API for voice recognition
voices = engine.getProperty('voices')       #Assiging voices that available in device
engine.setProperty('voice',voices[1].id)    #Voice setting
from AppOpener import open
import os
import random,pywhatkit
import webbrowser 


def speak(audio):                           
    '''defining speak() function that will speak\say the given text/string '''
    engine.say(audio)
    engine.runAndWait()
    pass

def Leave():
    response = "Bye! Have a great day"
    print(f"Assistant: {response}")
    speak(response)
    quit()

def Open_exe(text):
    if 'open' in text:
        text=text.replace('open','')
        open(f"{text}")
        speak(f"opening {text}")

def AssistantIntro():
    return "I am your personal assistant, Shirley. please tell me how can I help you."

def get_Greetings():
    response = "Hello! How can I assist you?"
    return response

def musicPlayer():
    music_dr = 'F:\My Music World\Audios'
    songs=os.listdir(music_dr)
    player = random.choice(songs)
    os.startfile(os.path.join(music_dr, player))

def YoutubePlayer(text):
    text = text.replace("play", "")
    text = text.replace("on","")
    text = text.replace("youtube","")
    speak(f"playing {text}")
    pywhatkit.playonyt(text)

def openSpotify():
    print(f"Opening Spotify")
    open("spotify")

def well_being(text):
    if 'how are you' in text:
        print(f"Assistant: I am fine. you are very kind to ask, especially in these tempestuous times")
        speak("I am fine. you are very kind to ask, especially in these tempestuous times")
    elif 'fine' in text:
        print(f"I'm glad to hear it.")
        speak("I'm glad to hear it.")
    elif 'thank you' in text:
        print(f"Assistant: You are welcome!")
        speak(f"you are welcome!")

def send_email():
    speak("Okay! Opening Email")
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")



