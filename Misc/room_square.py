print("Find square of the room");
length = int(input("Enter the length: "));
width = int(input("Enter the width: "));
sqr = length * width;
print(f"Room's square is equal {sqr}");
print("Enter 2 dimentions for 3 pieces of furniture:");
length1 = int(input('''      First piece, length '''));
width1 = int(input('''      First piece, width '''));
print();
length2 = int(input('''      Second piece, length '''));
width2 = int(input('''      Second piece, width '''));
print();
length3 = int(input('''      Third piece, length '''));
width3 = int(input('''      Third piece, width '''));
sqrFurniture = length1 * width1 + length2 * width2 + length3 * width3;
if (sqr > sqrFurniture):
    print(f"This furniture fits to the room and you will have free {sqr - sqrFurniture} square cm");
if (sqr < sqrFurniture):
    print(f"This furniture doesn't fit to the room, you need {sqrFurniture - sqr} more square cm")
if (sqr == sqrFurniture):
    print("This furniture fits to the room");
a = 5;
b = 1;
c=a//b;
print(c);
print(type(c));
