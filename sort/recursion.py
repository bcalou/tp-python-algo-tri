"""
Recursion practice
"""


def get_factorial(number: int) -> int:
    return 1 if number == 0 else number * get_factorial(number - 1)
