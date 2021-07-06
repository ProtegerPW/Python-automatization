#! /usr/bin/python3
#Usage: Program that goes through a folder tree and search
#       for files with certain extension. Then copy these files
#       to another folder
#       ./ch_9_selective_copy <source folder> <destination folder> <extension>

import sys, shutil, re, os

# TODO:validate input path

if len(sys.argv) != 4:
    print("./ch_9_selective_copy <source folder> <destination folder> <extension>")
    sys.exit()

if not os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]):
    print("You need to pass existing directory as first and second argument")
    sys.exit()

# TODO:goes through a folder tree
absFolderPath = os.path.abspath(sys.argv[1])
os.chdir(r"%s" %absFolderPath)
for foldername, subfolders, filenames in os.walk(absFolderPath):
    for filename in filenames:

        # TODO:find files with certain extension
        if filename.endswith(sys.argv[3]):
            # TODO:copy file to destination folder
            print(os.path.join(foldername, filename))
            print(os.path.abspath(sys.argv[2]))
            shutil.copy(os.path.join(foldername, filename), os.path.abspath(sys.argv[2]))