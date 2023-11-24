"""
Selon moi, Le tri par insertion va regarder le deuxieme element de la liste
et le placer avant ou après le premier si il est plus petit ou non. Puis faire
pareil avec les autres éléments en les comparant avec tous ceux avant
"""


def sort(array: list[int]) -> list[int]:
    """We make two loop,
    then compare one element of the second loop with element before,
    if it is smaller we permute those two elements we continue compare
    with the element before until we reach the top of the list
    or we find an element smaller. We do this the length of the list.
    So We insert one element between other"""
    for increment in range(len(array)):
        for implementation in range(increment):
            if array[increment] < array[implementation]:
                temp: int = array[implementation]
                array[implementation] = array[increment]
                array[increment] = temp
    return array


"""
Résultat :
Le résultat pour 1000 entrées est 0.017726898193359375
Le résultat pour 2000 entrées est 0.11009573936462402
Le résultat pour 3000 entrées est 0.21297407150268555
Le résultat pour 4000 entrées est 0.38732194900512695
Le résultat pour 5000 entrées est 0.6125597953796387
Le résultat pour 6000 entrées est 0.9321205615997314
Le résultat pour 7000 entrées est 1.2588913440704346
Le résultat pour 8000 entrées est 1.573819637298584
Le résultat pour 9000 entrées est 2.006103038787842
Le résultat pour 10000 entrées est 2.4676148891448975

Le tri par insertion est de complexité O(N**2)
Car entre la première et la dernière valeur les entrées sont multiplé par 10
alors que les temps sont multipliés par 100.
De plus on a directement une double boucle dans le programme
qui regarde tout les éléments, ce qui fait N*N donc N**2
"""
