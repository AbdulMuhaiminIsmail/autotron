from speech import setup, speak, listen
from names import assistantName, ownerName
from browser import youtubeSearch, webSearch, composeEmail
from gemini import commandToPrompt, getEmail, getExplanation
from softwares import open

#This function is converting the command into prompt using NLP
def handleCommand(command):
    if ("search" in command or "play" in command) and ("youtube" in command or "watch" in command):
        prompt = commandToPrompt(command)
        youtubeSearch(prompt)
    elif ("search" in command or "look for" in command or "find" in command) and ("web" in command or "google" in command or "firefox" in command or "browser" in command):
        prompt = commandToPrompt(command)
        webSearch(prompt)
    elif ("email" in command or "gmail" in command or "mail" in command):
        speak("Please enter the name of the recipient:")
        name = listen()
        print(name)
        speak("Please tell me the email of the recipient:")
        email = listen()
        print(email)
        speak("Why do you need to write this email?")
        reason = listen()
        print(reason)
        # name = "Salman Khan"
        # email = "salman.khan@gmail.com"
        # reason = "write an email to ask about his plans this summer"
        urlEncodedMail = getEmail(name, email, reason)
        composeEmail(urlEncodedMail)
    elif ("open" in command):
        open(command[5:])
    elif any(keyword in command for keyword in ["explain", "what", "why", "where", "who", "when", "how"]):
        response = getExplanation(command)
        print(response)
        speak(response)
        while("It was a pleasure to help you!" not in response):
            userResponse = listen()
            response = getExplanation(userResponse)
            print(response)
            speak(response)

def main():
    setup()
    command = ""
    while(True):
        command = listen()
        if(command == "00"):
            speak(f"Ok, have a great day")
            break
        speak(command)
        handleCommand(command)
        speak(f"Is there anything else I can help you with {ownerName}?")


if __name__ == "__main__":
    main()


