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

    def test_rook_corner(self):
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

    def test_bishop_d4_good(self):
        self.assertEqual(True, chess.check('bishop', 'd,4', 'a,1'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'b,2'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'c,3'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'e,5'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'f,6'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'g,7'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'h,8'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'a,7'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'b,6'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'c,5'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'e,3'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'f,2'))
        self.assertEqual(True, chess.check('bishop', 'd,4', 'g,1'))

    def test_bishop_d4_bad(self):
        self.assertEqual(False, chess.check('bishop', 'd,4', 'd,4'))
        self.assertEqual(False, chess.check('bishop', 'd,4', 'e,4'))
        self.assertEqual(False, chess.check('bishop', 'd,4', 'c,4'))
        self.assertEqual(False, chess.check('bishop', 'd,4', 'd,5'))
        self.assertEqual(False, chess.check('bishop', 'd,4', 'd,3'))
        self.assertEqual(False, chess.check('bishop', 'd,4', 'f,3'))
        self.assertEqual(False, chess.check('bishop', 'd,4', 'b,3'))
        self.assertEqual(False, chess.check('bishop', 'd,4', 'b,5'))
        self.assertEqual(False, chess.check('bishop', 'd,4', 'f,5'))

    def test_bishop_corner(self):
        self.assertEqual(True, chess.check('bishop', 'a,1', 'b,2'))
        self.assertEqual(False, chess.check('bishop', 'a,1', 'a,2'))
        self.assertEqual(False, chess.check('bishop', 'a,1', 'b,1'))
        self.assertEqual(True, chess.check('bishop', 'h,1', 'g,2'))
        self.assertEqual(False, chess.check('bishop', 'h,1', 'h,2'))
        self.assertEqual(False, chess.check('bishop', 'h,1', 'g,1'))
        self.assertEqual(True, chess.check('bishop', 'h,8', 'g,7'))
        self.assertEqual(False, chess.check('bishop', 'h,8', 'g,8'))
        self.assertEqual(False, chess.check('bishop', 'h,8', 'h,7'))
        self.assertEqual(True, chess.check('bishop', 'a,8', 'b,7'))
        self.assertEqual(False, chess.check('bishop', 'a,8', 'a,7'))
        self.assertEqual(False, chess.check('bishop', 'a,8', 'b,8'))



    def test_queen_d4_good(self):
        self.assertEqual(True, chess.check('queen', 'd,4', 'e,3'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'f,2'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'g,1'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'c,5'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'b,6'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'a,7'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'a,1'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'b,2'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'c,3'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'e,5'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'f,6'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'g,7'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'h,8'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'a,1'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'b,2'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'c,3'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'e,5'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'f,6'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'g,7'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'h,8'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'a,7'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'b,6'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'c,5'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'e,3'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'f,2'))
        self.assertEqual(True, chess.check('queen', 'd,4', 'g,1'))

    def test_queen_d4_bad(self):
        self.assertEqual(False, chess.check('queen', 'd,4', 'f,3'))
        self.assertEqual(False, chess.check('queen', 'd,4', 'f,5'))
        self.assertEqual(False, chess.check('queen', 'd,4', 'b,3'))
        self.assertEqual(False, chess.check('queen', 'd,4', 'b,5'))
        self.assertEqual(False, chess.check('queen', 'd,4', 'c,6'))
        self.assertEqual(False, chess.check('queen', 'd,4', 'e,6'))
        self.assertEqual(False, chess.check('queen', 'd,4', 'c,2'))
        self.assertEqual(False, chess.check('queen', 'd,4', 'e,2'))
        self.assertEqual(False, chess.check('queen', 'd,4', 'b,1'))
        self.assertEqual(False, chess.check('queen', 'd,4', 'f,1'))
        self.assertEqual(False, chess.check('queen', 'd,4', 'b,7'))
        self.assertEqual(False, chess.check('queen', 'd,4', 'f,7'))

    def test_queen_corner(self):
        self.assertEqual(True, chess.check('queen', 'a,1', 'a,2'))
        self.assertEqual(True, chess.check('queen', 'a,1', 'b,2'))
        self.assertEqual(True, chess.check('queen', 'a,1', 'b,1'))
        self.assertEqual(True, chess.check('queen', 'h,1', 'h,2'))
        self.assertEqual(True, chess.check('queen', 'h,1', 'g,2'))
        self.assertEqual(True, chess.check('queen', 'h,1', 'g,1'))
        self.assertEqual(True, chess.check('queen', 'h,8', 'g,8'))
        self.assertEqual(True, chess.check('queen', 'h,8', 'g,7'))
        self.assertEqual(True, chess.check('queen', 'h,8', 'h,7'))
        self.assertEqual(True, chess.check('queen', 'a,8', 'b,8'))
        self.assertEqual(True, chess.check('queen', 'a,8', 'b,7'))
        self.assertEqual(True, chess.check('queen', 'a,8', 'a,7'))

    def test_pawn_good(self):
        self.assertEqual(True, chess.check('pawn', 'e,2', 'e,3'))
        self.assertEqual(True, chess.check('pawn', 'e,2', 'e,4'))
        self.assertEqual(True, chess.check('pawn', 'e,3', 'e,4'))
        self.assertEqual(True, chess.check('pawn', 'e,7', 'e,8'))

    def test_pawn_bad(self):
        self.assertEqual(False, chess.check('pawn', 'e,2', 'e,5'))
        self.assertEqual(False, chess.check('pawn', 'e,3', 'e,5'))
        self.assertEqual(False, chess.check('pawn', 'e,3', 'f,4'))
        self.assertEqual(False, chess.check('pawn', 'e,7', 'h,7'))

    def test_pawn_corner(self):
        self.assertEqual(False, chess.check('pawn', 'a,2', 'a,1'))
        self.assertEqual(False, chess.check('pawn', 'a,2', 'b,2'))
        self.assertEqual(True, chess.check('pawn', 'a,2', 'a,3'))
        self.assertEqual(False, chess.check('pawn', 'a,8', 'a,8'))

    def test_knight_e4_good(self):
        self.assertEqual(True, chess.check('knight', 'e,4', 'g,3'))
        self.assertEqual(True, chess.check('knight', 'e,4', 'g,5'))
        self.assertEqual(True, chess.check('knight', 'e,4', 'c,3'))
        self.assertEqual(True, chess.check('knight', 'e,4', 'c,5'))
        self.assertEqual(True, chess.check('knight', 'e,4', 'f,6'))
        self.assertEqual(True, chess.check('knight', 'e,4', 'd,6'))
        self.assertEqual(True, chess.check('knight', 'e,4', 'f,2'))
        self.assertEqual(True, chess.check('knight', 'e,4', 'd,2'))

    def test_knight_e4_bad(self):
        self.assertEqual(False, chess.check('knight', 'e,4', 'f,3'))
        self.assertEqual(False, chess.check('knight', 'e,4', 'e,2'))
        self.assertEqual(False, chess.check('knight', 'e,4', 'e,5'))
        self.assertEqual(False, chess.check('knight', 'e,4', 'f,5'))

    def test_knight_e2_corner(self):
        self.assertEqual(True, chess.check('knight', 'a,1', 'b,3'))
        self.assertEqual(True, chess.check('knight', 'a,1', 'c,2'))
        self.assertEqual(False, chess.check('knight', 'a,1', 'd,2'))


if __name__ == '__main__':
    unittest.main()