"""
Insertion sort
"""


def sort(array: list[int]) -> list[int]:

    for i in range(1, len(array)):
        # J'enregistre la valuer que je vais comparer et je la retire de la liste
        value_use = array[i]
        array.pop(i)

        # Je parcour les valeurs déjà triées
        for insert_index in range(i):
            # Si une valeur est plus grande que celle actuellement comparée je l'insert avant
            if value_use < array[insert_index]:
                array.insert(insert_index, value_use)
                break

            # Sinon je l'insert à la fin des valeurs triées
            else:
                if insert_index + 1 == i:
                    array.insert(i, value_use)

    return array
