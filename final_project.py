#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tre O'Connell and Thomas Higgins's Final Project
CS1210-D
"""
import random

def create_background(bg):
    for i in range (10):
        row = []
        for i in range(20):
            x = random.random()
            if x < 0.2:
                row.append('B')
            elif x > 0.2:
                row.append(0)
        bg.append(row)
"""        
#def complete_background(bg):
    #left and right check
    for row in background:
        for ind, each in enumerate(row):
            if each != 'B':
                try:
                    if row[ind - 1] == 'B':
                        row[ind] += 1
                    if row(ind + 1) == 'B':
                        row[ind] += 1
                except: 
                    IndexError
    #up and down check
    
    #diagonal check
"""

display = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

background = []

create_background(background)
