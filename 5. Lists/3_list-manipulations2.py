str = input("Enter 10 numbers using spaсe as divider: ")
evenNumbers = []
numbers = str.split()
print(f"List of numbers: {numbers}")
for el in numbers:
    if int(el) % 2 == 0:
        evenNumbers.append(int(el))

print("List of even numbers: ", end=" ")
print(*evenNumbers, sep='/')
