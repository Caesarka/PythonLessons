import sys
print("Let's count the entered numbers that are more then previous one.")
str = input("Enter the numbers, use space as delimiter: ")
numbers = str.split()
print(numbers)
count = -1
prev_num = -sys.maxsize - 1

for num in numbers:
    num = int(num)
    if num > prev_num:
        count += 1
    prev_num = num
print(f"Count of numbers are: {count}")
