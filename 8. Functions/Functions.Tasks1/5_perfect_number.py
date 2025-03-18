def check_is_perfect_number(num):
    if num < 0:
        print('Number must be a positive.')
        return False
    else:
        sum_of_factors = 0
        for el in range(1, num - 1):
            if num % el == 0:
                sum_of_factors += el
        if sum_of_factors == num:
            return True
        else:
            return False


print('Let\'s check is the number you entered is perfect or not.')
while True:
    try:
        num = int(input('Enter the number: '))
        if check_is_perfect_number(num):
            print(f'Number {num} is a perfect number.')
        else:
            print(f'Number {num} is not a perfect number.')
    except:
        print('You should enter a positive number.')
    usrInput = input('Enter q for exit or any key for continue: ')
    if usrInput == 'q':
        break



for num in range(1, 10000):
    if check_is_perfect_number(num):
        print(f'Number {num} is a perfect number.')
