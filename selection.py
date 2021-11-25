import time
import random

def selection_sort(array: list[int])-> list[int]:
    start: float = time.time()
    for index in range (len(array)):
        range_of_minimum = index
        for compare in range (index+1, len(array)):
            if array[range_of_minimum] > array[compare]:
                range_of_minimum = compare
        array[index], array[range_of_minimum] = array[range_of_minimum], array[index]
    end: float = time.time()
    print("Temps écoulé pour trier un arrayleau a", len(array) ," entrées :", end - start)
    return array

def selection_sort_correction(array: list[int]) -> list[int]:
    for index, value in enumerate(array):
        permutation_index = index
        for j in range (index + 1, len(array)):
            if (value > array[j]):
                value = array[j]
                permutation_index = j
        array[index], array[permutation_index] = array[permutation_index], array[index]
    return array

selection_sort([0, 4, 5, 7, 2, 9, 3, 6, 8, 1])

for size in range (1_000, 11_000, 1_000):
    array = [random.randint(0, 100) for i in range(size)]
    selection_sort(array)
