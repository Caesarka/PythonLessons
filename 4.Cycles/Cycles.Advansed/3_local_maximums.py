import sys

print("Let's find all local maximums in sequense of entered numbers.")
while True:
    max_number = 0
    previouse_number = -sys.maxsize
    current_number = -sys.maxsize - 1
    next_number = -sys.maxsize - 1
    while True:
        next_number = int(input("Enter the number: "))
        if next_number == 0:
            break
        if current_number > previouse_number and current_number > next_number:
            max_number += 1
        previouse_number = current_number
        current_number = next_number
    print(max_number)
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break
