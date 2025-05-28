def get_set_intersection():
    while True:
        print("Let's extend the set.")
        set1 =set(input("Enter one list of elements: ").split())
        set2 =set(input("Enter another list of elements: ").split())

        common_elements = set1 & set2
    
        print("Amount of same elements in both of lists: ", len(common_elements))

        usrInput = input("Enter any key for repeat or q for quit: ")
        if usrInput == 'q':
            break

get_set_intersection()