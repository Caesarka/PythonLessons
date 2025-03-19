import os
import unittest
import crud

class TestStringMethod(unittest.TestCase):
    #def test_fill_list(self):
    #    crud.fill_list()
    #    self.assertEqual("['One', 'Two', 'Three', 'Four']", str(crud.book_list))
    
    def test_create_new_book(self):
        #cleanup
        crud.fill_list()
        for el in crud.book_list:
            os.remove(f'{el}.txt')
        if os.path.exists('book_titles.txt'):
            os.remove(f'book_titles.txt')

        crud.book_list = []

        #execute
        crud.create('Kolobok')
        crud.create('Vorona i lisitca')

        #verify
        self.assertEqual("['Kolobok', 'Vorona i lisitca']", str(crud.book_list), msg='first')
        crud.book_list.append('bad')
        crud.fill_list()
        self.assertEqual("['Kolobok', 'Vorona i lisitca']", str(crud.book_list), msg='second')
        
    def test_create_new_book(self):
        #cleanup
        crud.fill_list()
        for el in crud.book_list:
            os.remove(f'{el}.txt')
        if os.path.exists('book_titles.txt'):
            os.remove(f'book_titles.txt')

        crud.book_list = []

        #execute
        crud.create('Kolobok')
        crud.create('Vorona i lisitca')

        #verify
        self.assertEqual("['Kolobok', 'Vorona i lisitca']", str(crud.book_list), msg='first')
        crud.book_list.append('bad')
        crud.fill_list()
        self.assertEqual("['Kolobok', 'Vorona i lisitca']", str(crud.book_list), msg='second')

if __name__ == '__main__':
    unittest.main()