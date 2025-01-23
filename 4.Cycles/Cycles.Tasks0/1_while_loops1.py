print("Let's print numbers from the one your entered to zero.")
while True:
    number = int(input("Enter number: "))
    while number >= 0:
        print(number)
        number -= 1
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break