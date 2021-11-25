import time
import random
import matplotlib.pyplot as plt

numbers_in_list : list[int] = [10_000,20_000,40_000,80_000,160_000,1_000_000]

times_list : list[float] = []

test_tab1 : list[int] = [1,8,5,1,2,10]
test_tab2 : list[int] = [1,2,3,5,10,12]


def generated_array(nbr_entity : int) -> list[int]:
    array : list[int] = [random.randint(0,100) for i in range(nbr_entity)]
    return array



def sort( array : list[int]) -> list[int] :
    tab_left : list[int] = []
    tab_right : list[int] = []
    tab_final : list[int] = []

    if len(array) <= 1 :
        return array
    middle_array : int = len(array)//2
    tab_left = sort(array[:middle_array])
    tab_right = sort(array[middle_array:])  
       
    tab_final = merge(tab_left,tab_right)
    return tab_final
  
        
    
def merge( array1 : list[int], array2: list[int]) -> list[int] : 
    i : int = 0
    j : int = 0
    final_array : list[int] = []
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            final_array.append(array1[i]) 
            i+=1
        else :
            final_array.append(array2[j])
            j+=1

    while i < len(array1):
        final_array.append(array1[i])
        i+=1
    while j < len(array2):
        final_array.append(array2[j])
        j+=1
    return final_array
    


for nbr in numbers_in_list :
    array : list[int] = generated_array(nbr)
    start: float = time.time()
    sort(array)
    end: float = time.time()
    times_list.append(end - start)
    print("Temps écoulé :", end - start)
    print("---------------------------------------")


#creation du graphique
fig, ax =plt.subplots()
ax.plot(numbers_in_list,times_list)
plt.savefig("Fusion_graph.png")
plt.close(fig)