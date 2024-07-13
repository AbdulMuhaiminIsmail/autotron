from selenium import webdriver
import psutil

currentWindowIndex = 0
driver = None

def promptToQuery(prompt):
    return '+'.join(prompt.lower().split())

def is_browser_running(browser_name):
    # List all processes
    processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name'])]

    # Check if any process is a browser instance
    for process in processes:
        if browser_name in process['name'].lower():
            return True
    return False

def configBrowser():
    global driver, currentWindowIndex
    if is_browser_running("firefox") and driver != None:
        driver.execute_script("window.open('about:blank', '_blank');")
        # Get handles of all open tabs
        handles = driver.window_handles
        # Switch to the new tab
        currentWindowIndex = currentWindowIndex - 1
        driver.switch_to.window(handles[currentWindowIndex])
    else:
        # Initialize Firefox WebDriver
        driver = webdriver.Firefox()
        # Maximize window
        driver.maximize_window()
        
def youtubeSearch(prompt):
    configBrowser()
    SEARCH_QUERY = promptToQuery(prompt)
    driver.get(f"https://www.youtube.com/results?search_query={SEARCH_QUERY}")


def webSearch(prompt):
    configBrowser()
    SEARCH_QUERY = promptToQuery(prompt)
    driver.get(f"https://www.google.com/search?q={SEARCH_QUERY}")








