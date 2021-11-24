import time
import random
import numpy as np
import matplotlib.pyplot as plt

numbers_in_list : list[int] = [1_000_000, 5_000_000 , 10_000_000, 20_000_000 , 50_000_000, 100_000_000]

times_list : list[float] = []

def generated_array(nbr_entity : int) -> list[int]:
    array : list[int] = [random.randint(0,100) for i in range(nbr_entity)]
    return array


for nbr in numbers_in_list :

    start: float = time.time()
    generated_array(nbr)
    end: float = time.time()
    times_list.append(end - start)
    print("Temps écoulé :", end - start)
    print("---------------------------------------")

#creation du graphique
fig, ax =plt.subplots()
ax.plot(numbers_in_list,times_list)
plt.savefig("range_graph.png")
plt.close(fig)
