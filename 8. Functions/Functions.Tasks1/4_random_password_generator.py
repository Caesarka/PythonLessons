from random import randint


def generate_password():
    pwd = ''
    pwd_length = randint(7, 10)
    for el in range(pwd_length):
        pwd += chr(randint(33, 126))
    return pwd

print('"Let\'s generate the random password.')
while True:
    print(f'Password that was generated: {generate_password()}')
    usrInput = input('Enter q for exit or any key for continue: ')
    if usrInput == 'q':
        break
