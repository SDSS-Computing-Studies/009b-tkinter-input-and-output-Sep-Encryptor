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
win.title("Factor")
win.geometry("600x200")

eoutput = StringVar()
eoutput.set("Output goes here")

def clickFunction():
    answer=""
    number1 = e1.get()
    number2 = e2.get()
    number1=float(number1)
    number2=float(number2)
    c=float((number1)**2 - 4*1*number2)
    a=1
    if c >= 0 and c == int(c) and math.sqrt(c)==int(math.sqrt(c)):
        while a <= number2:
            if (number2)%a == 0:
                b=int((number2)/a)
                if a + b == number1:
                    b=str(b)
                    answer="(x + "+str(a)+")(x + "+b+")"
                a+=1

            if number1 < 0 or number2 < 0:
                a=-1
            while abs(a) < number2:
                if (number2)%a == 0:
                    b=int((number2)/a)
                    if a+b == number1:                    
                        b=str(b)
                        if int(b)>0:
                            answer="(x "+str(a)+")(x + "+b+")"
                        elif int(a)>0:
                            answer="(x + "+str(a)+")(x "+b+")"
                        else:
                            answer="(x "+str(a)+")(x "+b+")"

                a-=1

        else:
            answer="cannot be factored"

        e3.delete(0,END)
        e3.insert(0,answer)

l1=tk.Label(win,text="enter the coefficients: ")
l2=tk.Label(win,text="Factored form: ")
l3=tk.Label(win,text="x^2 + ")
l4=tk.Label(win,text="x + ")

b1 = tk.Button(win, text="Click to factor", command=clickFunction)

e1=tk.Entry(win,width=5)
e2=tk.Enrty(win,width=5)
e3=tk.Entry(win, width=2, textvariable=eoutput)


l1.grid(row=1,column=1)
l3.grid(row=1,column=2)

e1.grid(row=1,column=3)

l4.grid(row=1,column=4)

e2.grid(row=1,column=5)

b1.grid(row=2, column=1, columnspan=5)


l2.grid(row=3,column=1)
e3.grid(row=3,column=2,columnspan=4)

win.mainloop()