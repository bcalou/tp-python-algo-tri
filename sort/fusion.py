"""
Le tri fusion prend un tableau.
Si le tableau n'est pas vide ou n'est pas composé d'un seul élément,
Python vas le divisé en deux en rappelant la meme fonction puis le merger.
A chaque fois avant de merger les différents tableaux vont se réduire,
jusqu'à ce que chaque tableau n'ait qu'un élément.
Ensuite les tableaux vont se merger petit à petit en restant croissant et
en formant au final un seul tableau
"""


def sort(array: list[int]) -> list[int]:
    """if length of array <=1 return array,
    else return the merge of the left part and the right part of the array"""
    if len(array) <= 1:
        return array
    return merge(sort(array[:len(array) // 2]), sort(array[len(array) // 2:]))


def merge(array_gauche: list[int], array_droite: list[int]) -> list[int]:
    """merge take two array and create one new array we both of them,
    at every loop it takes the smallest number between two arrays
    and remove from the array. Then we return new array created"""
    new_array: list[int] = []
    while (True):
        if (array_gauche == []):
            new_array += array_droite
            return new_array
        elif (array_droite == []):
            new_array += array_gauche
            return new_array
        if array_droite[0] < array_gauche[0]:
            new_array.append(array_droite.pop(0))
        else:
            new_array.append(array_gauche.pop(0))


"""
Résultat :
Le résultat pour 10000 entrées est 0.14179372787475586
Le résultat pour 20000 entrées est 0.11987948417663574
Le résultat pour 30000 entrées est 0.18050265312194824
Le résultat pour 40000 entrées est 0.32453370094299316
Le résultat pour 50000 entrées est 0.38787841796875
Le résultat pour 60000 entrées est 0.49108314514160156
Le résultat pour 70000 entrées est 0.6442813873291016
Le résultat pour 80000 entrées est 0.9117996692657471
Le résultat pour 90000 entrées est 0.9976096153259277
Le résultat pour 100000 entrées est 1.2517235279083252

Le tri fusion a l'air d'etre de complexité N*log(N)
car on subdivise le tri en plusieurs tri de 1 élément.
Puis on les recombine ensemble en les lisant.
Le nombre d'étape ou on lit chaque valeur est
a chaque fois que l'on merge des élements (2**k)>=n>(2**(k-1))+1.
Il a donc k étapes ou on lit tout n. k est plus petit que N
car on prend le k supérieur ou égal à N

Si on considère que le tri par fusion a une complexité inférieur aux autres tri
alors plus le nombre de valeur va augmenté
plus l'écart entre les différentes complexités va augmenté également.
Le tri sera toujours plus rapide qu'un tri avec une complexité supérieur

"""
