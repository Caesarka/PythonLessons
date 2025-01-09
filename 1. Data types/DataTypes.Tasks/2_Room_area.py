while True:
    print("Let's find the area of the room")
    try:
        length = float(input("Enter the length in meters: "))
        width = float(input("Enter the width in meters: "))
        sqr = round(length * width, 2)
        print(f"The area of the room is {sqr} square meters")
        print()

        print("Enter 2 dimentions for 3 pieces of furniture:")
        try:
            length1 = float(input('''      First piece, length in meters: '''))
            width1 = float(input('''      First piece, width in meters: '''))
            print()
            length2 = float(input('''      Second piece, length in meters: '''))
            width2 = float(input('''      Second piece, width in meters: '''))
            print()
            length3 = float(input('''      Third piece, length in meters: '''))
            width3 = float(input('''      Third piece, width in meters: '''))
            print()
            sqrFurniture = round(length1 * width1 + length2 * width2 + length3 * width3)
            if (sqr > sqrFurniture):
                print(f"This furniture fits to the room and you will have free {sqr - sqrFurniture} square meters")
            if (sqr < sqrFurniture):
                print(f"This furniture doesn't fit to the room, you need {sqrFurniture - sqr} more square meters")
            if (sqr == sqrFurniture):
                print("This furniture fits to the room")
        except:
            print("Please use numbers for length and width")

        print()
        usrInput = input("Press any key to continue or q to exit ")

        if usrInput == 'q':
            break

    except:
        print("Please use numbers for length and width")
        usrInput = input("Press any key to continue or q to exit ")

    if usrInput == 'q':
        break
        print()