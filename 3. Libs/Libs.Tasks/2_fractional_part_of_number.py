print("Let's find fractional part of the entered number.")
while True:
    number = float(input("Enter the number: "))
    fraction = number - int(number)
    print(f"Fractional part of the number {number} is {round(fraction, 5)}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break