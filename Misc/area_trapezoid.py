print("Let's find area of trapezoid.")
a_base = int(input("Enter value for first base: "));
b_base = int(input("Enter value for second base: "));
height = int(input("Enter value for height: "));

area = round(((a_base + b_base) * height / 2), 4);
print(f"Area equals {area}");
