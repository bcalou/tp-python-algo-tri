import random
import time


def generate_array_of_number(array_size: int) -> list[int]:
    """Description"""
    array = [random.randint(0, 100) for i in range(array_size)]
    return array

start: float = time.time()
generate_array_of_number(10)
end: float = time.time()
print("Temps écoulé :", end - start)