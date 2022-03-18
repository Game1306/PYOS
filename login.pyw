import os
import time
from tkinter import messagebox, Tk, Label, Entry, Button

login_pass = open('user/password.pass')
login_name = open('user/dataname.pass')
l_p = login_pass.read()
l_n = login_name.read()

# Check Password
def Ok():
    uname = e1.get()
    password = e2.get()

    # Check if blank
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")

    # Check if correct
    elif(uname == l_n and password == l_p):

        messagebox.showinfo("Yep","Login Success")
        os.startfile("home.pyw")
        root.destroy()

    # Check if incorrect
    else :
        messagebox.showinfo("Nope","Incorrent Username|and|or|Password")


root = Tk()
root.title("Login")
root.geometry("300x200")
root.iconbitmap("images/icons/Main.ico")

global e1
global e2

Label(root, text="Username").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

Entry.insert(e1, 0, l_n)
Button(root, text="Login", command=Ok ,height = 3, width = 13).place(x=10, y=100)


root.mainloop()