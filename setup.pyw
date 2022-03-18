import os, time
from tkinter import Tk, PhotoImage, Canvas, Entry, Button

root = Tk()
root.title("Register")
root.geometry("465x350")
root.iconbitmap("images/icons/Main.ico")

# Define Image
bg = PhotoImage(file = "images/backgrounds/setup_bg.png")

Canvas = Canvas(root, width = 400, height = 400)
Canvas.pack(fill = "both", expand = True)

# Display Image
Canvas.create_image(0, 0, image = bg, anchor = "nw")

def check():
	name = Entry.get(name_e)
	pas = Entry.get(pas_e)
	with open('user/dataname.pass', 'w') as f:
		f.writelines(name)

	with open('user/password.pass', 'w') as f:
		f.writelines(pas)
	with open('user/info.data', 'w') as f:
		f.writelines("1")

	time.sleep(0.5)
	os.startfile('login.pyw')
	root.destroy()


name_e = Entry(Canvas)
Canvas.create_window(250, 175, window = name_e)

pas_e = Entry(Canvas)
Canvas.create_window(250, 225, window = pas_e)
pas_e.config(show="*")

register = Button(Canvas, text="Register", command=check)
Canvas.create_window(250, 250, window=register)

Canvas.create_text(250, 150, text = "Username", font = "helvetica")
Canvas.create_text(250, 200, text = "Password", font = "helvetica")

root.mainloop()

