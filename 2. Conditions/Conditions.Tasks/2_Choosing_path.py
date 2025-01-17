print('''Ты – храбрый путешественник, что забрался в замок найти сокровище.
Перед тобой выбор куда пойти: наверх, вниз, налево или направо.''')

while True:
    direction = input("Выбери направление: ")
    if direction == 'направо':
        print("Ты попал в большую залу с кучей ловушек!")
    elif direction == 'налево':
        print("Подарки которые не достались непослушным детям твои!")
    elif direction == 'вверх':
        print("На столе две пилюли: одна перенесёт тебя в 9 января, вторая запивается глинтвейном")
    elif direction == 'вниз':
        print('''Здесь комната нераспутанных гирлянд. Вперёд!
    Jingle bells
    Jingle bells
    Jingle all the way
    Oh, what fun
    It is to ride
    In a one-horse open sleigh''')
    else:
        usrInput = input("Press any key to continue or q to exit ")
        if usrInput == 'q':
            break