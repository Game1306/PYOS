from tkinter import *
import tkinter
import tkinter.font as font
from tkinter import messagebox

# Copywrite 2022 Paul Dannoot. Do Not Distibute (JK)

# V 2.5

# Setup
top = tkinter.Tk()
top.title('Calculator')
top.iconbitmap('images/icons/Calculator.ico')
clearFont = font.Font(family='Courier', weight="bold")
font = font.Font(family='Helvetica')

#####################
# NORMAL CALCULATOR #
#####################

# Default Calculator Process

def proces():
    number1=Entry.get(E1)
    number2=Entry.get(E2)
    operator=Entry.get(E3)
    try:
        number1=int(number1)
        number2=int(number2)
        if operator =="+":
                answer=number1+number2
        if operator =="-":
                answer=number1-number2
        if operator=="x" or operator=="*":
            answer=number1*number2
        if operator=="/":
            answer=number1/number2
        E4.delete(0, END)
        Entry.insert(E4,0,answer)
    except ValueError:
        messagebox.showerror("Error","Excpected number, found letter or blank")
 

# Clear Normal Calc
def nclear():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
     
# Calculator Labels

L1 = Label(top, text="Calculator",).grid(row=0,column=1)
L2 = Label(top, text="Number 1:",).grid(row=1,column=0)
L3 = Label(top, text="Number 2:",).grid(row=3,column=0)
L4 = Label(top, text="Operator:",).grid(row=2,column=0)
L4 = Label(top, text="Answer:",).grid(row=4,column=0)

# Calculator Entries

E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=3,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=2,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
B=Button(top, text ="Submit",command = proces).grid(row=5,column=1,)


####################
#  GCF CALCULATOR  #
####################


# GCF Calculator process

def gproces():
    Gnumber1=Entry.get(GE1)
    Gnumber2=Entry.get(GE2)
    try:
        Gnumber1=int(Gnumber1)
        Gnumber2=int(Gnumber2)

        if Gnumber1 > Gnumber2:
            Gnumber1, Gnumber2 = Gnumber2, Gnumber1

        for x in range (Gnumber1, 0, -1):
            if Gnumber1 % x == 0 and Gnumber2 % x == 0:
                GE3.delete(0, END)
                Entry.insert(GE3,0,x)
                break
    except ValueError:
        messagebox.showerror("Error","Excpected number, found letter or blank")

# Clear GFC
def gclear():
    GE1.delete(0, END)
    GE2.delete(0, END)
    GE3.delete(0, END)

# GCF Calculator Labels
GL1 = Label(top, text="GCF Calculator",).grid(row=0,column=4)
GL2 = Label(top, text="Number 1:",).grid(row=1,column=3)
GL3 = Label(top, text="Number 2:",).grid(row=2,column=3)
Gl4 = Label(top,text="Answer:",).grid(row=3,column=3)


# GCF Calculator Entries
GE1 = Entry(top, bd =5)
GE1.grid(row=1,column=4)
GE2 = Entry(top, bd =5)
GE2.grid(row=2,column=4)
GE3= Entry(top, bd =5)
GE3.grid(row=3,column=4)
GB=Button(top, text ="Submit",command = gproces).grid(row=4,column=4)


####################
#  LCM CALCULATOR  #
####################

# GCF Calculator process

def lproces():
    x=Entry.get(LE1)
    y=Entry.get(LE2)
    try:
        x=int(x)
        y=int(y)

        if x > y:
           greater = x
        else:
           greater = y

        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        LE3.delete(0, END)
        Entry.insert(LE3,0,lcm)
    except ValueError:
        messagebox.showerror("Error","Excpected number, found letter or blank")

# Clear LCM
def lclear():
    LE1.delete(0, END)
    LE2.delete(0, END)
    LE3.delete(0, END)

# GCF Calculator Labels
LL1 = Label(top, text="LCM Calculator",).grid(row=6,column=1)
LL2 = Label(top, text="Number 1:",).grid(row=7,column=0)
LL3 = Label(top, text="Number 2:",).grid(row=8,column=0)
Ll4 = Label(top,text="Answer:",).grid(row=9,column=0)


# LCM Calculator Entries
LE1 = Entry(top, bd =5)
LE1.grid(row=7,column=1)
LE2 = Entry(top, bd =5)
LE2.grid(row=8,column=1)
LE3= Entry(top, bd =5)
LE3.grid(row=9,column=1)
LB=Button(top, text ="Submit",command = lproces).grid(row=10,column=1,)

def CLEAR():
    lclear()
    gclear()
    nclear()

CLEARALL=Button(top, text="CLEAR ALL",command = CLEAR,font=clearFont).grid(row=8,column=4)
# GO
top.mainloop()