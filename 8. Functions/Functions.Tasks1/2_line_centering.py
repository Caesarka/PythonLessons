def center(string, width):
    str_length = len(string)
    print(string) if str_length >= width else print(f'{' ' * ((width - str_length) // 2)}{string}')

print('Let\'s center the string you entered to the width of the window.')
string = input('Enter the string: ')
width = int(input('Enter the width for window: '))
center(string, width)