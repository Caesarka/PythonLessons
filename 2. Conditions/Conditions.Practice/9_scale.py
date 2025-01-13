
print("Let's make a conversion from the Mercalli scale to the Richter scale and hope that you will NEVER need it!")
while True:
    intensityMercalli = int(input("Enter the intensity of the earthquake on the Mercalli scale from 1 to 12: "))
    if intensityMercalli in range(1, 4):
        print("0 - 4.3 Richter scale.")
        if intensityMercalli == 1:
            print("Vibration is recorded only by devices")
        elif intensityMercalli == 2:
            print("Vibrations are felt when standing on the stairs")
        else:
            print("Tremors are felt in closed spaces, slight vibrations of objects")
    elif intensityMercalli in range(4, 6):
        print("4.3 - 4.8 Richter scale.")
        if intensityMercalli == 4:
            print("Clinking of dishes, swaying of trees, tremors are felt in parked cars")
        else:
            print("Creaking of doors, awakening from sleep, pouring of liquids from vessels")
    elif intensityMercalli in range(6, 8):
        print("4.8 - 6.2 Richter scale.")
        if intensityMercalli == 6:
            print("Unsteady walking of people, damage to windows, falling of pictures from walls")
        else:
            print("Difficult to stand, tiles are falling from the walls, bells are ringing")
    elif intensityMercalli in range(8, 11):
        print("6.2 - 7.3 Richter scale.")
        if intensityMercalli == 8:
            print("Damage to chimneys, damage to sewers")
        elif intensityMercalli == 9:
            print("General panic, damage to foundations")
        else:
            print("Most buildings are damaged, large landslides, rivers overflow their banks")
    elif intensityMercalli in range(11, 13):
        print("7.3 - 8.9 Richter scale.")
        if intensityMercalli == 11:
            print("Damage to railway tracks, damage to roads, holes in the ground, falling stones")
        else:
            print("Total destruction, waves on the surface of the earth, changes in the flow of rivers, poor visibility")
    else:
        print("Youэve entered an invalid value for intensity.")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break
