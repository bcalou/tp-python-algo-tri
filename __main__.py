from sort.range import generate_array_of_number
from sort.insertion import sort as insertion_sort
from sort.selection import sort as selection_sort
from sort.fusion import sort as fusion_sort
from sort.recursion import get_factorial
import time


def main():
    for sample_size in range(0, 10_000_000, 1_000_000):
        start: float = time.time()
        sample: list[int] = generate_array_of_number(sample_size)
        end: float = time.time()
        print(f"Génération de {sample_size} nombres aléatoires en \
              {end-start:.2f}s")

    for sample_size in range(1_000, 11_000, 1_000):
        sample: list[int] = generate_array_of_number(sample_size)
        start: float = time.time()
        sorted_sample: list[int] = selection_sort(sample)
        end: float = time.time()
        print(f"Tri par selection: taille tableau={sample_size}, \
              temps={end-start}s")

    for sample_size in range(1_000, 11_000, 1_000):
        sample: list[int] = generate_array_of_number(sample_size)
        start: float = time.time()
        sorted_sample: list[int] = insertion_sort(sample)
        end: float = time.time()
        print(f"Tri par insertion: taille tableau={sample_size}, \
              temps={end-start}s")

    # print(get_factorial(5))

    for sample_size in range(1_000, 11_000, 1_000):
        sample: list[int] = generate_array_of_number(sample_size)
        start: float = time.time()
        sorted_sample: list[int] = fusion_sort(sample)
        end: float = time.time()
        print(f"Tri par fusion: taille tableau={sample_size}, \
              temps={end-start}s")

    for sample_size in range(100_000, 1_100_000, 100_000):
        sample: list[int] = generate_array_of_number(sample_size)
        start: float = time.time()
        sample.sort()
        end: float = time.time()
        print(f"Tri Python: taille tableau={sample_size}, \
              temps={end-start}s")


main()
