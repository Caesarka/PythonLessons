print("This program takes words and return formatting list of words:")

while True:
    words = []
    word = ' '
    print("Enter the words. One word for each string. Enter empty string for stop.")
    while word != '':
        word = input()
        words.append(word)
    del words[words.index('')]
    print("New list of words:")
    if len(words) == 1:
        print(words[0])
    else:
        last = words.pop()
        lst = ', '.join(words)
        print(f"{lst[0::]} и {last}")

    pressedKey = input("Press any key and try again or q to end the program ")
    if(pressedKey == 'q'):
        break
