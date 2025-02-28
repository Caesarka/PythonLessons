print('Let\'s remove all ampersands in the text you entered.')
string = input('Please enter your string: ')
for s in string:
    if s == '&':
        string = string.replace(s, '')
print(string)
