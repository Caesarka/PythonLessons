import unittest
import data_collection

class TestStringMethods(unittest.TestCase):

    def test_data_collection(self):
        self.assertEqual(True, data_collection.get_shortcut(3, 5, 3))


if __name__ == '__main__':
    unittest.main()