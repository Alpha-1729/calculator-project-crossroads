
#!usr/bin/python3
# Code to make a simple calculator(GUI) using python3

from tkinter import *
from tkinter import font as tkFont 



# Screen width and height
screen_width=700
screen_height=500

# Function for clearing the screen.
def clear_screen():
    pass

root=Tk()
root.geometry("{}x{}".format(screen_width,screen_height)) # Setting the geometry.
root.title("Simple Calculator")

# Setting the font.
text_font = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)

# Clear button
clr_btn = Button(root, text ="CLEAR",width=40,font=text_font,command = clear_screen)
clr_btn.config(anchor=CENTER) # To allign the text at the center.
clr_btn.grid(row=1,column=0,columnspan=4)


# Seven button
seven_btn = Button(root, text ="7",width=10,font=text_font,command = clear_screen)
seven_btn.grid(row=2,column=0)

# Eight button
eight_btn = Button(root, text ="8",width=10,font=text_font,command = clear_screen)
eight_btn.grid(row=2,column=1)

# Nine button
nine_btn = Button(root, text ="9",width=10,font=text_font,command = clear_screen)
nine_btn.grid(row=2,column=2)

# Divide button
divide_btn = Button(root, text ="/",width=10,font=text_font,command = clear_screen)
divide_btn.grid(row=2,column=3)




root.mainloop()
