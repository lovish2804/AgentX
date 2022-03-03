import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import pyjokes
import smtplib
import time
import subprocess

chrome="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning" + MASTER)
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon" + MASTER)  
  
    else:
        speak("Good Evening" + MASTER)   
    speak("Welcome to Agent x created by lovish!!") 
    speak("What do you want me to do for you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('28.dev.04@gmail.com', '28dev04..@')
    server.sendmail('28.dev.04@gmail.com', to, content)
    server.close()

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"You said: {query}\n")
        return query.lower()
    except Exception as e:
        speak("Say that again please")   
        query=None
        return query
    

speak("Agent X initiated")
speak("What should i call you sir?")
MASTER = takeCommand()
wishMe()
while(True):
    query = takeCommand()

    if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    elif 'exit' in query or 'stop' in query:
        speak("Okay, have a good day sir!!")
        break

    elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.get(chrome).open("youtube.com")
 
    elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.get(chrome).open("google.com")
 
    elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.get(chrome).open("stackoverflow.com")

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"Sir, the time is {strTime}") 

    elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "D:\\d\\Sangs"
            songs = os.listdir(music_dir)
            random = os.startfile(os.path.join(music_dir, songs[4]))

    elif "who are you" in query:
            speak("I am your virtual assistant")

    elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
    elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

    elif 'joke' in query:
            speak(pyjokes.get_joke())

    elif "who made you" in query or "who created you" in query:
            speak("I have been created by Lovish.")

    elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown /s')

    elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

    elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Agent X from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
    elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("You asked to Locate")
            speak(location)
            webbrowser.get(chrome).open("https://www.google.nl/maps/place/" + location + "")
    
    elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('ajentx.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
    elif "show note" in query:
            speak("Showing Notes")
            file = open("ajentx.txt", "r")
            print(file.read())
            speak(file.read(6))
 
    elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

    elif "agent x" in query:
             speak("Agent X in your service Mister"+MASTER)

    else:
        speak("i did not get you sir, speak again!!")
