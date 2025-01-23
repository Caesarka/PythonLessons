print("Let's count the sum of entered numbers.")
while True:
    sum = 0
    while True:
        number = int(input("Enter number: "))
        sum += number
        if number == 0:
            print(f"The sum of entered numbers is {sum}")
            break
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break