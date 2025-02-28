print('Let\'s reverse the text between first and second letter r that occured in string.')
string = input('Please enter your string: ')
cnt = string.count('r')
if cnt >= 2:
    substring = string[string.rfind('r') - 1 : string.find('r') : -1]
    #print(substring)
    res = string[0 : string.find('r') + 1] + substring + string[string.rfind('r') :: ]
    print('Result:', res)
