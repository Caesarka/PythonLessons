import random
import time

guess = 0
hack_password = ''
print('Let\'s see how strong your password is.')
password = input('Please enter the password: ')
start = time.time()
for el in password:
    while ord(el) != guess:
        guess = random.randint(33, 127)
        print(f'\rYour password is: {hack_password}{chr(guess)}', end='')
        time.sleep(0.05)
    hack_password += chr(guess)
stop = time.time()
tme = round((stop - start), 0)
print(f'. I spend {tme} seconds to hack it.')