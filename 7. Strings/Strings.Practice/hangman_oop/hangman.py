from tkinter import *
from PIL import ImageTk, Image



class Menu:
    def __init__(self, root):
        self.menu_frame = Frame(root, bd=5, bg='red')
        self.lbl_menu_frame = Label(self.menu_frame, text='Menu')
        self.menu_frame.pack()
        self.lbl_menu_frame.pack()

class Game:
    def __init__(self, root):
        self.game_frame = Frame(root, bd=5, bg='green')
        self.man = Man(self.game_frame)
        self.keyboard = Keyboard(self.game_frame, self)
        self.game_frame.pack()
        self.step_count = 0
        
class Man:
    def __init__(self, root):
        self.man_frame = Frame(root)
        self.man_frame.grid(row=0, column=0)
        self.canvas = Canvas(self.man_frame, width=250, height=300, bg='white', bd=0)
        self.canvas.grid(row=0, column=0)
    

class Keyboard:
    def __init__(self, root, game):
        self.game = game
        self.keyboard_frame = Frame(root)
        self.keyboard_frame.grid(row=0, column=1)
        self.btn = Button(self.keyboard_frame, text='Click', command=lambda: self.draw())
        self.btn.grid()

    def draw(self):
        step = steps[self.game.step_count]
        figures[step['type']](step['coords'])
        game.step_count += 1




class Word:
    def __init__(self, root):
        self.word_frame = Frame(root)
        self.word_frame.pack()



if __name__ == '__main__':
    root = Tk()
    root.geometry('600x500')
    root.title('Hangman')
    photo = ImageTk.PhotoImage(Image.open('icon.png'))
    root.iconphoto(False, photo)
    menu = Menu(root)
    game = Game(root)
    word = Word(root)

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