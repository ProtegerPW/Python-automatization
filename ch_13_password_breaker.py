#! /usr/bin/python3
# Program to find out password of encrypted file using brute-force technique
# Usage: ./ch_13_password_breaker.py <path to encrypted file> <path to password dict>


import sys, PyPDF2

if len(sys.argv) != 3:
    print("Usage: ./ch_13_password_breaker.py <path to encrypted file> <path to password dict>")
    sys.exit()

# create list from dict file
dictFile = open(sys.argv[2])
listOfPasswd = dictFile.read().splitlines()

# open .pdf file
pdfFileObj = open(sys.argv[1], 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# loop and try each word
for word in listOfPasswd:
    if pdfReader.decrypt(word) == 1:
        print("File was decrypted\n Password: " + word)
        break
    if pdfReader.decrypt(word.lower()) == 1:
        print("File was decrypted\n Password: " + word.lower())
        break
