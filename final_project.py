#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tre O'Connell and Thomas Higgins's Final Project
CS1210-D
"""
import random

import tkinter
import customtkinter  # <- import the CustomTkinter module



def button_function():
    print("button pressed")

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
                    
def create_display(disp):
    for _ in range(10):
        row = []
        for __ in range(20):
            row.append('')
        disp.append(row)

display = []
background = []

create_background(background)
create_display(display)

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("1600x880")
root_tk.title("Minesweeper")

button = customtkinter.CTkButton(master=root_tk, corner_radius=0, command=button_function)
button.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)

for i in range(10):  # Rows
    for j in range(20):  # Columns
        button = tkinter.Button(root_tk, text = display[i][j])
        button.grid(row=i, column=j, padx=5, pady=5)

root_tk.mainloop()