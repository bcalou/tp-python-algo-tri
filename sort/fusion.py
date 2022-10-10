"""
Fusion sort
"""

import random

def main():
    """Main function
    """
    array = [random.randint(0, 100) for _ in range(10)]
    print(array)
    print(sort(array))

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