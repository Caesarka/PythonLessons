from tkinter import *
#from tkinter.ttk import *
#from os import path
#from pathlib import Path
from PIL import ImageTk, Image
#from tkinter import filedialog

predictions = ["You’ll have a day full of laughter and joy.",
               "Adventure is in your future—pack your bags!",
               "Absolutely—just be ready to embrace it.",
               "Today is perfect for trying something new.",
               "You’ll cross paths with someone interesting.",
               "A surprise is waiting for you just around the corner.",
               "A stranger who will inspire you.",
               "Yes, luck is on your side today!",
               "You’ll find fortune in the most unexpected place.",
               "Yes, but don’t forget to make your own luck too!",
               "Your positive energy will attract good things.",
               "Someone who needs your advice or support."
]

def get_name(event):
    name = entry_name.get()
    lbl_greeting.config(text=f"Hello, {name}!")
    lbl_get_number.config(text="Ask a question and enter a number from 1 to 12")
    entry_number.focus()
    entry_number.pack(padx=10, anchor="w")

def get_number(event):
    number = int(entry_number.get())
    lbl_prediction.config(text=f"{predictions[number]}")
    lbl_prediction.pack(padx=10, pady=10, anchor="w")
    btn_close.pack()

root = Tk()
root.geometry("350x270")
root.title("Predictor")
photo = ImageTk.PhotoImage(Image.open("C:\Data\Python\\3. Libs\Libs.Practice\Predictor\\predictor.jpg"))
root.iconphoto(False, photo)
#path_to_dat = Path(__file__).resolve().with_name("info.png")
#root.iconphoto(False, path_to_dat)
#root.img = PhotoImage(file='C:\\Data\\Python\\3. Libs\\Libs.Practice\\Predictor\\predictor.jpg')
#root.iconphoto( False, root.img)

lbl = Label(root, text = "Hello!\nI am a fortune teller.", justify='left')
lbl_name = Label(root, text = "What is your name?")

entry_name = Entry(root)
entry_name.focus()
lbl_greeting = Label(root)
lbl_get_number = Label(root)
entry_number = Entry(root)
lbl_prediction = Label(root)
btn_close = Button(root, text = "Close", command=root.destroy) 

lbl.pack(padx=10, pady=10, anchor="w")
lbl_name.pack(padx=10, anchor="w")
entry_name.pack(padx=10, anchor="w")
lbl_greeting.pack(padx=10, pady=10, anchor="w")
lbl_get_number.pack(padx=10, anchor="w")

entry_name.bind("<Return>", get_name)
entry_number.bind("<Return>", get_number)

mainloop()