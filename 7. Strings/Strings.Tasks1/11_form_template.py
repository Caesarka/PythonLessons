print('Let\'s fill the form template.')

while True:
    name = input('Enter the name: ')
    amount = input('Enter the amount: ')
    print(f'Dear {name}, your order for {amount} has been confirmed.')
    usrInput = input('Enter any key for repeat or q for exit')
    if usrInput == 'q':
        break