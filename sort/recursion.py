"""
Recursion practice
"""


def get_factorial(number: int) -> int:
    return number * get_factorial(number - 1) if number > 1 else 1
