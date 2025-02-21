import datetime

file = open('log.txt', 'a')
while True:
    event = input('Enter event text. Enter q for exit: ')
    if event == 'q':
        break
    file.write(f'{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {event}\n')

file.close()
