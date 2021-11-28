import random
import time

#Try the python sort method
for i in range(1,11):
    start: float = time.time()
    tab = [random.randint(0, 100) for i in range(1_000*i)]
    tab.sort()
    end : float = time.time()
    print("Temps écoulé pour " + str(1_000 * i) + ":", end - start, "s")