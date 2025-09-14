from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime


global endTime


def quit(*arg):
    root.distroy()


def cant_wait():
    time_left = endTime - datetime.datetime.now()
    time_left = time_left - datetime.timedelta(microseconds=time_left.microseconds)

    txt.set(time_left)

    root.after(1000, cant_wait)


root = Tk()
root.attributes("-fullscreen", False)
root.configure(background="white")
root.bind("x", quit)
root.after(1000, cant_wait)

endTime = datetime.datetime(2023, 9, 26, 0, 0)

fnt = font.Font(family="Helvetica", size=90, weight="bold")
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()