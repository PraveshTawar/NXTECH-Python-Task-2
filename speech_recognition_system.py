import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)  # we have two voice i.e 0=david and 1 = zira
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good mouring")
    elif(hour >=12 and hour < 18):
        speak("good afternoon") 
    else:
        speak("good evening")
    speak("hi im your personal Assistant, how may i help you !")   

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio =r.listen(source)
    try:
        print("Recignizing...")
        query = r.recognize_google(audio,language="en-in")
        print("User said :",query)
    except Exception as e:
        print("please say that again..")
        return "None"
    return query

if __name__ == "__main__":
    

    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia...")
            print(result)
            speak(result)
        
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif "search" in query:
            query = query.replace("search","")
            url = "https://google.com/search?q=" + query
            webbrowser.get().open(url)
        elif "lokesh" in query:
            
            speak("Lokesh is your childhood friend  ")   
        
        elif "stop listening" in query:
            print("good bye sir... im leaving")
            speak("good bye sir... im leaving")
            break
