print("what color is the square on the chessboard")
while True:
    coordinate = input("Enter coordinate on the chessboard, f.e. 1, 1: ")
    x, _, y = coordinate.partition(', ')
    x = int(x)
    y = int(y)
    if (x + y) % 2 != 0:
        print("This square is while")
    else:
        print("This square is black")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break