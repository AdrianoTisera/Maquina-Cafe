import unittest
from machine import Machine

class TestMachine(unittest.TestCase):
    def test_coffee(self):
        self.assertEqual(Machine().prepare_coffee(3, 1), True)
        self.assertEqual(Machine().prepare_coffee(3, 2), False)
        self.assertEqual(Machine().prepare_coffee(3, 3), False)
    
    def test_d_coffee(self):
        self.assertEqual(Machine().prepare_d_coffee(3, 1), True)
        self.assertEqual(Machine().prepare_d_coffee(3, 2), False)
        self.assertEqual(Machine().prepare_d_coffee(3, 3), False)
    
    def test_coffee_w_milk(self):
        self.assertEqual(Machine().prepare_coffee_w_milk(5, 1), True)
        self.assertEqual(Machine().prepare_coffee_w_milk(3, 2), False)
        self.assertEqual(Machine().prepare_coffee_w_milk(15, 3), True)
    
    def test_d_coffee_w_milk(self):
        self.assertEqual(Machine().prepare_d_coffee_w_milk(7, 1), True)
        self.assertEqual(Machine().prepare_d_coffee_w_milk(3, 2), False)
        self.assertEqual(Machine().prepare_d_coffee_w_milk(15, 2), True)
    
    def test_chocolate(self):
        self.assertEqual(Machine().prepare_chocolate(5, 1), True)
        self.assertEqual(Machine().prepare_chocolate(3, 2), False)
        self.assertEqual(Machine().prepare_chocolate(15, 3), True)
    
    def test_capuccino(self):
        self.assertEqual(Machine().prepare_capuccino(7, 1), True)
        self.assertEqual(Machine().prepare_capuccino(3, 2), False)
        self.assertEqual(Machine().prepare_capuccino(15, 2), True)
    
    def test_tea(self):
        self.assertEqual(Machine().prepare_tea(1, 1), True)
        self.assertEqual(Machine().prepare_tea(3, 2), True)
        self.assertEqual(Machine().prepare_tea(3, 3), True)

if __name__ == '__main__':
    unittest.main()