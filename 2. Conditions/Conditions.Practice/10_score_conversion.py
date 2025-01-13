print("Let's convert primary score to final score and find the total mark for Physics.")
table = {
    1: 5,
    2: 9,
    3: 14,
    4: 18,
    5: 23,
    6: 27,
    7: 32,
    8: 36,
    9: 39,
    10: 41,
    11: 43,
    12: 44,
    13: 46,
    14: 48,
    15: 49,
    16: 51,
    17: 53,
    18: 54,
    19: 56,
    20: 58,
    21: 59,
    22: 61,
    23: 62,
    24: 64,
    25: 65,
    26: 67,
    27: 68,
    28: 70,
    29: 71,
    30: 73,
    31: 74,
    32: 76,
    33: 77,
    34: 79,
    35: 80,
    36: 82,
    37: 84,
    38: 86,
    39: 88,
    40: 90,
    41: 92,
    42: 94,
    43: 96,
    44: 98,
    45: 100
}
while True:
    primeScore = int(input("Enter the primary score: "))
    mark = 0
    if primeScore in range(0, 8):
        mark = 2
    elif primeScore == 8:
        mark = 3
    elif primeScore in range(9, 35):
        mark = 4
    elif primeScore in range(35, 46):
        mark = 5
    else:
        print("You've entered incorrect score.")
        break
    print(f"Final score equal {table[primeScore]}. Total mark {mark}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break