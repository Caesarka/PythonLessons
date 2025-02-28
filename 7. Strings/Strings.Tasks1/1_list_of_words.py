print('Let\'s count how many words you entered.')
words = input('Please enter words. Use space as delimiter: ')
cnt = len(words.split(' '))
print(f'{cnt} words was entered.')