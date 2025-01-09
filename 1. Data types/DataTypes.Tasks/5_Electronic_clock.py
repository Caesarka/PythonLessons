
while True:

    print("Let's find out what time it will be after given number of minutes")
    giveNumberOfMinutes = int(input("Enter the quantity of minutes: "))

    hours = giveNumberOfMinutes // 60
    minutesOnClock = giveNumberOfMinutes - hours * 60
    hoursOnClock = hours % 24
    
    print(f"It will be {hoursOnClock:02}:{minutesOnClock:02}")

    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break