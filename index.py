import speech_recognition as sr
import pyautogui
import webbrowser
import os
from filefinder import find_file
import subprocess
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 150)


def search_file():
    global file_paths
    engine.say("What is the name of the file you want to search for?")
    file_name = input("What is the name of the file you want to search for? ")
    engine.say("What is the name drive 'C','D','E','all': ")
    drive = input("What is the name drive 'C','D','E','all': ")
    engine.say("Searching for file.., this will take some time, depending upon your system speed.")
    print("Searching for file...")
    file_paths = find_file(file_name, drive_choice=drive)
    engine.say("here are the results")
    print(file_paths)
    print("Do you want to create or open this file/folder?")
    engine.say("Do you want to create or open this file/folder?")
    print("1. Create file/folder.")
    engine.say("1. Create file/folder.")
    print("2. Open file/folder.")
    engine.say("2. Open file/folder.")
    print("3. Return to main menu.")
    engine.say("3. Return to main menu.")
    engine.runAndWait()
    with sr.Microphone() as source:
        print("Listening...")
    try:
        text = input("Enter here which options : ")
        print(f"You said: {text}")
        if "1" in text:
            create_file_or_folder()
        elif "2" in text:
            while True:
                open_choice = input("Do you want to open a file or a folder? (F for file, D for folder, Q to quit): ")
                if open_choice.lower() == "f":
                    file_path = file_paths
                    os.startfile(file_path)
                    break
                elif open_choice.lower() == "d":
                    folder_path = file_paths
                    os.startfile(folder_path)
                    break
                elif open_choice.lower() == "q":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif "3" in text:
            return
        else:
            engine.say("Sorry, I didn't understand what you said.")
            engine.runAndWait()
    except sr.UnknownValueError:
        engine.say("Sorry, I didn't catch that. Please try again.")
        engine.runAndWait()
    except sr.RequestError as e:
        engine.say(f"Sorry, there was an issue with the speech recognition service: {e}")
        engine.runAndWait()

def create_file_or_folder():
    location = os.path.dirname(file_paths)
    print("Do you want to create a file or a folder?")
    engine.say("Do you want to create a file or a folder?")
    engine.say("Enter 'f' for file, 'd' for folder:")
    choice = input("Enter 'f' for file, 'd' for folder: ")
    print("Enter the name of the file/folder: ")
    name = input("Enter the name of the file/folder: ")
    full_path = os.path.join(location, name)
    if choice == 'f':
        with open(full_path, 'w'):
            print(f"File '{name}' created at {location}")
            engine.say(f"File '{name}' created at {location}")
    elif choice == 'd':
        os.mkdir(full_path)
        print(f"Folder '{name}' created at {location}")
        engine.say(f"Folder '{name}' created at {location}")
    else:
        print("Invalid choice. Please enter 'f' or 'd'.")
        engine.say("Invalid choice. Please enter 'f' or 'd'.")
    print("Do you want to open the file/folder or go back to the main menu?")
    engine.say("Do you want to open the file/folder or go back to the main menu?")
    engine.say("Enter 'o' to open, 'm' to go back to the main menu:")
    open_choice = input("Enter 'o' to open, 'm' to go back to the main menu: ")
    
    if open_choice == 'o':
        subprocess.run(["explorer", os.path.normpath(full_path)])
    elif open_choice == 'm':
        return
    else:
        print("Invalid choice. Going back to the main menu.")
        engine.say("Invalid choice. Going back to the main menu.")


def use_virtual_mouse():
    subprocess.call(['python', 'mouse\AIVirtualMouse.py'])


def do_google_search():
    subprocess.call(['python', 'webS\web.py'])

while True:

    print("What would you like to do? press.")
    engine.say("What would you like to do?, press")
    print("1. Search file.")
    engine.say("1 for Search file.")
    print("2. Do Google search.")
    engine.say("2 for Do Google search.")
    print("3 to Use virtual mouse.")
    engine.say("3. Use virtual mouse.")
    print("4 to Exit.")
    engine.say("4. Exit.")
    engine.runAndWait()

    with sr.Microphone() as source:
        print("Listening...")

    try:
        print("Please Enter options here :")
        text = input("Enter options here : ")
        print(f"You said: {text}")
        if "1" in text:
            search_file()
        elif "2" in text:
            do_google_search()
        elif "3" in text:
            use_virtual_mouse()
        elif "4" in text:
            print("Goodbye!")
            engine.say("Goodbye!")
            engine.runAndWait()
            break
        else:
            print("Sorry, I didn't understand what you said.")
            engine.say("Sorry, I didn't understand what you said.")
            engine.runAndWait()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        engine.say("Sorry, I didn't catch that. Please try again.")
        engine.runAndWait()
    except sr.RequestError as e:
        print(f"Sorry, there was an issue with the speech recognition service: {e}")
        engine.say(f"Sorry, there was an issue with the speech recognition service: {e}")
        engine.runAndWait()
