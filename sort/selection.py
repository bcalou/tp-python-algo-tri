"""
Selection sort
"""


def sort(array: list[int]) -> list[int]:
    # Je parcour la liste pour trouver la valeur la plus petite
    for i in range(len(array)):

        smallest: int = array[i]
        smallest_index: int = i

        for insert_index in range(i, len(array)):

            if smallest > array[insert_index]:

                smallest = array[insert_index]
                smallest_index = insert_index

        # J'inverse la valeur la plus petite avec la valeur la plus haute considérée comme trié
        array[i], array[smallest_index] = array[smallest_index], array[i]

    return array
