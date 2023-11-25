import time
from sort.range import generate_array_of_number


def sort(array: list[int]) -> list[int]:
    """Divise le tableau pour le trier plus facilement."""
    if len(array) <= 1:
        return array

    # On cherche le milieu pour séparer le tableau en 2 parties de même taille
    # (ou presque si impair, grâce à la division entière)
    center = len(array) // 2

    # On copie les sous-tableaux
    array_split_1 = array[:center]
    array_split_2 = array[center:]

    # On continue de manière récursive de diviser notre tableau
    sorted_array_1 = sort(array_split_1)
    sorted_array_2 = sort(array_split_2)

    # Puis on renvoie la fusion de nos tableaux triés
    return merge(sorted_array_1, sorted_array_2)


def merge(array1: list[int], array2: list[int]) -> list[int]:
    """Combine des tableaux triés."""
    temp_array = []
    index_1 = 0
    index_2 = 0

    while index_1 < len(array1) and index_2 < len(array2):
        if array1[index_1] < array2[index_2]:
            temp_array.append(array1[index_1])
            index_1 += 1
        else:
            temp_array.append(array2[index_2])
            index_2 += 1

    # Ajoute les éléments restants s'il y en a dans array1
    while index_1 < len(array1):
        temp_array.append(array1[index_1])
        index_1 += 1

    # Ajoute les éléments restants s'il y en a dans array2
    while index_2 < len(array2):
        temp_array.append(array2[index_2])
        index_2 += 1

    # Crée un nouvel array pour stocker le résultat fusionné
    merged_array = [0] * (len(array1) + len(array2))

    # Copie les éléments de temp_array dans merged_array
    # ( pylint m'a consillé cette syntaxe elle est pas mal je connaissais pas )
    for i, value in enumerate(temp_array):
        merged_array[i] = value

    return merged_array


def time_to_sort_fusion(length: int):
    """Temps pour trier un tableau d'une taille donnée en paramètre avec le
    tri par insertion."""
    array = generate_array_of_number(length)
    start_time = time.time()
    sort(array)
    end_time = time.time()
    print("Taille du tableau =", length)
    print("Temps écoulé :", end_time - start_time)
