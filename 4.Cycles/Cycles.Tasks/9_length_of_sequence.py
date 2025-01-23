print("Let's find the longest sequence of entered numbers.")
while True:
    count_max = 0
    value_max = 0
    numbers = []
    while True:
        number = int(input("Enter the number: "))
        if number == 0:
            count = 0
            value = numbers[0]
            for i in numbers:
                if value == i:
                    count += 1
                    if count_max < count:
                        count_max = count
                        value_max = value
                    elif count_max == count:
                        if value_max < value:
                            value_max = value
                else:
                    count = 0
                    value = i
                    count += 1
            break
        else:
            numbers.append(number)
    print(count_max)
    print(value_max)
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break
