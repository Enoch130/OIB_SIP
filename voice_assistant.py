import speech_recognition as recognise
import pyttsx3 
import datetime
import webbrowser

recognizer = recognise.Recognizer()
transition = pyttsx3.init()

def speak(text):
    transition.say(text)
    transition.runAndWait()

def listen():
    with recognise.Microphone(device_index=2) as audio_source:
        print("Please record your message")
        recognizer.adjust_for_ambient_noise(audio_source,duration=1)
        try:
            sound = recognizer.listen(audio_source, timeout=10,phrase_time_limit=10)
            recorded_text = recognizer.recognize_google(sound)
            print(f"You said: {recorded_text}")
            return recorded_text.lower()
        except recognise.UnknownValueError:
            speak("Sorry, I didnt hear what you said")
            return ""
        except recognise.RequestError:
            speak("Sorry, System is down. Try again later")
            return ""
        except recognise.WaitTimeoutError:
            speak("Sorry, You kept too long. Try again later")
            return ""
        
def respond(recorded_text):
    if "hello" in recorded_text:
        print("Hellooo, How can i help you?")
        speak("Hellooo, How can i help you?")
    elif "time" in recorded_text:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time now is {current_time}")
    elif "date" in recorded_text:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today' date is {current_date}")
    elif "search for" in recorded_text:
           research = recorded_text.replace("search for","").strip()
           url = f"https://www.google.com/search?q={research}"
           webbrowser.open(url)
           speak(f"Searching for {research} on Google.")
    else:
        speak("Can you clarify what you want me to do?")



speak("Voice Assistant is now active. Say something!")
while True:
    recorded_text = listen()
    if recorded_text:
        if "exit" in recorded_text or "stop" in recorded_text:
            speak("Goodbye!")
            break
        respond(recorded_text)



