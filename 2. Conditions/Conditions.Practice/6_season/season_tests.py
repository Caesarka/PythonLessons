import unittest
import season

class TestStringMethod(unittest.TestCase):
    def test_season_good(self):
        self.assertEqual('Fall', season.findSeasonByDayOfYear('12, 20'))
        self.assertEqual('Winter', season.findSeasonByDayOfYear('12, 21'))
        self.assertEqual('Winter', season.findSeasonByDayOfYear('12, 31'))
        self.assertEqual('Winter', season.findSeasonByDayOfYear('1, 1'))
        self.assertEqual('Winter', season.findSeasonByDayOfYear('3, 19'))
        self.assertEqual('Spring', season.findSeasonByDayOfYear('3, 20'))
        self.assertEqual('Spring', season.findSeasonByDayOfYear('6, 20'))
        self.assertEqual('Summer', season.findSeasonByDayOfYear('6, 21'))
        self.assertEqual('Summer', season.findSeasonByDayOfYear('9, 21'))
        self.assertEqual('Fall', season.findSeasonByDayOfYear('9, 22'))


if __name__ == '__main__':
    unittest.main()