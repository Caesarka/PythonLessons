print("Let's find numbers in range.")
while True:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    lst = []
    for i in range(min(number1, number2), max(number1, number2) + 1):
        lst.append(i)
    print(lst)
    ustInput = input("Enter any key for continue or q for exit. ")
    if ustInput == 'q':
        break