def get_factorial(number: int) -> int:
    """ return the factorial of the number"""
    return number * get_factorial(number - 1) if number >= 1 else 1


"""
Résultat :
Le résultat pour 10 entrées est 0.0
Le résultat pour 20 entrées est 0.0
Le résultat pour 30 entrées est 0.0
Le résultat pour 40 entrées est 0.0
Le résultat pour 50 entrées est 0.0
Le résultat pour 60 entrées est 0.0
Le résultat pour 70 entrées est 0.0
Le résultat pour 80 entrées est 0.0
Le résultat pour 90 entrées est 0.0
Le résultat pour 100 entrées est 0.0
"""
