"""
Fusion sort
"""

import time as t
import sort.rd_list_generator as rg

def main():
    """Main function
    """
    array = rg.generate_array_of_number(1000)

    start: float = t.time()
    sort(array)
    print("Sorted :", t.time()-start, "s")

def merge(left: list[int], right: list[int]) -> list[int]:
    """Merges two sorted arrays
    """
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result

def sort(array: list[int]) -> list[int]:
    """Sorts an array using the fusion sort algorithm
    """
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = sort(array[:middle])
    right = sort(array[middle:])

    return merge(left, right)


if __name__ == "__main__":
    main()