for i in range(1, 11):
    print('*', end=' ')
print()
for i in range(1, 6):
    print('*', end=' ')
print()
for i in range(1, 11):
    print('*', end=' ')
print()
print('###')
for i in range(1, 11):
    for j in range(1, 11):
        print('*', end=' ')
    print()

width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

for h in range(0, height):
    for w in range(0, width):
        print('*', end=' ')
    print()

