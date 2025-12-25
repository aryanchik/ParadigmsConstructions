
import unittest
from refactored_program import calculate_sum, calculate_product

class TestMathOperations(unittest.TestCase):

    def test_sum_positive(self):
        self.assertEqual(calculate_sum(5, 3), 8)

    def test_sum_negative(self):
        self.assertEqual(calculate_sum(-5, -3), -8)

    def test_product_positive(self):
        self.assertEqual(calculate_product(4, 7), 28)

    def test_product_with_zero(self):
        self.assertEqual(calculate_product(5, 0), 0)

    def test_product_negative(self):
        self.assertEqual(calculate_product(-4, 5), -20)

if __name__ == "__main__":
    unittest.main()
