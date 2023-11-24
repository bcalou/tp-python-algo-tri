def get_factorial(number: int) -> int:
    """
    Gets the factorial of a number.

    :param number:
    :return: factorial of a number
    """
    if number == 0:
        return 1
    else:
        return number * get_factorial(number - 1)
