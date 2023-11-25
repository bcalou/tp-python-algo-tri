def get_factorial(number: int, max: int = 100) -> int:
    '''
        Return the factorial of the number
    '''

    if (max == 0):
        return 0

    if number == 1:
        return number
    else:
        return number * get_factorial(number - 1, max - 1)
