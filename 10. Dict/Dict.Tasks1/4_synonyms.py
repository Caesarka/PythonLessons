def get_synonym():
    print("Let\'s find synonym.")
    while True:
        print("Enter pairs of words that will be synonyms. Press enter after each pair. Enter empty line when you finish.")
        synonyms = {}

        while True:
            pair = input()
            if pair == '':
                break

            words = pair.split()
            word1, word2 = words
            synonyms[word1] = word2
            synonyms[word2] = word1
            
        word = input("Enter one word from your list: ")

        if word in synonyms:
            print("Synonym:", synonyms[word])
        else:
            print("This word doesn't have synonym from words you entered.")

        userInput = input("Enter q for exit or any key for repeat: ")
        if userInput == 'q':
            break


if __name__ == "__main__":
    get_synonym()
