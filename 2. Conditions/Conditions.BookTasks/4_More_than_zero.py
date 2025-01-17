while True:
    isInt = False;
    number = float(input("Enter the number: "));

    if number.is_integer:
        isInt = True;

    if number > 0 and isInt == True:
        print("Number is integer and more than 0");
    elif number > 0 and isInt == False:
        print("Number is float and more than 0");
    elif number == 0:
        print("Number is equal to 0");
    if number < 0 and isInt == True:
        print("Number is integer and less than 0");
    elif number < 0 and isInt == False:
        print("Number is float and less than 0");
    pressedKey = input("Press any key and try again or q to end the program ")
    if(pressedKey == 'q'):
        break