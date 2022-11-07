"""
Recursion practice
"""


def get_factorial(number: int) -> int:
    """Returns the factorial of a number"""
    if number == 1:
        return 1
    else:
        return number * get_factorial(number - 1)
