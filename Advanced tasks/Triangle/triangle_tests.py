import unittest
import triangle

class TestStringMethods(unittest.TestCase):

    def test_triangle(self):
        self.assertEqual(True, triangle.check_is_triangle(3, 4, 5))
        self.assertEqual(False, triangle.check_is_triangle(3, 5, 10))
        self.assertEqual(True, triangle.check_is_triangle(4, 4, 4))
        self.assertEqual(True, triangle.check_is_triangle(4, 4, 5))
        self.assertEqual("right angled", triangle.get_type_of_triangle(5, 13, 12))
        self.assertEqual("acute", triangle.get_type_of_triangle(5, 5, 5))
        self.assertEqual("acute", triangle.get_type_of_triangle(17, 16, 11))
        self.assertEqual("obtuse", triangle.get_type_of_triangle(15, 10, 9))



if __name__ == '__main__':
    unittest.main()