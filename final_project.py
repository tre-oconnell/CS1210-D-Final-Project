#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tre O'Connell and Thomas Higgins's Final Project
CS1210-D
"""
import random

def create_background(bg):
    for _ in range (10):
        row = []
        for _ in range(20):
            x = random.random()
            if x < 0.2:
                row.append('B')
            elif x > 0.2:
                row.append(0)
        bg.append(row)

    #left and right check
    for row in bg:
        for row_ind, val in enumerate(row):
            if val != 'B' and row_ind - 1 >= 0:
                try:
                    if row[row_ind - 1] == 'B':
                        row[row_ind] += 1
                    if row[row_ind + 1] == 'B':
                        row[row_ind] += 1
                except: 
                    IndexError
    
    #up and down check 
    for row_num, row in enumerate(bg):
        for row_ind, row_val in enumerate(row):
            if row_val != 'B' and row_num - 1 >= 0:
                try:
                    if bg[row_num - 1][row_ind] == 'B':
                        bg[row_num][row_ind] += 1
                    if bg[row_num + 1][row_ind] == 'B':
                        bg[row_num][row_ind] += 1
                except:
                    IndexError
    #diagonal check
    for row_num, row in enumerate(bg):
        for row_ind, row_val in enumerate(row):
            if row_val != 'B':
                try:
                    if row_num - 1 >= 0:
                        if bg[row_num - 1][row_ind - 1] == 'B':
                            bg[row_num][row_ind] += 1
                        if bg[row_num - 1][row_ind + 1] == 'B':
                            bg[row_num][row_ind] += 1
                    if row_ind - 1 >= 0:
                        if bg[row_num + 1][row_ind - 1] == 'B':
                            bg[row_num][row_ind] += 1
                        if bg[row_num + 1][row_ind + 1] == 'B':
                            bg[row_num][row_ind] += 1
                except:
                    IndexError


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
"""
for ind, row in enumerate(bg):
    for row_ind, row_val in enumerate(row):
        try:
            if (ind - 1)[row_ind] == 'B':
                ind[row_ind] += 1
            if (ind + 1)[row_ind] == 'B':
                ind[row_ind] += 1
        except:
            IndexError
"""