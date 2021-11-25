import random
import time

for i in range(1,12):
    start: float = time.time()
    array = [random.randint(0, 100) for i in range(1_000_000*i)]
    end : float = time.time()
    print("Temps écoulé pour " + str(1_000_000 * i) + ":", end - start, "s")