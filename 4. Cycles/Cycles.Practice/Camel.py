from random import randint

print("""Добро пожаловать в игру Верблюд!
Вы украли верблюда, чтобы пересечь великую пустыню Гоби.
Туземцы хотят вернуть своего верблюда и преследуют вас! Пройдите через пустыню и обгоните туземцев.\n""")



class Game:
    done = False
    distance = 0
    thirst_level = 4
    fatigue = 0
    enemy_distance = -20
    sips_water_count = 3

new_game = Game()

while not new_game.done:
    print("""A. Выпить из фляги.
B. Ехать вперёд на умеренной скорости.
C. Ехать вперёд на полной скорости.
D. Остановиться на ночь.
E. Проверить статус.
Q. Выйти из игры.\n""")
    user_choice = input("Сделайте свой ход: ")
    if user_choice.upper() == 'Q':
        new_game.done = True
    elif user_choice.upper() == 'E':
        print(f"""\nПройдено миль: {new_game.distance}
Напитков во фляге: {new_game.sips_water_count}
Туземцы находятся на расстоянии {new_game.distance - new_game.enemy_distance} миль от вас.\n""")
    elif user_choice.upper() == 'D':
        new_game.fatigue = 0
        new_game.enemy_distance += randint(7, 14)
        print(f"\nВерблюд доволен! Туземцы находятся на расстоянии {new_game.distance - new_game.enemy_distance} миль от вас.")
    elif user_choice.upper() == 'C':
        add = randint(10, 20)
        new_game.distance += add
        new_game.thirst_level += 1
        new_game.fatigue += randint(1, 3)
        new_game.enemy_distance += randint(7, 14)
        print(f"\nСегодня вы проехали {add} миль, всего вы проехали {new_game.distance} миль.")
    elif user_choice.upper() == 'B':
        add = randint(5, 12)
        new_game.distance += add
        new_game.thirst_level += 1
        new_game.fatigue += 1
        new_game.enemy_distance += randint(7, 14)
        print(f"\nСегодня вы проехали {add} миль, всего вы проехали {new_game.distance} миль.")
    elif user_choice.upper() == 'A':
        if new_game.sips_water_count > 0:
            new_game.sips_water_count -= 1
            new_game.thirst_level = 0
            print("\nВы утолили жажду!")
        else:
            print("\nУ вас нет воды..")
    if 1 == 1:
        print("Вы нашли оазис!")
        new_game.sips_water_count = 3
        new_game.thirst_level = 0
        new_game.fatigue = 0
        new_game.enemy_distance += randint(7, 14)
        print(f"\nВерблюд доволен! Туземцы находятся на расстоянии {new_game.distance - new_game.enemy_distance} миль от вас.")
    if new_game.thirst_level >= 4 and new_game.thirst_level <= 6:
        print("Вы испытываете жажду.")
    if new_game.thirst_level > 6:
        print("Вы умерли от жажды!")
        new_game.done = True
    if new_game.fatigue > 5 and new_game.fatigue <= 8:
        print("Ваш верблюд устал.")
    if new_game.fatigue > 8:
        print("Ваш верблюд умер!")
        new_game.done = True
    if (new_game.distance - new_game.enemy_distance) < 15 and (new_game.distance - new_game.enemy_distance) > 0:
        print("Туземцы приближаются!")
    if new_game.enemy_distance >= new_game.distance:
        print("О нет! Туземцы вас догнали!")
        new_game.done = True
    if new_game.distance >= 200:
        print(f"Вы проехали {new_game.distance} миль. Вы пересекли пустыню! Вы победили!")
        new_game.done = True
    
    