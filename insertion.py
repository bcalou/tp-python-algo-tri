import random
import time

array = [random.randint(0, 100) for i in range(10)]

def insertion_sort(array: list[int]) -> list[int]:
    # for i in range(1, len(array)):
    #     number_i = array[i]
    #     for j in range(i):
    #         if array[i] < array[-j]:
    #             array[i] = array[-j]
    #             array[-j] = number_i
    #         elif array[i] >= array[-j] and array[-j + 1] == -1:
    #             array[-j + 1] = number_i

    for i in range(1, len(array)):
        start_value = array[i]
        for j in range(i-1, -1, -1):
            if start_value < array[j] and j == 0:
                array[j+1] = array[j]
                array[j] = start_value
            if start_value < array[j]:
                array[j+1] = array[j]
            if start_value >= array[j] and j == i:
                array[j+1] = start_value
                break

            
            

    return array

start: float = time.time()

print (insertion_sort(array))

end: float = time.time()

print("Temps écoulé :", end - start)
