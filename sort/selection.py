"""
Selection sort
"""

import random

def main():
    """Main function
    """
    array = [random.randint(0, 100) for _ in range(10)]
    print(array)
    print(sort(array))

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