import unittest
from LAB6_1 import sum_of_elements

a = [-1, 48, 50, 14, -5, -7, -6, 45, 30, -2, -2, -28, 15, -26, -33, -15, 10, -35, -16, 46, 46, -14]


class TestSum(unittest.TestCase):
    def test_sum_of_elements(self):
        self.assertEqual(sum_of_elements(a), -36)  # add assertion here


if __name__ == '__main__':
    unittest.main()
