#real time speech recognition and response program with deep learning
from asyncio.windows_events import NULL
from importlib.resources import path
import pyttsx3                              #text-to-speech module
import datetime                             #imporing time module to get time
import speech_recognition as sr             #importing speech_recongnition module to take vocal input
import wikipedia                            #wikipeia moudle for wikipedia results
import webbrowser                           #imporitng webbrowser module for web searchs
import pywhatkit                            #importing pywhatkit module for playing youtube video
import os                                   #importing os module for system file access
import random                               #using random moudle for random selection of any data
from datetime import date
from AppOpener import open,close

engine = pyttsx3.init('sapi5')              #sapi5 is a microsoft speech API for voice recognition
voices = engine.getProperty('voices')       #Assiging voices that available in device

engine.setProperty('voice',voices[1].id)    #Voice setting

def speak(audio):                           
    '''defining speak() function that will speak\say the given text/string '''
    engine.say(audio)
    engine.runAndWait()
    pass

def wishMe():                             
    '''defining wishMe() for Assistant to greet according to time'''
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

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

def voice_mode():
    query = takeCommand().lower()
    sites = [['youtube','https://www.youtube.com/'],['Google','https://www.google.com/'],['facebook','https://www.facebook.com/'],['map','https://www.google.co.in/maps'],['send email','https://mail.google.com/mail/u/0/#inbox?compose=new']]

    for site in sites:
        if f"Open {site[0]}".lower()  in query:
            print(f"Assistant: Oppening {site[0]}")
            speak(f"Oppening {site[0]}")
            webbrowser.open(site[1])
            

    if 'open' in query:
        query=query.replace('open','')
        open(f"{query}")

    elif 'wikipedia' in query:
        speak("Searching.")
        query = query.replace("wikipedia", "")
        query = query.replace("search", "")
        query = query.replace("on", "")
        result = wikipedia.summary(query, sentences=5)
        print(result)
        speak(result)

    elif 'play on youtube' in query:
        query = query.replace("play", "")
        query = query.replace("on youtube", "")
        speak(f"playing {query}")
        pywhatkit.playonyt(query)

    elif 'play music' in query:
        music_dr = 'F:\My Music World\Audios'
        songs=os.listdir(music_dr)
        player = random.choice(songs)
        os.startfile(os.path.join(music_dr, player))
    
    elif 'the time' in query:
        timenow=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {timenow}")

    elif 'open whatsapp' in query:
        speak(f"opening {query}")
        open("whatsapp beta")

    elif 'what is my name' in query:
        speak(f"your Name is {myname}")
    
    elif 'change my name' in query:
        speak("okay, sir What should i call you")
        myname=takeCommand()
        speak("Okay sir, I'll call you {myname}");
    
    elif 'what is' in query:
        query=query.replace("what is ", "")
        print(f"Assistant: searching {query}")
        speak("Here are some results from google")
        webbrowser.open(f"https://www.google.com/search?q={query}&sxsrf=APq-WBtgnhxglCPeSjYuXSjbcJmvw2eHTA%3A1643545268919&source=hp&ei=tIL2YbbtNd6H4-EPsv6isAM&iflsig=AHkkrS4AAAAAYfaQxFz1vh4c7fLpzfaZfHq5BTqGCVOB&ved=0ahUKEwi2l7Kfu9n1AhXewzgGHTK_CDYQ4dUDCAc&uact=5&oq=kite&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAguEIAEELEDMggILhCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggILhCABBCxAzIICAAQgAQQsQMyBQgAELEDOgcIIxDqAhAnOgcILhDqAhAnOgQIIxAnOgUILhCABDoLCAAQgAQQsQMQgwE6CwguEIAEEMcBEKMCOgsILhCABBCxAxCDAVDrB1jYC2CYEGgBcAB4AIAB6AGIAcoFkgEFMC4zLjGYAQCgAQGwAQo&sclient=gws-wiz")

    elif 'send email' in query:
        speak("Okay! Opening Email")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
    
        
    elif 'good morning' in  query:
        hour = int(datetime.datetime.now().hour)
        if hour>=3 and hour<12:
            speak("Good Morning.")
            speak("Tell me how can I help you")
        else:
            timenow=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Well, it's {timenow}")
            speak("by the way Good morning sir")
            speak("please tell me how can i help you")

    elif 'good afternoon' in  query:
        hour = int(datetime.datetime.now().hour)
        if hour>=12 and hour<18:
            speak("Good Afternoon.")
            speak("what can i do for you sir")
        else:
            timenow=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Well, it's {timenow}")
            speak("by the way Good Afternoon sir")
            speak("please tell me how can i help you")

    elif 'good evening' in  query:
        hour = int(datetime.datetime.now().hour)
        if hour>=18:
            speak("Good Evening.")
            speak("what can i do for you sir")
        else:
            timenow=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Well, it's {timenow}")
            speak("by the way Good Evening sir")
            speak("please tell me how can i help you")

    elif 'good Night' in  query:
        hour = int(datetime.datetime.now().hour)
        if hour>=18:
            speak("Okay bye sir, Good Night sweet dreams")
            quit()

        else:
            timenow=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Well, it's {timenow}")
            speak("by the way Good Night sir")
            quit()

    elif 'change command mode' in query:
        speak("Okay! Changeing to Text Command")
        while True:
            text_mode()
    elif 'ok bye' in query:
        speak("Bye!! Have a Good day Abhishek")
        quit()
    
