import time


def make_coffee():
    print('Let\'s prepare coffee as you like!')
    coffee = input('What coffee do you prefer? ')

    for i in range(5):
        print(f'\rCoffee is prepairing, please wait.  ', end='')
        time.sleep(0.5)
        print(f'\rCoffee is prepairing, please wait.. ', end='')
        time.sleep(0.5)
        print(f'\rCoffee is prepairing, please wait...', end='')
        time.sleep(0.5)
    print(f'\nYour {coffee} is ready, enjoy!')

def wash_dishes():
    print('\nLet\'s wash your dishes if you have some..')
    isAvailable = input('Do you have dishes that need to be washed? yes/no ')
    if isAvailable == 'yes':
        for i in range(5):
            print('\rThe dishes are being washed.  ', end='')
            time.sleep(0.5)
            print('\rThe dishes are being washed.. ', end='')
            time.sleep(0.5)
            print('\rThe dishes are being washed...', end='')
            time.sleep(0.5)
        print('\nThe dishes are washed!')
    else:
        print('There is nothing to wash.')
    
def preheat_oven():
    print('\nLet\'s preheat the oven.')
    temp = int(input('What temperature in Celsius do you need to preheat your oven? '))
    curtemp = 25
    while curtemp < temp:
        print(f'\r{curtemp}°C. The oven is preheating...', end='')
        time.sleep(0.5)
        curtemp += 10
    print(f'\r{' ' * 100}', end='')
    print(f'\r{temp}°C. The oven is heated.', end='')


make_coffee()
wash_dishes()
preheat_oven()