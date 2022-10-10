"""
Insertion sort
"""

import random

def main():
    """Main function
    """
    array = [random.randint(0, 100) for _ in range(10)]
    print(array)
    print(sort(array))

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