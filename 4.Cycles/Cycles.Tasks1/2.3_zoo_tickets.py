print("Let's calculate total price for tickets.")
while True:
    price = 0
    while True:
        age = input("Enter age for visitor. Enter a blank line to finish: ")
        if age == '':
            break
        else:
            age = int(age)
            if age >= 0 and age <= 2:
                continue
            elif age >= 3 and age <= 12:
                price += 14
            elif age >= 13 and age <= 64:
                price += 23
            elif age >= 65 and age < 130:
                price += 14
            else:
                print("Please enter valid age.")
    print(f"The total price equals {price}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break