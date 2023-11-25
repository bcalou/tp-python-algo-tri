import time
import random


def generate_array_of_number(array_size: int) -> list[int]:
    """Génère une array de taille donnée en paramètre"""
    array = [random.randint(0, 100) for i in range(array_size)]
    return array


def time_to_generate_array(length: int):
    """temps pour générer une array de taille passée en paramètre"""
    start: float = time.time()
    generate_array_of_number(length)
    end: float = time.time()
    print("Taille du tableau = ", length)
    print("Temps écoulé : ", end - start)
