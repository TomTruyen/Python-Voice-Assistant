# Imports
import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import wolframalpha
import webbrowser

# TODO

# use sound effects instead of some spoken things like 'Shutdown' should just make a sound instead of saying it

# Add Arrays of Phrases (insulting) for each question. Add multiple phrases for each question and put it in an array and choose a random option from it
# Improve list of commands (so there are more options)
# All 'Open' applications should also have a 'Close' option by saying for example: "Close Mail" to close outlookmail:
# Make it wait with asking a command until the previous one is finished. Example: When opening FireFox (which takes quite some time) the program should wait until an actual window of FireFox is active
# Fix the Calculate one (maybe try to use a different API for it, that has unlimited calls preferably)
# Make basic GUI (like Google Assistant on Phone)
# Turn it into an Executable + Make a version that works on mobile phones


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
        elif "play" in text_val:
            # Do something here to play music
            return
        elif "calculate" in text_val.lower():
            app_id = "VH8A6Y-EYQTE254K4"
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



#Make program start after saying 'hey echo [command]'
#Add a command Example: 'play Paradise by Coldplay' then it will play it using either youtube or spotify (or it asks the question which one you prefer if not mentioned in the initial command)

if __name__ == "__main__":
    while True:
        text = get_start_command()
        if "hey echo" in str(text).lower():
            text = text.lower().replace('hey echo', '')
            process_text(text)

        elif "shutdown" in str(
                text) or "shut down" in str(text):
            assistant_speaks("Okay I'll shutdown.")
            break
