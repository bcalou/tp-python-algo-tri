from typing import Callable

from sort.fusion import sort as fusion_sort
from sort.insertion import sort as insertion_sort
from sort.range import generate_array_of_number
from sort.selection import sort as selection_sort
from timer import Timer

benchmark_array: list[int] = []
NUMBER_OF_ELEMENT_PER_PASSES = 2000
NUMBER_OF_PASSES: int = 10


def benchmark_random_array_generation():
    print("Génération d'array random--------------------------------------------")
    for i in range(1, 11):
        number_of_elements = i * 1_000_000
        timer: Timer = Timer(
            f"Génération d'un tableau de {number_of_elements} éléments")
        generate_array_of_number(number_of_elements)


def benchmark_sorting_algorithms():

    # Setup benchmark array
    global benchmark_array
    benchmark_array = generate_array_of_number(NUMBER_OF_ELEMENT_PER_PASSES)

    print("Tri par insertion--------------------------------------------")
    benchmark_custom_algorithms(
        "insertion", insertion_sort, NUMBER_OF_PASSES)
    print("Tri par séléction--------------------------------------------")
    benchmark_custom_algorithms(
        "séléction", selection_sort, NUMBER_OF_PASSES)

    print("Tri par fusion--------------------------------------------")
    benchmark_custom_algorithms("fusion", fusion_sort, NUMBER_OF_PASSES)

    print("Tri natif--------------------------------------------")
    benchmark_natif_sort(NUMBER_OF_PASSES)


def benchmark_custom_algorithms(algorithm_name: str, sort_function: Callable, number_of_millions: int = 10) -> int:
    """Do multiple pass of sorting a "random" array using the provided sort algorithm and mesure the execution time"""
    for i in range(1, number_of_millions + 1):
        current_array = regenerate_benchmark_array(i)
        timer: Timer = Timer(
            algorithm_name +
            f" avec une liste de {len(current_array)} éléments")
        sort_function(current_array)


def benchmark_natif_sort(number_of_millions: int = 10):
    """Do multiple pass of sorting a "random" array using the native python sort algorithm and mesure the execution time"""
    for i in range(1, number_of_millions + 1):
        current_array = regenerate_benchmark_array(i)
        timer: Timer = Timer(
            f"sort() avec une liste de {len(current_array)} éléments")
        current_array.sort()


def regenerate_benchmark_array(number_of_millions: int) -> list[int]:
    new_benchmark_array = []
    for i in range(number_of_millions):
        new_benchmark_array += benchmark_array
    return new_benchmark_array


# benchmark_random_array_generation()
benchmark_sorting_algorithms()
