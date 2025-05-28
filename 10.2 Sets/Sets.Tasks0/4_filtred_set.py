def get_filtered_set():
    while True:
        print("Let's filter the set.")
        set1 =set(input("Enter the original list of words (space-separated): ").split())
        set2 =set(input("Enter the words to remove (space-separated): ").split())

        set1 = set1 - set2
    
        print("Set after filtering: ", set1)

        usrInput = input("Press any key to filter another set or 'q' to quit: ")
        if usrInput == 'q':
            break

get_filtered_set()