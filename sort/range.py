import random


def generate_array_of_number(array_size: int) -> list[int]:
    """ return an array generate number randomly between 1 and 100"""
    return [random.randint(0, 100) for i in range(array_size)]


"""
Résultat :
Le résultat pour 1000000 entrées est 0.4899604320526123
Le résultat pour 2000000 entrées est 0.9306461811065674
Le résultat pour 3000000 entrées est 1.527371883392334
Le résultat pour 4000000 entrées est 1.882685899734497
Le résultat pour 5000000 entrées est 2.3193047046661377
Le résultat pour 6000000 entrées est 3.0640199184417725
Le résultat pour 7000000 entrées est 3.450831651687622
Le résultat pour 8000000 entrées est 3.9937903881073
Le résultat pour 9000000 entrées est 4.156933307647705
Le résultat pour 10000000 entrées est 4.718446493148804
"""
