import webbrowser
from tkinter import Tk, Button, Entry, Label


root = Tk()
root.title("Browser")
root.geometry("300x200")
root.iconbitmap("images/icons/Browser.ico")

def browse():
    browser = Entry.get(url)
    webbrowser.open(browser)

Label(root, text="Enter website url or search the web!").pack()

url = Entry(root)
url.pack()

browse_button = Button(root, text="Browse", command=browse)
browse_button.pack()

root.mainloop()