#! /usr/bin/python3

# Description: Saves and loads pieces of text to the clipboard.
# Usage: <program name> save <keyword> - Saves clipboard to keyword.
#        <program name> <keyword> - Loads keyword to clipboard.
#        <program name> list - Loads all keywords to clipboard.v 
#        <program name> delete <keyword> - Delete value of the keyword-key
#        <program name> delete - Delete all keywords

import shelve, pyperclip, sys 
mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "delete":
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == "delete":
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()