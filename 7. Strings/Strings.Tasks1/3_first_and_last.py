print('Let\'s count how many times letter r occurred in your string.')
string = input('Please enter your string: ')
cnt = string.count('r')
if cnt == 0:
    res = -1
elif cnt == 1:
    res = string.index('r')
else:
    res = f'{string.find('r')}, {string.rfind('r')}'

print('Result:', res)