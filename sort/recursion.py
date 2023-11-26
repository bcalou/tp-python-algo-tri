def get_factorial(number: int) -> int:
    """
    Gets the factorial of a number.

    :param number:
    :return: factorial of a number
    """
    return 1 if number == 0 else number * get_factorial(number - 1)
