import sys

print("Let's find the longest sequence of entered numbers.")
while True:
    max_length = 0
    max_number = 0
    current_number = -sys.maxsize - 1
    previouse_number = -sys.maxsize - 1
    current_length = 0
    while current_number != 0:
        current_number = int(input("Enter the number: "))
        if current_number == previouse_number:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                max_number = current_number
            elif current_length == max_length:
                if max_number < current_number:
                    max_number = current_number
        else:
            previouse_number = current_number
            current_length = 1
    print(max_length)
    print(max_number)
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break
