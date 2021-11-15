import random
import time

number_entry : int = 9000
array : list = [random.randint(0, number_entry) for i in range(number_entry)]

start: float = time.time()

for j in range(len(array)) :
    min : int = j
    for i in range(len(array)) :
        if array[i] >= array[min] :
            min = i
        if min != j :
            #Swap two index
            array[j], array[min] = array[min], array[j]
            
end: float = time.time()
print("Temps écoulé :", end - start)
