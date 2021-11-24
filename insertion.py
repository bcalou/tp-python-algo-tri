import time
import random
import numpy as np
import matplotlib.pyplot as plt

numbers_in_list : list[int] = [1000,2000,3000,5000,10000,15000]

times_list : list[float] = []

def generated_array(nbr_entity : int) -> list[int]:
    array : list[int] = [random.randint(0,100) for i in range(nbr_entity)]
    return array

def insertion_sort(input_array : list[int] ) -> list[int] :
    for i in range(1, len(input_array)):

        start_value = input_array[i]
        current_idx = i-1
        while current_idx >=0 and start_value < input_array[current_idx]  :

            input_array[current_idx + 1] = input_array[current_idx]
            current_idx -=1
        input_array[current_idx+1] = start_value
    return input_array



for nbr in numbers_in_list :
    array : list[int] = generated_array(nbr)
    start: float = time.time()
    insertion_sort(array)
    end: float = time.time()
    times_list.append(end - start)
    print("Temps écoulé :", end - start)
    print("---------------------------------------")


#creation du graphique
fig, ax =plt.subplots()
ax.plot(numbers_in_list,times_list)
plt.savefig("Insertion_graph.png")
plt.close(fig)