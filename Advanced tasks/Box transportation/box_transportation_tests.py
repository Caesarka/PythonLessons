import unittest
import box_transportation

class TestStringMethods(unittest.TestCase):

    def test_box_transportation(self):
        self.assertEqual("Boxes are incomparable", box_transportation.check_it_fit([2, 1, 1], [1, 1, 1]))
        self.assertEqual("Equal", box_transportation.check_it_fit([1, 1, 1], [1, 1, 1]))
        self.assertEqual("matched: box1 to box2", box_transportation.check_it_fit([1, 1, 1], [2, 2, 2]))
        self.assertEqual("Boxes are incomparable", box_transportation.check_it_fit([2, 1, 1], [2, 2, 2]))
        self.assertEqual("Boxes are incomparable", box_transportation.check_it_fit([1, 1, 3], [2, 2, 2]))
        self.assertEqual("matched: box2 to box1", box_transportation.check_it_fit([10, 10, 10], [2, 2, 2]))





if __name__ == '__main__':
    unittest.main()