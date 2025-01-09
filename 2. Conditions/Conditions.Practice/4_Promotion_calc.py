PROMO_CODE = "PROMO2025"
discountForFiveMoreItems = 0.05
discountForTenMoreItems = 0.1
discountForCode = 0.07
discount = 0

def promoCodeCalc():
    promoByQuantity = 0
    finalPromo = 0
    while True:
        while True:
            try:
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
                if quantity > 5 and quantity <= 10:
                    promoByQuantity = discountForFiveMoreItems
                elif quantity > 10:
                    promoByQuantity = discountForTenMoreItems
                discount = promoByQuantity
                break
            except:
                print("Price and quantity should be entered like a number. Please try again.")
                usrInput = input("Press any key to continue or q to exit ")
            if usrInput == 'q':
                return
        promo = input("Do you have the promo code? Y/N: ")
        while True:
            if promo == 'Y':
                promoCode = input("Please enter the promo code: ")
                if promoCode == PROMO_CODE:
                    if discount == 0 or discount == discountForFiveMoreItems:
                        discount = discountForCode
                    totalPrice = price * quantity * (1 - discount)
                    print(f"Total price: ${totalPrice}. Your discount is {round(discount * 100)}% and equal ${round(price * quantity * discount, 2)}")
                    break
                else:
                    usrInput = input("Oh no! Your promo code is not valid! Please try again (a) or continue without promo code (q). ")
                    if usrInput == 'q':
                        break
            totalPrice = price * quantity * (1 - discount)
            if discount > 0:
                print(f"Total price: ${totalPrice}. Your discount is {round(discount * 100)}% and equal ${round(price * quantity * discount, 2)}")
                break
            else:
                totalPrice = price * quantity
                print(f"Total price: ${totalPrice}.")
                break
        usrInput = input("Press any key to continue or q to exit ")
        if usrInput == 'q':
            break
