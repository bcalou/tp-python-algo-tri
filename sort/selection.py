"""
Selon moi le tri par selection va regarder toute la liste,
il va selectionner l'element le plus petit et le placer au début de la liste.
Ensuite, il recommence avec le reste de la liste tant qu'elle n'est pas vide.
"""


def sort(array: list[int]) -> list[int]:
    """We sort a list of int by select the minimum number
    each time for build the list"""

    # The first loop can permit us to search the minimum of the list then
    # we sort it and we search again the minimum until we reach end of list
    for increment in range(len(array)):

        # We define the minimum at the increment index
        index_min: int = increment

        # The second loop check all number between the index "increment" and
        # the end of the list. Number before increment index are already sorted
        for number in range(increment, len(array)):

            # We modify index of the minimum if we find a number smaller.
            # Each turn we search the minimum of rest of the list
            # that we weren't sort
            if array[index_min] > array[number]:
                index_min = number

        # We permut the minimum we find with the increment who represent
        # the begin of the list we already search
        array[increment], array[index_min] = array[index_min], array[increment]
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
