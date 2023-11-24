def sort(array: list[int]) -> list[int]:
    """sort the array using fusion sort"""
    return fusion_sort(array)


def fusion_sort(array: list[int]) -> list[int]:
    # Fusion sort est une fonction récursive, elle s'apelle elle même
    # On commence donc par définir les conditions de fin de cette recursion

    # Si le passé est vide on arrette la récursion
    if array == []:
        return []

    size: int = len(array)

    # Si le tableau est de taille 1, on arrete la récursion
    if size == 1:
        return array

    # La fonction s'appelle elle même deux fois,
    # Une fois pour chaque moitiée du tableau,
    # afin de couper le tableau jusqu'a avoir des morceaux de taille 1
    first_half: list[int] = fusion_sort(array[:size//2])
    second_half: list[int] = fusion_sort(array[size//2:])

    # On fusionne nos deux tableaux
    return fuse_2_array(first_half, second_half)


def fuse_2_array(array1: list[int], array2: list[int]) -> list[int]:
    """Fuse 2 arrays into 1, the result array is sorted"""

    # Le deuxième tableau peut être vide si le tableau original
    # a une taille impaire
    if array2 == []:
        return array1

    # On a un curseur dans chacun des tableaux
    index1: int = 0
    index2: int = 0

    size1: int = len(array1)
    size2: int = len(array2)

    sorted_array: list[int] = []
    while len(sorted_array) < size1 + size2:
        # Si l'un ou l'autre des curseurs a atteinds la fin de son tableau
        # alors on insère les données de l'autre tableau
        if index1 >= size1 and index2 < size2:
            sorted_array.append(array2[index2])
            index2 += 1
            continue
        elif index2 >= size2 and index1 < size1:
            sorted_array.append(array1[index1])
            index1 += 1
            continue

        # Sinon comportement classique, on insère le plus petit des deux
        # nombres en premier
        number1: int = array1[index1]
        number2: int = array2[index2]

        if number1 < number2:
            sorted_array.append(number1)
            index1 += 1
        else:
            sorted_array.append(number2)
            index2 += 1

    # print(f"fuse {array1} and {array2} => {res}")
    return sorted_array
