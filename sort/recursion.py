def get_factorial(number: int) -> int:
    """factoctorielle"""

    if number <= 1:
        return number
    else:
        return number * get_factorial(number - 1)



print(get_factorial(5))