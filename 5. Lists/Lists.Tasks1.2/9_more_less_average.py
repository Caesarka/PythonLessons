import math
from random import randrange
from random import randint

print("Let's find average, more and less numbers among entered numbers.")

numbers = []
quantity = randint(6, 12)
cnt = 0
dict = {'less': [],
        'equal': [],
        'more': []}

while cnt < quantity:
    numbers.append(randint(1, 100))
    cnt += 1
print(' '.join(map(str, numbers)))

average = math.floor(sum(numbers) / cnt)

print(f"Average for list of numbers equals: {average}")

for j in numbers:
    if j < average:
        dict['less'].append(j)
    elif j == average:
        dict['equal'].append(j)
    else:
        dict['more'].append(j)

print(f"Numbers less than average: {' '.join(map(str, dict['less']))} ")
print(f"Numbers equal average: {' '.join(map(str, dict['equal']))} ")
print(f"Numbers more than average: {' '.join(map(str, dict['more']))} ")