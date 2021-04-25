
"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk
from tkinter import * 
import math

win = tk.Tk()

eoutput = StringVar()
eoutput.set("Output goes here")

def clickFunction():
    num1 = e1.get()
    num2 = e2.get()
    num1 = float(num1)
    num2 = float(num2)

    x1 = (-num1 + math.sqrt((num1 ** 2) - 4 * 1 * num2)) / (2 * 1)
    x2 = (-num1 - math.sqrt((num1 ** 2) - 4 * 1 * num2)) / (2 * 1)
    quadAnswer = [x1,x2]
    quadAnswer.sort()

    eoutput.set(str(resultvar1.get())+str(resultvar2.get()))


l1 = Label(win, text="ax^2 + bx + c")
l2 =  Label(win, text="Enter in coefficients b and c")
l3 = Label(win, text="Entry b")
e1 = Entry(win)
l4 = Label(win, text="Entry c")
e2 = Entry(win)
b1 = Button(win, text="Click to see output", command=clickFunction)
a_entry1 = Entry(win, width=70, textvariable=eoutput)

l1.pack()
l2.pack()
l3.pack()
e1.pack()
l4.pack()
e2.pack()
b1.pack()
a_entry1.pack()

win.mainloop()