import os
import sys
fromStr = sys.argv[1]
toStr = sys.argv[2]
print fromStr
print toStr
folderList = os.listdir(os.getcwd())

for folder in folderList:
    newFolder = folder.replace(fromStr, toStr)
    os.rename(folder, newFolder)