#! /usr/bin/python3

import re,sys

def ifPasswordStrong(password):
    passwordRegex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")

    result = passwordRegex.search(password)
    
    if result != None:
        print("Strong password")
    else:
        print("Password is to weak")
    
if len(sys.argv) < 2:    
    print('Usage: ./ch_7_strong_password <typed password>')
    sys.exit()
    
ifPasswordStrong(sys.argv[1])  
