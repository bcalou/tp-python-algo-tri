def get_factorial(number: int) -> int:
    """Returns the factorial of the given number."""

    if number == 0:
        return 1
    else:
        return number * get_factorial(number - 1)
