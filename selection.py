import time
import random
import matplotlib.pyplot as plt


numbers_in_list : list[int] = [1000,2000,3000,5000,10000,15000]

times_list : list[float] = []

def generated_array(nbr_entity : int) -> list[int]:
    array : list[int] = [random.randint(0,100) for i in range(nbr_entity)]
    return array

def selection_sort(input_array : list[int] ) -> list[int] :
    temp_number_idx : int  = -1
    temp_value : int = -1
    for i in range(len(array)) :
        temp_value = array[i]
        for j in range(i+1,len(array)):
            if temp_value > array[j]:
                temp_number_idx = j
                temp_value = array[j]
        input_array[temp_number_idx] = array[i]
        input_array[i] = temp_value
    return input_array




for nbr in numbers_in_list :
    array : list[int] = generated_array(nbr)
    start: float = time.time()
    selection_sort(array)
    end: float = time.time()
    times_list.append(end - start)
    print("Temps écoulé :", end - start)
    print("---------------------------------------")


#creation du graphique
fig, ax =plt.subplots()
ax.plot(numbers_in_list,times_list)
plt.savefig("Selection_graph.png")
plt.close(fig)
