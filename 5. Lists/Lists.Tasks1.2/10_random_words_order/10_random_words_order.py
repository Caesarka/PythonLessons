import random

print("Let's pick some random words from the list, print it and delete from the list.\n")

word_file = "C:\Data\Python\\5. Lists\Lists.Tasks1.2\\10_random_words_order\\random_words.txt"
words = open(word_file).read().split()
print(f"List of words as it is: {' '.join(map(str, words))}\n")

quantity = random.randint(5, 15)
lst = list(random.sample(words, quantity))

for el in lst:
    del words[words.index(el)]
#new_words = list(set(words) - set(lst))

print(f"A few random words from the list: {' '.join(map(str, lst))}\n")
print(f"List after deleting th words: {' '.join(map(str, words))}")

