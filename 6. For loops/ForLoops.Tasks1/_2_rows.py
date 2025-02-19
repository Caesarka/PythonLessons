for i in range(0, 10):
    for j in range(0, 10):
        print(j, end=' ')
    print()

print('#######')
for i in range(0, 10):
    for j in range(0, 10):
        print(i, end=' ')
    print()

print('#######')
for i in range(1, 11):
    for j in range(0, i):
        print(j, end=' ')
    print()

print('#######')
for i in range(10, 0, -1):
    for j in range(0, i):
        print(j, end=' ')
    print()

print('#######')
for i in range(10, 0, -1):
    s = ''
    for j in range(0, i):
        s += f"{j} "
    print(f'{s : >20}', end=' ')
    print()

print('#######')
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j * i : >2}", end=' ')
    print()

print('#######')
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{j * i : >3}", end=' ')
    print()
