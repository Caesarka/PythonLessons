import math
from random import randint, sample
import sys


def sqrt(lst):
    for i in range(len(lst) - 1):
        x = 0
        y = 0
        reversed = False
        while x < len(lst) - 1:
            cur = abs(lst[x])
            next = abs(lst[x + 1])
            if cur > next:
                var = cur
                cur = next
                next = var
                reversed = True
            lst[x] = cur
            lst[x + 1] = next
            x += 1
        if reversed == False:
            print(f'List sorted by abs value {lst}')
            for y in range(len(lst)):
                lst[y] *= lst[y]
            break
    return lst



def sorted_squares(arr):
    n = len(arr)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result[pos] = arr[left] ** 2
            left += 1
        else:
            result[pos] = arr[right] ** 2
            right -= 1
        pos -= 1
    
    return result





def convert_string(string):
    new_string = ''
    x = 0
    count = 1
    while x < len(string) - 1:
        if string[x] == string[x + 1]:
            count += 1
        else:
            new_string += f'{string[x - 1]}{count}'
            count = 1
        x += 1
    return new_string + f'{string[-1]}{count}'

#lst = [1600, 1521, 625, 1, 81, 169, 256, 529, 1225, 2116]

count = 10
a = randint(-100, -1)
b = randint (0, 100)
arr = sample(range(a, b), count)
arr.sort()
print(arr)
string = 'AAABBBBSSCCEEEYYY'

print(sqrt(arr))
print(f'GPT: {sorted_squares(arr)}')
print(convert_string(string))