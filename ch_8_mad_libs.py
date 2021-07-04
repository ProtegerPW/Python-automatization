#! /usr/bin/python3

keywords = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]

import sys,re, os

if len(sys.argv) != 2:
    print("Usage: ch_8_mad_libs.py <path to file>")
    sys.exit()

# TODO: read text files
textToFormat = open(sys.argv[1], "r")
readText = textToFormat.read()

# TODO: ask user about ADJECTIVE, NOUN, ADVERB, or VERB
keywordsRegex = re.compile("|".join(keywords))

while True:
    foundWord = keywordsRegex.search(readText)
    if foundWord:
        print("Type " + foundWord.group().lower() + ":")
    else:
        break;

# TODO: change words
    readText = keywordsRegex.sub(input(), readText, 1)

# TODO: save to new file
print(readText)

filename, extenstion = os.path.basename(sys.argv[1]).split(".")
# saveFile = open(os.path.dirname(sys.argv[1]) + "/" + filename + "_formatted.txt", "w")
saveFile = open(filename + "_formatted.txt", "w")
saveFile.write(readText)
textToFormat.close()
saveFile.close()
