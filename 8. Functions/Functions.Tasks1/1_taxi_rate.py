def calculate_taxi_rate(destination):
    base_rate = 4
    added_tariff = 0.25
    added_dest = 140

    final_price = 4 + destination // 140 * 0.25
    return final_price

print('Let\'s calculate the price for taxi ride.')
destination = int(input('Enter the destination in metres: '))

print(f'The total price for ride is {calculate_taxi_rate(destination)}')
