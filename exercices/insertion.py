from typing import List


"""
Le tri par insertion dans un tableau consiste en :
"""

def insertion_sort(unsortedList : List[int]) -> List[int]:
    unsortedList = [5, 88, 42, 91, 15, 20, 16, 18, 17]
    sortedList = unsortedList.copy()

    if len(sortedList) <= 1:
        return sortedList

    for i in range(1, len(sortedList)):
        tested_value = sortedList[i]
        reverse_index = i - 1 
        while sortedList[reverse_index] > tested_value and reverse_index != 0:
            reverse_index -= 1
            
        val = sortedList.pop(i)
        sortedList.insert(reverse_index+1, val)
    
    print("\n{}\n{}".format(unsortedList,sortedList))
    return sortedList
        