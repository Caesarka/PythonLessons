print("Let's find the number in Fibonacci sequence by its ordinal number.")
while True:
    prev = 0
    cur = 1
    index = 0
    number = int(input("Enter the ordinal number: "))
    while number != index:
        next = prev + cur
        prev = cur
        cur = next
        index += 1
    print(f"The {number} number in Fibonacci sequence is {prev}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break
