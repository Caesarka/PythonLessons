
'''
LOGIN = input("Create login: ");
if bool(LOGIN) :
    print("Login was created");
PASSWORD = input("Create password: ");
if bool(PASSWORD) :
    print("Password was created");

print(''''''Log in into system'''''');
_login = input("Enter login: ");
_password = input("Enter password: ");

if LOGIN != _login and PASSWORD != _password:
    print("Login and password are incorrect");

if LOGIN != _login and PASSWORD == _password:
    print("Login is incorrect")

if PASSWORD == _password and LOGIN == _login:
    print("Login and password are correct");

if PASSWORD != _password and LOGIN == _login:
    print("Password is incorrect");


color = input("Enter the color: ");

if color == 'red':
    print('#FF0000');
elif color == 'white':
    print('#000000');
else:
    print("There isn't such of color")
'''
isInt = False;
number = float(input("Enter the number: "));

if number.is_integer:
    isInt = True;

if number > 0 and isInt == True:
    print("Number is integer and more than 0");
elif number > 0 and isInt == False:
    print("Number is float and more than 0");
elif number == 0:
    print("Number is equal to 0");
if number < 0 and isInt == True:
    print("Number is integer and less than 0");
elif number < 0 and isInt == False:
    print("Number is float and less than 0");