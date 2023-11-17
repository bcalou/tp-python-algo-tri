def get_factorial(number: int) -> int:
    if number > 1:
        return number * get_factorial(number - 1)
    else:
        return 1
