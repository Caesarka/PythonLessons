def check_is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("This is a triangle.")
        return True
    else:
        print("This is not a triangle.")
        return False

def get_type_of_triangle(a, b, c):
    triangle = [a, b, c]
    triangle.sort()
    hypotenuse  = triangle.pop()
    side1 = triangle.pop()
    side2 = triangle.pop()

    if pow(hypotenuse, 2) == (pow(side1, 2) + pow(side2, 2)):
        print("Type: right angled triangle")
        return "right angled"
    elif pow(hypotenuse, 2) < (pow(side1, 2) + pow(side2, 2)):
        print("Type: acute triangle")
        return "acute"
    else:
        print("Type: obtuse triangle")
        return "obtuse"




if __name__ == '__main__':
    a = int(input("Enter a: " ))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    check_is_triangle(a, b, c)
    get_type_of_triangle(a, b, c)