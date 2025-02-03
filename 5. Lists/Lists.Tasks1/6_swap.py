from random import randint
import copy

print("Let's swap the heaviest and lightest box.")

boxes = []
unique_barcodes = []
max_weight = 1
min_weight = 25
max_index = -1
min_index = -1
#boxes = [10, 5, 15, 7, 20, 5, 15]
quantity = randint(5, 10)
i = 0
j = 0

while i < quantity:
    boxes.append(randint(1, 25))
    i += 1

print(boxes)
boxes = list(dict.fromkeys(boxes))
print(f"Boxes: {boxes}")

while j < len(boxes):
    if boxes[j] > max_weight:
        max_weight = boxes[j]
        max_index = j
    if boxes[j] < min_weight:
        min_weight = boxes[j]
        min_index = j
    j += 1

boxes[max_index] = min_weight
boxes[min_index] = max_weight

print(f"New order for boxes: {boxes}")