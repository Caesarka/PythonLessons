print('Let\'s delete the text between first and second letter r that occured in string.')
string = input('Please enter your string: ')
cnt = string.count('r')
if cnt >= 2:
    substring = string[string.find('r') + 1 : string.rfind('r')]
    string = string.replace(substring, '')
    print(string)
