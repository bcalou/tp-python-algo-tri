"""
Number generator
"""

import random
import time


def generate_array_of_number(array_size: int) -> list[int]:
    return [random.randint(0, 100) for i in range(array_size)]



start: float = time.time()

# do something
generate_array_of_number(10000000)

end: float = time.time()
print("Temps écoulé :", end - start)
