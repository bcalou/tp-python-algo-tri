import random
import time
def insertion_sort(array: list[int]) -> list[int]:

    for start in range(len(array)):
        current_number: int = array[start]
        for i in range(start-1, -1, -1):
            if current_number < array[i]:
                temp: int = array[i]
                array[i] = current_number
                array[i+1] = temp
            else:
                break
    return array