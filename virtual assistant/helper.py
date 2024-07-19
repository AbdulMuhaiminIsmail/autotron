ASSISTANT_NAME = "Max"
OWNER_NAME = "Muhaimin"
SLEEP_WORD = "power off"

import pyperclip as clipboard
import psutil
from software import Software
from browser import Browser

def copy_to_clipboard(text):
    clipboard.copy(text)
    print("The text has been copied to clipboard successfully")

def shut_down():
    common_processes = ["BlueStacksAppplayerWeb.exe", "BlueStacks X.exe", "BlueStacksAppplayerWeb.exe", "BlueStacksWeb.exe", "BlueStacksWeb.exe", "BlueStacksAppplayerWeb.exe", "Discord.exe", "Whatsapp.exe", "qtcreator.exe", "studio64.exe", "obs.exe", "Photoshop.exe", "TradingView.exe", "Spotify.exe", "firefox.exe", "chrome.exe", "steam.exe", "GitHubDesktop.exe", "Calculator.exe", "Code.exe"]
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in common_processes:
            proc.terminate()

def start_default():
    browser = Browser()
    browser.visit_site("https://www.chatgpt.com")
    browser.visit_site("https://www.google.com")
    Software("spotify").open()
    Software("vscode").open()
