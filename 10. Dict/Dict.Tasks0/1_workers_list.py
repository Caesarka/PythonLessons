from datetime import datetime


def add_employee(employees, id):
    print("\nLet's add all requied information about employee.")

    firstname = input("Enter firstname: ")
    lastname = input("Enter lastname: ")
    work_place = int(input("Enter work place number: "))
    role = input("Enter role: ")
    salary = int(input("Enter salary, $: "))

    employee = []
    employee.extend([firstname, lastname, work_place, role, salary])
    employees[id] = employee

    print("Employee was cuccessfully added.\n")


def get_employee(employees):
    lines = ['Firstname: ', 'Lastname: ',
             'Work place number: ', 'Role: ', 'Salary: ']

    print("List of employees:")
    for key in employees:
        if isinstance(employees[key], str):
            print(f"ID {key}. {employees[key]}")
        else:
            print(f"ID {key}. {employees[key][0]} {employees[key][1]}")

    id = int(input("Enter the employee ID you want to retrieve: "))

    if id in employees:
        print(f"ID: {id}")
        for i in range(len(employees[id])):
            if isinstance(employees[id], str):
                print(f"{employees[id]}")
                break
            else:
                print(f"{lines[i]}{employees[id][i]}")
    else:
        print("There is no employee with such of ID.")

    print()


def fire_employeer(employees):
    print("List of employees:")
    for key in employees:
        if isinstance(employees[key], str):
            print(f"ID {key}. {employees[key]}")
        else:
            print(f"ID {key}. {employees[key][0]} {employees[key][1]}")
    id = int(input("Enter the employee ID you want to fire: "))
    if id in employees:
        usrInput = input(
            f"Attention! The employee {employees[id][0]} {employees[id][1]} will be fired. Are you sure? Y/N: ")
        if usrInput == 'Y':
            print(
                f"Employee {employees[id][0]} {employees[id][1]} was fired {datetime.today().strftime('%d-%m-%Y')}.")
            employees[id] = f"Fired: {datetime.today().strftime('%d-%m-%Y')}"


def delete_all(employees):
    usrInput = input("Are you sure to delete records for all employees? Y/N: ")
    if usrInput == 'Y':
        employees.clear()
        print("All data was deleted.")


def max_salary(employees):
    keys = []
    max_salary = 0
    for key in employees:
        if isinstance(employees[key], str):
            continue
        elif employees[key][-1] == max_salary:
            keys.append(key)
        elif employees[key][-1] > max_salary:
            max_salary = employees[key][-1]
            keys = [key]

    print("Names of employees with highest salary:")
    for el in keys:
        print(f"{employees[el][0]} {employees[el][1]}")


def list_workers(employees):
    print(f"{'ID':<10}{'Firstname':<10}{'Lastname':<10}{'Work place':<13}{'Role':<10}{'Salary, $':<10}")
    for key in employees:
        if isinstance(employees[key], str):
            print(f"{key:<10}{employees[key]}")
        else:
            print(
                f"{key:<10}{employees[key][0]:<10}{employees[key][1]:<10}{employees[key][2]:<13}{employees[key][3]:<10}{employees[key][4]:<10}")


def list_current_workers(employees):
    print(f"{'ID':<10}{'Firstname':<10}{'Lastname':<10}{'Work place':<13}{'Role':<10}{'Salary, $':<10}")
    for key in employees:
        if isinstance(employees[key], str):
            continue
        else:
            print(
                f"{key:<10}{employees[key][0]:<10}{employees[key][1]:<10}{employees[key][2]:<13}{employees[key][3]:<10}{employees[key][4]:<10}")


def get_choice():

    employees = {}
    id = 0

    while True:
        print('''Menu.
Enter A for add employee.
Enter I for show information about exact employee.
Enter F for fire exact employee.
Enter D for delete records for all employees.
Enter M to get names of employees with highest salary.
Enter L to get all employees.
Enter C to get all current employees.
Enter Q for exit.''')
        action = input('Please choose what you want to do: ')
        match action:
            case 'A':
                id += 1
                add_employee(employees, id)
            case 'I':
                get_employee(employees)
            case 'F':
                fire_employeer(employees)
            case 'D':
                delete_all(employees)
            case 'M':
                max_salary(employees)
            case 'L':
                list_workers(employees)
            case 'C':
                list_current_workers(employees)
            case 'Q':
                break


get_choice()
