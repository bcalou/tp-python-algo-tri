"""
Fusion sort
"""


def sort(array: list[int]) -> list[int]:
# Je vérifie que la liste possède plus d'un élément pour engager la division de liste
    if not len(array) <= 1:
        f_half: list[int] = array[:int(len(array)/2)]
        s_half: list[int] = array[int(len(array)/2):]
# Je répète l'opération jusqu'à n'avoir qu'une valeur dans chaque tableau
        return merge(sort(f_half), sort(s_half))
    else:
        return array


# Fonction de fusion de liste avec tri par croissance
def merge(merge_array: list[int], array: list[int]) -> list[int]:
    for value in merge_array:
        too_big: bool = True
        for index in range(len(array)):
            if value < array[index]:
                too_big = False
                array.insert(index, value)
                break
        if too_big:
            array.insert(len(array), value)

    return array
