"""
Number generator
"""
import random
import time as t    

def generate_array_of_number(array_size: int) -> list[int]:
    """Generates an array of random numbers
    """
    start: float = t.time()
    to_ret: list[int] = [random.randint(0, 100) for _ in range(array_size)]
    print("Generated :", t.time()-start, "s")
    return to_ret
