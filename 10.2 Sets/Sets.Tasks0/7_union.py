def get_union():
    while True:
        print("Let\'s find words that appear in three sets.")
        set1 =set(map(int, set(input("Enter first list of words (space-separated): ").split())))
        set2 =set(map(int, set(input("Enter second list of words (space-separated): ").split())))
        set3 =set(map(int, set(input("Enter third list of words (space-separated): ").split())))

        common = set1 | set2 | set3
    
        print("Intersection: ", common)

        usrInput = input("Enter any key for repeat or q for quit: ")
        if usrInput == 'q':
            break

get_union()