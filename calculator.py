#!usr/bin/python3
# Code to make a simple calculator(GUI) using python3.

from tkinter import *
from tkinter import font as tkFont

# Screen width and height.
screen_width = 730
screen_height = 355


# Function for clearing the screen.
def clear_screen():
    display.set("")


# Function for displaying entered data on screen.
def print_data(key):
    if display.get() == "ERROR":
        clear_screen()
    word = display.get() + key
    display.set(word)


# Function for showing answer, when = is pressed.
def get_ans():
    # Check errors in expression entered
    try:
        word = eval(display.get())
        display.set(word)
    except:
        word = "ERROR"
        display.set(word)


root = Tk()

# Setting the geometry.
root.geometry("{}x{}".format(screen_width, screen_height))
root.title("Simple Calculator")
root.resizable(0, 0)  # Setting a fixed size for calculator.

# Setting the font.
text_font = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)

# Adding the display area.
display = StringVar()
display_area = Entry(root, width=46, bd=20, textvariable=display,
                     justify="right", font=text_font, bg="powder blue")
display_area.grid(row=0, column=0, columnspan=4)

# Clear button
clr_btn = Button(root, text="CLEAR", width=43, font=text_font,
                 bg="darkOrchid1", command=clear_screen)
clr_btn.grid(row=1, column=0, padx=2, sticky=W, columnspan=4)

# Seven button
seven_btn = Button(root, text="7", width=10, font=text_font,
                   bg="black", fg="white", command=lambda: print_data("7"))
seven_btn.grid(row=2, column=0)

# Eight button
eight_btn = Button(root, text="8", width=10, font=text_font,
                   bg="black", fg="white", command=lambda: print_data("8"))
eight_btn.grid(row=2, column=1)

# Nine button
nine_btn = Button(root, text="9", width=10, font=text_font,
                  bg="black", fg="white", command=lambda: print_data("9"))
nine_btn.grid(row=2, column=2)

# Divide button
divide_btn = Button(root, text="/", width=10, font=text_font,
                    bg="orange", fg="black", command=lambda: print_data("/"))
divide_btn.grid(row=2, column=3)

# Four button
four_btn = Button(root, text="4", width=10, font=text_font,
                  bg="black", fg="white", command=lambda: print_data("4"))
four_btn.grid(row=3, column=0)

# Five button
five_btn = Button(root, text="5", width=10, font=text_font,
                  bg="black", fg="white", command=lambda: print_data("5"))
five_btn.grid(row=3, column=1)

# Six button
six_btn = Button(root, text="6", width=10, font=text_font,
                 bg="black", fg="white", command=lambda: print_data("6"))
six_btn.grid(row=3, column=2)

# Mul button
mul_btn = Button(root, text="*", width=10, font=text_font,
                 bg="orange", fg="black", command=lambda: print_data("*"))
mul_btn.grid(row=3, column=3)

# One button
one_btn = Button(root, text="1", width=10, font=text_font,
                 bg="black", fg="white", command=lambda: print_data("1"))
one_btn.grid(row=4, column=0)

# Two button
two_btn = Button(root, text="2", width=10, font=text_font,
                 bg="black", fg="white", command=lambda: print_data("2"))
two_btn.grid(row=4, column=1)

# Three button
three_btn = Button(root, text="3", width=10, font=text_font,
                   bg="black", fg="white", command=lambda: print_data("3"))
three_btn.grid(row=4, column=2)

# Minus button
minus_btn = Button(root, text="-", width=10, font=text_font,
                   bg="orange", fg="black", command=lambda: print_data("-"))
minus_btn.grid(row=4, column=3)

# Dot button
dot_btn = Button(root, text=".", width=10, font=text_font,
                 bg="black", fg="white", command=lambda: print_data("."))
dot_btn.grid(row=5, column=0)

# Zero button
zero_btn = Button(root, text="0", width=10, font=text_font,
                  bg="black", fg="white", command=lambda: print_data("0"))
zero_btn.grid(row=5, column=1)

# Equal button
equal_btn = Button(root, text="=", width=10, bg="green",
                   fg="white", font=text_font, command=get_ans)
equal_btn.grid(row=5, column=2)

# Plus button
plus_btn = Button(root, text="+", width=10, font=text_font,
                  bg="orange", fg="black", command=lambda: print_data("+"))
plus_btn.grid(row=5, column=3)

root.mainloop()
