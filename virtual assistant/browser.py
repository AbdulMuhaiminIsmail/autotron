import pyautogui as pointer
import psutil
from selenium import webdriver
from software import Software
from speech import SpeechSystem

class Browser:
    def __init__(self, name="firefox"):
        self.name = name
        self.current_window_index = 0
        self.driver = None
        self.ss = SpeechSystem()
    
    def config_browser(self):
        if self.is_browser_running("firefox") and self.driver is not None:
            self.driver.execute_script("window.open('about:blank', '_blank');")
            # Get handles of all open tabs
            handles = self.driver.window_handles
            # Switch to the new tab
            self.current_window_index = len(handles) - 1
            self.driver.switch_to.window(handles[self.current_window_index])
        else:
            # Initialize Firefox WebDriver
            self.driver = webdriver.Firefox()
            # Maximize window
            self.driver.maximize_window()
        
    def youtube_search(self, prompt):
        self.ss.speak("OK! Let's watch " + prompt + " on Youtube")
        self.config_browser()
        search_query = self.prompt_to_query(prompt)
        self.driver.get(f"https://www.youtube.com/results?search_query={search_query}")

    def web_search(self, prompt):
        self.ss.speak("Surely! Let's search " + prompt + " on the web")
        self.config_browser()
        search_query = self.prompt_to_query(prompt)
        self.driver.get(f"https://www.google.com/search?q={search_query}")

    def compose_email(self, url_encoded_mail):
        self.ss.speak("Hold tight, your E-mail is almost ready!")
        firefox = Software("firefox")
        firefox.open()
        pointer.hotkey('ctrl', 't')
        pointer.typewrite(url_encoded_mail)
        pointer.press('enter')

    @staticmethod
    def prompt_to_query(prompt):
        return '+'.join(prompt.lower().split())
    
    @staticmethod
    def is_browser_running(browser_name):
        # List all processes
        processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name'])]
        # Check if any process is a browser instance
        for process in processes:
            if browser_name in process['name'].lower():
                return True
        return False
