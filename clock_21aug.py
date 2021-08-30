from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("GHADI")

def time():
        string = strftime("%I:%M:%S %p")
        label.config(text=string)
        label.after(1000, time)


label = Label(root,font =("ds-digital",70),background= "black",foreground="cyan")
label.pack(anchor='center')

time()
mainloop()











# import time as t
#
# dc = Tk()
# dc.title("Digital clock")
# dc.geometry("500*100")
#
# mainloop()
