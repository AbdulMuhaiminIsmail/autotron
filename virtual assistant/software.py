import time
import pyautogui as pointer
from speech import SpeechSystem

class Software:
    def __init__(self, name):
        self.name = name.lower()
        self.ss = SpeechSystem()

    def open(self):
        self.ss.speak("Opening " + self.name)
        if self.name != "firefox":
            pointer.moveTo(190, 1079)
            time.sleep(1)
            pointer.click()
            pointer.typewrite(self.name)
            pointer.press('enter')
        else:
            pointer.moveTo(500, 1079)
            pointer.click()
        time.sleep(3)
        pointer.hotkey('win', 'up')

class Spotify(Software):
    def __init__(self):
        super().__init__("spotify")    

    def play(self, songName):
        self.ss.speak("Playing " + songName + " on Spotify")
        super().open()
        time.sleep(6)
        pointer.hotkey('ctrl', 'l')
        pointer.typewrite(songName)
        time.sleep(1.5)
        pointer.moveTo(443, 359)
        pointer.click()

class Whatsapp(Software):
    def __init__(self):
        super().__init__("whatsapp")

    def text(self):
        self.ss.speak("What's the message?")
        message = self.ss.listen()
        self.ss.speak("Target contact?")
        contact_name = self.ss.listen()
        self.ss.speak("Sending a text to " + contact_name + " on WhatsApp")
        super().open()
        time.sleep(1)
        pointer.hotkey('ctrl', 'f')
        pointer.typewrite(contact_name)
        time.sleep(1)
        pointer.click(233, 188) #Clicks the first contact which shows up
        time.sleep(1)
        pointer.typewrite(message)
        pointer.press('enter')

    def call(self):
        self.ss.speak("Whom to call?")
        contact_name = self.ss.listen()
        self.ss.speak("Calling " + contact_name + " on WhatsApp")
        super().open()
        time.sleep(1)
        pointer.hotkey('ctrl', 'f')
        pointer.typewrite(contact_name)
        time.sleep(1)
        pointer.click(233, 188)
        time.sleep(1)
        pointer.click(1836, 66) #Clicks where the voice call icon is


