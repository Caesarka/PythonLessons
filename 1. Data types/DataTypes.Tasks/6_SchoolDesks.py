while True:

    print("Let's calculate how namy school desks need to be purchased for all students")

    studentsInFirstClass = int(input("Enter number on student in first class: "))
    studentsInSecondClass = int(input("Enter number on student in second class: "))
    studentsInThirdClass = int(input("Enter number on student in third class: "))
    
    totalDesks = (studentsInFirstClass + 1) // 2 + (studentsInSecondClass + 1) // 2 + (studentsInThirdClass + 1) // 2
    print(f"{totalDesks} school desks need to be purchased")

    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break