cart = []

def add_to_cart(item):
    global cart
    cart.append(item)
    print(f'Item {item} added to cart.')

def remove_from_cart(item):
    global cart
    if item in cart:
        cart.remove(item)
        print(f'Item {item} removed from cart.')
    else:
        print('There is no such item in your cart.')

def show_cart():
    print('Your cart contains the following items:')
    for el in cart:
        print(f'- {el}')

def make_choice():
    print('Enter a for adding the item.')
    print('Enter r for removing the item.')
    print('Enter s for exploring all items in your cart.')
    print('Enter q for exit .')
    while True:
        item = ''
        action =  input('Please choose what you want to do: ')
        match action:
            case 'a':
                item = input('Enter the item you want to add to your cart: ')
                add_to_cart(item)
            case 'r':
                item = input('Enter the item you want to remove from your cart: ')
                remove_from_cart(item)
            case 's':
                show_cart()
            case 'q':
                break

print('Hello, this is an online cart. You can add or delete items or show your cart content.')

make_choice()