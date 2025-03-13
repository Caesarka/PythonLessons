def attack(attack_power, defense_level, health):
    damage = attack_power - defense_level
    damage = 0 if damage <= 0 else damage
    health = health - damage
    health = 0 if health <= 0 else health

    print(f'The attacked player\'s health level is {health}')

print('Let\'s calculate the damage done to one character by another.')

attack_power = int(input('Enter attack power of the attacking character '))
defense_level = int(input('Enter defense level of the defending character '))
health = int(input('Enter current health of the defending character '))
attack(attack_power, defense_level, health)