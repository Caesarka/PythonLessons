print('Let\'s change lowercase vowel letters to uppercase letters in the text you entered.')
string = input('Please enter your string: ')
vowels = 'aeiou'
for letter in string:
    if letter in vowels:
        string = string.replace(letter, letter.capitalize())
print(string)
