#!usr/bin/python3
# Code for creating a button for running the python script.

"""
NOTE:
>>>>font, height and width parameter work for tkinter Button and not for ttk Button.
"""
import os
from tkinter import *
from tkinter import ttk


def run_file():
    os.startfile("run_file.bat")


root = Tk()
root.geometry('30x30+{}+{}'.format(+1300, +550))

run_button = Button(root, text="R", bg="orange", font=(
    'Arial Bold', '12'), command=run_file)
run_button.pack()
root.update()

# Create the gui window above all other apps.
root.attributes("-topmost", True)
root.overrideredirect(True)     # Removing the x button in window.
root.lift()    # Bring tk window to front.
root.mainloop()
