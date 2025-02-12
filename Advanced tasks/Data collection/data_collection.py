def get_shortcut(m, n, x, y):
    min_distance = y
    if m > n:
        if min_distance > (n - y):
            min_distance = n - y
        if min_distance > x:
            min_distance = x
        if min_distance > m - x:
            min_distance = m - x
    else:
        if min_distance > (m - y):
            min_distance = m - y
        if min_distance > x:
            min_distance = x
        if min_distance > n - x:
            min_distance = n - x
    print(f"Shortest way to charge station is {min_distance}")
    return min_distance

if __name__ == '__main__':
    m = int(input("Enter m: " ))
    n = int(input("Enter n: "))
    x = int(input(f"Enter distance to shorter side: "))
    y = int(input(f"Enter distance to longer side: "))

    get_shortcut(m, n, x, y)