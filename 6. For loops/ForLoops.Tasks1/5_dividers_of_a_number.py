print("Let's find dividers of a number.")
while True:
    number = int(input("Enter the number: "))
    dividers = ''
    for i in range(2, number):
        if number % i == 0:
            dividers += f'{str(i)}, '
    dividers = dividers[:-2]
    print(f"Dividers for number {number}: {dividers}")
    ustInput = input("Enter any key for continue or q for exit. ")
    if ustInput == 'q':
        break