from random import randint

my_list = []
i = 0

while i < 10:
    my_list.append(randint(1, 100))
    i += 1
print(f"My list: {my_list}")
print(f"Third element of list: {my_list[2]}")
print(f"Last but one element of list: {my_list[8]}")
print(f"The first five elements of list: {my_list[0:5]}")
print(f"Elements of list except the last two: {my_list[0:8]}")
print(f"Elements of list with even indexes: {my_list[::2]}")
print(f"Elements of list with odd indexes: {my_list[1::2]}")

print(f"Elements of list in reverse order: {my_list[-1::-1]}")
my_list.reverse()
print(f"Elements of reversed list with even indexes: {my_list[0::2]}")
