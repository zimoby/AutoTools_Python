# add random project start
# add projects prior
# добвить сравнение времени

import time
import os
import platform
import sys
from datetime import datetime
import curses
from math import *

def checkOs():
    return platform.system()

def makeSound():
    os.system('afplay /System/Library/Sounds/Glass.aiff')

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def getChanksTime():
    if "test" in sys.argv:
        chankTime = 1
        restTime = 1
    else:
        chankTime = 25*60
        restTime = 5*60
    return [chankTime, restTime]

def getCurrentTime(mode):
    if mode == "full":
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def sleepFunction(t):
    print("press ctrl-c to stop")
    getCurrentTime("full")
    loop_forever = True
    y = 0
    while loop_forever:
        try:
            # print("y:", str(y), "t:", str(t))
            for x in range(y, t):
                if x % (60 * 2) == 0:
                    print(str(x / 60), "min")
                time.sleep(1)
            loop_forever = False
        except KeyboardInterrupt:
            print("\n")
            tst = input("continue or reset(rp - reset proj)?: ")
            if tst == "r":
                loop_forever = False
                print("")
                return "rest cancel"
            if tst == "rp":
                loop_forever = False
                print("")
                return "reset proj"
            else:
                print("Start from ", str(x / 60), "min")

def makeOtdyh(iter):
    print("")
    notify("Chank end", "some chill?")
    restTime = getChanksTime()
    c = iter
    if c != 0:
        print("Note or chill")
        sleepFunction(restTime[1])
        print("\nChill end", "\n")
    makeSound()

# def chankCounter(iter):

def startChank(t, iter):
    notify("Sprint start", str(iter) + " chank")
    mm = sleepFunction(t)
    if mm != "rest cancel" or mm != "reset proj":
        makeOtdyh(iter)
    notify("Chank end", "what next?")
    return mm

def startProj(text, mode, chankTime, restTime):
    if mode != "ui":
        projAmount = 0
        projNames = []
    else:
        projAmount = 10
        projNames = ["Сценарий",
                    "Проходка",
                    "Подготовка проекта",
                    "Черновая озвучка",
                    "Проходка2",
                    "Скринкас",
                    "Монтаж",
                    "Графика",
                    "Озвучка",
                    "Финальный монтаж"]
        projTime = [16, 6, 2, 2, 4, 6, 8, 8, 4, 2]
    
    if mode != "ui":
        projPrior = []
        # projIter = 0
        projAmount = 0
        stopAddProj = "Add"
        while stopAddProj != "":
            projName = input("enter proj names: ")
            if projName == "":
                break
            projAmount += 1
            projNames += [projName]
            if mode == "pp":
                projPrior += [input("enter prior 1-3: ")]


        if mode == "pri":
            numChanks = int(input("number of chanks: "))
            projIter = 0
            koefArr = []
            priorArr = []
            while projIter < projAmount:
                print("\n", projNames[projIter], "\n")
                koef = int(input("Enter proj prior: "))
                priorArr += [koef]
                koef2 = koef / 2 / projAmount
                koef3 = round(numChanks * koef2)
                koefArr += [koef3]
                projIter += 1

    projIter2 = 0
    rev = ""

    # print(priorArr)
    # print(koef3)
    
    while projIter2 < projAmount:
        print("")
        # print(projNames)
        for x in range(0, projAmount):
            # print(x)
            if mode == "p":
                print(str(x + 1) + ")", projNames[x])
            else:
                print(str(x + 1) + ")", projNames[x], "prior:", priorArr[x], "chanks:", koefArr[x])
        print("")
        choice = input("What project start? (a - add proj): ")
        # print(type(choice))
        # if choice > 0:
        #     choice = int(choice)

        if choice == "":
            break
        elif choice == "a":
            projName = input("enter proj names: ")
            projAmount += 1
            projNames += [projName]
        # elif choice <= projAmount:
        else:
            print("start Project:", projNames[int(choice) - 1])
            # revtext = limitChank(mode, chankTime, restTime, projNames[int(choice) - 1], projTime[int(choice) - 1])
            revtext = limitChank(mode, chankTime, restTime, projNames[int(choice) - 1])
            rev += "Project: " + projNames[int(choice) - 1] + "\n" + "Chanks: " + revtext + "\n"
            projNames[int(choice) - 1] += " :done" 

            projIter2 += 1
        # else:
        #     print("\nUncorrect choice")
    print("\n", rev)

