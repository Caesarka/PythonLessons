lst = input("Enter numbers, use space as delimiter: ").split()
print(lst)
reverse_str = ''
even_str = ''
for i in range(len(lst) - 1, -1, -1):
    reverse_str += f'{lst[i]} '
print(reverse_str)

for i in range(0, len(lst), 2):
    even_str += f'{lst[i]} '
print(even_str)