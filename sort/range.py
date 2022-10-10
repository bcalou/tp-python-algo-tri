"""
Number generator
"""

import random
import time
from fusion import sort as fusion_sort

def generate_array_of_number(array_size: int) -> list[int]:
    return [random.randint(0, 100) for i in range(array_size)]


start: float = time.time()
fusion_sort(generate_array_of_number(10000))
end: float = time.time()
print("Temps écoulé :", end - start)