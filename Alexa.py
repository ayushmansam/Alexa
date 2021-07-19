import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def say(text):
    engine.say(text)
    engine.runAndWait()
say("I am your alex")
say("What can i do for you?")
engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Speak my friend, I am listening!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                command = command.replace('alex', '')
            print(command)


    except:
        pass
    return command


def run_alex():
     command = take_command()
     if 'play' in command:
         print(command)
         song = command.replace('play', '')
         say('playing' + song)
         pywhatkit.playonyt(song)
     elif 'time' in command:
         time = datetime.datetime.now().strftime('%H:%M:%S')
         say('the time is' + time)
         print(time)
     elif 'according to wikipedia' in command:
         answer = command.replace('according to wikipedia', '')
         info = wikipedia.summary(answer, 1)
         print(info)
         say(info)
     elif 'who made you' in command:
         say('Ayushman Samal')
     elif 'who are you' in command:
         say('I said you in the beginning that I am Alex')
     elif 'what will you do for me' in command:
         say('Anything you will say')
     elif 'can you make coffee for me' in command:
         say('Have you gone mad? I am a robot not a human')
     elif 'are you python program' in command:
         say('yes obviously i am python programmed? Have not read the manual')
     elif 'joke' in command:
         a = pyjokes.get_joke()
         say(a)
         print(a)
     else:
         say('I cant understand what you are saying. give me 100 dollars for wasting my time')


while True:
    run_alex()
