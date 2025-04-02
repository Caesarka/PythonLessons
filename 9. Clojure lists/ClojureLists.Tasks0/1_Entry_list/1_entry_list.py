import random


status = ['present', 'absent', 'registered']
first_names = open('first_names.txt', encoding='utf-8')
last_names = open('last_names.txt', encoding='utf-8')

clojure_list = []
index = 0

for line in first_names:
    first_name = line.strip()
    last_name = last_names.readline().strip()
    stat = random.choice(status)
    clojure_list.append([first_name, last_name, stat])

first_names.close()
last_names.close()

print(clojure_list)

def show_all():
    for el in clojure_list:
        print(f"{el[0]} {el[1]}: {el[2]}")

def at_point():
    print('\nGuests present:')
    for el in clojure_list:
        if el[2] == 'present':
            print(f"{el[0]} {el[1]}")
show_all()

at_point()