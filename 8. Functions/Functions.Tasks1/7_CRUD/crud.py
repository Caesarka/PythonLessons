from random import randint
import os

book_list = []

def make_choice():
    while True:
        choice = input(
            '''Menu
C. Add new book to the library catalog.
R. Open book in reading mode.
U. Update title of the book.
D. Delete book from library catalog.
Q. Exit from library catalog.
Your choice: ''').lower()
        if choice in ['c', 'r', 'u', 'd', 'q']:
            return choice
        else:
            print('Invalid choice. Please try again.')

def create(name):
    text = open('random_text.txt')
    source = text.read().splitlines()
    line_num = randint(0, len(source) - 1)
    book_text = source[line_num]

    book = open(f'{name}.txt', 'w')
    book.write(f'{randint(10000, 99999)}\n')
    book.write('Some Author\n')
    book.write(f'{randint(1200, 2025)}\n')
    book.write(book_text)
    book_list.append(name)
    book_titles = open('book_titles.txt', 'a')
    book_titles.write(f'{name}\n')
    print(f'Book with title \'{name}\' was successfully added to the library catalog.\n')

    text.close()
    book.close()
    book_titles.close()

def enter_unique_name():
    name = input('Enter the name of book: ')
    while name in book_list:
        name = input('There is a book with same title. Please Try again: ')
    return name

def read():
    print('\nBooks available for reading:')
    name = choose_book()
    book = open(f'{name}.txt', 'r')
    line = book.readline()
    while line:
        print(line, end='')
        line = book.readline()
    print('\n')
    book.close()
    return 0

def update():
    print('\nBooks available for updating:')
    name = choose_book()
    new_name = input('Enter a new name: ')
    source = f'{name}.txt'
    dest = f'{new_name}.txt'
    os.rename(source, dest)
    for i in range(0, len(book_list) - 1):
        if book_list[i] == name:
            book_list[i] = new_name
    print('Name was successfully changed.')
    return 0

def delete():
    print('\nBooks available for deleting:')
    name = choose_book()
    sure = input('Are you sure? This action deletes book permanently. y/n: ')
    if sure == 'y':
        os.remove(f'{name[0 : -1]}.txt')
        for i in range(0, len(book_list) - 1):
            if book_list[i] == name:
                book_list.remove(name)
    return 0

def transmit(choice):
    if choice == 'c':
        name = enter_unique_name()
        create(name)
    
    elif choice == 'r':
        read()
    
    elif choice == 'u':
        update()
    
    elif choice == 'd':
        delete()
    
    elif choice =='q':
        return False
    return True
    
def fill_list():
    book_titles = open('book_titles.txt', 'r')
    try:
        while True:
            line = book_titles.readline()
            if line:
                book_list.append(line.strip())
            else:
                break
    finally:
        book_titles.close()
    print(book_list)
    for el in book_list:
        print(f'*{el}')

def choose_book():
    for i in range(0, len(book_list)):
        print(f'{i}. {book_list[i]}')
    name = int(input('Enter the book number: '))
    return book_list[name]

def main_program():
    fill_list()
    print('Hello, this is library catalog.')
    while True:
        choice = make_choice()
        if not transmit(choice):
            break


if __name__ == '__main__':
    main_program()
