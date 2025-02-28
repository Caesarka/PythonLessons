print('Let\'s find index of letter r if it occurred two or more times.')
string = input('Please enter your string: ')
cnt = string.count('r')
if cnt == 0:
    res = -2
elif cnt == 1:
    res = -1
else:
    index = string.find('r') + 1
    new_str = string[index::]
    res = new_str.find('r') + index
print(res)
