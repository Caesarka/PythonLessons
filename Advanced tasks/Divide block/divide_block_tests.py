import unittest
import divide_block

class TestStringMethods(unittest.TestCase):

    def test_divide_block_good(self):
        self.assertEqual(True, divide_block.divide(3, 5, 3))

    def test_divide_block_bad(self):
        self.assertEqual(False, divide_block.divide(3, 5, 4))

if __name__ == '__main__':
    unittest.main()