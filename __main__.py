import random
import time

from sort import selection, insertion, fusion


def generate_array_of_number(n):
    return [random.randint(0, 100) for _ in range(n)]


def measure_time(sort_function, array):
    start = time.time()
    sort_function(array)
    end = time.time()
    return end - start


def main():
    sizes = [1000 * i for i in range(1, 11)]  # 1000, 2000, ..., 10000
    algorithms = [selection.sort, insertion.sort, fusion.sort, sorted]
    algorithms_names = ["Selection", "Insertion", "Fusion", "Python's sorted"]

    for algorithm, name in zip(algorithms, algorithms_names):
        print(f"\nTime measurements for {name} sort:")
        for size in sizes:
            array = generate_array_of_number(size)
            elapsed_time = measure_time(algorithm, array)
            print(f"Size: {size}, Time: {elapsed_time} seconds")


main()
