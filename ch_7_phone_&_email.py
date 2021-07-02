#! /usr/bin/python3

import pyperclip, re

phoneRegex = re.compile(r'''(    
    (\d{3}|\(\d{3}\))?                # area code    
    (\s|-|\.)?                        # separator    
    (\d{3})                           # first 3 digits    
    (\s|-|\.)                         # separator    
    (\d{4})                           # last 4 digits    
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension    
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               #username
    @                               #at 
    [a-zA-Z0-9+-]+                  #domain
    (\.[a-zA-Z]{2,4})               #extension
)''', re.VERBOSE)

analyzedText = str(pyperclip.paste())

matches = []

for tuple in phoneRegex.findall(analyzedText):
    phoneNum = "-".join([tuple[1], tuple[3], tuple[5]])
    if tuple[8] != "":
        phoneNum += " x" + tuple[8]
    matches.append(phoneNum)

for tuple in emailRegex.findall(analyzedText):
    matches.append(tuple[0])

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard")
    print("\n".join(matches))

else:
    print("There is no email address or phone numbers in clipboard")


"""This is example text to check:
Ala has a cat with number 123.456.4321
& he likes to use his office email address catLikeMice@gmail.compile
That is it - if you have a question please contact us: 546-678-1234"""
