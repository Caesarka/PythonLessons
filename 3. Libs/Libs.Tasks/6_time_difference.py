print("Let's find the difference between two moments of the day.")
while True:
    print("Enter time for start.")
    hours_first = int(input("Enter hours: "))
    minutes_first = int(input("Enter minutes: "))
    seconds_first = int(input("Enter seconds: "))
    print("Enter time for end.")
    hours_second = int(input("Enter hours: "))
    minutes_second = int(input("Enter minutes: "))
    seconds_second = int(input("Enter seconds: "))
    difference = (hours_second - hours_first) * 3600 + (minutes_second - minutes_first) * 60 + (seconds_second - seconds_first)

    print(f"Differense between {hours_second:02}:{minutes_second:02}:{seconds_second:02} and {hours_first:02}:{minutes_first:02}:{seconds_first:02} equals {difference} seconds")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break