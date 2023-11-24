def get_factorial(number: int) -> int:
    """
    Calculate the factorial of a given number.

    :param number: The number for which the factorial needs to be calculated.
    :return: The factorial of the given number.
    """
    if number == 0:
        return 1
    return number * get_factorial(number - 1)

