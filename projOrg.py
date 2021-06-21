import sys
import os
# from pathlib import Path

def createFolder(newPath):
    if not os.path.exists(newPath):
        # print(newPath)
        os.mkdir(newPath)

def parseFolders(arr, path, iter):
    for y in range(iter, len(arr)):
        if isinstance(arr[y], list):
            parentFolder = os.path.join(path, arr[y][0])
            print("New folder: " + parentFolder)
            # print(parentFolder)
            createFolder(parentFolder)
            parseFolders(arr[y], parentFolder, 1)
        else:
            subFolder = os.path.join(path, arr[y])
            print("New folder: " + subFolder)
            # print(parentFolder)
            createFolder(subFolder)

argumentsNum = len(sys.argv)
path = ""
type = ""

if argumentsNum == 3:
    if sys.argv[1]:
        type = sys.argv[1]
    if sys.argv[2]:
        if os.path.normpath(sys.argv[2][-1]) == "/" or os.path.normpath(sys.argv[2][-1]) == "\\":
            path = os.path.normpath(sys.argv[2][0:-1])
        else:
            path = os.path.normpath(sys.argv[2])
    else:
        path = ""

if type == "def":
    folders = [
        ["Assets",
            "Frames", "Fonts"],
        "Export",
        "Projects",
        "Proxy",
        "Share"
    ]

if path != "":
    parseFolders(folders, path, 0)
else:
    print("Path not found")



# for y in folder:
#     # newPath = path + "\\" + y[0]
#     if len(y) > 0:
#         parseFolders(y, path)

#     newPath = path + "\\" + y[0]
#     # createFolder(newPath)
#     # if len(y) == 1:
#         # if not os.path.exists(newPath):
#         #     os.mkdir(newPath)
#         # print(newPath)
#     # else:
#     for x in range(1, len(y)):
#         newPath = path + "\\" + y[0] + "\\" + y[x]
#         # print(newPath)
#         createFolder(newPath)


    # for x in range(argumentsNum):
        # print(x, sys.argv[x])
        # if 
        # if sys.argv[1]:
            # arg = 
            # alert(path.split(" "))
        #     path = sys.argv[1]
        # else:
        #     path = "Path not found"

        # if sys.argv[2]:
        #     type = sys.argv[2]
        # else:
        #     type = "default"

# print(path)

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()


# parser.add_argument("file_path", type=Path)

# p = parser.parse_args()
