print("Let's count elephants.")

while True:
    count = 0
    print('Buy an epephant!')
    while True:
        answer = input('Your answer: ')
        if answer == 'buy':
            print('Hooray!')
            print('Buy an epephant!')
            count += 1
        elif answer == 'stop':
            if count == 0:
                print("Oh, no! You didn't buy a single elephant!")
            elif count == 1:
                print(f"You bought {count} elephan.")
            else:
                print(f"You bought {count} elephans.")
            break
        else:
            print(f"Every one say {answer}, but you go and buy an elephant!")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break