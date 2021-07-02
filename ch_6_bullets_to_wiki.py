#! /usr/bin/python3

# Program that will get a text from clipboard and then add asterix at the beggining of the line

import pyperclip

clipboardText = pyperclip.paste()

splittedText = clipboardText.split("\n")

for i in range(len(splittedText)):
    splittedText[i] = "* " + splittedText[i]

clipboardText = "\n".join(splittedText)

pyperclip.copy(clipboardText)
