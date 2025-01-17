while True:
    day = input("Enter the number of the day: ")
    if day == '1':
        print("Monday")
    elif day == '2':
        print("Tuesday")
    elif day == '3':
        print("Wednesday")
    elif day == '4':
        print("Thursday")
    elif day == '1':
        print("Friday")
    elif day == '6':
        print("Saturday")
    elif day == '7':
        print("Sunday")
    else:
        print("Please use numbers 1 to 7")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break