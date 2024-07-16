import speech_recognition as sr
import pyttsx3 as tts

class SpeechSystem:
    def __init__(self):
        #Initializing speech self.engine and recognizer
        self.engine = tts.init()
        self.recognizer = sr.Recognizer()
        #Speech settings
        self.engine.setProperty('voice' , self.engine.getProperty('voices')[1].id) #Setup female voice for the assistant
        self.engine.setProperty('rate', 150) #Setup the speech rate of the assistant

    #Function for speaking content
    def speak(self, content):
        # if("play" in content):
        #     self.engine.say("Playing " + content[4:])
        # elif("search" in content):
        #     self.engine.say("Searching " + content[5:])
        # elif("write" in content):
        #     self.engine.say("Writing " + content[5:])
        # elif("send" in content):
        #     self.engine.say("Sending " + content[4:])
        # else:
        self.engine.say(content)
        self.engine.runAndWait()

    #Function for listening to command
    def listen(self):
        with sr.Microphone() as source:
            try:
                # Adjust for ambient noise
                print("Calibrating microphone...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

                # Listen for the user's input
                print("Listening")
                self.speak("Listening")
                command = self.recognizer.listen(source)
                
                # Using Google to recognize audio
                commandText = self.recognizer.recognize_google(command).lower()
                print(commandText)
                
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                self.speak("There's some kinda request error, maybe bad internet or something.")
                return ""
            
            except sr.UnknownValueError:
                print("Unknown error occurred or could not understand the audio")
                self.speak("There's some unknown error or maybe audio could not be understood")
                return ""
            
        return commandText
