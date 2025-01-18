import math
print("Let's find roots of a quadratic equation.")
while True:
    roots = []
    a = int(input("Enter the first constant: "))
    b = int(input("Enter the second constant: "))
    c = int(input("Enter the third constant: "))
    discriminant = math.pow(b, 2) - (4 * a * c)
    print(discriminant)
    if discriminant > 0:
        print(math.sqrt(discriminant))
        roots.append((-b + math.sqrt(discriminant)) / (2 * a))
        roots.append((-b - math.sqrt(discriminant)) / (2 * a))
    elif discriminant == 0:
        roots.append(-b / (2* a))
    else:
        roots
    print(f"Roots of a quadratic equation: {roots}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break