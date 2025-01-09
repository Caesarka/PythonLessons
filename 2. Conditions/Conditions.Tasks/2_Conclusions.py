x = int(input("Enter int number x: "));
y = int(input("Enter int number y: "));
z = float(input("Enter float number z: "));

print(f"{x} > {y}: {bool(x > y)}");
print(f"{z} <= {x} + {y}: {bool(int(z) <= (x + y))}");
print(f"{y} == 0: {bool(y == 0)}");
print(f"{x} * 2 >= {y} * 3: {bool((x * 2) >= (y * 3))}");
print(f"{x} - {y}  =  {z}: {bool((x - y) == (z))}");