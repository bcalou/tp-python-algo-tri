from sort.range import generate_array_of_number
from sort.insertion import sort as insersion_sort
from sort.selection import sort as selection_sort
from sort.fusion import sort as fusion_sort

import time


def main():
    array_list: list[list[int]] = []
    array_size: int = 1000

    for i in range(10):
        array_list.append(generate_array_of_number(array_size))
        array_size += 1000

    for i in range(10):
        start: float = time.time()
        selection_sort(array_list[i])
        end: float = time.time()
        print(f"Time for {len(array_list[i])} (selection):", end - start)

    for i in range(10):
        start: float = time.time()
        insersion_sort(array_list[i])
        end: float = time.time()
        print(f"Time for {len(array_list[i])} (insertion):", end - start)

    for i in range(10):
        start: float = time.time()
        fusion_sort(array_list[i])
        end: float = time.time()
        print(f"Time for {len(array_list[i])} (fusion):", end - start)

    for i in range(10):
        start: float = time.time()
        array_list[i].sort()
        end: float = time.time()
        print(f"Time for {len(array_list[i])} (python sort):", end - start)


main()
