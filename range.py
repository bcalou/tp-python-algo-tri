import random
import time
import matplotlib.pyplot as plt

entries = []
time_per_entry = []

for i in range(1, 24):
    number_of_entries = 2 ** i
    start: float = time.time()
    [random.randint(0, 100) for i in range(number_of_entries)]
    end: float = time.time()
    time_elpased = end - start
    entries.append(number_of_entries)
    time_per_entry.append(time_elpased)

plt.plot(entries, time_per_entry, 'ro')
plt.xlabel("Nombre d'entrées")
plt.ylabel("Temps d'exécution (en s)")
plt.axis([1, 2**24, 0, 6])
plt.savefig("graph.png")