import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

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


class FrameConstructor:
    def __init__(self, frame, **config):
        self.config = config
        self.pos = config.pop('pos', {})
        self.root_frame = frame
        self.frame = None
        self.method = 'pack'

    def create_frame(self):
        self.frame = Frame(self.root_frame, **self.config)
        return self.frame

    def render(self, method):
        if method == 'pack':
            self.render_pack()
        elif method == 'grid':
            self.render_grid()

    def render_pack(self):
        if self.frame is None:
            raise ValueError("Frame is not created")
        self.frame.pack()

    def render_grid(self):
        if self.frame is None:
            raise ValueError("Frame is not created")
        self.frame.grid(row=self.pos.get('row', 0),
                        column=self.pos.get('column', 0))


class Menu:
    def __init__(self, root_frame):
        self.menu = Frame(root_frame)
        self.menu.pack(fill='x', side='top')
        self.game = None
        self.root_frame = root_frame

        self.btn_new_game = Button(self.menu, text='new game')
        self.btn_new_game.bind('<Button-1>', self.start_new_game)
        self.btn_new_game.grid(padx=(10, 0), row=0, column=0)

    def start_new_game(self, x):
        if self.game is not None:
            self.game.game_frame.destroy()
            self.game = None
        self.game = Game(self.root_frame)

    def get_word(word):
        word.current_word


class Game:
    def __init__(self, parent_frame):
        self.game_frame = Frame(parent_frame, bd=5, width=500, height=300)
        self.game_frame.pack()

        self.man = ManCanvas(self.game_frame, width=200, height=200,
                             bg='red', bd=0, pos={'row': 0})
        self.man.create_frame()
        self.man.render(self.man.method)
        self.word = Word(self, self.game_frame)
        self.word.choose_word(self.game_frame)
        self.keyboard = Keyboard(
            self.game_frame, self.word, width=250, height=300, bd=0, pos={'column': 1})
        self.keyboard.create_frame()
        self.keyboard.render(self.keyboard.method)
        self.keyboard.create_keyboard_btn()
        self.label = Label(self.game_frame, justify='center')
        self.label.grid(row=2, column=0, columnspan=3)

    def resume_game(self):
        print(f"Mask: {self.word.word_mask}")
        print(f"Word: {self.word.current_word}")
        print(
            f"True or False: {self.word.word_mask == self.word.current_word}")
        if self.word.step_count == len(steps) or self.word.word_mask == self.word.current_word:
            for btn in self.keyboard.buttons:
                btn.unbind('<Button-1>')
                btn.config(state='disabled')

    def set_game_label(self):
        if self.word.word_mask == self.word.current_word:
            self.label.config(text='Congradulation!',
                              fg='green', font=('Arial', 24, 'bold'))
        if self.word.step_count == len(steps):
            self.label.config(text='You lost!', fg='red',
                              font=('Arial', 24, 'bold'))
            self.word.lbl_word.config(text=' '.join(self.word.current_word))


class ManCanvas(FrameConstructor):

    def __init__(self, game_frame, **config):
        super().__init__(game_frame, **config)
        self.figures = {
            'wide_line': lambda coord: self.canvas.create_line(coord, width=5),
            'oval': lambda coord: self.canvas.create_oval(coord, width=5),
            'narrow_line': lambda coord: self.canvas.create_line(coord, width=3)
        }
        self.method = 'grid'
        self.game_frame = game_frame

    def create_frame(self):
        super().create_frame()

        self.canvas = Canvas(self.game_frame, width=250,
                             height=300, bg='white', bd=0)
        self.canvas.grid(row=0, column=0)
        return self.game_frame

    def draw(self, step_count):  # увеличивать после вызова
        step = steps[step_count]
        self.figures[step['type']](step['coords'])


class Keyboard(FrameConstructor):
    def __init__(self, frame, word, **config):
        super().__init__(frame, **config)
        self.buttons = []
        self.check_word = word
        self.letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.method = 'grid'

    def create_keyboard_btn(self):
        for index, letter in enumerate(self.letters):
            btn = Button(self.frame, text=letter)
            btn.index = index
            btn.letter = letter
            btn.bind('<Button-1>', lambda event: self.check_word.check_letter(
                event.widget.letter, event.widget.index, self.buttons))
            btn.grid(padx=2, pady=2, row=3 + index//7, column=2 + index % 7)
            self.buttons.append(btn)


class Word(FrameConstructor):
    def __init__(self, game, frame, **config):
        super().__init__(frame, **config)
        self.game = game
        self.current_word = ''
        self.word_mask = ''
        self.step_count = 0

    def choose_word(self, game):
        words = []
        self.lbl_word = Label(self.root_frame, text='', font=24)
        self.lbl_word.grid()
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
                self.word_mask = self.word_mask[0:i] + \
                    f'{letter}' + self.word_mask[i + 1:]
                self.lbl_word.config(text=' '.join(self.word_mask))
                print(self.word_mask)
                guess = True
        if not guess:
            self.game.man.draw(self.step_count)
            self.step_count += 1
        self.game.resume_game()
        self.game.set_game_label()


def main():
    root_frame = Tk()
    root_frame.geometry('600x500')
    root_frame.title('Hangman')
    photo = ImageTk.PhotoImage(Image.open('icon.png'))
    root_frame.iconphoto(False, photo)

    menu = Menu(root_frame)

    print(isinstance(menu, Menu))
    print(isinstance(menu, FrameConstructor))
    print(isinstance(menu, object))
    print(type(menu))

    mainloop()


if __name__ == '__main__':
    main()
