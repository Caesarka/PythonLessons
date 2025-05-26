
def get_message():
    t9_format = ''
    print("This program creates sequence of numbers in T9 format.")
    
    dictionary = {
        '1': ['.', ',', '?', '!', ':'],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z'],
        '0': [' ']
    }

    text_msg = input("Enter your message: ").upper()

    for sym in text_msg:
        for key, value in dictionary.items():
            if sym in value:
                t9_format += key * (value.index(sym) + 1)
                break

    print(t9_format)

get_message()
