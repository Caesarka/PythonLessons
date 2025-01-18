print("Let's find total price.")
while True:
    rubles = int(input("Enter the price for one piece of pie, rubles: "))
    coins = int(input("Enter the price for one piece of pie, coins: "))
    quantity = int(input("Enter quantity: "))
    total_price = rubles * quantity + coins * quantity / 100
    print(f"Total price: {total_price}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break