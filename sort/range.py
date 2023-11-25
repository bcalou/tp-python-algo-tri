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
    print("Taille du tableau = " , length)
    print("Temps écoulé : ", end - start )
    

# time_to_generate_array(1000000)
# time_to_generate_array(2000000)
# time_to_generate_array(3000000)
# time_to_generate_array(4000000)
# time_to_generate_array(5000000)
# time_to_generate_array(6000000)
# time_to_generate_array(7000000)
# time_to_generate_array(8000000)
# time_to_generate_array(9000000)
# time_to_generate_array(10000000)