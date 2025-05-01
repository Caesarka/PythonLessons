print("Hello! This program can draw same numbers in diagonals.")

size = int(input("Enter size of matrix: "))

matrix = [[0 for _ in range(size)]for _ in range(size)]

for i in range(size):
    for j in range(size):
        matrix[i][j] = abs(i - j)
        print(str(matrix[i][j]).rjust(3), end='')
    print()