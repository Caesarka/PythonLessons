FAN_ZONE = 800
DANCE_FLOOR = 650
PARTER = 500
FAN_ZONE_QTY_LIMIT = 5

def get_tickets(quantity, fan_zone_tickets_quantity, dance_floor_tickets_quantity, parter_tickets_quantity):
    fan_zone_total_quantity = 0
    dance_floor_total_quantity = 0
    parter_total_quantity = 0

    parter_total_quantity = min(quantity, parter_tickets_quantity)
    quantity -= parter_total_quantity
    if quantity > 0:
        dance_floor_total_quantity = min(quantity, dance_floor_tickets_quantity)
        quantity -= dance_floor_total_quantity
        if quantity > 0:
            fan_zone_total_quantity = min(quantity, fan_zone_tickets_quantity)

    print(f"Parter tickets, quantity: {parter_total_quantity}")
    print(f"Fan zone tickets, quantity: {fan_zone_total_quantity}")
    print(f"Dance floor tickets, quantity: {dance_floor_total_quantity}")
    return [parter_total_quantity, fan_zone_total_quantity,dance_floor_total_quantity]


if __name__ == '__main__':
    quantity = int(input("Enter total quantity of tickets you'll going to purchase: "))
    get_tickets(quantity, fan_zone_tickets_quantity=100, dance_floor_tickets_quantity=100, parter_tickets_quantity=100)

