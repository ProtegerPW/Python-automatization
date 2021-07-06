#! /usr/bin/python3
#Usage: Program that will copy entire folder into .zip file
#       and increment its filename

import zipfile, os, sys

def backupToZip(folderPath):
    # Backup the entire contents of "folder" into a ZIP file.    
    folderPath = os.path.abspath(folderPath)
        
    # Figure out the filename this code should use based on    
    # what files already exist.
    occurency = 1     
    while True:        
        zipFilename = os.path.basename(folderPath) + '_' + str(occurency) + '.zip'        
        if not os.path.exists(os.path.join(os.path.dirname(folderPath), zipFilename)):            
            break        
        occurency = occurency + 1     
    # TODO: Create the ZIP file.  
    backupZip = zipfile.ZipFile(zipFilename, 'w')  
    # TODO: Walk the entire folder tree and compress the files in each folder.

    for foldername, subfolders, filenames in os.walk(folderPath):
        print("Adding files in %s..." % foldername)
        backupZip.write(foldername)

        for filename in filenames:
            oldBackups = os.path.basename(folderPath) + "_"

            if filename.startswith(oldBackups) and filename.endswith(".zip"):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip(sys.argv[1])