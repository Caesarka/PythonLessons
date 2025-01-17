import unittest
import leap_year

class TestStringMethods(unittest.TestCase):
    def test_checkIsLeapYear_good(self):
        self.assertEqual(True, leap_year.checkIsLeapYear(400))
        self.assertEqual(True, leap_year.checkIsLeapYear(2032))
        self.assertEqual(False, leap_year.checkIsLeapYear(2033))
        self.assertEqual(True, leap_year.checkIsLeapYear(1908))

if __name__ == '__main__':
    unittest.main()