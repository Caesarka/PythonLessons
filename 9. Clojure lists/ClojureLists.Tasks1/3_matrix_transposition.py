from random import randint

print("Hello! This program can transpose the matrix.")

x = int(input("Enter size for the first dimention of the matrix: "))
y = int(input("Enter size for the second dimention of the matrix: "))
matrix = [[randint(1, 100) for _ in range(x)] for _ in range(y)]

for i in range(y):
    for j in range(x):
        print(str(matrix[i][j]).rjust(3), end='')
    print()

print('Transposition:')

for i in range(x):
    for j in range(y):
        print(str(matrix[j][i]).rjust(3), end='')
    print()
