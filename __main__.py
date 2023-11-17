from sort.range import generate_array_of_number
from sort.selection import sort
import time


def main():
    for sample_size in range(1_000, 35_000, 5_000):
        sample: list[int] = generate_array_of_number(sample_size)
        start: float = time.time()
        sorted_sample: list[int] = sort(sample)
        end: float = time.time()
        print(f"Trie par insertion: taille tableau={sample_size}, \
              temps={end-start}s")


main()
