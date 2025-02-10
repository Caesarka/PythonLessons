'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a < b:
    for i in range(a , b + 1, 1):
        if i % 2 == 0:
            print(i)
else:
    for i in range(b, a + 1, 1):
        if i % 2 == 0:
            print(i)
'''

a = input().split()

for element in a:
    print(element)
