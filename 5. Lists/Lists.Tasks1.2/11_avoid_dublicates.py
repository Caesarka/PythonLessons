print("This program takes cell numbers and return list of unique numbers:")

while True:
    numbers = []
    number = ' '
    print("Enter cell numbers. One number for each string. Enter empty string for stop.")
    while number != '':
        number = input()
        if number not in numbers:
            numbers.append(number)
    del numbers[numbers.index('')]
    print("List of unique numbers:")
    for num in numbers:
        print(num)

    pressedKey = input("Press any key and try again or q to end the program ")
    if(pressedKey == 'q'):
        break
