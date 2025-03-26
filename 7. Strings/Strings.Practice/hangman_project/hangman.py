import random
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk 

cur_step = 0
letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

file = open('countries.txt', encoding='utf-8')
words = []
for line in file:
    words.append(line.strip())
file.close()
word = random.choice(words)

txt = ''
for w in word:
    if w == ' ' or w == '-':
        txt += w
    else:
        txt += '_'
buttons = []

steps = [
    lambda: canvas.create_line(50, 250, 150, 250, width=5),
    lambda: canvas.create_line(100, 250, 100, 50, width=5),
    lambda: canvas.create_line(100, 50, 150, 50, width=5),
    lambda: canvas.create_line(150, 50, 150, 80, width=5),
    lambda: canvas.create_oval(135, 80, 165, 110, width=3),
    lambda: canvas.create_line(150, 110, 150, 170, width=3),
    lambda: canvas.create_line(150, 120, 130, 150, width=3),
    lambda: canvas.create_line(150, 120, 170, 150, width=3),
    lambda: canvas.create_line(150, 170, 130, 200, width=3),
    lambda: canvas.create_line(150, 170, 170, 200, width=3)
]

def add_part():
    global cur_step
    cur_step += 1
    if cur_step == len(steps):
        lbl_word.config(text=' '.join(word))
        lbl_result.config(text='Sorry. You lose', fg='red', font=32)
    elif cur_step < len(steps):
        steps[cur_step]()

def new_game():
    global cur_step
    global word
    global txt
    cur_step = 0
    canvas.delete('all')
    lbl_result.config(text='')
    word = random.choice(words)
    txt = ''
    for w in word:
        if w == ' ':
            txt += ' '
        else:
            txt += '_'
    lbl_word.config(text=' '.join(txt))
    i = 0
    for letter in letters:
        btn_letter = Button(letters_frame, text=letter, width=3, command=lambda l=letter, index=i: check_letter(l, index))
        btn_letter.grid(padx=2, pady=2, row=3 + i//7, column=2 + i%7)
        buttons.append(btn_letter)
        i += 1

def check_letter(letter, index):
    global buttons
    buttons[index].config(state='disabled')
    global word
    global txt
    guess = False

    for i in range(len(word)):
        if word[i] == letter:
            txt = txt[0:i] + f'{letter}' + txt[i + 1:]
            print(txt)
            guess = True
    if txt == word:
        lbl_result.config(text='Congratulations!', fg='green', font=32)
    lbl_word.config(text=' '.join(txt))
    if not guess:
        add_part()

root = Tk()
root.geometry('600x500')
root.title('Hangman')
photo = ImageTk.PhotoImage(Image.open('icon.png'))
root.iconphoto(False, photo)

frame_settings = Frame(root, height=70)
frame_settings.grid()

btn_new_game = Button(frame_settings, text="new game", command=new_game)
btn_new_game.grid(padx=(10, 0), row=0, column=0)

lbl_category = Label(frame_settings, text='category')
lbl_category.grid(padx=(10, 0), row=1, column=0)

var = StringVar()

category = ttk.Combobox(frame_settings, width=15, textvariable=var)
category['values'] = ('Countries',
                      'Animals',
                      'Trees',
                      'Cities')

category.grid(row=1, column=1)
category.current()

btn_reveal = Button(frame_settings, text="reveal answer")
btn_reveal.grid(padx=(10, 0), row=2, column=0)

game_frame = Frame(root, bg='white')
game_frame.grid(padx=10, pady=10, row=3, column=0, columnspan=2, rowspan=2)

canvas = Canvas(game_frame, width=250, height= 300, bg='white', bd=0, highlightthickness=0)
canvas.grid(padx=20, pady=20, row=3, columnspan=2)

letters_frame = Frame(root)
letters_frame.grid(padx=10, pady=10, row=3, column=2, columnspan=7)



lbl_word = Label(letters_frame, text=' '.join(txt), font=24)
lbl_word.grid(row=8, column=3 // (len(word)//2) + 1, columnspan=len(word), padx=2, pady=2)

lbl_result = Label(letters_frame)
lbl_result.grid(row=10, column=4, columnspan=3)
mainloop()