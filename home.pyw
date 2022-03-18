import time, os, socket
from tkinter import Tk, Button, Label, Canvas, GROOVE, PhotoImage, mainloop


root = Tk()
root.title("Home")
root.iconbitmap("images/icons/Main.ico")
root.geometry("1400x800")

Home = Canvas(root, width= 1400, height= 800)
Home.pack(fill = "both", expand = True)

Title = Label(root, text= "PYOS", font= ("helvetica", 30),bd=2,relief=GROOVE)
Home.create_window(80, 45, window= Title)

def startedit():
    os.startfile("edit.pyw")

def startbrows():
    os.startfile("brows.pyw")

def startterminal():
    os.startfile("terminal.py")

def startfile():
    os.startfile("file.pyw")

def startcalc():
    os.startfile("calc.pyw")

def startBIOS():
	os.startfile("BIOS.py")

def shutdown():
    root.destroy()

def restart():
    os.startfile("login.pyw")
    root.destroy()


main_icon = PhotoImage(file= 'images/icon_pngs/Main.png')
edit_icon = PhotoImage(file= 'images/icon_pngs/Text_Editor.png')
brows_icon = PhotoImage(file= 'images/icon_pngs/Browser.png')
terminal_icon = PhotoImage(file= 'images/icon_pngs/Terminal.png')
file_icon = PhotoImage(file= 'images/icon_pngs/File_Explorer.png')
calc_icon = PhotoImage(file= 'images/icon_pngs/Calculater.png')
BIOS_icon = PhotoImage(file= 'images/icon_pngs/BIOS.png')
shutdown_icon = PhotoImage(file= 'images/icon_pngs/shutdown.png')

main_btn = Button(root, image= main_icon, command= restart, borderwidth= 7)
Home.create_window(1300, 90, window= main_btn)

brows_btn = Button(root, image= brows_icon, command= startbrows,borderwidth= 0)
Home.create_window(250, 700, window= brows_btn)

edit_btn = Button(root, image= edit_icon, command= startedit, borderwidth= 0)
Home.create_window(400, 700, window= edit_btn)

terminal_btn = Button(root, image= terminal_icon, command= startterminal, borderwidth= 0)
Home.create_window(550, 700, window= terminal_btn)

file_btn = Button(root, image= file_icon, command= startfile, borderwidth= 0)
Home.create_window(700, 700, window= file_btn)

calc_btn = Button(root, image= calc_icon, command= startcalc, borderwidth= 0)
Home.create_window(850, 700, window= calc_btn)

BIOS_btn = Button(root, image= BIOS_icon, command= startBIOS, borderwidth= 0)
Home.create_window(1000, 700, window= BIOS_btn)

shutdown_btn = Button(root, image= shutdown_icon, command= shutdown, borderwidth= 10)
Home.create_window(1300, 700, window= shutdown_btn)

mainloop()