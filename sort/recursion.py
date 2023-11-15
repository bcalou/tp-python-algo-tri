def get_factorial(number: int) -> int:
    """Compute the factorial of the given number

    n! = n * (n - 1)!
    Example : 5! = 5 * 4!
    If the number is 5, we need to multiply 5 by 4!
    4! is obtained by recursion : get_factorial(4)
    So get_factorial(5) = 5 * get_factorial(5 - 1)
    """
    return number if number <= 1 else (number * get_factorial(number - 1))
