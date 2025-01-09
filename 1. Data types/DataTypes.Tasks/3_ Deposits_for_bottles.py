while True:
    print("Let's calculate your refund for containers")
    try:
        smallContainer = float(input("Enter the number of containers of 1 liter or less: "))
        bigContainer = float(input("Enter the number of containers grater than 1 liter:  "))
        totalReturn = round((smallContainer * 0.10 + bigContainer * 0.25), 2)
        print(f"Your refund will be ${totalReturn}")
    except:
        print("Please use numbers for length and width")
    print()
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break