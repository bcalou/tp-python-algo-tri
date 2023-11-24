import random
import time


def generate_array_of_number(n):
    start = time.time()
    array = [random.randint(0, 100) for _ in range(n)]
    end = time.time()
    print(f"Time taken to generate an array of {n} entries: {end - start} seconds")
    return array


for i in range(1, 11):
    generate_array_of_number(i * 1_000_000)