print("Let's sort entered numbers.")
str1 = input("Enter the numbers, use space as delimiter: ")
numbers = list(map(str, str1.split()))
positive_numbers = []
zeros = []
negative_numbers = []

for num in numbers:
    if int(num) > 0:
        positive_numbers.append(num)
    elif int(num) == 0:
        zeros.append(num)
    else:
        negative_numbers.append(num)
negative_numbers = ' '.join(map(str, negative_numbers))
zeros = ' '.join(map(str, zeros))
positive_numbers = ' '.join(map(str, positive_numbers))

print(f"Negative numbers: {negative_numbers}")
print(f"Zeros: {zeros}")
print(f"Positive numbers: {positive_numbers}")
