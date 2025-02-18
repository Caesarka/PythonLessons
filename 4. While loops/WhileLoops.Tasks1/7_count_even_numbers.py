print("Let's enter a few numbers and count odd and even separately.")
while True:
    count_odd = []
    count_even = []
    while True:
        number = int(input("Enter number: "))
        if number == 0:
            print(f"Even numbers: {len(count_even)}, odd numbers: {len(count_odd)}.")
            break
        if number % 2 == 0:
            count_even.append(number)
        else:
            count_odd.append(number)
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break