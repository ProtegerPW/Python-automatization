#! /usr/bin/python3
#Usage: Program to open any .txt in folder 
#       and searches for any line that matches a user-suplied regex.
#       All results are then printed
#       ./ch_8_regex_search.py <folder path> <regex>

import sys, re, os, glob

#TODO: validate input
if len(sys.argv) != 3:
    print("Usage: ./ch_8_regex_search.py <folder path> <regex>")
    sys.exit()

if not os.path.isdir(sys.argv[1]):
    print("Folder path argument is not a directory")
    sys.exit()

#TODO: open each file and read lines
os.chdir(sys.argv[1])
txtFiles = glob.glob("*.txt")
argRegex = re.compile(r"{}".format(sys.argv[2]))

for fileName in txtFiles:
    activeFile = open(fileName)
    contentOfFile = activeFile.readlines()

#TODO: search for regex and print results
    for index in range(len(contentOfFile)):
        findRegex = argRegex.findall(contentOfFile[index])
        if findRegex:
            print("In file: " + fileName + " at line: " + str(index + 1) + ":")
            print(findRegex)
    print("") # empty string for pretty printing

#TODO: close each file
    activeFile.close()




