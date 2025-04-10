import random
from turtledemo.penrose import makeshapes

status = ['present', 'absent', 'registered']

def create_clojure_list():
    first_names = open('first_names.txt', encoding='utf-8')
    last_names = open('last_names.txt', encoding='utf-8')

    clojure_list = []

    for line in first_names:
        first_name = line.strip()
        last_name = last_names.readline().strip()
        stat = random.choice(status)
        clojure_list.append([first_name, last_name, stat])

    first_names.close()
    last_names.close()

    return clojure_list

def work_with_list(clojure_list):
    print("\nThis is a menu for working with list of participants.")

    while True:
        print("\nEnter S for show all participants.")
        print("Enter P for show participants who are present.")
        print("Enter C for change status for participant.")
        print("Enter A for add a new participant.")
        print("Enter D for delete participant.")
        print("Enter Q for exit.\n")
        num = input("Your choice: ")

        match num:
            case 'S':
                show_all(clojure_list)
            case 'P':
                at_point(clojure_list)
            case 'C':
                change_point(clojure_list)
            case 'A':
                add_member(clojure_list)
            case 'D':
                delete_member(clojure_list)
            case 'Q':
                break

def show_all(clojure_list):
    print("\nList of all participants:")

    for el in clojure_list:
        print(f"{el[0]} {el[1]}: {el[2]}")

def at_point(clojure_list):
    print('\nParticipants present:')

    for el in clojure_list:
        if el[2] == 'present':
            print(f"{el[0]} {el[1]}")

def change_point(clojure_list):
    flag = False
    print("Let\'s change the status of participant.")
    name = input("Enter first name and last name: ")

    for part in clojure_list:
        if f"{part[0]} {part[1]}"  == name:
            new_stat = input(f"Enter new status for participant {part[0]} {part[1]}: ")
            if new_stat in status:
                part[2] = new_stat
                flag = True
                print("Status changed.")
            else:
                print("There is no such status.")

    if not flag:
        print("Sorry, the participant doesn't exist.")

def add_member(clojure_list):
    print("Enter new participant first name, last name and status: ")
    new_member = input("Use the mask: first_name last_name, status: ")
    new_member_name = new_member.split(', ')[0]
    new_status = new_member.split(', ')[1]
    flag = False
    
    for i in range(len(clojure_list)):
        if new_member_name == ' '.join(clojure_list[i][0:2]):
            flag = True
            print("This participant already exist.")
            break

    if not flag:
        if new_status in status:
            clojure_list.append([new_member_name.split(' ')[0], new_member_name.split(' ')[1], new_status])
            print("New participants was successfully added.")
        else: print('Status is not valid.')

def delete_member(clojure_list):
    member = input("Enter participant\'s first name and last name: ")
    
    for i in range(len(clojure_list)):
        if member == ' '.join(clojure_list[i][0:2]):
            check = input(f"Are you sure? {member} will deleted from list of participants. Y/N: ")
            if check == 'Y':
                clojure_list.pop(i)
                print("Participant was deleted.")
                break

work_with_list(create_clojure_list())
