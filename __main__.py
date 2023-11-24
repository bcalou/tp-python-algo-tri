from sort.range import generate_array_of_number
from sort.insertion import sort as insertion_sort
from sort.selection import sort as selection_sort
from sort.fusion import sort as fusion_sort
import time


def main():
    for sample_size in range(0, 10_000_000, 1_000_000):
        sample: list[int] = generate_array_of_number(sample_size)

    for sample_size in range(1_000, 11_000, 1_000):
        sample: list[int] = generate_array_of_number(sample_size)
        start: float = time.time()
        sorted_sample: list[int] = selection_sort(sample)
        end: float = time.time()
        print(f"Trie par selection: taille tableau={sample_size}, \
              temps={end-start}s")

    for sample_size in range(1_000, 10_000, 1_000):
        sample: list[int] = generate_array_of_number(sample_size)
        start: float = time.time()
        sorted_sample: list[int] = insertion_sort(sample)
        end: float = time.time()
        print(f"Trie par insertion: taille tableau={sample_size}, \
              temps={end-start}s")




main()
