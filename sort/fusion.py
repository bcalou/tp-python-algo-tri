def sort(array: list[int]) -> list[int]:
    """Tri par algorithme de fusion"""
    if len(array) <= 1:
        return array

    if len(array) <= 10:
        # Utiliser un tri plus simple pour de petites listes
        return sorted(array)

    mid = len(array) // 2
    left = sort(array[:mid])
    right = sort(array[mid:])
    return merge(left, right)


def merge(array1: list[int], array2: list[int]) -> list[int]:
    """Donne 1 liste triée à partir de 2 listes triées"""
    array: list[int] = []

    # Indices pour les deux listes
    i = j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array.append(array1[i])
            i += 1
        else:
            array.append(array2[j])
            j += 1

    # Ajouter les éléments restants de array1 et array2
    array.extend(array1[i:])
    array.extend(array2[j:])

    return array
