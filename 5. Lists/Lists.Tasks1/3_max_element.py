import sys

print("Let's find max element in sequence of numbers.")
str = input("Enter the numbers, use space as delimiter: ")
numbers = str.split()
numbers = list(map(int, numbers))
max_num = -sys.maxsize-1
index = -1
i = 0
while i < len(numbers):
    if numbers[i] > max_num:
        max_num = numbers[i]
        index = i
    i += 1

print(f"The maximum number in sequence equals {max_num}, index equals {index}")


