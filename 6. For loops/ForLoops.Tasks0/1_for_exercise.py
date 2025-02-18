#Exercise 1.1
colors = ["Red", "Yellow", "Blue", "While", "Black"]

for color in colors:
    print("\t•", color, end="\n")

# Exercise 1.2
data_example = input(("Enter numbers, use space as delimiter: ")).split()
numbers = list(map(int, data_example))
print(numbers)
str_with_dashes = ''
for num in numbers:
    if num % 3 == 0:
        str_with_dashes += '•—'
    else:
        str_with_dashes += f'{num}—'
str_with_dashes = str_with_dashes[:len(str_with_dashes) - 1]
print(str_with_dashes)
#–
#—