import speech_recognition as sr
import pyttsx3 as tts

engine = None
r = None

#Initial setup settings
def setup():
    global engine, r
    #Initializing speech engine and recognizer
    engine = tts.init()
    r = sr.Recognizer()
    #Speech settings
    engine.setProperty('voice' , engine.getProperty('voices')[1].id) #Setup female voice for the assistant
    engine.setProperty('rate', 150) #Setup the speech rate of the assistant

#Function for speaking content
def speak(content):
    if("play" in content):
        engine.say("Playing " + content[4:])
    elif("search" in content):
        engine.say("Searching " + content[5:])
    elif("write" in content):
        engine.say("Writing " + content[5:])
    elif("send" in content):
        engine.say("Sending " + content[4:])
    else:
        engine.say(content)
    engine.runAndWait()

#Function for listening to command
def listen():
    with sr.Microphone() as source:
        try:
            # Adjust for ambient noise
            print("Calibrating microphone...")
            r.adjust_for_ambient_noise(source, duration=0.5)

            # Listen for the user's input
            print("Listening")
            speak("Listening")
            command = r.listen(source)
            
            # Using Google to recognize audio
            commandText = r.recognize_google(command).lower()
            print(commandText)
            
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("There's some kinda request error, maybe bad internet or something.")
            return ""
        
        except sr.UnknownValueError:
            print("Unknown error occurred or could not understand the audio")
            speak("There's some unknown error or maybe audio could not be understood")
            return ""
        
    return commandText
