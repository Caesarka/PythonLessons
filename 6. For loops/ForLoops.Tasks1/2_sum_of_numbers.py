print("Let's find sum of numbers.")
while True:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    sum = 0
    for i in range(min(number1, number2), max(number1, number2) + 1):
        sum += i
    print(sum)
    ustInput = input("Enter any key for continue or q for exit. ")
    if ustInput == 'q':
        break