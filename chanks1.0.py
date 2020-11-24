#! /usr/bin/env python
# -*- coding: utf-8 -*-
from math import *

def dopChankFunc(inputMin):
    if inputMin >= 30:
        dopChank = 1
    else:
        dopChank = 0
    return dopChank

def hourMinCount(hours, koef, chank):
    h = hours
    k = koef
    ch = chank

    t = h * k
    easH = floor(t)
    easM = int(((t - easH) * 100) * 60 / 100)
    dopChank = easH * 2 + dopChankFunc(easM)

    export = [easH, easM, dopChank]
    return export
    

def chankFunction(timeIn, a):
    stand = timeIn
    chank = 25
    a = a

    hours = stand - a

    print("Ease mod")
    ex = hourMinCount(hours, 0.25, chank)
    print("hours:", ex[0], " min:", ex[1])
    print("Chanks:", ex[2])
    ch1 = ex[2]
    print()

    print("Standart mod")
    ex = hourMinCount(hours, 0.5, chank)
    print("hours:", ex[0], " min:", ex[1])
    print("Chanks:", ex[2])
    ch2 = ex[2]
    print()

    print("Hard mod")
    ex = hourMinCount(hours, 0.75, chank)  
    print("hours:", ex[0], " min:", ex[1])
    print("Chanks:", ex[2])
    ch3 = ex[2]
    print()
    print("-"*20, "\n")
    chanks = [ch1, ch2, ch3]
    return chanks

def autoDayChank():
    print()
    a = int(input("current time: "))
    print()
    return a

mode = input("d - day, h - hours\nMode: ")

print("до 4 часов ночи:", "\n")

if mode == "d":
    a = autoDayChank()
    x = chankFunction(28, a)
elif mode == "h":
    startHour = 14
    x = chankFunction(28, startHour)
    b = int(input("hours: "))
    for i in x:
        xx = ceil(b/ (i/2))
        print("days of work:", xx, " chanks for day:", i)


# print("до 2 часов ночи:", "\n")
# chankFunction(26, a)

# print("до 6 часов ночи:", "\n")
# chankFunction(30, a)