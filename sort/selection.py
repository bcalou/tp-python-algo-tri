import time
from typing import List
import range as range_array

def main():
    '''Function to evaluate the algorithm complexity'''
    for size in range(1, 11):
        array: List[int] = range_array.generate_array_of_number(size * 1000)
        start_time: float = time.time()
        sort(array)
        end_time: float = time.time()
        print("Taille de tableau : ", size * 1000,
              " Temps écoulé :", end_time - start_time)

def sort(array: List[int]) -> List[int]:
    '''Selection sort algorithm'''

    for iterator in range(len(array)):
        min_index = find_min_index(array, iterator)
        array[iterator], array[min_index] = array[min_index], array[iterator]

    return array

def find_min_index(array: List[int], start_index: int) -> int:
    min_index = start_index

    for index in range(start_index, len(array)):
        if array[index] < array[min_index]:
            min_index = index

    return min_index

if __name__ == "__main__":
    main()
