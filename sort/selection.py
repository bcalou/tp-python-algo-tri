"""
Selon moi le tri par selection va regarder toute la liste,
il va selectionner l'element le plus petitet le pla cer au début de la liste.
Ensuite, il recommence avec le reste de la liste tant qu'elle n'est pas vide.
"""


def sort(array: list[int]) -> list[int]:
    """We make two loop. if an element is smaller than "index_min_number",
      we change "index_min_number" we permut first element with element
      at this index. We do it again for second element of the list
      until end of the list """

    for increment in range(len(array)):
        index_min_number: int = increment
        for implementation in range(increment, len(array)):
            if array[index_min_number] > array[implementation]:
                index_min_number = implementation
        temp: int = array[increment]
        array[increment] = array[index_min_number]
        array[index_min_number] = temp
    return array


"""
Résultat :
Le résultat pour 1000000 entrées est 0.45252156257629395
Le résultat pour 2000000 entrées est 0.9531290531158447
Le résultat pour 3000000 entrées est 1.4106464385986328
Le résultat pour 4000000 entrées est 1.9002070426940918
Le résultat pour 5000000 entrées est 2.3450512886047363
Le résultat pour 6000000 entrées est 2.733344554901123
Le résultat pour 7000000 entrées est 3.4658050537109375
Le résultat pour 8000000 entrées est 4.107401609420776
Le résultat pour 9000000 entrées est 4.056782007217407
Le résultat pour 10000000 entrées est 4.458217620849609
"""
