print("Let's find first digit of fractional part of the entered number.")
while True:
    number = float(input("Enter the number: "))
    fraction = number - int(number)
    digit = int((fraction * 10) // 1)
    print(f"Fractional part of the number {number} is {digit}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break