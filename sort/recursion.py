def get_factorial(number: int) -> int:
    """Get the factorial of a number using recursion"""
    return get_factorial(number-1) * number if number > 1 else 1
