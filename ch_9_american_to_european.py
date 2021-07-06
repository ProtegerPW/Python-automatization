#! /usr/bin/python3

#Usage: Renames all files in directory with american date format (MM-DD-YYYY) to european format (DD-MM-YYYY)
#       ./ch_9_american_to_european  <path to folder>

import re, sys, shutil, os

if len(sys.argv) != 2:
    print("Usage: ./ch_9_american_to_european  <path to folder>")
    sys.exit()

#TODO: create regex for american date format
usaTimeRegex = re.compile(r"""^(.*?) # all text before the date    
((0|1)?\d)-                     # one or two digits for the month
((0|1|2|3)?\d)-                 # one or two digits for the day    
((19|20|)\d\d)                   # four digits for the year    
(.*?)$                          # all text after the date
""", re.VERBOSE)

# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir(sys.argv[1]):
    foundDateFile = usaTimeRegex.search(amerFilename)

# TODO: Skip files without a date.
    if foundDateFile == None:
        continue

# TODO: Get the different parts of the filename.
    beforePart = foundDateFile.group(1)    
    monthPart  = foundDateFile.group(2)    
    dayPart    = foundDateFile.group(4)    
    yearPart   = foundDateFile.group(6)    
    afterPart  = foundDateFile.group(8)

# TODO: Form the European-style filename.
    euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart

# TODO: Get the full, absolute file paths.
    absPath = os.path.abspath(sys.argv[1])
    amerFilename = os.path.join(absPath,amerFilename)
    euroFilename = os.path.join(absPath,euroFilename)

# TODO: Rename the files.
    print("Switch name from: '%s' to: '%s'" % (amerFilename,euroFilename))
    # schutil.move(amerFilename,euroFilename)