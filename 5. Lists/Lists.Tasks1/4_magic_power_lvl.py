from random import randint

print("Let's give Argus his place in the ranks of mages.")

#range = [162, 163, 160, 160, 157, 157, 155, 154]
range = []
quantity = randint(5, 20)
power_Argus = 160 #randint(70, 200)
i = 0

while i < quantity:
    range.append(randint(70, 200))
    i += 1

range.sort()
print(f"Range of mages: {range}")
print(f"The power of Argus: {power_Argus}")
j = 0
while j < len(range):
    if power_Argus <= range[j]:
        range.insert(j, f"Argus:{power_Argus}")
        break
    j += 1
range.reverse()
print(range)
print(f"Argus takes the place {len(range) - 1 - j}")
