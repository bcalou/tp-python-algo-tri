import random
import time

start: float = time.time()

# do something
array = [random.randint(0, 100) for i in range(10_000)]

for i in range(len(array)):
    variable_temporaire: int = 0
    for j in range(i+1, len(array)):
        if array[j] < array[i]:
            variable_temporaire = array[i] 
            array[i] = array[j]
            array[j] = variable_temporaire

end: float = time.time()

print("Temps écoulé :", end - start)
