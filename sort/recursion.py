def get_factorial(number: int) -> int:
    """Get the factorial of a number using recursion"""

    if number != 1:
        number = number * get_factorial(number - 1)

    return number
