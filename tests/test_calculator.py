import unittest
import calculator  # import your calculator.py file

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 7), 21)

    def test_divide(self):
        # Normal division
        self.assertEqual(calculator.divide(10, 2), 5)
        # Division by zero should match the exact message from calculator.py
        self.assertEqual(calculator.divide(5, 0), "Error: Division by zero is not allowed.")

if __name__ == "__main__":
    unittest.main()