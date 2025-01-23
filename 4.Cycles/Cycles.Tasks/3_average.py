print("Let's calculate the average value for entered numbers.")
while True:
    count = 0
    sum = 0
    while True:
        number = int(input("Enter number: "))
        sum += number
        if number == 0:
            avg = sum / count
            print(f"The average number is {round(avg, 2)}.")
            break
        count += 1
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break