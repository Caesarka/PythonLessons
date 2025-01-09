from tkinter import *

def foo():
    label["text"] = "Julianna"

root = Tk()

label = Label(root, text = "Hello, world!")
button = Button(root, text='Click', bg ="red", width=10, height=8, command = lambda: foo())
label.pack()
button.pack()
root.mainloop()