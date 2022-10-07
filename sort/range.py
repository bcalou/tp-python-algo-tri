"""
Number generator
"""

import random
import time


def generate_array_of_number(array_size: int) -> list[int]:
    """Generate an array of random numbers between 0 and 100"""
    # Start the timer
    start: float = time.time()

    # Generate a big array of random numbers
    array = [random.randint(0, 100) for i in range(array_size)]

    # Stop the timer
    end: float = time.time()

    # Show the ellapsed time
    print(f"Temps écoulé : {end - start}s")

    return array
