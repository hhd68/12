#!/usr/bin/env python3
"""
Tests for Problem 12 solution
"""

import unittest
from solution import count_divisors, find_triangle_number_with_divisors


class TestProblem12(unittest.TestCase):
    """Test cases for Problem 12 solution"""
    
    def test_count_divisors(self):
        """Test the count_divisors function with known values"""
        self.assertEqual(count_divisors(1), 1)   # 1
        self.assertEqual(count_divisors(3), 2)   # 1, 3
        self.assertEqual(count_divisors(6), 4)   # 1, 2, 3, 6
        self.assertEqual(count_divisors(10), 4)  # 1, 2, 5, 10
        self.assertEqual(count_divisors(15), 4)  # 1, 3, 5, 15
        self.assertEqual(count_divisors(21), 4)  # 1, 3, 7, 21
        self.assertEqual(count_divisors(28), 6)  # 1, 2, 4, 7, 14, 28
    
    def test_triangle_number_with_5_divisors(self):
        """Test finding the first triangle number with over 5 divisors"""
        result = find_triangle_number_with_divisors(5)
        self.assertEqual(result, 28)
        self.assertGreater(count_divisors(result), 5)
    
    def test_triangle_number_with_500_divisors(self):
        """Test finding the first triangle number with over 500 divisors"""
        result = find_triangle_number_with_divisors(500)
        self.assertEqual(result, 76576500)
        self.assertGreater(count_divisors(result), 500)


if __name__ == "__main__":
    unittest.main()
