while True:
    LOGIN = input("Create login: ")
    if not bool(LOGIN):
        print("Login can not be empty. Please try again.")
        continue
    print("Login was created")
    break
while True:
    PASSWORD = input("Create password: ")
    if not bool(PASSWORD) :
        print("Password can not be empty. Please try again.")
        continue
    print("Password was created")
    break

print('''   Log in into system''')

while True:
    _login = input("Enter login: ")
    _password = input("Enter password: ")
    if LOGIN != _login or PASSWORD != _password:
        if LOGIN != _login and PASSWORD != _password:
            print("Login and password are incorrect")
        elif LOGIN != _login and PASSWORD == _password:
            print("Login is incorrect")
        elif PASSWORD != _password and LOGIN == _login:
            print("Password is incorrect")
        pressedKey = input("Press any key and try again or q to end the program ")
        if(pressedKey == 'q'):
            break
    elif PASSWORD == _password and LOGIN == _login:
        print("Login and password are correct")
        pressedKey = input("Press any key and try again or q to end the program ")
        if(pressedKey == 'q'):
            break




