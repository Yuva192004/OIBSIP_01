import speech_recognition as sr
import pyttsx3 as py3
import datetime
import webbrowser

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = py3.init()

# Define a function to speak out the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to handle different commands
def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        query = command.split("search")[1].strip()
        speak(f"Searching the web for {query}")
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")

# Main loop to continuously listen for commands
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        handle_command(command.lower())
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")
