import sys
import os

foldersDef = [
    ["Assets",
        "Frames", "Fonts"],
    "Export",
    "Projects",
    "Proxy",
    "Share"
]

def createFolder(newPath):
    if not os.path.exists(newPath):
        os.mkdir(newPath)

def parseFolders(arr, path, iter):
    for y in range(iter, len(arr)):
        if isinstance(arr[y], list):
            parentFolder = os.path.join(path, arr[y][0])
            print("New folder: " + parentFolder)
            createFolder(parentFolder)
            parseFolders(arr[y], parentFolder, 1)
        else:
            subFolder = os.path.join(path, arr[y])
            print("New folder: " + subFolder)
            createFolder(subFolder)

argumentsNum = len(sys.argv)
foldersType = ""

if argumentsNum == 3:
    if sys.argv[1]:
        foldersType = sys.argv[1]
    if sys.argv[2]:
        lastPathChar = os.path.normpath(sys.argv[2][-1])
        if lastPathChar == "/" or lastPathChar == "\\":
            path = os.path.normpath(sys.argv[2][0:-1])
        else:
            path = os.path.normpath(sys.argv[2])
    else:
        path = ""

if foldersType == "def":
    foldersStructure = foldersDef

if path != "":
    parseFolders(foldersStructure, path, 0)
else:
    print("Path not found")