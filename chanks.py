#! /usr/bin/env python
# -*- coding: utf-8 -*-
from math import *

def dopChankFunc(inputMin):
    if inputMin >= 30:
        dopChank = 1
    else:
        dopChank = 0
    return dopChank

def hourMinCount(hours, factor, chank):
    h = hours
    k = factor
    ch = chank

    t = h * k
    easH = floor(t)
    easM = int(((t - easH) * 100) * 60 / 100)
    dopChank = easH * 2 + dopChankFunc(easM)

    export = [easH, easM, dopChank]
    return export
    

def chankFunction(timeIn, a, factorArr, chank):
    stand = timeIn

    hours = stand - a

    print("Ease mod")
    ex = hourMinCount(hours, factorArr[0], chank)
    print("hours:", str(ex[0]) + ":" + str(ex[1]))
    print("Chanks:", ex[2])
    ch1 = ex[2]
    print()

    print("Standart mod")
    ex = hourMinCount(hours, factorArr[1], chank)
    print("hours:", str(ex[0]) + ":" + str(ex[1]))
    print("Chanks:", ex[2])
    ch2 = ex[2]
    print()

    print("Hard mod")
    ex = hourMinCount(hours, factorArr[2], chank)  
    print("hours:", str(ex[0]) + ":" + str(ex[1]))
    print("Chanks:", ex[2])
    ch3 = ex[2]
    print()

    print("-"*20, "\n")
    chanks = [ch1, ch2, ch3]
    return chanks

def inputTime(textTime):
    print()
    a = int(input(textTime + ": "))
    print()
    return a

mode = input("d - day, h - hours of work, l - limit\nMode: ")

startHour = 14
endHour = 24 + 4
factorArr = [0.25, 0.5, 0.75]
chank = 25

if mode == "d":
    print("до", endHour % 24, "часов ночи:")
    startHour = inputTime("current time")
    print("осталось", abs(endHour % 24 - startHour), "часов", "\n")
    x = chankFunction(endHour, startHour, factorArr, chank)
elif mode == "h":
    print("до", endHour % 24, "часов ночи:", "\n")
    b = int(input("hours: "))
    for i in x:
        xx = ceil(b/ (i/2))
        print("days of work:", xx, " chanks for day:", i)
elif mode == "l":
    print("до", endHour % 24, "часов ночи:")
    startHour = inputTime("current time")
    endHour = inputTime("end time")
    print("осталось", abs(endHour % 24 - startHour), "часов", "\n")
    x = chankFunction(endHour, startHour, factorArr, chank)