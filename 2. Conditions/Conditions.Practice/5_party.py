while True:
    while True:
        print("Let's prepare for party. Enter nick and level for each gamer, f.e. Name,100")
        gamer1 = input("Gamer 1: ")
        gamer2 = input("Gamer 2: ")
        gamer3 = input("Gamer 3: ")


        name1, _, level1 = gamer1.partition(',')
        name2, _, level2 = gamer2.partition(',')
        name3, _, level3 = gamer3.partition(',')
        try:
            gamers = {name1: int(level1), name2: int(level2), name3: int(level3)}
        except:
            print("Levels should be positive numbers. Please try again.")

        sortedDict = dict(sorted(gamers.items(), key = lambda item: item[1]))
        print(sortedDict)



        usrInput = input("Press any key to continue or q to exit ")
        if usrInput == 'q':
            break