from random import randint


def guess_number():
    while True:
        print("Let's play! I thought of a number between 0 and 100.")
        number = set()
        number.add(randint(0, 100))
        #nu = {number}
        possible_numbers = set(range(0, 101))
        print(number)
        while True:
            usrInput = input("Enter a set of numbers (or type HELP): ")
            if usrInput == 'q':
                break
            elif usrInput == 'HELP':
                print(f"Possible numbers: {' '.join(map(str, sorted(possible_numbers)))}")
            else:
                guessed_set = set(map(int, usrInput.split()))
                if number == guessed_set:
                    print('YOU WIN!')
                    break
                if guessed_set.issuperset(number):
                    possible_numbers = guessed_set
                    print('YES')
                else:
                    possible_numbers = possible_numbers - guessed_set
                    print('NO')

        usrInput = input("Press 'q' for exit or any key for continue: ")
        if usrInput == 'q':
            break



guess_number()