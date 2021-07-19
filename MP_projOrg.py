import sys
import os

folders_Array = {
    "def": [
        ["Assets", "Frames", "Fonts"],
        "Export",
        "Projects",
        "Proxy",
        "Share"
    ],
    "classic": [
        ["1_Assets", "Frames", "Fonts"],
        "2_Projects",
        "3_Proxy",
        "4_Export",
        "5_Share"
    ],
    "advanced": [
        "01_Moodboard",
        "02_Assets",
        ["03_StyleFrames", "StyleFrames_01", "StyleFrames_02", "StyleFrames_03"],
        "04_Voiceover",
        ["05_Illustrations", "Illustrations_01", "Illustrations_02", "Illustrations_03"],
        ["06_Animation", "AE Projects", "Cinema4D Projects", "Proxy", "Export"],
        ["07_Sound_Design", "01_SFX", "02_Master"],
        "08_Share"
    ]
}

def Create_Folder(newPath):
    if not os.path.exists(newPath):
        os.mkdir(newPath)

def Parse_Folders(arr, path, start_From):
    for y in range(start_From, len(arr)):
        if isinstance(arr[y], list):
            parentFolder = os.path.join(path, arr[y][0])
            print("New folder: " + parentFolder)
            Create_Folder(parentFolder)
            Parse_Folders(arr[y], parentFolder, 1)
        else:
            subFolder = os.path.join(path, arr[y])
            print("New folder: " + subFolder)
            Create_Folder(subFolder)

arguments_Number = len(sys.argv)
folders_Type = ""
type_Finder = False
path = ""

# Argument Parser
if arguments_Number == 3:
    if sys.argv[1]:
        folders_Type = sys.argv[1]
    if sys.argv[2]:
        last_Path_Char = os.path.normpath(sys.argv[2][-1])

        if last_Path_Char == "/" or last_Path_Char == "\\" or last_Path_Char == "\"" or last_Path_Char == "\'":
            path = os.path.normpath(sys.argv[2][0:-1])
        else:
            path = os.path.normpath(sys.argv[2])

# Type Checker
for type in folders_Array:
    if folders_Type.lower() == type:
        Folders_Structure = folders_Array[type]
        type_Finder = True
        break

# Parse Folders
if type_Finder == False:
    print("Type not found")
else:
    if path != "":
        Parse_Folders(Folders_Structure, path, 0)
    else:
        print("Path not found")