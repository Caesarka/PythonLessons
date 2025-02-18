print("Let's find dividers for number that you are going to enter.")

while True:
    divider = 2
    dividers = []
    while True:
        number = int(input("Enter number that more than 2: "))
        if number > 2:
            while divider < number:
                if number % divider == 0:
                        dividers.append(divider)
                divider += 1
            print(f"Dividers for number {number}: {dividers}")
            break
        else:
            print("The number is equal or less than 2.")
            break
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break