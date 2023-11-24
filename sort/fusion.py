def sort(array: list[int]) -> list[int]:
    # Arrays of size 0/1 are already sorted.
    if len(array) < 2:
        return array

    if len(array) > 2:
        # Split and merge sorted
        middle: int = len(array) // 2 + 1
        return merge(sort(array[:middle]), sort(array[middle:]))
    else:
        # For array of size 2, just swap if needed
        return [array[1], array[0]] if array[1] < array[0] else array


def merge(array_1: list[int], array_2: list[int]):
    final_array: list[int] = []
    index_1: int = 0
    index_2: int = 0
    len_1: int = len(array_1)
    len_2: int = len(array_2)

    for i in range(len_1 + len_2):
        # If either list is empty, that means the other list is the end of
        # the final array
        if index_1 == len_1:
            final_array += array_2[index_2:]
            break
        elif index_2 == len_2:
            final_array += array_1[index_1:]
            break

        # Append the smallest value of either list.
        if array_1[index_1] < array_2[index_2]:
            final_array.append(array_1[index_1])
            index_1 += 1
        else:
            final_array.append(array_2[index_2])
            index_2 += 1

    return final_array
