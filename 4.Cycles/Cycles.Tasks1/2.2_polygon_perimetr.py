import sys
import math

print("Let's calculate the perimetr for polygon.")
while True:
    index = 1
    current_coordinateX = 0
    current_coordinateY = 0
    next_coordinateX = 0
    next_coordinateY = 0
    perimeter = 0
    first_coordinateX = previous_coordinateX = input(f"Enter {index} coordinate X: ")
    first_coordinateY = previous_coordinateY = input(f"Enter {index} coordinate Y: ")
    while True:
        current_coordinateX = input(f"Enter {index} coordinate X: ")
        if current_coordinateX == '':
            break
        else:
            current_coordinateY = input(f"Enter {index} coordinate Y: ")
            index += 1
            perimeter += math.sqrt(pow((int(current_coordinateX) - int(previous_coordinateX)), 2) + pow((int(current_coordinateY) - int(previous_coordinateY)), 2))
            previous_coordinateX = current_coordinateX
            previous_coordinateY = current_coordinateY
    perimeter += math.sqrt(pow((int(previous_coordinateX) - int(first_coordinateX)), 2) + pow((int(previous_coordinateY) - int(first_coordinateY)), 2))
    print(f"Perimeter is equal: {perimeter}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break