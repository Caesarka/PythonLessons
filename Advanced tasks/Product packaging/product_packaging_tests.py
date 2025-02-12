import unittest
import product_packaging

class TestStringMethods(unittest.TestCase):

    def test_product_packaging(self):
        self.assertEqual("Too large", product_packaging.check_it_fit([2, 1, 1], [1, 1, 1]))
        self.assertEqual("Equal", product_packaging.check_it_fit([1, 1, 1], [1, 1, 1]))
        self.assertEqual("Matched", product_packaging.check_it_fit([1, 1, 1], [2, 2, 2]))
        self.assertEqual("Matched", product_packaging.check_it_fit([2, 1, 1], [2, 2, 2]))
        self.assertEqual("Too large", product_packaging.check_it_fit([1, 1, 3], [2, 2, 2]))


    def test_uz(self):
        self.assertEqual("Equal", product_packaging.check_it_fit([1, 2, 2], [1, 2, 2]))



if __name__ == '__main__':
    unittest.main()