def text_mode():
            print("You: ",end='')
            query=input().lower()

            sites = [['youtube','https://www.youtube.com/'],['Google','https://www.google.com/'],['facebook','https://www.facebook.com/'],['map','https://www.google.co.in/maps'],['send email','https://mail.google.com/mail/u/0/#inbox?compose=new']]

            for site in sites:
                if f"Open {site[0]}".lower()  in query:
                    print(f"Assistant: Oppening {site[0]}")
                    speak(f"Oppening {site[0]}")
                    webbrowser.open(site[1])
            

            if 'open' in query:
                query=query.replace('open','')
                open(f"{query}")

            elif 'wikipedia' in query:
                speak("Searching.")
                query = query.replace("wikipedia", "")
                query = query.replace("search", "")
                query = query.replace("on", "")
                result = wikipedia.summary(query, sentences=5)
                print(result)
                speak(result)
        
            elif 'what is your name' in query:
                print("Assistant: I am your virtual Assistant Shirley.")
                speak("I am your virtual Assistant Shirley.")
                

            elif 'play on youtube' in query:
                query = query.replace("play", "")
                query = query.replace("on youtube", "")
                print(f"Assistant: playing {query}")
                speak(f"playing {query}")
                pywhatkit.playonyt(query)
        
            elif 'play music' in query:
                music_dr = 'F:\My Music World\Audios'
                songs=os.listdir(music_dr)
                player = random.choice(songs)
                os.startfile(os.path.join(music_dr, player))
                print(f"Assistant: playing {player}")
            
            elif 'time' in query:
                timenow=datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Assistant: sir the time is {timenow}")
                speak(f"sir the time is {timenow}")

            elif 'open whatsapp' in query:
                query.replace("open","")
                open(query)
        
            elif 'what is my name' in query:
                print(f"Assistant: your Name is {myname}")
                speak(f"your Name is {myname}")
            
            elif 'change my name' in query:
                print("Assistatn: okay, sir What should i call you")
                speak("okay, sir What should i call you")
                myname=input().upper()
                print(f"Assistant: Okay sir, I'll call you {myname}")
                speak(f"Okay sir, I'll call you {myname}")
                    
            elif 'what is' in query:
                query=query.replace("what is ", "")
                print(f"Assistant: searching {query}")
                speak("Here are some results from google")
                webbrowser.open(f"https://www.google.com/search?q={query}&sxsrf=APq-WBtgnhxglCPeSjYuXSjbcJmvw2eHTA%3A1643545268919&source=hp&ei=tIL2YbbtNd6H4-EPsv6isAM&iflsig=AHkkrS4AAAAAYfaQxFz1vh4c7fLpzfaZfHq5BTqGCVOB&ved=0ahUKEwi2l7Kfu9n1AhXewzgGHTK_CDYQ4dUDCAc&uact=5&oq=kite&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAguEIAEELEDMggILhCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggILhCABBCxAzIICAAQgAQQsQMyBQgAELEDOgcIIxDqAhAnOgcILhDqAhAnOgQIIxAnOgUILhCABDoLCAAQgAQQsQMQgwE6CwguEIAEEMcBEKMCOgsILhCABBCxAxCDAVDrB1jYC2CYEGgBcAB4AIAB6AGIAcoFkgEFMC4zLjGYAQCgAQGwAQo&sclient=gws-wiz")
                
            elif 'good morning' in  query:
                hour = int(datetime.datetime.now().hour)
                if hour>=3 and hour<12:
                    print("Assistant: Good Morning.")
                    speak("Good Morning.")
                    print("Assistant: what can i do for you sir")
                    speak("what can i do for you sir")
                else:
                    timenow=datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Assistant: Well, it's {timenow}")
                    speak(f"Well, it's {timenow}")
                    print("Assistant: by the way Good morning sir")
                    speak("by the way Good morning sir")
                    print("Assistant: please tell me how can i help you")
                    speak("please tell me how can i help you")

            elif 'good afternoon' in  query:
                hour = int(datetime.datetime.now().hour)
                if hour>=12 and hour<18:
                    print("Assistant: Good Afternoon.")
                    speak("Good Afternoon.")
                    print("Assistant: what can i do for you sir")
                    speak("what can i do for you sir")
                else:
                    timenow=datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Assistant: Well, it's {timenow}")
                    speak(f"Well, it's {timenow}")
                    print("Assistatn: by the way Good Afternoon sir")
                    speak("by the way Good Afternoon sir")
                    print("Assistant: please tell me how can i help you")
                    speak("please tell me how can i help you")

            elif 'good evening' in  query:
                hour = int(datetime.datetime.now().hour)
                if hour>=18:
                    print("Assistant: Good Evening")
                    speak("Good Evening.")
                    print("Assistant: please tell me how can i help you")
                    speak("please tell me how can i help you")
                else:
                    timenow=datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Assistant: Well, it's {timenow}")
                    speak(f"Well, it's {timenow}")
                    print("Assistant: by the way Good Evening sir")
                    speak("by the way Good Evening sir")
                    print("Assistant: please tell me how can i help you")
                    speak("please tell me how can i help you")

            elif 'good night' in  query:
                hour = int(datetime.datetime.now().hour)
                if hour>=18:
                    print("Assistant: Okay bye sir, Good Night sweet dreams")
                    speak("Okay bye sir, Good Night sweet dreams")
                    quit()
            

                else:
                    timenow=datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Assistant: Well, it's {timenow}")
                    speak(f"Well, it's {timenow}")
                    print("Assistant: By the way Good Night sir")
                    speak("by the way Good Night sir")
                    quit()
                
            elif 'send email' in query:
                speak("Okay! Opening Email")
                print(f"Assistant: Opening Email")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
            
            elif 'ok bye' in query:
                print(f"Okay, Bye! Have a good day!")
                speak("Okay, Bye! Have a good day!")
                quit()

            elif 'change command mode' in query:
                while True:
                    voice_mode()
            
if __name__ == "__main__":
    timenow=datetime.datetime.now().strftime("%H:%M:%S")
    speak("Activating Console!!")
    speak(f"Activation Time {timenow}")
    speak("Please select, Voice Command or Text Command")
    inpfr=input("Voice Command or Text Command\n")
    global myname
    myname="Abhishek Srivastava"
    inpfr=inpfr.lower()

    #if user choose voice command
    if 'voice' in inpfr:
        wishMe()
        speak("Hello Abishek, I am Shirley")
        speak("please tell me How can i help you?")

        while True:
            voice_mode()

    else:
        wishMe()
        speak("Hello Abishek, I am Shirley")
        speak("please tell me How can i help you?")
        while True:
            text_mode()


