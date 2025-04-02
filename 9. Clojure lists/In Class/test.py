import random
from module_matrix import hello
hello()


def create_matrix(x, y):
    matrix = []
    for first_dimention in range(x):
        matrix.append([])
        for second_dimention in range(y):
            matrix[first_dimention].append(random.randint(-100, 100))
    return matrix

x = int(input('Enter x:'))
y = int(input('Enter y:'))

matrix = create_matrix(x, y)
print(matrix)
print(matrix[0])
print(matrix[-1])
#2
for el in range(x):
    print(matrix[el][0])

for el in range(x):
    print(matrix[el][-1])
#3
for el in range(x):
    if el % 2 == 0:
        print(matrix[el])
#4
for el in range(x):
    for le in range(y):
        if le % 2 != 0 and matrix[0][le] > matrix[-1][le]:
            print(matrix[el][le])

#5
k = int(input())
p = int(input())

print(matrix[k])

for i in range(len(matrix)):
    print(matrix[i][p])