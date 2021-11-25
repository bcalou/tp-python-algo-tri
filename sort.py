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



for nbr in numbers_in_list :
    array : list[int] = generated_array(nbr)
    start: float = time.time()
    array.sort()
    end: float = time.time()
    times_list.append(end - start)
    print("Temps écoulé :", end - start)
    print("---------------------------------------")


#creation du graphique
fig, ax =plt.subplots()
ax.plot(numbers_in_list,times_list)
plt.savefig("PySort_graph.png")
plt.close(fig)