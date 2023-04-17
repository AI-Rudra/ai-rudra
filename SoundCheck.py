import pyttsx3
import time

engine = pyttsx3.init()


voices = engine.getProperty('voices')
selected_voice = voices[1]  
engine.setProperty('voice', selected_voice.id)


speech_rate = 150 
engine.setProperty('rate', speech_rate)


intro_text = """
Hello there! 
I'm Rudra, ||pause||
your innovative and versatile voice assistant, ||pause||
masterfully crafted by Raman Sharma and Shivanshu Singh. ||pause||

I'm here to make your life easier ||pause||
by empowering you to control your device effortlessly with just your voice. ||pause||
Let's explore a world of endless possibilities together! ||pause||
"""


def speak_with_pauses(text, pause_duration=0.5):
    segments = text.split("||pause||")
    for segment in segments:
        segment = segment.strip()
        if segment:
            engine.say(segment)
            engine.runAndWait()
            time.sleep(pause_duration)


speak_with_pauses(intro_text)
