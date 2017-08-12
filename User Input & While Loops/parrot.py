import win32com.client as wincl
import logging

def synth(strVal):
    if strVal is None:
        logging.debug("You have not set a value. Set a value before using synth")
    else:
        speak = wincl.Dispatch("SAPI.spVoice")
        speak.Speak(strVal)

def main():
    message = input("Tell me something, and I will repeat it back to you: ")
    synth(message)

main()

