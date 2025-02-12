import unittest
import tickets

class TestStringMethods(unittest.TestCase):

    def test_tickets(self):
        self.assertEqual([2, 0, 0], tickets.get_tickets(1000, fan_zone_tickets_quantity=100, dance_floor_tickets_quantity=100, parter_tickets_quantity=100))
        self.assertEqual([10, 1, 0], tickets.get_tickets(5800, fan_zone_tickets_quantity=100, dance_floor_tickets_quantity=100, parter_tickets_quantity=10))
        self.assertEqual([10, 5, 0], tickets.get_tickets(9000, fan_zone_tickets_quantity=100, dance_floor_tickets_quantity=100, parter_tickets_quantity=10))
        self.assertEqual([10, 5, 0], tickets.get_tickets(9600, fan_zone_tickets_quantity=100, dance_floor_tickets_quantity=100, parter_tickets_quantity=10))
        self.assertEqual([10, 5, 1], tickets.get_tickets(9650, fan_zone_tickets_quantity=100, dance_floor_tickets_quantity=100, parter_tickets_quantity=10))
        self.assertEqual([10, 5, 1], tickets.get_tickets(9650, fan_zone_tickets_quantity=100, dance_floor_tickets_quantity=100, parter_tickets_quantity=10))
        self.assertEqual([10, 5, 100], tickets.get_tickets(74000, fan_zone_tickets_quantity=100, dance_floor_tickets_quantity=100, parter_tickets_quantity=10))
        self.assertEqual([10, 3, 100], tickets.get_tickets(74000, fan_zone_tickets_quantity=3, dance_floor_tickets_quantity=100, parter_tickets_quantity=10))
        self.assertEqual([10, 3, 102], tickets.get_tickets(74000, fan_zone_tickets_quantity=3, dance_floor_tickets_quantity=150, parter_tickets_quantity=10))
        self.assertEqual([10, 5, 100], tickets.get_tickets(74000, fan_zone_tickets_quantity=30, dance_floor_tickets_quantity=150, parter_tickets_quantity=10))
        self.assertEqual([10, 5, 99], tickets.get_tickets(74000, fan_zone_tickets_quantity=30, dance_floor_tickets_quantity=99, parter_tickets_quantity=10))
        self.assertEqual([0, 0, 0], tickets.get_tickets(300, fan_zone_tickets_quantity=30, dance_floor_tickets_quantity=99, parter_tickets_quantity=10))



