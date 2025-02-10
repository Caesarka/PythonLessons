from random import randint

def divide(m, n, k):
    i = 1
    j = 1
    while i < m:
        if (i * n) == k:
            print("Yes")
            return True
        i += 1
    while j < n:
        if (j * m) == k:
            print("Yes")
            return True
        j += 1
    print("No")
    return False



if __name__ == '__main__':
    m = int(input("Enter m: " ))
    n = int(input("Enter n: "))
    k = int(input(f"Enter number of pieces you desire: "))

    divide(m, n, k)