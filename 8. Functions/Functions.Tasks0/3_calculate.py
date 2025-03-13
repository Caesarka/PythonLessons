def calculate_area_and_perimeter(length, width):
    area = length * width
    perimeter = (length + width) * 2
    return area, perimeter

print('Let\'s calculate area and perimeter for rectangle.')
a ,__, b = input('Enter two sides for rectangle: ')

area, perimeter = calculate_area_and_perimeter(int(a), int(b))

print(f'Area equals {area}, perimeter equals {perimeter}.')