class Character:
    list_char = ["power", "health", "wisdom", "dexterity"]
    remaining_points = 30
    char = {}
    for el in list_char:
        char[el] = 0

    def __str__(self):
        return f'''\nPower: {self.char["power"]}, Health: {self.char["health"]}, Wisdom: {self.char["wisdom"]}, Dexterity: {self.char["dexterity"]}
Remaining points: {self.remaining_points}\n
Select a characteristic (1-Strength, 2-Health, 3-Wisdom, 4-Dexterity) and the number of points you want to add or remove:'''
    
    def change_character(self, characteristic, points):
        index = self.list_char[characteristic - 1]
        self.char[index] += (points)
        self.remaining_points -= points


inp = ' '
while True:
    character = Character()
    while True:
        print(character)
        inp = input()
        if inp == '':
            break
        characteristic, __, points = inp.partition(' ')
        characteristic = int(characteristic)
        points = int(points)
        character.change_character(characteristic, points)



    pressedKey = input("Press any key and try again or q to end the program ")
    if(pressedKey == 'q'):
        break


