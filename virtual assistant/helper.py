assistantName = "Max"
ownerName = "Muhaimin"

import pyperclip as clipboard

def copyToClipboard(text):
    clipboard.copy(text)
    print("The text has been copied to clipboard successfully")
    