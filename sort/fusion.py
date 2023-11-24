def sort(array: list[int]) -> list[int]:
    """Tri par algorithme de fusion"""
    if len(array) <= 1:
        print(array)
        return array
    else:
        print(array)
        array1: list[int] = array[0 : len(array) // 2]
        sort(array1)
        array2: list[int] = array[len(array) // 2: len(array)]
        sort(array2)
        return merge(array1, array2)


def merge(array1: list[int], array2: list[int]) -> list[int]:
    """Donne 1 liste triée à partir de 2 listes triées"""
    array: list[int] = []

    while len(array1) > 1 or len(array2) > 1:
        print("merging arrays", array1, array2)
        if array1[0] < array2[0]:
            array.append(array1[0])
            array1.pop(0)
        else:
            array.append(array2[0])
            array2.pop(0)

    return array + array1 + array2

merge([1, 2, 5], [3, 4, 6])
#print(sort([1, 2, 5, 6, 3, 4, 7, 8, 9]))