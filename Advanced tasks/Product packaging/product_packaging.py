def check_it_fit(product, box):
    status = ''
    box.sort()
    product.sort()
    if box == product:
        status = "Equal"
    else:
        i = 0
        while i < len(box):
            if product[i] > box[i]:
                status = "Too large"
                break
            elif product[i] < box[i]:
                status = "Matched"
            i += 1
    print(status)
    return status

if __name__ == '__main__':
    box = []
    product = []

    product_width = int(input("Enter product width: " ))
    product_length = int(input("Enter product length: "))
    product_height = int(input("Enter product height: "))
    box_width = int(input("Enter box width: " ))
    box_length = int(input("Enter box length: "))
    box_height = int(input("Enter box height: "))

    box.extend([box_width, box_length, box_height])
    product.extend([product_width, product_length, product_height])
    check_it_fit(product, box)