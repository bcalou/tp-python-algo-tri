def get_factorial(number: int) -> int:
    """factoctorielle"""
    return number if number <= 1 else number * get_factorial(number - 1)
