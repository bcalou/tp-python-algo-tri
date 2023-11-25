import time
from sort.range import generate_array_of_number


def sort(array: list[int]) -> list[int]:
    """Tri par sélection"""

    # On parcourt la liste une fois de moins que sa taille
    for iteration in range(len(array) - 1):

        # On affecte la première valeur non triée à la variable smallest_number
        smallest_number = array[iteration]
        index_pop = iteration

        # On parcourt la liste pour trouver la plus petite valeur non triée
        for iteration2 in range(iteration + 1, len(array)):

            if smallest_number > array[iteration2]:

                # Quand on trouve une valeur plus petite,
                # on la stocke dans la variable
                smallest_number = array[iteration2]
                index_pop = iteration2

        # On échange la plus petite valeur trouvée avec
        # l'élément non trié actuel
        array[index_pop], array[iteration] = array[iteration], array[index_pop]

    return array


def time_to_sort_selection(length: int):
    """Temps pour trier un tableau d'une taille donnnée en paramètre avec le
    tri par selection"""
    array = generate_array_of_number(length)
    start: float = time.time()
    sort(array)
    end: float = time.time()
    print("Taille du tableau = ", length)
    print("Temps écoulé : ", end - start)
