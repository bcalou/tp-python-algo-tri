from typing import List


"""
Le tri par selection dans un tableau consiste en :
    - Rechercher la valeur la plus petite
    - Échanger ce min avec la premiere case du tableau non trié
    - Recommencer jusqu'à ce que le tableau soit trié
"""

def basic_list_sort(unsortedList : List[int]) -> List[int]:
    sortedList = unsortedList.copy()

    if len(sortedList) == 0:
        return sortedList
    sorted = False
    i : int = 0
    partial_i : int = 0
    while not sorted:

        mini = sortedList[i]
        mini_i = 0

        for partial_i in range(len(sortedList[i:])):
            if mini > sortedList[i:][partial_i]:
                mini = sortedList[i:][partial_i]
                mini_i = partial_i

        sortedList[i+mini_i] = sortedList[i]
        sortedList[i] = mini
        i += 1
        if i == len(sortedList):
            sorted = True

    #print("{} -> {}".format(unsortedList, sortedList))
    return sortedList
        