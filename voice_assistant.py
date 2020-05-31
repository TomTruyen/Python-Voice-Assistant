# Imports
import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import wolframalpha
import webbrowser

num = 1
def assistant_speaks(output):
    global num

    num += 1
    print("Person: ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    file = str(num) + ".mp3"
    toSpeak.save(file)

    playsound.playsound(file, True)
    os.remove(file)


def get_start_command():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Waiting for Command...")
        rObject.adjust_for_ambient_noise(source)
        audio = rObject.listen(source)

    try:
        print("Command Received.")
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text
    except:
        print("Timeout expired / Command wasn't understandable")
        return 0


def get_audio():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        rObject.adjust_for_ambient_noise(source)
        audio = rObject.listen(source, phrase_time_limit=10)

    print("Stop.")

    try:
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return str(text.lower())
    except:
        assistant_speaks("Could not understand, Please try again!")
        return 0


def open_application(input):
    if "chrome" in input:
        assistant_speaks("Opening Google Chrome")
        os.system("cmd /c start chrome.exe")
        return
    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.system("cmd /c start firefox.exe")
        return
    elif "youtube" in input:
        assistant_speaks("Opening Youtube")
        webbrowser.open('http://www.youtube.com')
        return
    elif "google" in input:
        assistant_speaks("Opening Google")
        webbrowser.open('http://www.google.com')
        return
    elif "spotify" in input:
        assistant_speaks("Opening Spotify")
        os.system("cmd /c start spotify.exe")
        return
    elif "mail" in input or "email" in input:
        assistant_speaks("Opening Email")
        os.system("cmd /c start outlookmail:")
        return
    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.system("cmd /c start excel.exe")
        return
    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.system("cmd /c start winword.exe")
        return
    elif "powerpoint" in input:
        assistant_speaks("Opening Microsoft Powerpoint")
        os.system("cmd /c start powerpnt.exe")
        return
    elif "visual studio code" in input or "code" in input:
        assistant_speaks("Opening Microsoft Visual Studio Code")
        os.system("cmd /c code")
        return
    else:
        assistant_speaks("Application not available")
        return

def search_google(text_val):
    text_val = text_val.replace('google', '').strip()

    if text_val != "":
        assistant_speaks("I'm searching Google for: " + text_val)
        print("https://www.google.com/search?q=" + text_val)
    else:
        assistant_speaks("I couldn't understand. Please try again.")


def process_text(text_val):
    try:
        if "google" in text_val:
            search_google(text_val)
            return
        elif "who are you" in text_val or "define yourself" in text_val:
            speak = 'Hello, I am Person. Your personal Assistant. I am here to make your life easier.'
            assistant_speaks(speak)
            return
        elif "who made you" in text_val or "created you" in text_val:
            speak = "I have been created by Tom Truyen"
            assistant_speaks(speak)
            return
        elif "calculate" in text_val.lower():
            app_id = "WOLFRAMALPHA_API_KEY_HERE"
            client = wolframalpha.Client(app_id)

            indx = text_val.lower().split().index('calculate')
            query = text_val.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return
        elif "open" in text_val:
            open_application(text_val.lower())
            return
        else:
            assistant_speaks("I couldn't understand. Please try again.")
            return
    except:
        assistant_speaks("Could not understand, Please try again")


if __name__ == "__main__":
    while True:
        text = get_start_command()
        if "ok assistant" in str(text) or "okay assistant" in str(text):
            while True:
                assistant_speaks("What do you want?")
                text = get_audio()

                if text == '0':
                    continue
                if "exit" in str(text) or "bye" in str(text) or "stop" in str(text):
                    assistant_speaks("Bye.")
                    break

                process_text(text)
        elif "stop spying" in str(text) or "leave me alone" in str(text) or "shutdown" in str(
                text) or "shut down" in str(text):
            assistant_speaks("Okay I'll shutdown.")
            break
