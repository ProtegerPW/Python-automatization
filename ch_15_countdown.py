#! /usr/bin/python3
# Simple countdown timer

import sys, time, subprocess

if len(sys.argv) != 2:
    print('Usage: ./ch_15_countdown <amount of time in secoonds>')
    sys.exit()

timeLeft = int(sys.argv[1])
if timeLeft < 1:
    print('Amount of time is lower than zero')
    sys.exit()

while timeLeft > 0:
    print(timeLeft, sep = ' ')
    time.sleep(1)
    timeLeft -= 1

subprocess.Popen(['see', './example_files/alarm.wav'])
