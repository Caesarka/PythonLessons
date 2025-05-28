import re


def get_quantity_of_unique_words():
    print("Let's find how many unique words in the text you enter.")
    while True:
        cnt = int(input("Enter the quantity of strings: "))
        unique_words = set()
        words = []

        while cnt > 0:
            unique_words.update(re.sub(r'[^\w\s]', '', (input())).split())
            cnt -= 1
        
        print("Answer: ", len(unique_words))
        print(unique_words)

        usrInput = input("Enter any key for repeat or q for quit: ")
        if usrInput == 'q':
            break

get_quantity_of_unique_words()
