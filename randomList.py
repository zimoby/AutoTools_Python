#!/bin/python
import os, sys
import random 

# if len(sys.argv) > 1: #argparse
list_arg = sys.argv
param=list_arg[1]

if "pr1" in list_arg:
    FS = [
        # 'Awesome Creative Coding',
        'AEXPRESSIONS_Course_1',
        'Character Animation Bootcamp',
        'Classical Animation Workflow & Techniques',
        'Cinema 4D Infinite 3D Loops',
        'Cinema 4D Journey',
        # 'houdini',
        # 'td',
        # 'draw',
        # 'processing',
        # 'fusion',
        # 'c4d',
        # 'python',
        # 'dota',
        # 'arduino',
        'eng',
        # 'jap',
        'Trigonometry',
        ]

if "pr2" in list_arg:
    FS = [
        'Stocks',
        'fastsprints',
        # 'allTasks',
        ]

if "pr3" in list_arg:
    FS = [
    # ------ random
        'Тонкое искусство пофигизма'
        'jedy technics',
        'integral meditation',
        # 'volk',
        # 'creativity,inc ed catmullc'
        # 'iskusstvo voyny, sun dzy'
    # ------ photo & video
        # 'Filmmakers_Eye',
        # 'v poiskah kadra (7\160)'
    # ------ design and art
        'Graphic_Design_-_The_New_Basics',
        # 'Istoriya isskustva. Ernst Gombrih'
        # 'Osnovy_kompozitsii__Golubeva_O_L'
        # 'Rudolf Arnheym Art and visual 1974'
        # 'Josef Albers Interaction of Color',
    # ------ colorist
        # 'COLOR CORRECTION HAND BOOK (Alexis Van Hurkman)'
        # 'VISION AND ART: The biology of seeing (Margaret Livingstone)'
        # 'STEVE HULLFISH: The Art & Technique of Digital Color Correction'
    # ------ illustration   
        # 'Ken_Hultgren_-_The_Know_How_of_Cartooning', 
    # ------ animation
        # 'Design for Motion Fundamentals (186/334)',
        # '_The Animators Workbook_, Tony White',
        # '_Cartoon Animation_, Preston Blair'
    # ------ coding
        'Code Complete',
        # 'Clean code, Robert Cecil Martin'
    # ------ finish
        # 'The Animators Survival Kit', 
        # 'tramp and postpravda'
        # 'Jokhanns_Itten_Iskusstvo_formy'
        # 'design-form_and_chaos',
        # 'Магическая уборка'
    ]

summe=random.choice(FS)        
# print(random.choice(FS))
# if summe = 'books':
#     summe=random.choice(FS)  
print(summe)

# print(param)