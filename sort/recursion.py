"""
Recursion practice
"""


def get_factorial(number: int) -> int:

    if number == 1:
        return number
    else:
        return number * get_factorial(number - 1)
