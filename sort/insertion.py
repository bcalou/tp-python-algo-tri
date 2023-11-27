def sort(array: list[int]) -> list[int]:
    """Tri par algorithme d'insersion"""
    len_list = len(array)
    for index in range(1, len_list):
        value = array[index]
        j = index - 1
        while j >= 0 and array[j] > value:
            array[j + 1], array[j] = array[j], value
            j -= 1
    return array
