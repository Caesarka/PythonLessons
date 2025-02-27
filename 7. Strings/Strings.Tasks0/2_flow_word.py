import time
text = 'Peace'
length = 100
i = 0
#print('WarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWarWar', end='')
while i <= length:
    print(f"\r{' ' * i}{text}", end='')
    time.sleep(0.1)
    i += 1
