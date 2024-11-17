import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
from openai import OpenAI
from gtts import gTTS
import pygame
import os

engine = pyttsx3.init()

def aiProcess(command):
    client = OpenAI(
    api_key="dlkrje343dferit45erdfdlgj32")  # provide your api key here
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis and skilled in doing general tasks like alexa and google cloud give short responses"},
        {
            "role": "user",
            "content": command
        }
    ]
)

    return completion.choices[0].message.content
    
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.split(" ")[1]
        link = musiclib.music[song.lower()]
        webbrowser.open(link)
    else:
        output = aiProcess(command)
        speak(output)

    
if __name__ ==  "__main__":
    speak("Initialising Jarvis...")
    

    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("How can I help you")
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                processCommand(command)
            
        except Exception as e:
            print("Error; {0}".format(e))