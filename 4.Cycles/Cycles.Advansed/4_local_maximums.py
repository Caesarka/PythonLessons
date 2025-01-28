import sys

print("Let's find minimum distanse between two local maximums.")
while True:
    max_number_count = 0
    previouse_distance = sys.maxsize
    previouse_max_number_index = 0
    min_distance = 0
    previouse_number = -sys.maxsize
    current_number = -sys.maxsize
    next_number = -sys.maxsize
    distance = 0
    index = 0
    while True:
        next_number = int(input("Enter the number: "))
        index += 1
        if next_number == 0:
            break
        if current_number > previouse_number and current_number > next_number:
            max_number_count += 1
            distance = index - previouse_max_number_index
            previouse_max_number_index = index
            if previouse_distance > distance:
                min_distance = distance
            previouse_distance = distance
        previouse_number = current_number
        current_number = next_number
    if max_number_count == 0:
        min_distance = 0
    print(min_distance)
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break

