"""
Selon moi, Le tri par insertion va regarder chaque élément de la liste,
les uns après les autres. A chaque fois, l'élément sera inséré
entre deux autres éléments dans la liste déja trié,
à la fin ou au début de la liste. On décalera tous les éléments triés
après la nouvelle position, de cette nouvelle position
vers l'ancienne position de l'élément
"""


def sort(array: list[int]) -> list[int]:
    """we sort a list of int by insert each number at their position"""

    # The first loop represent element who search to sort
    # and who will be insert between other number
    for increment in range(len(array)):

        # The secund loop go from the element who want to sort
        # to the begin of the list
        for number in range(increment, -1, -1):

            # if the element size is between two element or
            # if we reach the top of the list we insert it on list
            if (array[increment] < array[number]
                and (array[increment] >= array[number-1]
                     or number == 0)):

                # We remove the element at increment
                # position and we insert it at number position
                array.insert(number, array.pop(increment))
    return array


"""
Résultat :
Le résultat pour 1000 entrées est 0.028821706771850586
Le résultat pour 2000 entrées est 0.16448330879211426
Le résultat pour 3000 entrées est 0.3654301166534424
Le résultat pour 4000 entrées est 0.691014289855957
Le résultat pour 5000 entrées est 1.0119526386260986
Le résultat pour 6000 entrées est 1.4506659507751465
Le résultat pour 7000 entrées est 2.0582830905914307
Le résultat pour 8000 entrées est 2.850092887878418
Le résultat pour 9000 entrées est 3.4401211738586426
Le résultat pour 10000 entrées est 4.12743878364563

Le tri par insertion est de complexité O(N**2)
Car entre la première et la dernière valeur les entrées sont multiplé par 10
alors que les temps sont multipliés par 100.
De plus on a directement une double boucle dans le programme
qui regarde tout les éléments, ce qui fait N*N donc N**2
"""
