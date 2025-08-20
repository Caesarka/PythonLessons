from random import randint
from tkinter import *
from tkinter import Tk
from PIL import ImageTk, Image


class Game:
    done = False
    distance = 0
    thirst_level = 4
    fatigue = 0
    enemy_distance = -20
    sips_water_count = 3


new_game = Game()


def check_status():
    new_text = (
        f"Пройдено миль: {new_game.distance}. Напитков во фляге: {new_game.sips_water_count}. Туземцы находятся на расстоянии {new_game.distance - new_game.enemy_distance} миль от вас.")
    print(new_text)
    lbl_text.config(text=new_text)
    set_image("camel_check_status")


def set_image(image_name):
    image = Image.open(f"{image_name}.png")
    image_man_camel_resize = image.resize((400, 300))
    image_tk = ImageTk.PhotoImage(image_man_camel_resize)
    lbl_image_man_camel.config(image=image_tk)


def drink():
    if new_game.sips_water_count > 0:
        new_game.sips_water_count -= 1
        new_game.thirst_level = 0
        new_text = "Вы утолили жажду!\n"
        set_image("camel_drank_water")
    else:
        new_text = "У вас нет воды..\n"
        set_image("camel_no_more_water")
    lbl_text.config(text=new_text)


def go():
    add = randint(5, 12)
    new_game.distance += add
    new_game.thirst_level += 1
    new_game.fatigue += 1
    new_game.enemy_distance += randint(7, 14)
    new_text = (
        f"Сегодня вы проехали {add} миль, всего вы проехали {new_game.distance} миль.\n")
    set_image("camel_go")
    lbl_text.config(text=events(new_text))
    #lbl_text.config(text=new_text)


def run():
    add = randint(10, 20)
    new_game.distance += add
    new_game.thirst_level += 1
    new_game.fatigue += randint(1, 3)
    new_game.enemy_distance += randint(7, 14)
    new_text = (
        f"Сегодня вы проехали {add} миль, всего вы проехали {new_game.distance} миль.\n")
    set_image("camel_run")
    lbl_text.config(text=events(new_text))
    #lbl_text.config(text=new_text)


def rest():
    new_game.fatigue = 0
    new_game.enemy_distance += randint(7, 14)
    new_text = (
        f"Верблюд доволен! Туземцы находятся на расстоянии {new_game.distance - new_game.enemy_distance} миль от вас.\n")
    set_image("camel_rest")
    lbl_text.config(text=events(new_text))
    #lbl_text.config(text=new_text)


def events(new_text):
    if new_game.thirst_level > 6:
        new_text = ("Вы умерли от жажды!")
        lbl_text.config(text=new_text)
        set_image("camel_die_without_water")
        btn_drink.config(state=DISABLED)
        btn_drive.config(state=DISABLED)
        btn_rest.config(state=DISABLED)
        btn_slow_drive.config(state=DISABLED)
        btn_status.config(state=DISABLED)
        new_game.done = True
        return new_text


    elif new_game.fatigue > 8:
        new_text = ("Ваш верблюд умер!")
        lbl_text.config(text=new_text)
        set_image("camel_die")
        btn_drink.config(state=DISABLED)
        btn_drive.config(state=DISABLED)
        btn_rest.config(state=DISABLED)
        btn_slow_drive.config(state=DISABLED)
        btn_status.config(state=DISABLED)
        new_game.done = True
        return new_text


    elif new_game.enemy_distance >= new_game.distance:
        new_text = ("О нет! Туземцы вас догнали!")
        lbl_text.config(text=new_text)
        set_image("camel_game_over")
        btn_drink.config(state=DISABLED)
        btn_drive.config(state=DISABLED)
        btn_rest.config(state=DISABLED)
        btn_slow_drive.config(state=DISABLED)
        btn_status.config(state=DISABLED)
        new_game.done = True
        return new_text

    elif new_game.distance >= 200:
        new_text = (
            f"Вы проехали {new_game.distance} миль. Вы пересекли пустыню! Вы победили!")
        lbl_text.config(text=new_text)
        set_image("camel_win")
        new_game.done = True
        btn_drink.config(state=DISABLED)
        btn_drive.config(state=DISABLED)
        btn_rest.config(state=DISABLED)
        btn_slow_drive.config(state=DISABLED)
        btn_status.config(state=DISABLED)
        new_game.done = True
        return new_text

    if randint(1, 20) == 1:
        new_text += "Вы нашли оазис!\n"
        new_game.sips_water_count = 3
        new_game.thirst_level = 0
        new_game.fatigue = 0
        new_game.enemy_distance += randint(7, 14)
        new_text += (
            f"Верблюд доволен! Туземцы находятся на расстоянии {new_game.distance - new_game.enemy_distance} миль от вас.\n")
        set_image("camel_oazis")

    if new_game.thirst_level >= 4 and new_game.thirst_level <= 6:
        new_text += ("Вы испытываете жажду.\n")
        set_image("camel_thirst")

    if new_game.fatigue > 5 and new_game.fatigue <= 8:
        new_text += ("Ваш верблюд устал.\n")
        set_image("camel_tired")

    if (new_game.distance - new_game.enemy_distance) < 15 and (new_game.distance - new_game.enemy_distance) > 0:
        new_text += ("Туземцы приближаются!\n")
        set_image("camel_natives_are_comming")

    return new_text


root = Tk()
root.geometry("600x550")
root.title("Camel")
photo = ImageTk.PhotoImage(Image.open(
    "C:\\Data\\Python\\4. While loops\\WhileLoops.Practice\\camel.png"))
root.iconphoto(False, photo)

lbl_image_man_camel = Label(root)
lbl_image_man_camel.grid(column=0, row=1, columnspan=2, pady=5)

set_image("camel_start")

lbl_intro = Label(root, text="Добро пожаловать в игру Верблюд!\nВы украли верблюда, чтобы пересечь великую пустыню Гоби.\nТуземцы хотят вернуть своего верблюда и преследуют вас!\nПройдите через пустыню и обгоните туземцев.", justify=LEFT)
lbl_intro.grid(column=0, row=0, sticky=W, padx=2, pady=5)



lbl_text = Label(root, text='', justify=LEFT)
lbl_text.grid(column=0, row=2, columnspan=2, pady=5)

btn_drink = Button(root, text="Выпить из фляги", command=drink)
btn_drink.grid(column=0, row=3, sticky=W)

btn_drive = Button(root, text="Ехать вперёд на умеренной скорости", command=go)
btn_drive.grid(column=1, row=3, sticky=W)

btn_slow_drive = Button(
    root, text="Ехать вперёд на полной скорости", command=run)
btn_slow_drive.grid(column=0, row=4, sticky=W)

btn_rest = Button(root, text="Остановиться на ночь", command=rest)
btn_rest.grid(column=1, row=4, sticky=W)

btn_status = Button(root, text="Проверить статус", command=check_status)
btn_status.grid(column=0, row=5, sticky=W)

btn_exit = Button(root, text="Выйти из игры", command=root.destroy)
btn_exit.grid(column=1, row=5, sticky=W)

mainloop()
