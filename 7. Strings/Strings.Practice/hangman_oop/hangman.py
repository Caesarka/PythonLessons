import random
from tkinter import *
from PIL import ImageTk, Image

letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

class Menu:
    def __init__(self, root):
        self.menu = Frame(root, bd=5, bg='red')
        self.lbl_menu_frame = Label(self.menu, text='Menu')
        self.menu.pack()
        self.lbl_menu_frame.pack()

class Game:
    def __init__(self, root, word):
        self.game = Frame(root, bd=5, bg='green')
        self.man = Man(self.game)
        self.keyboard = Keyboard(self.game, word)
        self.game.pack()
        
class Man:
    def __init__(self, root):
        self.man = Frame(root)
        self.man.grid(row=0, column=0)
        self.canvas = Canvas(self.man, width=250, height=300, bg='white', bd=0)
        self.canvas.grid(row=0, column=0)

class Keyboard:
    def __init__(self, root, word):
        self.word = word
        self.keyboard = Frame(root)
        self.keyboard.grid(row=0, column=1)
        self.buttons = []

        for index, letter in enumerate(letters):
            btn = Button(self.keyboard, text=letter, command=lambda l=letter, i=index: self.word.check_letter(l, i, self.buttons))
            btn.grid(padx=2, pady=2, row=3 + index//7, column=2 + index%7)
            self.buttons.append(btn)

class Word:
    def __init__(self, root):
        self.word = Frame(root)
        self.word.pack()
        self.lbl_word = Label(self.word, text='', font=24)
        self.lbl_word.pack(padx=20, pady=20)
        self.current_word = ''
        self.word_mask = ''
        self.step_count = 0

    def choose_word(self):
        words = []

        file = open('countries.txt', encoding='utf-8')
        for line in file:
            words.append(line.rstrip())
        file.close()

        self.current_word = random.choice(words)
        self.get_word_mask()
    
    def get_word_mask(self):
        for letter in self.current_word:
            if letter == ' ' or letter == '-':
                self.word_mask += letter
            else:
                self.word_mask += '_'
        
        self.word_mask = ''.join(self.word_mask)
        self.lbl_word.config(text=' '.join(self.word_mask))

    def check_letter(self, letter, index, buttons):
        buttons[index].config(state='disabled')
        guess = False

        for i in range(len(self.current_word)):
            if self.current_word[i] == letter:
                self.word_mask = self.word_mask[0:i] + f'{letter}' + self.word_mask[i + 1:]
                print(self.word_mask)
                guess = True
            
        self.lbl_word.config(text=' '.join(self.word_mask))

#        if self.word_mask == self.current_word:
#            lbl_result.config(text='Congratulations!', fg='green', font=32)
#            self.lbl_word.config(text=' '.join(self.txt))
        if not guess:
            self.draw()

    def draw(self):
        step = steps[self.step_count]
        figures[step['type']](step['coords'])
        self.step_count += 1


if __name__ == '__main__':
    root = Tk()
    root.geometry('600x500')
    root.title('Hangman')
    photo = ImageTk.PhotoImage(Image.open('icon.png'))
    root.iconphoto(False, photo)

    menu = Menu(root)
    word = Word(root)
    word.choose_word()

    game = Game(root, word)

    figures = {
        'wide_line': lambda coord: game.man.canvas.create_line(coord, width=5),
        'oval': lambda coord: game.man.canvas.create_oval(coord, width=5),
        'narrow_line': lambda coord: game.man.canvas.create_line(coord, width=3)
    }

    steps = [
        {
            'type': 'wide_line',
            'coords': (50, 250, 150, 250)
        },
        {
            'type': 'wide_line',
            'coords': (100, 250, 100, 50)
        },
        {
            'type': 'wide_line',
            'coords': (100, 50, 150, 50)
        },
        {
            'type': 'wide_line',
            'coords': (150, 50, 150, 80)
        },
        {
            'type': 'oval',
            'coords': (135, 80, 165, 110)
        },
        {
            'type': 'narrow_line',
            'coords': (150, 110, 150, 170)
        },
        {
            'type': 'narrow_line',
            'coords': (150, 120, 130, 150)
        },
        {
            'type': 'narrow_line',
            'coords': (150, 120, 170, 150)
        },
        {
            'type': 'narrow_line',
            'coords': (150, 170, 130, 200)
        },
        {
            'type': 'narrow_line',
            'coords': (150, 170, 170, 200)
        }
    ]

    mainloop()