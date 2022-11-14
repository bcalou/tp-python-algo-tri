"""
Fusion sort
"""


def sort(array: list[int]) -> list[int]:
    """Sort the array with fusion sort"""

    # If there are several elements in the array
    if len(array) > 1:

        # Split the array in two smaller parts and use recursion to sort them
        middle_index: int = len(array) // 2
        left_part: list[int] = sort(array[:middle_index])
        right_part: list[int] = sort(array[middle_index:])

        # Merge the two parts to have a final sorted array
        return merge(left_part, right_part)

    # If there is only one element, the array is already sorted, return it
    return array


def merge(left_part: list[int], right_part: list[int]) -> list[int]:
    """Merge two sorted array into a single sorted array"""
    merged_array: list[int] = []

    # Keep track of where we are in both arrays
    left_index = right_index = 0

    # While they're still values to look at in both of the arrays
    while left_index < len(left_part) and right_index < len(right_part):

        # Use value from the left array if it's the smallest
        if left_part[left_index] < right_part[right_index]:
            merged_array.append(left_part[left_index])
            left_index += 1

        # Else, use value from the right array
        else:
            merged_array.append(right_part[right_index])
            right_index += 1

    # Concatenate remaining slices of both arrays
    # One of them is empty, the other contains the remaining values (sorted)
    return merged_array + left_part[left_index:] + right_part[right_index:]
