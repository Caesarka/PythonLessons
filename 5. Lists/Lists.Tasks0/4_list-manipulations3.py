str = input("Enter numbers using spaсe as divider: ")

numbers = str.split()
positive_numbers = []
length = len(numbers)
i = 0

while i < length:
    print(f"Repeat {i + 1}")
    if int(numbers[i]) > 0:
            positive_numbers.append(numbers[i])
    i += 1
    
print(f"Positive numbers in list: {positive_numbers}")