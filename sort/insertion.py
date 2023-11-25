import time
from typing import List
import range as range_array 
# Assuming you have a module named 'range_array' for generating arrays

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
    for old_index in range(1, len(array)):
        current_value = array[old_index]
        index_to_place = old_index - 1

        while index_to_place >= 0 and current_value < array[index_to_place]:
            array[index_to_place + 1] = array[index_to_place]
            index_to_place -= 1

        array[index_to_place + 1] = current_value

    return array

if __name__ == "__main__":
    main()
