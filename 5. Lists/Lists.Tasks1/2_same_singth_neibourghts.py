print("Let's count the entered numbers that are same singth.")
str = input("Enter the numbers, use space as delimiter: ")
numbers = str.split()
neighbourghts = []
prev_num = int(numbers[0])
count = 0
i = 0
while i < len(numbers) - 1:
    num = int(numbers[i + 1])
    if (num >= 0 and prev_num >= 0) or (num < 0 and prev_num < 0):
        count += 1
        neighbourghts.append((prev_num, num))
    prev_num = num
    i += 1
print(f"Count of pairs equals: {count}")
if count > 0:
    print(f"The first pair is: {neighbourghts[0][0]}, {neighbourghts[0][1]}")
'''
for i in numbers:
    num = int(num)
    if (num >= 0 and prev_num >= 0) or (num < 0 and prev_num < 0):
        count += 1
        neighbourghts
    prev_num = num
print(f"Count of numbers are: {count}")
'''