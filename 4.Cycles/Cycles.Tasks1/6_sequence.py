import sys

print("Let's enter a few numbers and find the biggest one.")
while True:
    max_number = -sys.maxsize - 1
    pos = 0
    count = 1
    while True:
        number = int(input("Enter number: "))
        if number == 0:
            print(f"The biggest number: {max_number}, position in sequence: {pos}.")
            break
        if number > max_number:
            max_number = number
            pos = count
        count += 1
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break