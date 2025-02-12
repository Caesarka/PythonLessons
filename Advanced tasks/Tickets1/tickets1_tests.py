import unittest
import tickets1

class TestStringMethods(unittest.TestCase):

    def test_tickets(self):
        self.assertEqual([2, 0, 0], tickets1.get_tickets(2, fan_zone_tickets_quantity=0, dance_floor_tickets_quantity=0, parter_tickets_quantity=2))
        self.assertEqual([2, 0, 0], tickets1.get_tickets(2, fan_zone_tickets_quantity=10, dance_floor_tickets_quantity=10, parter_tickets_quantity=2))
        self.assertEqual([10, 0, 0], tickets1.get_tickets(20, fan_zone_tickets_quantity=0, dance_floor_tickets_quantity=0, parter_tickets_quantity=10))
        self.assertEqual([10, 10, 0], tickets1.get_tickets(20, fan_zone_tickets_quantity=11, dance_floor_tickets_quantity=0, parter_tickets_quantity=10))
        self.assertEqual([10, 0, 10], tickets1.get_tickets(20, fan_zone_tickets_quantity=11, dance_floor_tickets_quantity=10, parter_tickets_quantity=10))
        self.assertEqual([10, 9, 11], tickets1.get_tickets(30, fan_zone_tickets_quantity=11, dance_floor_tickets_quantity=11, parter_tickets_quantity=10))
        self.assertEqual([10, 9, 11], tickets1.get_tickets(30, fan_zone_tickets_quantity=11, dance_floor_tickets_quantity=11, parter_tickets_quantity=10))
        self.assertEqual([0, 0, 0], tickets1.get_tickets(0, fan_zone_tickets_quantity=11, dance_floor_tickets_quantity=11, parter_tickets_quantity=10))




