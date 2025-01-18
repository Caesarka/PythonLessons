import math
print("Let's find length of hypotenuse.")
while True:
    leg1 = int(input("Enter length of first leg: "))
    leg2 = int(input("Enter length of second leg: "))
    hypotenuse = int(math.sqrt(math.pow(leg1, 2) + math.pow(leg2, 2)))
    print(f"Hypotenuse equals: {hypotenuse}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break