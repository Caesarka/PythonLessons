def get_union():
    while True:
        print("Let\'s find whether it has been encountered before or not.")
        numbers =list(map(int, (input("Enter first list of words (space-separated): ").split())))
        occurence = ''
        my_set = set()
        for num in numbers:
            if num in my_set:
                occurence += 'YES '
            else:
                occurence += 'NO '
                my_set.add(num)


        print(occurence)
        usrInput = input("Enter any key for repeat or q for quit: ")
        if usrInput == 'q':
            break

get_union()