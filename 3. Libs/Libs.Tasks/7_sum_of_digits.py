print("Let's find sum of all digits in number.")
while True:
    number = int(input("Enter the 3 digit number: "))
    ones = number % 10
    hundreds = number // 100
    tens = (number - hundreds * 100) // 10
    sum = hundreds + tens + ones
    print(f"Sum of digits in number {number}: {sum}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break