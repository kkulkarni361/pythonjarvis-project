from typing import Text
from urllib.parse import quote_from_bytes
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
import webbrowser
import os

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Mooring!")
    
    elif hour>=12 and hour<=18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("I am jarvis sir. please tell me hoe may i help you")
#it take microphone input from user and return output

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listing...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        Query = r.recognize_google(audio,language="en-in")
        print(f"user said:{Query}\n")

    except Exception as e:
        #print(e)ca
        print("say that again please...")
        return "none"
    return Query

if __name__== "__main__":
    wishMe()
    while True:
        Query = takeCommand().lower()
        
    #logic for executing task based on query
        if 'wikipedia' in Query:
            speak("searching wikipedia...")
            Query = Query.replace("wekipedia","")
            results = wikipedia.summary(Query,sentences=2)
            speak("Acording to wikipedia")
            speak(results)

        elif 'open youtube' in Query:
            webbrowser.open("youtube.com")

        elif 'play music' in Query:
            music_dir = "G:\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif "the time" in Query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir time is {strTime}")

        elif 'open pycharm' in Query:
            pycharmpath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe"
            os.startfile(pycharmpath)