file = open('employees.txt', 'w')
while True:
    name = input("Enter firstname and lastname, use space as delimiter: ")
    salary = input("Enter salary: ")
    file.write(f"{name}, {salary}\n")
    usrInput = input("Enter any key for continue or q for exit. ")
    if usrInput == 'q':
        break
file.close()