print("Let's find numbers that equal to their index.")
while True:
    numbers = input("Enter the numbers: ")
    lst = list(map(int, numbers.split()))
    new_list = []
    for i, el in enumerate(lst, start=1):
        if i == el:
            new_list.append(el)
    print(new_list)
    ustInput = input("Enter any key for continue or q for exit. ")
    if ustInput == 'q':
        break