from random import randint
import os

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
    global book_list
    book_text = generate_book_text()
    book = open(f'{name}.txt', 'w')
    book.write(f'{randint(10000, 99999)}\n')
    book.write('Some Author\n')
    book.write(f'{randint(1200, 2025)}\n')
    book.write(book_text)
    book.flush()
    book.close()

    book_list.append(name)

    book_titles = open('book_titles.txt', 'a')
    book_titles.write(f'{name}\n')
    print(f'Book with title \'{name}\' was successfully added to the library catalog.\n')

    book_titles.close()

def generate_book_text():
    text = open('random_text.txt', 'r')
    try:
        source = text.read().splitlines()
        line_num = randint(0, len(source) - 1)
        line = source[line_num]
        return line
    finally:
        text.close()

def enter_unique_name():
    name = input('Enter the name of book: ')
    while name in book_list:
        name = input('There is a book with same title. Please Try again: ')
    return name

def read():
    print('\nBooks available for reading:')
    name, index = choose_book()
    book = open(f'{name}.txt', 'r')
    line = book.readline()
    
    print()
    
    while line:
        print(line, end='')
        line = book.readline()
    print('\n')
    
    book.close()

def update():
    print('\nBooks available for updating:')
    
    name, index = choose_book()
    new_name = enter_unique_name()
    source = f'{name}.txt'
    dest = f'{new_name}.txt'
    os.rename(source, dest)
    
    for i in range(0, len(book_list) - 1):
        if book_list[i] == name:
            book_list[i] = new_name
            
    update_index_file_from_list()
    print('Name was successfully changed.\n')

def delete():
    print('\nBooks available for deleting:')
    
    name, index = choose_book()
    sure = input('Are you sure? This action deletes book permanently. y/n: ')
    
    if sure == 'y':
        book_list.remove(name)
        update_index_file_from_list()
    
def fill_list():
    global book_list
    book_list = []
    
    if not os.path.exists('book_titles.txt'):
        return
    
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

def update_index_file_from_list():
    book_titles = open('book_titles.txt', 'w')
    
    for el in book_list:
        book_titles.write(f'{el}\n')

def choose_book():
    for i in range(0, len(book_list)):
        print(f'{i}. {book_list[i]}')
        
    index = int(input('Enter the book number: '))
    
    return book_list[index], index

def main_program():
    fill_list()
    print('Hello, this is library catalog.')
    transmit = {
        'c': lambda: create(enter_unique_name()),
        'r': read,
        'u': update,
        'd': delete,
    }
    
    while True:
        choice = make_choice()
        if choice == 'q':
            break
        
        transmit.get(choice, lambda: print('This f-n is not available') )()

book_list = []

if __name__ == '__main__':
    main_program()
