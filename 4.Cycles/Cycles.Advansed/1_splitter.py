
print("Let's find second number from the first one by dividing and substraction the first number.")
print("First number has to be bigger than second one!")
while True:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    if first_number <= second_number:
        print("First number has to be bigger than second number!")
        break
    else:
        while second_number != first_number:
            if (first_number % 2) == 0 and (first_number / 2) >= second_number:
                first_number = first_number / 2
                print(":2")
            else:
                if first_number - 1 >= second_number:
                    first_number -= 1
                    print("-1")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break
