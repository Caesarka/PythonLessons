PROMO_CODE = "PROMO2025"
dict = {
    'discountForFiveMoreItems': 0.05,
    'discountForPromoCode': 0.07,
    'discountForTenMoreItems': 0.12
    }

def promoCodeCalc():
    print("Let's calculate the amount of discount and the final price for your purchases")
    discount = 0
    while True:
        while True:
            try:
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
                if quantity <= 10:
                    if quantity > 5 and quantity <= 10:
                        discount = dict["discountForFiveMoreItems"]
                    promo = input("Do you have the promo code? Y/N: ")
                    while True:
                        if promo == 'Y':
                            promoCode = input("Please enter the promo code: ")
                            if promoCode == PROMO_CODE:
                                discount = dict["discountForPromoCode"]
                                break
                            else:
                                usrInputWrongCode = input("Oh no! Your promo code is not valid! Please try again (a) or continue without promo code (q). "),
                                if usrInputWrongCode == 'q':
                                    break
                        else:
                            break
                elif quantity > 10:
                    discount = dict["discountForTenMoreItems"]
            except:
                
                usrImputWrongData =  input("Press any key to continue or q to exit "),
                if usrImputWrongData == 'q':
                    return

            totalPrice = price * quantity * (1 - discount)
            if discount > 0:
                print(f"Total price: ${totalPrice}. Your discount is {round(discount * 100)}% and equal ${round(price * quantity * discount, 2)}")
                break
            else:
                totalPrice = price * quantity
                print(f"Total price: ${totalPrice}.")
                break
        discount = 0
        usrInputExit = input("Press any key to continue or q to exit ")
        if usrInputExit == 'q':
            return

if __name__ == '__main__':
    promoCodeCalc()