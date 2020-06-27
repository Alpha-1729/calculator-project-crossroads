import os
from tkinter import *
from tkinter import ttk
def make_file():
    os.startfile("run.bat")
root=Tk()
root.geometry('30x30+{}+{}'.format(+1300,+550))
#root.title("")
button=Button(root,text="R",font=('Arial Bold', '12'),command=make_file) #font,height,width parameter work for tkinter Button and not for ttk Button
button.pack()
root.update()
#create the gui window above all other apps
root.attributes("-topmost", True)
root.overrideredirect(True)
root.lift()
#root.destroy()
root.mainloop()
