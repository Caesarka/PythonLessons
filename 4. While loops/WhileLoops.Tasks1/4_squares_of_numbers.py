import math

print("Let's find all squares for numbers that less or equal the number that you'll enter.")

while True:
    squares = {}
    number = 0
    item = 1
    while True:
        number = int(input("Enter number: "))
        if number > 0:
            while item <= number:
                squares[item] = int(math.pow(item, 2))
                item += 1
            for k, v in squares.items():
                print(f"Number {k}, square {v}")
        else:
            print("Number should be more than 0")
        break
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break