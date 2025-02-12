import unittest
import data_collection

class TestStringMethods(unittest.TestCase):

    def test_data_collection(self):
        self.assertEqual(1, data_collection.get_shortcut(6, 4, 2, 1))
        self.assertEqual(1, data_collection.get_shortcut(4, 6, 2, 1))
        self.assertEqual(1, data_collection.get_shortcut(4, 6, 1, 2))
        self.assertEqual(1, data_collection.get_shortcut(4, 6, 1, 1))
        self.assertEqual(1, data_collection.get_shortcut(4, 6, 2, 3))



if __name__ == '__main__':
    unittest.main()