while True:
    print("Let's find area of the triangle!")
    try:
        base = float(input("Enter the base of the triangle in cm: "))
        height = float(input("Enter the height of the triangle in cm: "))
        area = round(base * height * 0.5, 2)
        print(f"The area of triangle with base {base} cm and height {height} cm is equal {area} square cm")
        print()
    except:
        print("Please enter a numbers")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break