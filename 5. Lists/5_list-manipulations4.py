str = input("Enter numbers using spaсe as divider: ")

numbers = str.split()
even_indexes = []
length = len(numbers)
i = 0

while i < length:
    print(f"Repeat {i + 1}")
    if i % 2 == 0:
            even_indexes.append(numbers[i])
    i += 1
    
print(f"Numbers from the list with even indexes: {even_indexes}")