def nonStopChank(chankTime, restTime):
    restTime = restTime
    c = 0
    stop = ""
    while stop != "s":
        c += 1
        print("+" * c)
        startChank(chankTime, c)
        stop = input("next chank? ")


# def limitChank(mode, chankTime, restTime, prName, chanks):
def limitChank(mode, chankTime, restTime, prName):
    c = 0
    stop = ""
    numChanks = ""
    dopChanks = 0
    if mode == "a":
        limit = 1
    elif mode == "ui":
        limit = chanks
    else:
        limit = int(input("number of chanks: "))

    while c < limit:
        stop = input("start chank? ")
        if stop == "n":
            break
        elif stop == "m":
            # chankCounter(c, numChanks)
            c += 1
            numChanks += "+"
            print(numChanks)
            print("")
        else:
            c += 1
            numChanks += "+"
            print(numChanks)
            projCommand = startChank(chankTime, c)
    while stop != "f" and projCommand != "reset proj":
        stop = input("finish or add? ")
        if stop == "a":
            c += 1
            dopChanks += 1
            if dopChanks == 1:
                numChanks += "("
            numChanks += "+"
            print(numChanks)
            startChank(chankTime, c)
        else:
            stop = "f"
    if dopChanks > 0:
        numChanks += "), dop chanks: " + str(dopChanks)
        print(numChanks)

    return str(numChanks)

def prior():
    chanks = int(input("enter chanks: "))
    projNames = []
    projAmount = 0
    stopAddProj = "Add"
    while stopAddProj != "":
        projName = input("enter proj prior: ")
        if projName == "":
            break
        projAmount += 1
        projNames += [projName]
    print(projNames)
    koefArr = []
    koefArr2 = []
    koefArr3 = []
    for x in range(0, projAmount):
        koef = int(projNames[x]) / 2
        koef2 = int(projNames[x]) / 2 / projAmount
        koef3 = round(chanks * koef2)
        koefArr += [koef]
        koefArr2 += [koef2]
        koefArr3 += [koef3]

    print(koefArr)
    print(koefArr2)
    print(koefArr3)
# screen = curses.initscr()

if "test" in sys.argv:
    chankTime = 1
    restTime = 1
else:
    chankTime = 25*60
    restTime = 5*60

mode = input("mode: ")

if mode == "n":
    print("NON STOP CHANK STARTED", "\n")
    nonStopChank(chankTime, restTime)
elif mode == "l":
    print("LIMIT CHANK STARTED", "\n")
    limitChank(mode, chankTime, restTime, "process", 1)
elif mode == "c":
    print("CHANK STARTED", "\n")
    startChank(chankTime, 1)
elif mode == "p":
    print("PROJECTS CHANK STARTED", "\n")
    startProj("how many projects today? ", mode, chankTime, restTime)
elif mode == "ui":
    print("LESSON CHANK STARTED", "\n")
    startProj("", mode, chankTime, restTime)
elif mode == "pp":
    print("PRIOR PROJECTS CHANK STARTED", "\n")
    startProj("how many projects today? ", mode, chankTime, restTime)
elif mode == "a":
    print("ARCHI CHANK STARTED", "\n")
    chankTime = 15*60
    # chank = 1
    # restTime = 1
    startProj("how many projects to process? ", mode, chankTime, restTime)
elif mode == "pri":
    # prior()
    print("PRIOR PROJECTS CHANK STARTED", "\n")
    startProj("how many projects today? ", mode, chankTime, restTime)
elif int(mode) > 0:
    print("CHANK STARTED", int(mode), "min\n")
    startChank(int(mode)*60, 1)
elif mode == "test":
    # print('Before: %s' % time.ctime())
    # time.sleep(2)
    # print('After: %s\n' % time.ctime())
    makeSound()
    # projNames = [input("enter proj names: "), input("enter prior 1-3: ")]
    # projNames += [input("enter proj names: "), input("enter prior 1-3: ")]
    # print(projNames)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print("\n", "finish")