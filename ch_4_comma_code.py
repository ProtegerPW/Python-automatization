def commaCode(argList):
    returnString = ""
    for i in range(len(argList)):
        if(i == 0):
            returnString += argList[i]

        elif(i == len(argList) - 1):
            returnString += ", and " + argList[i]
        
        else:
            returnString += ", " + argList[i]
        
    return returnString

if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']

    print(commaCode(spam))