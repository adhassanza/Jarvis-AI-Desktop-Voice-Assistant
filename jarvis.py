import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib

engine = pyttsx3.init( 'sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<17:
        speak("Good afternoon")
    else:
        speak("Good evening")
    
    speak("I am Jarvis sir, please tell how can I help you ")

# https://stackoverflow.com/questions/62109289/getting-attributeerror-enter-when-using-microphone-from-speech-recognizer
def takeCommand():

    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :{query}\n")

    except Exception as e:
        # print(e)
        print("Say again please...")
        return "None"
    return query
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adhassanza@gmail.com', 'Kishwar@1612')
    server.sendmail('adhassanza@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'play music' in query:
            music_dir = 'D:\\Adnan\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir), songs[0])

        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f'Sir the time is {strTime}')

        elif 'open code' in query:
            codePath = 'C:\\Users\\afzal\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
            os.startfile(codePath)

        elif 'email to adnan' in query:
            try:
                speak("What should I mail?")
                content = takeCommand()
                to = 'adhassanza@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent.')
            except Exception as e:
                    print(e)
                    speak('Sorry Adnan, Email not sent')
        elif 'exit' in query:
            speak('It was nice to talking you')
            print('Bye Adnan')
            break
