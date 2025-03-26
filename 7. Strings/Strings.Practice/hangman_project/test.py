import random


file = open('countries.txt', encoding='utf-8')
lst = file.readlines()
word = random.choice(lst)
print(lst)