def check_is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print('All side lengths must be a positive numbers.')
        return False
    else:
        if a >= b + c or b >= a + c or c >= a + b:
            print('It\'s not a triangle. One side more or equal sum of two other sides.')
            return False
        else:
            print('It\'s a triangle.')
            return True

print('"Let\'s check whether it is possible to construct a triangle from the three sides you entered or not.')
while True:
    try:
        a = int(input('Enter first side: '))
        b = int(input('Enter second side: '))
        c = int(input('Enter third side: '))
        check_is_triangle(a, b, c)
    except:
        print('Lengths must be integer numbers!')
    usrInput = input('Enter q for exit or any key for continue: ')
    if usrInput == 'q':
        break
