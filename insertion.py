import random
import time

def insertion_sort():
    for i in range(1,11):
        tab = [random.randint(0, 100) for i in range(1000*i)]
        print(i,tab)
        start: float = time.time()
        for index in range(1,len(tab)):
            #for pointer in reversed(range(0,index+1)):
            pointer = index-1
            while pointer >= 0 and tab[pointer+1] < tab[pointer] :
                    tab[pointer+1],tab[pointer] = tab[pointer],tab[pointer+1]
                    pointer -= 1
        end : float = time.time()
        print("Temps écoulé pour " + str(1_000 * i) + ":", end - start, "s")
        print (i,tab)
    
insertion_sort()