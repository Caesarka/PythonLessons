lst = input("Enter numbers, use space as delimiter: ").split()
numbers = []
for el in lst:
    numbers.append(int(el))

print(numbers)


for num in range(len(numbers), numbers[0], -1):
    print(num)
