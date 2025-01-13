while True:
    while True:
        print("Let's prepare for the party. Enter nick and level for each gamer, f.e. Name,100")
        gamer1 = input("Gamer 1: ")
        gamer2 = input("Gamer 2: ")
        gamer3 = input("Gamer 3: ")

        name1, _, level1 = gamer1.partition(',')
        name2, _, level2 = gamer2.partition(',')
        name3, _, level3 = gamer3.partition(',')

        gamers = [
            (name1, int(level1)),
            (name2, int(level2)),
            (name3, int(level3)),
        ]

        dict = {}
        for name, level in gamers: 
            if level not in dict: 
                dict[level] = []
            dict[level].append(name)

        found = False

        for k, v in dict.items():
            if len(v) > 1:
                print(f"{len(v)}. Gamers with the same level: ", end='')
                for item in v:
                    print(item, end=', ')
                print()
                found = True
                break
        if not found:
            print("0. All gamers have different level")
            break
        
        break
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break