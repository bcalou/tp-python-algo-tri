import time
from typing import Callable

from sort import selection, insertion, fusion
from sort.range import generate_array_of_number


def measure_time(sort_function: Callable[[list[int]], list[int]], array: list[int]) -> float:
    """
    Measure the time it takes to run a sorting function on an array.

    :param sort_function: The sorting function to be measured.
    :param array: The array to be sorted.
    :return: The time taken to run the sorting function on the array.
    """
    start: float = time.time()
    sort_function(array)
    end: float = time.time()
    return end - start


def main() -> None:
    sizes: list[int] = [1000 * i for i in range(1, 11)]  # 1000, 2000, ..., 10000
    algorithms: list[Callable[[list[int]], list[int]]] = [selection.sort, insertion.sort, fusion.sort, sorted]
    algorithms_names: list[str] = ["Selection", "Insertion", "Fusion", "Python's sorted"]

    # Loop to measure and print the time taken by each sorting algorithm for different array sizes
    for algorithm, name in zip(algorithms, algorithms_names):
        print(f"\nTime measurements for {name} sort:")
        for size in sizes:
            array: list[int] = generate_array_of_number(size)
            elapsed_time: float = measure_time(algorithm, array)
            print(f"Size: {size}, Time: {elapsed_time} seconds")


main()
