#def sortSymbols(string):
#    lst = [0, 0, 0]
#    for el in string:
#        if el == ' ':
#            lst[2] += 1
#        elif el.isupper():
#            lst[0] += 1
#        elif el.islower():
#            lst[1]  += 1
#    return lst
#
#string = input('Enter your string: ')
#lst = sortSymbols(string)
#print(f'Uppercase letters: {lst[0]}, lowercase letters: {lst[1]}, spaces: {lst[2]}')

#def getMax(a, b, c):
#    if a > b and a > c:
#        return a
#    elif b > a and b > c:
#        return b
#    else:
#        return c
#
#a = int(input('Enter first number: '))
#b = int(input('Enter second number: '))
#c = int(input('Enter third number: '))
#print(f'Max number: {getMax(a, b, c)}')
import os
if os.name == 'nt':
    os.system('')

def returnAnswer(string, isTrue='False', color='red'):
    if isTrue == 'False':
        print(f'\033[91mERROR: \033[0m')
    if color == 'green':
        print(f'\033[92m{string}\033[0m')
    elif color == 'yellow':
        print(f'\033[93m{string}\033[0m')
    elif color == 'blue':
        print(f'\033[94m{string}\033[0m')
    elif color == 'violet':
        print(f'\033[95m{string}\033[0m')
    else:
        print(f'\033[91m{string}\033[0m')
    return 0

color = input('Enter color: ')
isTrue = input('Error or not: ')
text = input('Enter text: ')
returnAnswer(text, isTrue, color)



