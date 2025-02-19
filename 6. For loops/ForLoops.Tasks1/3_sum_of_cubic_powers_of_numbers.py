print("Let's find sum of cubic powers of numbers.")
while True:
    number = int(input("Enter the number: "))
    sum = 0
    for i in range(1, number + 1):
        sum += pow(i, 3)
    print(sum)
    ustInput = input("Enter any key for continue or q for exit. ")
    if ustInput == 'q':
        break