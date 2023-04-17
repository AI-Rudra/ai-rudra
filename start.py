import pyttsx3
import subprocess
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# for i, voice in enumerate(voices):
#     print(f"Voice {i}: {voice.name}")
selected_voice = voices[0]  
engine.setProperty('voice', selected_voice.id)
print("Hello there! I'm Rudra, your innovative and versatile voice assistant, masterfully crafted by Raman Sharma and Shivanshu Singh. I'm here to make your life easier by empowering you to control your device effortlessly with just your voice. Let's explore a world of endless possibilities together!")
engine.say("Hello there! I'm Rudhra, your innovative and versatile voice assistant, masterfully crafted by Raman Sharma and Shivanshu Singh. I'm here to make your life easier by empowering you to control your device effortlessly with just your voice. Let's explore a world of endless possibilities together!")
engine.runAndWait()
def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        with microphone as source:
            print("Please say your command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            engine.say(f"You said: {text}")
            if text.lower() == "drop my needle":
                subprocess.call(['python', 'music.py'])
                break
            elif text.lower() == "wake up":
                subprocess.call(['python', 'index.py'])
                break
            else:
                print("Command not recognized. Please try again.")
                engine.say("Command not recognized. Please try again.")
        except sr.UnknownValueError:
            print("Could not understand your command. Please try again.")
            engine.say("Could not understand your command. Please try again.")
        except sr.RequestError:
            print("Error connecting to the speech recognition service. Retrying...")
            engine.say("Error connecting to the speech recognition service. Retrying...")
            continue
    return text

command = recognize_speech()


# command = recognize_speech()

# import pyttsx3

# engine = pyttsx3.init()
# engine.setProperty("rate", 150)
# engine.say("Hello there! I'm Rudhra, your innovative and versatile voice assistant, masterfully crafted by Raman Sharma and Shivanshu Singh. I'm here to make your life easier by empowering you to control your device effortlessly with just your voice. Let's explore a world of endless possibilities together!")
# engine.runAndWait()
