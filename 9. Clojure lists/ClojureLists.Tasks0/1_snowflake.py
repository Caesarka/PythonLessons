print("Hello! This program can draw a snowflakes.")

size = int(input("Enter size of snowflake: "))
blue_flake = '\033[94m❄\033[0m'

if size % 2 == 0:
    print("Size was increased by 1 to make it odd.")
    size += 1

snowflake = [['●' for _ in range(size)] for _ in range(size)]
median_index = size // 2

for i in range(size):
    for j in range(size):
        if i == median_index or j == median_index or i == j or i == (size - j - 1):
            snowflake[i][j] = blue_flake
        print(snowflake[i][j], end=' ')
    print()
