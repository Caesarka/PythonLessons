from random import randint

test_list = []
i = 0

while i < 10:
    test_list.append(randint(-100, 100))
    i += 1
print(f"List elements: {test_list}")
del test_list[2]
del test_list[7]
print(f"List after deleting 2nd and 8th elements (by index): {test_list}")

pop_elem = test_list.pop(4)
print(f"List after deleting 5th element (by count): {test_list}")

if test_list[3] > 0:
    test_list[3]  = 'More'
elif test_list[3] < 0:
    test_list[3] = 'Less'

print(f"List after checking 3d element (by index): {test_list}")