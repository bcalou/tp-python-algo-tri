from sort.range import generate_array_of_number
from sort.selection import sort
import time


def main():
    for sample_size in range(1000, 11_000, 1000):
        sample: list[int] = generate_array_of_number(sample_size)
        start: float = time.time()
        sorted_sample: list[int] = sort(sample)
        end: float = time.time()
        print(f"Trie par insertion: taille tableau={sample_size}, \
              temps={end-start}s")


main()
