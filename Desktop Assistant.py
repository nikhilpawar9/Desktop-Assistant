import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random

import requests



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<16.5:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am your assistant ") ;speak("how may I help you")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    print("Enter your Email id")
    speak("Enter your Email id")
    mailId = input()
    print("Enter your password")
    speak("Enter your password")
    passWord = input()
    server.login(mailId, passWord)
    server.sendmail('nikhilpawar982001@gmail.com', to, content)
    server.close()


"""def getweather():
    url='https://samples.openweathermap.org/data/2.5/weather?q=Pune&appid=8a1f7a021709a861367fa0283418cc26'
    res=requests.get(url)
    data=res.json()
    pprint(data)"""
def getweather():
    city='Pune'
    key='8a1f7a021709a861367fa0283418cc26'
    URL = 'http://api.openweathermap.org/data/2.5/weather?appid={}&q={}'.format(key, city)
    print(URL)
    data = requests.get(URL).json()
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    temp1=data['main']['temp']
    print(temp1)
    print(humidity)
    return humidity, wind_speed
#getweather()



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\prathmesh\\Music\\folder'
            songs = os.listdir(music_dir)
            #print(songs)
            n=random.randint(0,40)
            os.startfile(os.path.join(music_dir, songs[n]))
            #music_dir= 'C:\\Users\\'
            #os.startfile(music_dir)


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("please enter recievers mail id")
                to = input("please enter recievers mail id")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")

        elif 'hello' in query:
            speak('hi sir, how are you')

        elif 'bye' in query:
            speak('quitting, goodbye sir, have a nice day')
            exit()

        elif 'shutdown' in query:
            os.system('shutdown /s')

        elif 'play song' in query:
            speak('which  song should i play')