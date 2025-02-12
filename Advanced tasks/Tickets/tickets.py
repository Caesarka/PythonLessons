FAN_ZONE = 800
DANCE_FLOOR = 650
PARTER = 500
FAN_ZONE_QTY_LIMIT = 5

def get_tickets(amount, fan_zone_tickets_quantity, dance_floor_tickets_quantity, parter_tickets_quantity):
    fan_zone_total_quantity = 0
    dance_floor_total_quantity = 0
    parter_total_quantity = 0

    parter_total_quantity = min(amount // PARTER, parter_tickets_quantity)
    amount -= parter_total_quantity * PARTER

    fan_zone_total_quantity = min(amount // FAN_ZONE, fan_zone_tickets_quantity, FAN_ZONE_QTY_LIMIT)
    amount -= fan_zone_total_quantity * FAN_ZONE

    dance_floor_total_quantity = min(amount // DANCE_FLOOR, dance_floor_tickets_quantity)
    
    print(f"Parter tickets, quantity: {parter_total_quantity}")
    print(f"Fan zone tickets, quantity: {fan_zone_total_quantity}")
    print(f"Dance floor tickets, quantity: {dance_floor_total_quantity}")
    return [parter_total_quantity, fan_zone_total_quantity,dance_floor_total_quantity]




if __name__ == '__main__':
    amount = int(input("Enter total amount: "))

    get_tickets(amount, fan_zone_tickets_quantity=100, dance_floor_tickets_quantity=100, parter_tickets_quantity=100)

