from tkinter import *
from PIL import ImageTk, Image
from datetime import date
from dateutil import relativedelta

today = date.today()

def get_date(event):
    day = int(entry_day.get())
    month = int(entry_month.get())
    year = int(entry_year.get())
    years = today.year - year
    birthday = date(year + years, month, day)
    if((today - birthday).days < 0):
        years -= 1
        birthday = date(year + years, month, day)

    days = (today - birthday).days
    lbl_age = Label(root, text=f"You are {years} years and {days} days")
    lbl_age.grid(column=0, row=5)
    btn_close = Button(root, text = "Close", command=root.destroy)
    btn_close.grid(column=1, row=8, sticky = W)

root = Tk()
root.geometry("350x170")
root.title("Ageometer")
photo = ImageTk.PhotoImage(Image.open("C:\Data\Python\\3. Libs\Libs.Practice\Ageometer\\test.png"))
root.iconphoto(False, photo)

lbl = Label(root, text = "Hello!", justify='left')
lbl_today = Label(root, text = f"Today is {today.strftime("%B %d, %Y")}")

lbl_day = Label(root, text="Enter day of your birthday")
entry_day = Entry(root, width=10)
entry_day.focus()
lbl_month = Label(root, text="Enter month of your birthday")
entry_month = Entry(root, width=10)
lbl_year = Label(root, text="Enter year of your birthday")
entry_year = Entry(root, width=10)



lbl.grid(column=0, row=0, sticky = W, padx=2, pady=5)
lbl_today.grid(column=0, row=1, sticky = W, padx=2)
lbl_day.grid(column=0, row=2, sticky = W, padx=2)
entry_day.grid(column=1, row=2)
lbl_month.grid(column=0, row=3, sticky = W, padx=2)
entry_month.grid(column=1, row=3)
lbl_year.grid(column=0, row=4, sticky = W, padx=2)
entry_year.grid(column=1, row=4)

entry_year.bind("<Return>", get_date)

mainloop()