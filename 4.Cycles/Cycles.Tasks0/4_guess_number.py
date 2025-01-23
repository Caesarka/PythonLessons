import random
import sys

print("Let's guess the number that on computer's mind")
while True:
    rand = random.randint(1, 100)
    number = -sys.maxsize - 1
    attempts = 8
    while attempts > 0:
        number = int(input(f"You have {attempts} attempts left. Enter number: "))
        if number == rand:
            print("Congratulations, you guessed it!")
            break
        else:
            attempts -= 1
            if rand > number:
                print("Incorrect. The number is bigger")
            else:
                print("Incorrect. The number is smaller")
    else:
        print(f"Attempts ended. You did not guess. The computer's number is {rand}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break