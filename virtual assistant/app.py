from helper import assistantName, ownerName
from speech import SpeechSystem
from browser import Browser
from gemini import Gemini
from software import Software, Spotify, Whatsapp
from system import System

class App:
    def __init__(self):
        self.command = ""
        self.ss = SpeechSystem()

    def handleCommand(self, command):
        if ("youtube" in command) and any(keyword in command for keyword in ["watch", "play", "search"]): 
            prompt = Gemini().command_to_prompt(command)
            Browser().youtube_search(prompt)
        
        elif any(keyword in command for keyword in ["search", "look for", "look up", "find", "search for"]) and any(keyword in command for keyword in ["web", "google", "firefox", "browser"]):
            prompt = Gemini().command_to_prompt(command)
            Browser().web_search(prompt)
        
        elif any(keyword in command for keyword in ["email", "gmail", "mail"]):
            urlEncodedMail = Gemini().get_email()
            Browser().compose_email(urlEncodedMail)
        
        elif ("play" in command) and any(keyword in command for keyword in ["song", "music", "spotify", "songs", "tunes", "pop", "rock", "lo-fi", "remix"]):
            prompt = Gemini().command_to_prompt(command)
            Spotify().play(prompt)
        
        elif "open" in command:
            software = Software(command[5:].strip())  # Adjusted to trim whitespace and remove "open"
            software.open()

        elif any(keyword in command for keyword in ["explain", "what", "why", "where", "who", "when", "how"]):
            Gemini().get_explanation(command)

        elif any(keyword in command for keyword in ["system info", "pc information", "pc stats", "system stats", "system details", "system information"]):
            System().stats()

        elif any(keyword in command for keyword in ["text", "txt", "message", "msg"]):
            Whatsapp().text()

        elif any(keyword in command for keyword in ["call", "audio call"]):
            Whatsapp().call()
        else:
            self.ss.speak("Sorry, I do not recognize this command")

    def start(self):
        self.ss.speak(f"Hey, I am {assistantName}, your personal voice assistant! How may I help you today, {ownerName}?")
        
        while True:
            command = self.ss.listen()

            if command == "00":
                self.ss.speak("Ok, have a great day! GoodBye")
                break
            
            self.handleCommand(command)
            self.ss.speak(f"Is there anything else I can help you with, {ownerName}?")

if __name__ == "__main__":
    App().start()


