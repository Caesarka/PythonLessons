print("Let's print the stairs.")
while True:
    number = int(input("Enter the number: "))
    for i in range(1, number + 1):
        for i in range(1, i + 1):
            print(i, end='')
        print(end='\n')
    ustInput = input("Enter any key for continue or q for exit. ")
    if ustInput == 'q':
        break