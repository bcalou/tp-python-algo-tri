def sort(array: list[int]) -> list[int]:
    return fusion_sort(array)


def fusion_sort(array: list[int]) -> list[int]:
    if array == []:
        return []

    size: int = len(array)
    if size == 1:
        return array

    first_half: list[int] = fusion_sort(array[:size//2])
    second_half: list[int] = fusion_sort(array[size//2:])

    return fuse_2_array(first_half, second_half)


def fuse_2_array(array1: list[int], array2: list[int]) -> list[int]:
    if array2 == []:
        return array1

    index1: int = 0
    index2: int = 0

    size1: int = len(array1)
    size2: int = len(array2)

    res: list[int] = []
    while len(res) < size1 + size2:
        if index1 >= size1 and index2 < size2:
            res.append(array2[index2])
            index2 += 1
            continue
        elif index2 >= size2 and index1 < size1:
            res.append(array1[index1])
            index1 += 1
            continue

        number1: int = array1[index1]
        number2: int = array2[index2]

        if number1 < number2:
            res.append(number1)
            index1 += 1
        else:
            res.append(number2)
            index2 += 1

    # print(f"fuse {array1} and {array2} => {res}")
    return res
