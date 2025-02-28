print('Let\'s validate the phone number.')
symbols = ' ()-'

while True:
    valid_number = ''
    number = input('Please enter phone number: ')
    for num in number:
        if num not in symbols:
            valid_number += num
    valid_number = '+7' + valid_number[-10 : -1]

    print(valid_number)
    usrInput = input('Enter any key for repeat or q for exit')
    if usrInput == 'q':
        break