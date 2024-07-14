import pyautogui as pointer

#These are the x-coordinates of the apps on taskbar
apps = {
    "spotify": 555,
    "firefox": 500,
    "whatsapp": 700,
    "vscode": 750
}

def open(appName):
    pointer.moveTo(apps[appName], 1079)
    pointer.click()


