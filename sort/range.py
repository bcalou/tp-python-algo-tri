import time
import random

def generate_array_of_number(array_size: int) -> list[int]:
    start: float = time.time()
    array = [random.randint(0, 100) for i in range(array_size)]
    end: float = time.time()
    print("Taille du tableau = " , array_size)
    print("Temps écoulé : ", end - start )
    return []

generate_array_of_number(1000000)
generate_array_of_number(2000000)
generate_array_of_number(3000000)
generate_array_of_number(4000000)
generate_array_of_number(5000000)
generate_array_of_number(6000000)
generate_array_of_number(7000000)
generate_array_of_number(8000000)
generate_array_of_number(9000000)
generate_array_of_number(10000000)