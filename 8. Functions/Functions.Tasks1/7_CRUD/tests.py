import os
import unittest
import crud

class TestStringMethod(unittest.TestCase):
    #def test_fill_list(self):
    #    crud.fill_list()
    #    self.assertEqual("['One', 'Two', 'Three', 'Four']", str(crud.book_list))
    
    def test_create_new_book(self):
        crud.fill_list()
        for el in crud.book_list:
            os.remove(f'book_titles.txt')
        crud.create('Kolobok')
        self.assertEqual("['One', 'Two', 'Three', 'Four', 'Kolobok']", str(crud.book_list))
        crud.fill_list()
        self.assertEqual("['One', 'Two', 'Three', 'Four', 'Kolobok']", str(crud.book_list))

if __name__ == '__main__':
    unittest.main()