import unittest
import strength_password_methods

class TestStringMethod(unittest.TestCase):
    def test_strength_password_methods(self):
        self.assertEqual(True, strength_password_methods.checkStrengthOfPasswordMethods('fFhfkf6*65'))
        self.assertEqual((False, ['Password does not consist at least one appercase letter.', 'Password is not valid, please try again.']), strength_password_methods.checkStrengthOfPasswordMethods('fhfkf6*65'))
        self.assertEqual((False, ['Password does not consist at least one lowercase letter.', 'Password is not valid, please try again.']), strength_password_methods.checkStrengthOfPasswordMethods('F6*65HJKJKHGG'))
        self.assertEqual((False, ['Password does not consist at least one digit.', 'Password is not valid, please try again.']), strength_password_methods.checkStrengthOfPasswordMethods('fhfkf*Gjjk'))
        self.assertEqual((False, ['Password does not consist at least one special character.', 'Password is not valid, please try again.']), strength_password_methods.checkStrengthOfPasswordMethods('fGhfkf665'))
        self.assertEqual((False, ['Password consists at least one character that out of range.', 'Password is not valid, please try again.']), strength_password_methods.checkStrengthOfPasswordMethods('fGhfkf665*дj'))
        self.assertEqual((False, ['Password consists at least one character that out of range.', 'Password is not valid, please try again.']), strength_password_methods.checkStrengthOfPasswordMethods('fGhfkf665* j'))
        self.assertEqual((False, ['Password is weak.', 'Password does not consist at least one appercase letter.', 'Password does not consist at least one special character.', 'Password is not valid, please try again.']), strength_password_methods.checkStrengthOfPasswordMethods('qwerty1234'))
        self.assertEqual((False, ['Password\'s length is less than 8 characters.', 'Password does not consist at least one appercase letter.', 'Password does not consist at least one digit.', 'Password does not consist at least one special character.', 'Password consists at least one character that out of range.', 'Password is not valid, please try again.']), strength_password_methods.checkStrengthOfPasswordMethods('д'))
        self.assertEqual((False, ['Password\'s length is less than 8 characters.', 'Password does not consist at least one lowercase letter.', 'Password does not consist at least one digit.', 'Password does not consist at least one special character.', 'Password consists at least one character that out of range.', 'Password is not valid, please try again.']), strength_password_methods.checkStrengthOfPasswordMethods('Д'))
        #self.assertEqual('Password\'s length less than 8 characters. Password is not valid, please try again.', strength_password_methods.checkStrengthOfPasswordMethods('dfhg'))

        #self.assertEqual('Password\'s length less than 8 characters. Password is not valid, please try again.', strength_password_methods.checkStrengthOfPasswordMethods('1223'))
        #self.assertEqual('Password\'s length less than 8 characters. Password is not valid, please try again.', strength_password_methods.checkStrengthOfPasswordMethods('sdf43'))
        #self.assertEqual('Password is valid', strength_password_methods.checkStrengthOfPasswordMethods('gghD65$km'))
        #self.assertEqual('Password is not valid, please try again.', strength_password_methods.checkStrengthOfPasswordMethods('gghD65$kmфыв'))



if __name__ == '__main__':
    unittest.main()