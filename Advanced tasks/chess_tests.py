import unittest
import chess

class TestStringMethods(unittest.TestCase):

    def test_king_b2_good(self):
        self.assertEqual(True, chess.check('king', 'b,2', 'a,1'))
        self.assertEqual(True, chess.check('king', 'b,2', 'a,2'))
        self.assertEqual(True, chess.check('king', 'b,2', 'a,3'))
        self.assertEqual(True, chess.check('king', 'b,2', 'b,1'))
        self.assertEqual(True, chess.check('king', 'b,2', 'b,3'))
        self.assertEqual(True, chess.check('king', 'b,2', 'c,1'))
        self.assertEqual(True, chess.check('king', 'b,2', 'c,2'))
        self.assertEqual(True, chess.check('king', 'b,2', 'c,3'))

    def test_king_b2_bad(self):
        self.assertEqual(False, chess.check('king', 'b,2', 'a,4'))
        self.assertEqual(False, chess.check('king', 'b,2', 'b,4'))
        self.assertEqual(False, chess.check('king', 'b,2', 'c,4'))
        self.assertEqual(False, chess.check('king', 'b,2', 'd,4'))
        self.assertEqual(False, chess.check('king', 'b,2', 'd,3'))
        self.assertEqual(False, chess.check('king', 'b,2', 'd,2'))
        self.assertEqual(False, chess.check('king', 'b,2', 'd,1'))
        self.assertEqual(False, chess.check('king', 'b,2', 'b,2'))

    def test_king_corner(self):
        self.assertEqual(True, chess.check('king', 'a,1', 'b,2'))
        self.assertEqual(False, chess.check('king', 'a,1', 'a,3'))
        self.assertEqual(True, chess.check('king', 'h,8', 'h,7'))
        self.assertEqual(False, chess.check('king', 'h,8', 'f,8'))

    def test_rook_e3_good(self):
        self.assertEqual(True, chess.check('rook', 'e,3', 'e,2'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'e,1'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'e,4'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'e,5'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'e,6'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'e,7'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'e,8'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'a,3'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'b,3'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'c,3'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'd,3'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'f,3'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'g,3'))
        self.assertEqual(True, chess.check('rook', 'e,3', 'h,3'))

    def test_rook_e3_bad(self):
        self.assertEqual(False, chess.check('rook', 'e,3', 'e,3'))
        self.assertEqual(False, chess.check('rook', 'e,3', 'd,2'))
        self.assertEqual(False, chess.check('rook', 'e,3', 'd,1'))
        self.assertEqual(False, chess.check('rook', 'e,3', 'h,6'))
        self.assertEqual(False, chess.check('rook', 'e,3', 'h,8'))
        self.assertEqual(False, chess.check('rook', 'e,3', 'a,7'))
        self.assertEqual(False, chess.check('rook', 'e,3', 'a,8'))
        self.assertEqual(False, chess.check('rook', 'e,3', 'g,1'))
        self.assertEqual(False, chess.check('rook', 'e,3', 'h,1'))

    def test_rook_e3_corner(self):
        self.assertEqual(True, chess.check('rook', 'a,1', 'a,2'))
        self.assertEqual(False, chess.check('rook', 'a,1', 'b,2'))
        self.assertEqual(True, chess.check('rook', 'a,1', 'b,1'))
        self.assertEqual(True, chess.check('rook', 'h,1', 'h,2'))
        self.assertEqual(False, chess.check('rook', 'h,1', 'g,2'))
        self.assertEqual(True, chess.check('rook', 'h,1', 'g,1'))
        self.assertEqual(True, chess.check('rook', 'h,8', 'g,8'))
        self.assertEqual(False, chess.check('rook', 'h,8', 'g,7'))
        self.assertEqual(True, chess.check('rook', 'h,8', 'h,7'))
        self.assertEqual(True, chess.check('rook', 'a,8', 'b,8'))
        self.assertEqual(False, chess.check('rook', 'a,8', 'b,7'))
        self.assertEqual(True, chess.check('rook', 'a,8', 'a,7'))

if __name__ == '__main__':
    unittest.main()