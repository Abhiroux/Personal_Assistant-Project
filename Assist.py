from asyncio.windows_events import NULL
from cgi import print_directory
from importlib.resources import path
from re import search
from typing import Mapping
from unittest import result
import pyttsx3                              #text-to-speech module
import datetime                             #imporing time module to get time
import speech_recognition as sr             #importing speech_recongnition module to take vocal input
import wikipedia                            #wikipeia moudle for wikipedia results
import webbrowser                           #imporitng webbrowser module for web searchs
import pywhatkit                            #importing pywhatkit module for playing youtube video
import os                                   #importing os module for system file access
import random                               #using random moudle for random selection of any data
from datetime import date

engine = pyttsx3.init('sapi5')              #sapi5 is a microsoft speech API for voice recognition
voices = engine.getProperty('voices')       #Assiging voices that available in devic

engine.setProperty('voice',voices[2].id)    #Voice setting

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
        # print(e)
        print("say that again please...")
        return "none"
    return query

if __name__ == "__main__":
    timenow=datetime.datetime.now().strftime("%H:%M:%S")
    speak("Activating Console!!")
    speak(f"Activation Time {timenow}")
    speak("Please select, Voice Command or Text Command")
    inpfr=input("Voice Command or Text Command\n")
    myname="Abhishek Srivastava"
    inpfr=inpfr.lower()
    if 'voice' in inpfr:
        wishMe()
        speak("I am Shirley sir")
        speak("please tell me How can i help you?")

        while True:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak("Searching.")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=5)
                print(result)
                speak(result)
        
            elif 'play' in query:
                query = query.replace("play", "")
                speak(f"playing {query}")
                pywhatkit.playonyt(query)

            elif 'open google' in query:
                query = query.replace("open","")
                speak(f"opening {query}")
                webbrowser.open("google.com")

            elif 'open facebook' in query:
                query = query.replace("open","")
                speak(f"opening {query}")
                webbrowser.open("facebook.com")
        
            elif 'open map' in query:
                query = query.replace("open","")
                speak(f"opening {query}")
                webbrowser.open("https://www.google.co.in/maps")
        
            elif 'play music' in query:
                music_dr = 'E:\\My Music World\\Audios'
                songs=os.listdir(music_dr)
                print(songs )
                os.startfile(os.path.join(music_dr, random.choice(songs)))
            
            elif 'the time' in query:
                timenow=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir the time is {timenow}")

            elif 'open code' in query:
                path="C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak(f"opening")
                os.startfile(path)
        
            elif 'open whatsapp' in query:
                path="C:\\ProgramData\\ASUS\\WhatsApp\\WhatsApp.exe"
                query=query.replace("open","")
                speak(f"opening {query}")
                os.startfile(path)
        
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

            elif 'ok bye' in query:
                speak("Bye!! Have a Good day sir")
                break
            
            elif 'send email' in query:
                speak("Okay! Opening Email")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
                
            elif 'good morning' in  query:
                hour = int(datetime.datetime.now().hour)
                if hour>=3 and hour<12:
                    speak("Good Morning.")
                    speak("what can i do for you sir")
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
                    break

                else:
                    timenow=datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Well, it's {timenow}")
                    speak("by the way Good Night sir")
                    break

                    
            # elif '' in query:
            #     engine.runAndWait()


            # else:
            #     speak(f"I found these Results on google regarding {query}")
            #     webbrowser.open(f"https://www.google.com/search?q={query}&sxsrf=APq-WBtgnhxglCPeSjYuXSjbcJmvw2eHTA%3A1643545268919&source=hp&ei=tIL2YbbtNd6H4-EPsv6isAM&iflsig=AHkkrS4AAAAAYfaQxFz1vh4c7fLpzfaZfHq5BTqGCVOB&ved=0ahUKEwi2l7Kfu9n1AhXewzgGHTK_CDYQ4dUDCAc&uact=5&oq=kite&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAguEIAEELEDMggILhCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggILhCABBCxAzIICAAQgAQQsQMyBQgAELEDOgcIIxDqAhAnOgcILhDqAhAnOgQIIxAnOgUILhCABDoLCAAQgAQQsQMQgwE6CwguEIAEEMcBEKMCOgsILhCABBCxAxCDAVDrB1jYC2CYEGgBcAB4AIAB6AGIAcoFkgEFMC4zLjGYAQCgAQGwAQo&sclient=gws-wiz")


    else:
        wishMe()
        print("Assistant: I am Shirley sir")
        speak("I am Shirley sir")
        speak("please tell me How can i help you?")
        while True:
            print("You: ",end='')
            query=input().lower()

            if 'wikipedia' in query:
                speak("Searching.")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=5)
                print(result)
                speak(result)
        
            elif 'what is your name' in query:
                print("I am your virtual Assistant Shirley.")
                speak("I am your virtual Assistant Shirley.")
                

            elif 'youtube' in query:
                query = query.replace("play", "")
                print(f"Assistant: playing {query}")
                speak(f"playing {query}")
                pywhatkit.playonyt(query)

            elif 'open google' in query:
                query = query.replace("open","")
                print(f"Assistant: opening {query}")
                speak(f"opening {query}")
                webbrowser.open("google.com")

            elif 'open facebook' in query:
                query = query.replace("open","")
                print(f"Assistant: opening {query}")
                speak(f"opening {query}")
                webbrowser.open("facebook.com")
        
            elif 'open map' in query:
                query = query.replace("open","")
                print(f"Assistant: opening {query}")
                speak(f"opening {query}")
                webbrowser.open("https://www.google.co.in/maps")
        
            elif 'play music' in query:
                music_dr = 'E:\\My Music World\\Audios'
                songs=os.listdir(music_dr)
                print(f"Assistant: playing {random.choice(songs)}")
                os.startfile(os.path.join(music_dr, random.choice(songs)))
            
            elif 'time' in query:
                timenow=datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Assistant: sir the time is {timenow}")
                speak(f"sir the time is {timenow}")

            elif 'open code' in query:
                path="C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                print(f"Assistatn: opening")
                speak(f"opening")
                os.startfile(path)
        
            elif 'open whatsapp' in query:
                path="C:\\ProgramData\\ASUS\\WhatsApp\\WhatsApp.exe"
                query=query.replace("open","")
                print(f"Assistant: opening {query}")
                speak(f"opening {query}")
                os.startfile(path)
        
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
                    break

                else:
                    timenow=datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Assistant: Well, it's {timenow}")
                    speak(f"Well, it's {timenow}")
                    print("Assistant: By the way Good Night sir")
                    speak("by the way Good Night sir")
                    break

            elif 'ok bye' in query:
                break
            
            else:
                print(f"I found these Results on google regarding {query}")
                speak(f"I found these Results on google regarding {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}&sxsrf=APq-WBtgnhxglCPeSjYuXSjbcJmvw2eHTA%3A1643545268919&source=hp&ei=tIL2YbbtNd6H4-EPsv6isAM&iflsig=AHkkrS4AAAAAYfaQxFz1vh4c7fLpzfaZfHq5BTqGCVOB&ved=0ahUKEwi2l7Kfu9n1AhXewzgGHTK_CDYQ4dUDCAc&uact=5&oq=kite&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAguEIAEELEDMggILhCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggILhCABBCxAzIICAAQgAQQsQMyBQgAELEDOgcIIxDqAhAnOgcILhDqAhAnOgQIIxAnOgUILhCABDoLCAAQgAQQsQMQgwE6CwguEIAEEMcBEKMCOgsILhCABBCxAxCDAVDrB1jYC2CYEGgBcAB4AIAB6AGIAcoFkgEFMC4zLjGYAQCgAQGwAQo&sclient=gws-wiz")

