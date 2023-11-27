def sort(array: list[int]) -> list[int]:
    """Tri par algorithme d'insertion"""
    len_list = len(array)
    for index in range(1, len_list):
        value = array[index]
        start = index - 1

        # Trouver le bon emplacement en déplaçant les éléments plus grands
        while start >= 0 and array[start] > value:
            array[start + 1] = array[start]
            start -= 1

        # Insérer la valeur à la bonne position
        array[start + 1] = value

    return array
