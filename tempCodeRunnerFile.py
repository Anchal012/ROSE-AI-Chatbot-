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
        
        elif 'open stakeoverflow' in query:
            webbrowser.open("stakeoverflow.com")
            
        elif 'play music' in query:
            music_dir = 'C:\\My_music'
            songs = os.listdir(music_dir)
            index = random.randint(0, len(songs))
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