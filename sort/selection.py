"""
Selon moi le tri par selection va regarder toute la liste,
il va selectionner l'element le plus petit et le placer au début de la liste.
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
Le résultat pour 1000 entrées est 0.027270793914794922
Le résultat pour 2000 entrées est 0.10175871849060059
Le résultat pour 3000 entrées est 0.2276897430419922
Le résultat pour 4000 entrées est 0.41335439682006836
Le résultat pour 5000 entrées est 0.7159967422485352
Le résultat pour 6000 entrées est 0.9541590213775635
Le résultat pour 7000 entrées est 1.2389578819274902
Le résultat pour 8000 entrées est 1.6056084632873535
Le résultat pour 9000 entrées est 2.092197895050049
Le résultat pour 10000 entrées est 2.540802001953125

Le tri par selection est de complexité O(N**2)
Car entre la première et la dernière valeur les entrées sont multiplé par 10
alors que les temps sont multipliés par 100.
De plus on a directement une double boucle dans le programme
qui regarde tout les éléments, ce qui fait N*N donc N**2
"""
