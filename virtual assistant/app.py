import threading
import tkinter as tk
from tkinter import scrolledtext
from speech import SpeechSystem
from browser import Browser
from gemini import Gemini
from software import Software, Spotify, Whatsapp
from system import System
from helper import ASSISTANT_NAME, OWNER_NAME, SLEEP_WORD, start_default, shut_down

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.ss = SpeechSystem()
        self.setupGUI()

    def setupGUI(self):
        # Main Window
        self.root.title("Voice Assistant")
        self.root.geometry("1280x720")
        self.root.configure(background="#17202A")

        # Header
        self.header_frame = tk.Frame(self.root)
        self.header_frame.pack(pady=10)

        self.logo_label = tk.Label(self.header_frame, text="Voice Assistant", font=("Arial", 24))
        self.logo_label.pack()

        # Conversation Area
        self.conversation_frame = tk.Frame(self.root)
        self.conversation_frame.pack(pady=10)

        self.conversation_text = scrolledtext.ScrolledText(self.conversation_frame, wrap=tk.WORD, height=20, state='disabled', font=("Arial", 14))
        self.conversation_text.pack()

        # Input Area
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.mic_button = tk.Button(self.input_frame, text="🎤", font=("Arial", 16), command=self.on_mic_button_click)
        self.mic_button.pack(side=tk.LEFT, padx=5)

        self.text_entry = tk.Entry(self.input_frame, font=("Arial", 14), width=50)
        self.text_entry.pack(side=tk.LEFT, padx=5)

        self.send_button = tk.Button(self.input_frame, text="Send", font=("Arial", 14), command=self.on_send_button_click)
        self.send_button.pack(side=tk.LEFT, padx=5)


    def write_text_to_conversation(self, text):
        self.conversation_text.configure(state='normal')
        self.conversation_text.insert(tk.END, text)
        self.conversation_text.configure(state='disabled')

    def handle_command(self, command):
        try:
            if ("youtube" in command.lower().split()) and any(keyword in command.lower().split() for keyword in ["watch", "play", "search"]): 
                prompt = Gemini().command_to_prompt(command)
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: OK! Let's watch " + prompt + " on Youtube \n")
                self.root.update()
                self.ss.speak("OK! Let's watch " + prompt + " on Youtube")
                Browser().youtube_search(prompt)
            
            elif any(keyword in command.lower().split() for keyword in ["search", "look for", "look up", "find", "search for"]) and any(keyword in command.lower().split() for keyword in ["web", "google", "firefox", "browser", "internet"]):
                prompt = Gemini().command_to_prompt(command)
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Surely! Let's search " + prompt + " on the web \n")
                self.root.update()
                self.ss.speak("Surely! Let's search " + prompt + " on the web")
                Browser().web_search(prompt)
            
            elif any(keyword in command.lower().split() for keyword in ["email", "gmail", "mail"]):
                url_encoded_email = Gemini().get_email()
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Composing an email for you \n")
                self.root.update()
                self.ss.speak("Composing an email for you")
                Browser().compose_email(url_encoded_email)
            
            elif ("play" in command.lower().split() or "listen" in command.lower().split()) and any(keyword in command.lower().split() for keyword in ["song", "playlist", "album", "music", "spotify", "songs", "tunes", "pop", "rock", "lo-fi", "remix"]):
                song_name = Gemini().command_to_prompt(command)
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Playing " + song_name + " on Spotify \n")
                self.root.update()
                self.ss.speak("Playing " + song_name + " on Spotify")
                Spotify().play(song_name)

            elif any(keyword in command.lower().split() for keyword in ["explain", "how", "what", "where", "when", "who", "whom"]):
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Getting the explanation ready, please wait. \n")
                self.root.update()
                self.ss.speak("Getting the explanation ready, please wait.")
                response = Gemini().get_explanation(command)
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: {response}")
                self.root.update()
                self.ss.speak(response)
            
            elif "open" in command.lower().split():
                software_name = command[5:].strip()
                software = Software(software_name)  
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Opening " + software_name + "\n")
                self.root.update()
                self.ss.speak("Opening " + software_name)
                software.open()


            elif any(keyword in command.lower().split() for keyword in ["system info", "pc information", "pc stats", "system stats", "system details", "system information"]):
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Fetching current system details, please wait. \n")
                self.root.update()
                self.ss.speak("Fetching current system details, please wait.")
                System().stats()

            elif any(keyword in command.lower().split() for keyword in ["text", "txt", "message", "msg"]):
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: What's the message? \n")
                self.root.update()
                self.ss.speak("What's the message?")
                message = self.ss.listen()
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Target contact? \n")
                self.root.update()
                self.ss.speak("Target contact?")
                contact_name = self.ss.listen()
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Sending a text to {contact_name} on WhatsApp \n")
                self.root.update()
                self.ss.speak("Sending a text to " + contact_name + " on WhatsApp")
                Whatsapp().text(contact_name, message)

            elif any(keyword in command.lower().split() for keyword in ["call", "audio call"]):
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Whom to call? \n")
                self.root.update()
                self.ss.speak("Whom to call?")
                contact_name = self.ss.listen()
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Calling {contact_name} on WhatsApp \n")
                self.root.update()
                self.ss.speak("Calling " + contact_name + " on WhatsApp")
                Whatsapp().call(contact_name)
            
            elif command == "start default":
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Getting your desktop ready! \n")
                self.root.update()
                self.ss.speak("Getting your desktop ready!")
                start_default()
            
            elif command == "shut down":
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Closing all apps and shutting down! \n")
                self.root.update()
                self.ss.speak("Closing all apps and shutting down!")
                shut_down()

            elif command.lower() == SLEEP_WORD:
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Ok! Have a great day, {OWNER_NAME} \n")
                self.root.update()
                self.ss.speak(f"Ok! Have a great day, {OWNER_NAME}")
                self.root.destroy()

            else:
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Sorry, I do not recognize this command \n")
                self.root.update()
                self.ss.speak("Sorry, I do not recognize this command")
            
            
        except Exception as e:
                print(f"Exception encountered: {e}")
                self.write_text_to_conversation(f"{ASSISTANT_NAME}: Unfortunately, an unexpected error occured while processing the command. \n")
                self.root.update()
                self.ss.speak(f"Unfortunately, an unexpected error occured while processing the command. \n")

        self.write_text_to_conversation(f"{ASSISTANT_NAME}: Is there anything else I can help you with, {OWNER_NAME}? \n")   
        self.root.update()
        self.ss.speak(f"Is there anything else I can help you with, {OWNER_NAME}?")
    
    def process_command(self, command):
        thread = threading.Thread(target=self.handle_command, args=(command,))
        thread.start()

    def on_mic_button_click(self):
        user_input = self.ss.listen()
        print(user_input)
        self.write_text_to_conversation("You: " + user_input + "\n")
        self.process_command(user_input)
        
    def on_send_button_click(self):
        user_input = self.text_entry.get()
        print(user_input)
        self.text_entry.delete(0, tk.END)
        self.write_text_to_conversation("You: " + user_input + "\n")
        self.process_command(user_input)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
   App().run()


