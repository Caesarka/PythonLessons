import unittest
import strength_password

class TestStringMethod(unittest.TestCase):
    def test_strength_password(self):
        self.assertEqual(False, strength_password.checkStrengthOfPassword('qwerty1234'))
        self.assertEqual(False, strength_password.checkStrengthOfPassword('dfhg'))
        self.assertEqual(False, strength_password.checkStrengthOfPassword('1223'))
        self.assertEqual(False, strength_password.checkStrengthOfPassword('sdf43'))
        self.assertEqual(False, strength_password.checkStrengthOfPassword('gghD65$kmфыв'))
        
        self.assertEqual(False, strength_password.checkStrengthOfPassword('ggh65$km'))
        self.assertEqual(False, strength_password.checkStrengthOfPassword('gghD$km'))
        self.assertEqual(False, strength_password.checkStrengthOfPassword('gghD65km'))
        self.assertEqual(False, strength_password.checkStrengthOfPassword('D65$FFDDSKSALA'), "should require lower case")

    def test_strength_password_good(self):
        self.assertEqual(True, strength_password.checkStrengthOfPassword('gghD65$km'))



if __name__ == '__main__':
    unittest.main()