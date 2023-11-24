def sort(array: list[int]) -> list[int]:
    """Tri par algorithme de sélection"""
    len_list = len(array)

    for index in range(len_list - 1):
        min_index = index

        for j in range(index + 1, len_list):
            if array[j] < array[min_index]:
                min_index = j

        # échanger les valeurs seulement si nécessaire
        if min_index != index:
            array[index], array[min_index] = array[min_index], array[index]

    return array

print(sort([1, 2, 3, 4, 6, 9, 5, 7, 9, 1, 2, 0]))
