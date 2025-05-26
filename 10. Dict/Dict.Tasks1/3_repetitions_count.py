def count_words():
    print("Let\'s count the number of each occurence for each word.")
    while True:
        words = input("Enter some words: ").split()
        word_counts = {}
        result = []

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 0
            result.append(str(word_counts[word]))

        print("Answer:", ' '.join(result))

        userInput = input("Enter q for exit or any key for repeat: ")
        if userInput == 'q':
            break


if __name__ == "__main__":
    count_words()
