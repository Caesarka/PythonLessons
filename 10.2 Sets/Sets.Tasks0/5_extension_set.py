def get_extension_set():
    while True:
        print("Let\'s extend elements of two sets.")
        set1 =set(input("Enter first list of words (space-separated): ").split())
        set2 =set(input("Enter second list of words (space-separated): ").split())

        set1 = set1 | set2
    
        print("Extended set: ", set1)

        usrInput = input("Enter any key for repeat or q for quit: ")
        if usrInput == 'q':
            break

get_extension_set()