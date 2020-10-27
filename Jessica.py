import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import random
import datetime
import os
import datef
import wolframalpha

try:
    app = wolframalpha.Client("4WEHAE-89P6J7XW7V")
except Exception:
    print("No results found")
    speak("Sorry sir, no results found")

random = ("good evening sir, Jessica online, how may I help you?")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning sir, jessica online")
        elif hour >= 12 and hour < 17:
                speak("Good Afternoon sir, jessica here")
        else:
                     speak (random)


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
        try:
            print("Recognising")
            text = r.recognize_google(audio,language='en-in')
            print(text)
        except Exception:
             return "none"
        return text
                
    

if __name__ == "__main__":
            wish()
            while True:
                query  = takecom().lower()
                
                if "wikipedia" in query:
                    print("Searching details.....Please Wait")
                    speak("Searching details.....Please Wait")
                    query.replace("wikipedia","")
                    results = wikipedia.summary(query,sentences=2)
                    print(results)
                    engine.setProperty('rate',150)
                    speak(results)
                elif 'open youtube' in query or "open video online" in query:
                        webbrowser.open("www.youtube.com")
                        speak("open youtube")
                elif 'open google' in query or "search google" in query:
                        webbrowser.open("www.google.co.in")
                        speak("opening google")
                elif 'bye' in query:
                        speak("Bye sir, jessica going offline")
                elif "shutdown operating system" in query:
                        speak("Ok sir. Shutting down the system")
                        os.system('shutdown -s')
                elif 'open facebook' in query:
                    speak("Ok sir, opening facebook")
                    webbrowser.open("http://www.facebook.com/")
                elif 'open white hat' in query:
                    speak("opening whitehat")
                    webbrowser.open("https://www.whitehatjr.com/")
                elif'who are you' in query or 'introduce'in query:
                    speak("I am jessica, a programme created by mister bajajj, jessica stands for just an engine with simple system with great intellect for a computer which is also known as an AI")
                elif 'what can you do'in query or 'what are your abilities'in query:
                    speak("I can open many websites and open applications like vs code and can search anything for you, in wikipedia")
                elif 'open vs code' in query:
                    speak("opening vs code")
                    codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                elif 'alarm'in query:
                    speak("ok sir, your alarm has started")
                    datef.alarm(query)
                    speak("sir, your time is up")
                elif  'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir,the time is {strTime}")
                elif 'open meet'in query or 'start meet'in query:
                    speak("yes sir, starting meet")
                    webbrowser.open("meet.google.com")
                elif 'open class'in query or 'open gc'in query:
                    speak("ok sir, opening google classroom")
                    webbrowser.open("https://classroom.google.com/u/1/c/OTYwMDU0NjE5NDha")
                elif 'nice day'in query or 'great day'in query or 'best day'in query:
                    speak("good to hear that sir, how may i help you?")
                elif 'mail'in query:
                    speak("sure sir, opening mail")
                    webbrowser.open("https://mail.google.com/mail/u/0/inbox")
                elif 'thanks'in query or 'thank you'in query:
                    speak("your most welcome sir")
                elif 'open your system'in query:
                    speak("ok sir, opening my operating system")
                    codePath = "C:\\Users\\DELL\\Desktop\\Jess Operating System"
                    os.startfile(codePath)
                elif'open my achievements'in query:
                    speak("ok sir, opening your trophies")
                    codePath = "C:\\Users\\DELL\\Desktop\\WHJ Achievments"
                    os.startfile(codePath)
                elif 'open my works'in query:
                    speak("opening your works folder")
                    codePath = "C:\\Users\\DELL\\Desktop\\WhiteHatJr Work"
                    os.startfile(codePath)
                elif 'open chrome'in query or 'open google chrome'in query:
                    speak("sure sir, opening chrome")
                    codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(codePath)
                elif'open edge'in query:
                    speak("opening microsoft edge")
                    codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    os.startfile(codePath)
                elif 'drive'in query:
                    speak("opening google drive")
                    webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
                elif 'git'in query:
                    speak("opening your git bash")
                    codePath = "C:\\Program Files\\Git\\git-bash.exe"
                    os.startfile(codePath)
                elif'firefox'in query:
                    speak("sure sir, opening firefox")
                    codePath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
                    os.startfile(codePath)
                elif'hello'in query or 'hi'in query:
                    speak("Hello sir, how may i help you?")
                elif'good night'in query:
                    speak("good night sir, sweet dreams")
                    exit()
                elif'sleep'in query:
                    speak ("bye sir, going offline")
                    exit()
                elif'here'in query or 'online'in query:
                    speak("yes sir, i am online, how may i help you?")
                elif'network speed'in query or 'open fast.com'in query or 'open fast'in query:
                    speak("sure sir, opening fast.com")
                    webbrowser.open("fast.com")
                elif 'server'in query:
                    speak("opening web server for chrome 200 OK")
                    codePath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps"
                    os.startfile(codePath)
                elif'notepad'in query or 'notes'in query or 'nootbook'in query:
                    speak("sure thing, opening notepad")
                    codePath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories"
                    os.startfile(codePath)
                elif'open word folder'in query or 'open word'in query:
                    speak("sure sir, opening word")
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office"
                    os.startfile(codePath)
                elif 'how are you'in query:
                    speak(" i am fine, how are you?")
                elif'good afternoon'in query or 'afternoon'in query:
                    speak("good afternoon sir, Jessica ready for help")
                elif 'good morning Jessica'in query or 'good morning'in query or 'morning'in query:
                    speak("good morning sir, how may i help you?")
                elif'good evening Jessica'in query or 'good evening'in query:
                    speak("good eveing sir, how was your day?")
                elif'namaste'in query:
                    speak("namaste, looks like you are Indian")
                elif' i am an indian'in query or 'i am indian' in query:
                    speak("nice to hear that, how do you want me to help you?")
                elif'who is your owner'in query:
                    speak("my owner, is the greatest programmer in the world, Pratham bajajj")
                elif"mother"in query or "mom"in query:
                    speak("My owner, Pratham, his mother is miss,Riya Bajajj")
                elif'open rd'in query or 'open realtime database'in query or 'open database'in query or 'open firebase'in query or 'open real time database'in query:
                    speak("sure thing, opening realtime database firebase")
                    webbrowser.open("https://console.firebase.google.com/u/0/project/_/database/data")
                elif'chat'in query:
                    speak("sure sir, opening WhatsApp")
                    webbrowser.open("https://web.whatsapp.com/")
                elif'none'in query:
                    print("cannot understand")
                elif'deactivate Jessica'in query or 'deactivate'in query:
                    speak("sure sir, going offline, have a nice day sir")
                elif'jessica'in query or 'j'in query or 'J'in query or 'Jess'in query:
                    speak("Hello sir, Jessica online, how may I help you?")
                elif 'open wolfram aplha'in query or 'open wolframalpha'in query or 'open alpha'in query or 'open wall frame alpha'in query or 'open wallframe alpha'in query:
                    speak("sure thing, opening wolfram alpha")
                    webbrowser.open("https://www.wolframalpha.com/")
                elif'open quiz'in query:
                    speak("Yes sir, opening quizziz.com")
                    webbrowser.open("https://quizizz.com/join#")
                elif 'stats'in query or 'status'in query:
                    speak("status good, problems none, ready for the updates and for your help")
                elif'shutdown'in query or 'quit'in query or 'shut down'in query:
                    speak("sure sir, going offline, have a nice day")
                    exit()
                elif'great'in query or 'perfect'in query or 'nice'in query or 'fantastic'in query or 'wonderful'in query:
                    print("thank you sir")
                elif'ok'in query:
                    print("ok sir")
                elif'temperature'in query:
                    try:
                        response = app.query(query)
                        print(next(response.results).text)
                        speak(next(response.results).text)
                    except:
                        print("Net issues")
                else:
                    try:
                        response = app.query(query)
                        print(next(response.results).text)
                        speak("searching details, please wait")
                        speak(next(response.results).text)
                    except:
                        print("No results found")

            
                        
