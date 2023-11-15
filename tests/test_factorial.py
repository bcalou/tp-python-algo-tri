import unittest

from sort.recursion import get_factorial


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        factorials = {
            1: 1,
            2: 2,
            5: 120,
            10: 3628800,
        }

        for number, factorial in factorials.items():
            result = get_factorial(number)
            self.assertEqual(
                result,
                factorial,
                f"Factorial of {number} is wrong \
                (expected: {factorial}, got: {result})"
            )
