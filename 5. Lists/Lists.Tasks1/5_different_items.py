from random import randint
import copy

print("Let's count unique barcodes.")

barcodes = []
unique_barcodes = []
#barcodes = [101, 101, 150, 150, 150, 200]
quantity = randint(5, 10)
i = 0
while i < quantity:
    barcodes.append(randint(100, 105))
    i += 1
barcodes.sort()

print(f"Barcodes: {barcodes}")
for el in barcodes:
    if el not in unique_barcodes:
        unique_barcodes.append(el)

print(f"Quantity of unique barcodes equals: {len(unique_barcodes)}")