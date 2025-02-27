def checkStrengthOfPassword(pwd):
        uppercase = False
        lowercase = False
        number = False
        symbol = False
        inRange = True
        length = True
        weak_pwd_list = ['abcd1234', '1234abcd', 'qwerty1234']
        pwd_result_msg = ''

        if len(pwd) < 8:
            length = False
            return False

        for el in pwd:
            if (ord(el) >= 65 and ord(el) <= 90):
                uppercase = True
            elif ord(el) >= 97 and ord(el) <= 122:
                lowercase = True
            elif ord(el) >= 48 and ord(el) <= 57:
                number = True
            elif (ord(el) >= 33 and ord(el) <= 46) or (ord(el) >= 58 and ord(el) <= 64) or (ord(el) >= 91 and ord(el) <= 96):
                symbol = True
            else:
                inRange = False
        if pwd in weak_pwd_list:
            return False
        
        if not (uppercase and lowercase and number and symbol and inRange and length):
            return False
        return True


if __name__ == '__main__':
    while True:
        pwd = input('Enter password: ')
        res = checkStrengthOfPassword(pwd)
        if res:
            print('Password is valid.')
        else:
            print('Password is not valid')
        usrInput = input('Enter q for exit or any key for repeat. ')
        if usrInput == 'q':
            break