import math

print("Let's explore generators in Python.")
while True:
    count = int(input("Enter the quantity of numbers in list: "))
    lst = [pow(i, 2) for i in range(1, count + 1)]
    print(f"List: {lst}")
    ustInput = input("Enter any key for continue or q for exit. ")
    if ustInput == 'q':
        break
    numbers = input("Enter numbers, use space as delimiter: ")
    numbers_list =list(map(int, numbers.split()))
    numbers_list = [i for i in numbers_list if i > 0]
    print(f"List of numbers that more than zero: {numbers_list}")
    ustInput = input("Enter any key for continue or q for exit. ")
    if ustInput == 'q':
        break