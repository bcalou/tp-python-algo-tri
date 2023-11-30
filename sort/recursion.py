def get_factorial(number: int) -> int:
    """Get the factorial of a number using recursion"""

    return number * get_factorial(number - 1) if number > 1 else 1
