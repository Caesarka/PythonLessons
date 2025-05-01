from random import randint

print("Hello! This program searches for the max number.")

x = int(input("Enter size for the first dimention of the matrix: "))
y = int(input("Enter size for the second dimention of the matrix: "))
matrix = [[randint(1, 100) for _ in range(x)] for _ in range(y)]
max = 0
pos = []

for i in range(y):
    for j in range(x):
        if matrix[i][j] > max:
            max = matrix[i][j]
            pos = (i, j)
        print(str(matrix[i][j]).rjust(3), end='')
    print()

print(f"Max value: {max}")
print(f"Position: {pos[0]}, {pos[1]}")
