#! /usr/bin/python3

# It is a simple (insecure) program to store password to a certain account.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:    
    print('Usage: python ch_6_password_locker.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1]    # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password copied to clipboard")
else:
    print("There is no account of this name")