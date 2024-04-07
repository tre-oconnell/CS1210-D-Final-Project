#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tre O'Connell and Thomas Higgins's Final Project
CS1210-D
"""
import random

import tkinter
import customtkinter  # <- import the CustomTkinter module

root_tk = tkinter.Tk()
root_tk.geometry("1600x880")
root_tk.title("Minesweeper")

restart_button = tkinter.Button(root_tk, text='Restart', height = 2, width = 10, command = lambda: restart())
restart_button.grid(row=(11), column=5, columnspan=4)



def reveal(row, column):
    display[row][column] = background[row][column]
    button = buttons[row][column]
    button.config(text = display[row][column])
    print(display)


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
            if row_val != 'B':
                try:
                    if bg[row_num - 1][row_ind] == 'B' and row_num - 1 >= 0:
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
def create_buttons(bttns):
    for i in range(10):  # Rows
        row_buttons = []  # Create a list to store buttons in each row
        for j in range(20):  # Columns
            button = tkinter.Button(root_tk, text=display[i][j], height = 2, width = 1)
            button.grid(row=(i), column=j)
            button.config(command=lambda i=i, j=j: reveal(i, j))
            row_buttons.append(button)  # Append button to row_buttons
        bttns.append(row_buttons)  # Append row_buttons to buttons

def start():
    global display, background, buttons
    create_background(background)
    create_display(display)
    create_buttons(buttons)

def restart():
    global display, background, buttons
    display = []
    background = []
    buttons = []
    start()

display = []
background = []
buttons = []

if __name__ == '__main__':
    start()

    root_tk.mainloop()