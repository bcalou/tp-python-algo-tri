def get_factorial(number: int) -> int:
    """Retoune la factorielle de manière recursive"""
    # On test le cas de factotrielle de 0
    if number == 0:
        return 1
    # Sinon on calcule la factorille récursivement
    else:
        return number * get_factorial(number - 1)
