"""
Selection sort
"""

import time as t
import rd_list_generator as rg

def main():
    """Main function
    """
    array = rg.generate_array_of_number(1000)

    start: float = t.time()
    sort(array)
    print("Sorted :", t.time()-start, "s")

def sort(array: list[int]) -> list[int]:
    """Sorts an array using the selection sort algorithm
    """
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


if __name__ == "__main__":
    main()