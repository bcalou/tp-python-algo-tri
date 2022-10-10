"""
Insertion sort
"""

import time as t
import sort.rd_list_generator as rg

def main():
    """Main function
    """
    array = rg.generate_array_of_number(200000)

    start: float = t.time()
    sort(array)
    print("Sorted :", t.time()-start, "s")

def sort(array: list[int]) -> list[int]:
    """Sorts an array using the insertion sort algorithm
    """
    for old_index in range(1, len(array)):
        index_to_place = 0
        while array[old_index] > array[index_to_place]:
            index_to_place += 1

        array.insert(index_to_place, array.pop(old_index))

    return array


if __name__ == "__main__":
    main()