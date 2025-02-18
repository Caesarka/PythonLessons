print("Let's print elements with order number.")
while True:
    sequence = input("Enter the sequence of something. Use space as delimiter: ")
    lst = list(map(str, sequence.split()))
    for i, el in enumerate(lst, start=1):
        print(i, el)
    ustInput = input("Enter any key for continue or q for exit. ")
    if ustInput == 'q':
        break