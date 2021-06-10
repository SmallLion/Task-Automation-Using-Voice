import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os
import smtplib
import socket

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please.. I didn't get it.")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('boobagames123@gmail.com', 'Chenuli14836')
    server.sendmail('boobagames123@gmail.com', to, content)
    server.close()

if __name__ == "__main__":

    while True:
    # if 1:
        query = takeCommand().lower()
# ____________________________Browser_______________________________________________________
        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\MyPlayList'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
 # ____________________________your computer_______________________________________________________
        elif 'open code' in query:
            codePath = "C:\\Users\\chenuli\\AppData\\Local\\Programs\\Microsoft VS Code\\levelmenu.exe"
            os.startfile(codePath)
        elif 'open downloads' in query:
            downloadsPath = "C:\\Users\\Admin\\Downloads"
        elif 'open Among Us' in query:
            amongUs = "C:\\Users\\Admin\\AmongUs.exe"
        elif 'display hostname' in query:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            print(f"Hostname: {hostname}")
            print(f"IP Address: {ip_address}")


    #____________________________Hashnode_______________________________________________________
        elif 'open hashnode'in query:
             webbrowser.open("hashnode.com")

        elif 'open notifications' in query:
            webbrowser.open("hashnode.com/notifications")
        elif 'write new article' in query:
            webbrowser.open("hn.new")
           # Jist use these lines to open any web site's url
#________________________________________________________________________________________

        elif 'email to Victoria' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "chenuliilz@gmail.com.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my buddy. I am not able to send this email")
