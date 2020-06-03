# Python-Voice-Assistant - NOTE: IN PROGRESS

# Currently working on: Play function --> "play [songname] by [artist]" will play music (stream) from spotify and/or youtube

Module list:
  - SpeechRecognition (pip install SpeechRecognition)
  - playsound (pip install playsound)
  - gTTS (pip install gTTS)
  - wolframalpha (pip install wolframalpha) ==> REQUIRES API KEY FROM THEIR SITE (free 2000 api calls/month)
  - webbrowser (pip install webbrowser)
  - os (Already installed with Python)
  
Basic Python Voice Assistant (in progress) as replacement for assistants like 'Cortana' and in the future 'Google Assistant/Siri)

To start using:
say: "hey echo [command]"

Possible commands:
- "google [search]" --> prints (in console) google URL for the 'search'
- "who are you" --> says: 'Hello, I am Person. Your personal Assistant. I am here to make your life easier.'
- "who made you" --> says: "I have been created by Tom Truyen"
- "calculate [calculation] --> says: "[calculation] is "[outcome]"
- "open [application]" --> opens application
  * Currently only supports the following applications:
    + Google Chrome ("open chrome")
    + Mozilla Firefox ("open firefox" or "open mozilla")
    + Youtube ("open youtube") NOTE: opens youtube in the default browser
    + Google ("open google") NOTE: opens google in default browser
    + Spotify ("open spotify")
    + Windows 10 Mail ("open mail" or "open email")
    + Microsoft Excel ("open excel")
    + Microsoft Word ("open word")
    + Microsoft PowerPoint ("open powerpoint")
    + Microsoft Visual Studio Code ("open visual studio code" or "open code")
    
