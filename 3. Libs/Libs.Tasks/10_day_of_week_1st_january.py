import math

days = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}

print("Let's find day of week for January 1st. .")
while True:
    year = int(input("Enter the year: "))
    day_of_week = (year + math.floor((year - 1)/4) - math.floor((year - 1)/100) + math.floor((year - 1)/400)) % 7
    print(days.get(day_of_week))
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break