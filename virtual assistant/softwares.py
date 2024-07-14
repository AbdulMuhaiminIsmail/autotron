import pyautogui as pointer

#These are the x-coordinates of the apps on taskbar
apps = {
    "spotify": 555,
    "firefox": 500,
    "whatsapp": 700,
    "vscode": 750
}

def open(appName):
    if appName != "firefox":
        pointer.moveTo(190, 1079)
        pointer.sleep(1)
        pointer.click()
        pointer.typewrite(appName)
        pointer.press('enter')
    else:
        pointer.moveTo(apps[appName], 1079)
        pointer.click()
    pointer.sleep(3)
    pointer.hotkey('win', 'up')
            
def spotifySearch(songName):
    open("spotify")
    pointer.sleep(6)
    pointer.hotkey('ctrl', 'l')
    pointer.typewrite(songName)
    pointer.sleep(1.5)
    pointer.moveTo(443, 359)
    pointer.click()

def whatsappText(contactName, message):
    open("whatsapp")
    pointer.sleep(1)
    pointer.hotkey('ctrl', 'f')
    pointer.typewrite(contactName)
    pointer.sleep(1)
    pointer.click(233, 188) #Clicks the first contact which shows up
    pointer.sleep(1)
    pointer.typewrite(message)
    pointer.press('enter')

def whatsappCall(contactName):
    open("whatsapp")
    pointer.sleep(1)
    pointer.hotkey('ctrl', 'f')
    pointer.typewrite(contactName)
    pointer.sleep(1)
    pointer.click(233, 188)
    pointer.sleep(1)
    pointer.click(1836, 66) #Clicks where the voice call icon is
