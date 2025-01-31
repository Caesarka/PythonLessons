from tkinter import *
from PIL import ImageTk, Image
import random

rnd = random.randint(1, 6)
print(rnd)

def get_name(event):
    name = entry_name.get()
    lbl_greeting.config(text=f"Hello, {name}!")
    lbl_get_number.config(text="Enter a digit from 1 to 6")
    entry_number.focus()
    entry_number.pack(padx=10, anchor="w")

def get_number(event):
    number = int(entry_number.get())
    if number == rnd:
        lbl_try.config(text=f"Oh no! You're dead! You'll have better luck in your next life.")
    else:
        lbl_try.config(text=f"You're alive! The bullet was in the barrel {number}")
    lbl_try.pack(padx=10, pady=10, anchor="w")
    btn_close.pack()

root = Tk()
root.geometry("350x270")
root.title("Russian roulette")
photo = ImageTk.PhotoImage(Image.open("C:\Data\Python\\3. Libs\Libs.Practice\Russian roulette\\russian-roulette.png"))
root.iconphoto(False, photo)

lbl = Label(root, text = "Hello!\nLet's play in Russian roulette?", justify='left')
lbl_name = Label(root, text = "What is your name?")

entry_name = Entry(root)
entry_name.focus()
lbl_greeting = Label(root)
lbl_get_number = Label(root)
entry_number = Entry(root)
lbl_try = Label(root)
btn_close = Button(root, text = "Close", command=root.destroy) 

lbl.pack(padx=10, pady=10, anchor="w")
lbl_name.pack(padx=10, anchor="w")
entry_name.pack(padx=10, anchor="w")
lbl_greeting.pack(padx=10, pady=10, anchor="w")
lbl_get_number.pack(padx=10, anchor="w")

entry_name.bind("<Return>", get_name)
entry_number.bind("<Return>", get_number)

mainloop()