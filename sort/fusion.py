from typing import List
import time
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
    if len(array) <= 1:
        return array

    separation: int = len(array) // 2
    array1: List[int] = array[:separation]
    array2: List[int] = array[separation:]

    return merge(sort(array1), sort(array2))

def merge(array1: List[int], array2: List[int]) -> List[int]:
    result_array: List[int] = []
    i = j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result_array.append(array1[i])
            i += 1
        else:
            result_array.append(array2[j])
            j += 1

    result_array.extend(array1[i:])
    result_array.extend(array2[j:])

    return result_array

if __name__ == "__main__":
    main()
