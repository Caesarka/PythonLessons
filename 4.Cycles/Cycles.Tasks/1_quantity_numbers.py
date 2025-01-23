print("Let's count the numbers that you are going to enter.")
while True:
    count = 0
    while True:
        number = int(input("Enter number: "))
        if number == 0:
            print(f"{count} numbers was entered.")
            break
        count += 1
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break