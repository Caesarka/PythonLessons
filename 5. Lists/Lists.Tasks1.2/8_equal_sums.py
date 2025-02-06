from random import randrange
from random import randint
from typing import Counter

print("Let's count equal sums.")
sums = []
quantity = randint(6, 12)
i = 0

while i < quantity:
    sums.append(randrange(100, 400, 100))
    i += 1

sums.sort()
print(sums)

count = 1
pairs_count = 0

for j in range(1, len(sums)):
    if sums[j] == sums[j - 1]:
        count += 1
    else:
        if count > 1:
            pairs_count += (count * (count - 1)) // 2
        count = 1
if count > 1:
    pairs_count += (count * (count - 1)) // 2

print(f"{pairs_count} pairs in this sequence of numbers")