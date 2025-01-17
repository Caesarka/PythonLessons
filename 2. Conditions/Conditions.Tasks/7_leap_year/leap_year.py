def checkIsLeapYear(year):
    print("Let's determine if the year is a leap year")
    if year % 4 == 0:
        if year % 400 == 0 or year % 100 != 0:
            print(f"{year} year is leap.")
            return True
    else:
        print(f"{year} year is not leap.")
        return False

if __name__ == '__main__':
    year = int(input("Enter the year: "))
    checkIsLeapYear(year)