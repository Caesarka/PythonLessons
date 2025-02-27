import re

def checkStrengthOfPasswordMethods(pwd):
    uppercase = False
    lowercase = False
    number = False
    symbol = False
    inRange = True
    length = True
    weak_pwd_list = ['abcd1234', '1234abcd', 'qwerty1234']
    weakPwd = False
    pwd_result = []


    if any(el.isupper() for el in pwd):
            uppercase = True
    if any(el.islower() for el in pwd):
            lowercase = True
    if any(el.isdigit() for el in pwd):
            number = True
    if re.search(r'[!@#$%^&*()\-_=+{}[\]:;"\'<>,.?/\\|`~]', pwd):
         symbol = True
    if re.search(r'[^a-zA-Z0-9!@#$%^&*()\-_=+{}[\]:;"\'<>,.?/\\|`~]', pwd):
        inRange = False
    if len(pwd) < 8:
        length = False
    if pwd in weak_pwd_list:
        weakPwd = True
    
    if uppercase and lowercase and number and symbol and inRange and length and weakPwd == False:
        return True
    else:
        if length == False:
            pwd_result.append('Password\'s length is less than 8 characters.')
        if weakPwd == True:
            pwd_result.append('Password is weak.')
        if uppercase == False:
            pwd_result.append('Password does not consist at least one appercase letter.')
        if lowercase == False:
            pwd_result.append('Password does not consist at least one lowercase letter.')
        if number == False:
            pwd_result.append('Password does not consist at least one digit.')
        if symbol == False:
            pwd_result.append('Password does not consist at least one special character.')
        if inRange == False:
            pwd_result.append('Password consists at least one character that out of range.')
        pwd_result.append('Password is not valid, please try again.')
    return (False, pwd_result)

if __name__ == '__main__':
    while True:
        pwd = input('Enter password: ')
        res = checkStrengthOfPasswordMethods(pwd)
        if res == True:
             print('Password is valid.')
        else:
             for el in res[1]:
                  print(el)
        usrInput = input('Enter q for exit or any key for repeat. ')
        if usrInput == 'q':
            break