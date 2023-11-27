import random


def generate_array(array_size: int) -> list[int]:
    """Génère un tableau de n entiers posififs aléatoires (avec n la
    taille du tableau en para)"""
    return [random.randint(0, 100) for i in range(array_size)]
