import random


def generate_array_of_number(array_size: int) -> list[int]:
    """ return an array generate number randomly between 1 and 100"""
    return [random.randint(0, 100) for i in range(array_size)]


"""
Résultat :
Le résultat pour 1000000 entrées est 0.49683332443237305
Le résultat pour 2000000 entrées est 0.9791500568389893
Le résultat pour 3000000 entrées est 1.5108468532562256
Le résultat pour 4000000 entrées est 1.8603689670562744
Le résultat pour 5000000 entrées est 2.314495086669922
Le résultat pour 6000000 entrées est 2.7060232162475586
Le résultat pour 7000000 entrées est 3.1330814361572266
Le résultat pour 8000000 entrées est 3.629992723464966
Le résultat pour 9000000 entrées est 4.128807783126831
Le résultat pour 10000000 entrées est 4.500385284423828
"""
