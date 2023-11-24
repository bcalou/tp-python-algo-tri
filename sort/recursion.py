def get_factorial(number: int) -> int:
    """Returns the factorial of a number"""
    return number * get_factorial(number-1) if number > 1 else 1
