import datetime
def findSeasonByDayOfYear(date):
    season = ''
    month, _, day = date.partition(', ')

    formatDate = datetime.datetime(2025, int(month), int(day))

    dateAsNumber = formatDate.timetuple().tm_yday

    if dateAsNumber in range(0, 79) or dateAsNumber in range(355, 366):
        season = "Winter"
    elif dateAsNumber in range(79, 172):
        season = "Spring"
    elif dateAsNumber in range(172, 265):
        season = "Summer"
    elif dateAsNumber in range(265, 355):
        season = "Fall"
    else:
        print("Could not recognize season for this day.")
    print(season)
    return season


if __name__ == '__main__':
    print("Let's determine what season it will be on a certain date.")
    date = input("Enter month and day, f.e.: 7, 12: ")
    findSeasonByDayOfYear(date)