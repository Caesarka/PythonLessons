def check_it_fit(box1, box2):
    status = ''
    box1.sort()
    box2.sort()
    if box1 == box2:
        status = "Equal"
    else:
            combine = zip(box1, box2)
            if all(x > y for x, y in combine):
                status = "matched: box2 to box1"
            elif all(x < y for x, y in combine):
                status = "matched: box1 to box2"
            else:
                status = "Boxes are incomparable"
    print(status)
    return status

if __name__ == '__main__':


    box1_width = int(input("Enter width for box 1: " ))
    box1_length = int(input("Enter length for box 1: "))
    box1_height = int(input("Enter height for box 1: "))
    box2_width = int(input("Enter box width for box 2: " ))
    box2_length = int(input("Enter box length for box 2: "))
    box2_height = int(input("Enter box height for box 2: "))

    box1 = [box1_width, box1_length, box1_height]
    box2 = [box2_width, box2_length, box2_height]
    check_it_fit(box1, box2)