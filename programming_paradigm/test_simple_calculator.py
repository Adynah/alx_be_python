import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    # Test for addition
    def test_addition(self):
        """Test the addition method"""
        self.assertEqual(self.calc.add (2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, 5), 4)

    # Test for substraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
    
    # Test for multiplication
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(4, -3), -12)
        self.assertEqual(self.calc.multiply(-5, -2), 10)
    
    # Test for division
    def test_division(self):
        self.assertEqual(self.calc.divide(12, 2), 6)
        self.assertEqual(self.calc.divide(8, 8), 1)
        self.assertEqual(self.calc.divide(0, 5), 0)
    
    # Test dividion by zero
    def test_division_by_zero(self):
        self.assertEqual(self.calc.divide(4, 0), None)



