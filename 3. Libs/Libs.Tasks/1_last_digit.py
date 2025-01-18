print("Let's find last digit of the entered number.")
while True:
    number = input("Enter the number: ")
    digit = number[len(number) - 1]
    print(f"Last digit in number {number} is {digit}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break