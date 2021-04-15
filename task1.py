"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title("Madlib")
win.geometry("900x300")

eoutput = StringVar()
eoutput.set("Output goes here")

def clickFunction():
    e2.delete(0,END)
    number = e1.get()
    number2 = e3.get()
    number3 = e4.get()
    text1="My name is"
    text2=", and I am a"
    text3=". I like"
    a=str(text1+number+text2+number2+text3+number3)
    e2.insert(0,a)

l1=tk.Label(win,text="My name is")
l2=tk.Label(win,text=+", and I am a")
L3=tk.Label(win,text=". I like")

b1 = tk.Botton(win, text="Click to enter",command=clickFunction)
e1=tk.Entry(win,width=20)
e2=tk.Entry(win, width=120, textvariable=eoutput)

e3=tk.Entry(win,width=20)
e4=tk.Entry(win,width=20)

l1.grid(row=1,column=1)
l2.grid(row=1,column=3)
L3.grid(row=1,column=5)
e1.grid(row=1,column=2)
e3.grid(row=1,column=4)
e4.grid(row=1,column=6)
b1.grid(row=2,column=1,columnspan=3)
e2.grid(row=3,column=1,columnspan=6)

win.mainloop()


