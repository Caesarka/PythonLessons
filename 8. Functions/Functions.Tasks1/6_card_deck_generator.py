from random import randint

def createDeck():
    deck = []
    meaning = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
    suit = ['s', 'h', 'd', 'c']

    for m in meaning:
        for s in suit:
            deck.append(f'{m}{s}')
    print(f'Card deck befor shuffle: {deck}')
    return deck

def shuffle(deck):
    pos = 0
    while pos < len(deck) - 1:
        cur = deck[pos]
        index = pos
        while index == pos:
            index = randint(pos, len(deck) - 1)
        deck[pos] = deck[index]
        deck[index] = cur
        pos += 1
    print(f'Card deck after shuffle: {deck}')
    return deck

deck = createDeck()
shuffle(deck)