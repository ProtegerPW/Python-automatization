#! /usr/bin/python3
#Usage: Program that scan folder tree to find files or folders
#       which are bigger than X MB and then print their absolute paths
#       ./ch_9_find_big_files <folder path> <size>

import os, sys

#TODO: validate input arguments
if len(sys.argv) != 3:
    print("./ch_9_find_big_files <folder path> <size>")
    sys.exit()

#TODO: scan folder tree 
absPath = os.path.abspath(sys.argv[1])
os.chdir(r"%s" % absPath)

size = 0
for folderName, subFolders, fileNames in os.walk(absPath):
    for file in fileNames:
        fileAbsPath = os.path.join(folderName, file)
        size += os.path.getsize(fileAbsPath)

        #TODO: print files which meet condition
        if(os.path.getsize(fileAbsPath)/ 1024**2 > float(sys.argv[2])):
            print(fileAbsPath)

if size/1024**2 > float(sys.argv[2]):
    print(absPath)


