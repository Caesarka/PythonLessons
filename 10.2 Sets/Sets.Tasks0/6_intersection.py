def get_intersection_set():
    while True:
        print("Let\'s find words that appear in two sets.")
        set1 =set(input("Enter first list of words (space-separated): ").split())
        set2 =set(input("Enter second list of words (space-separated): ").split())

        set3 = set1 & set2
    
        print("Intersection: ", set3)

        usrInput = input("Enter any key for repeat or q for quit: ")
        if usrInput == 'q':
            break

get_intersection_set()