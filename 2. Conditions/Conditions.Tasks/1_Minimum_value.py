while True:

    try:
        firstNumber = int(input("Enter the first number: "))
        secondNumber = int(input("Enter the second number: "))
        if firstNumber > secondNumber:
            print(f"The smallest number is {secondNumber}")
        elif firstNumber < secondNumber:
            print(f"The smallest number is {firstNumber}")
        else:
            print(f"Numbers are equal")

    except:
        print("Please use numbers. Try again")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break



