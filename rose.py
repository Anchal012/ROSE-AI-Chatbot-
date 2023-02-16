import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
from email.message import EmailMessage

contact = {'anchal': 'anchalgupta1203@gamil.com', 'aditi': 'aditigupta0852@gamil.com', 'isha': 'agen20cs304011@gmail.com'}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greetMe():
    """
    It greets the user as per the time 
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    
    elif hour >= 18 or hour < 0:
        speak("Good Evening!")
        
    speak(f"I am rose, your assistant please tell me how may i help you?")
    
def takeCommand():
    """
    It takes microphone input from the user and returns a string as an output
    """
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        print("Pardon me, can you please say that again....")
        return "None"
    return query

def sendEmail(to, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
    server.login('anchalgupta1203@gmail.com', 'xdirpguoqneomtuh') 
    email = EmailMessage()
    email['From'] = 'anchalgupta1203@gmail.com'
    email['To'] = to
    email['subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()
       
if __name__ == "__main__":
    greetMe()
    
    
# Logic for exceuting tasks based on query
while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results) 
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stake overflow' in query:
            webbrowser.open("stakeoverflow.com")
            
        elif 'play music' in query:
            music_dir = 'C:\\My_music'
            songs = os.listdir(music_dir)
            index = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[index]))
            
        elif 'time' in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Currently the time is {strfTime}")
            
            
        elif 'open code' in query:
            codePath = "C:\\Users\\RanuIshu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'send email' in query:
            try:
                speak("To whom you want to send the email")
                name = takeCommand().lower()
                speak("What is the subject")
                subject = takeCommand().capitalize()
                speak("What should i say?")
                content = takeCommand().capitalize()
                to = contact[name]
                sendEmail(to, subject, content)
                speak("Your email has been sent")
                
            except Exception as e:
                print(e)
                speak("sorry, i am enable to send the email.")
            
        elif 'quit' in query:
            exit()