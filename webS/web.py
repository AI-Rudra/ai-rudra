import speech_recognition as sr
from selenium import webdriver
import pyttsx3

engine = pyttsx3.init()

r = sr.Recognizer()

def open_browser():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.maximize_window()
    return driver

def navigate_to_website(driver, url):
    driver.get(url)

def search_on_google(driver, query):
    driver.get("https://www.google.com")
    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys(query)
    search_bar.submit()

def close_browser(driver):
    driver.quit()
    
driver = None


while True:
    with sr.Microphone() as source:
        print("Say a command:")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said: " + command)

        if "open browser" in command:
            driver = open_browser()
            print("Browser opened")
            engine.say("Browser opened")

        elif "close browser" in command:
            close_browser(driver)
            print("Browser closed")
            engine.say("Browser closed")
            break

        elif "go to" in command:
            url = command.split("go to ")[1]
            driver = open_browser()
            navigate_to_website(driver, "https://" + url)
            print("Navigating to: " + url)
            engine.say("Navigating to: " + url)

        elif "search for" in command:
            query = command.split("search for ")[1]
            driver = open_browser()
            search_on_google(driver, query)
            print("Searching for: " + query)
            engine.say("Searching for: " + query)

        else:
            print("Sorry, I didn't understand that command.")
            engine.say("Sorry, I didn't understand that command.")

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that command.")
        engine.say("Sorry, I didn't understand that command.")