import random
import time

#Insertion method
def insertion(tab:list[int])->list[int]:
    for index in range(1,len(tab)):
        pointer = index-1
        #compare the pointer with the upper nmuber and exhange them if the upper is smallest
        while pointer >= 0 and tab[pointer+1] < tab[pointer] :
            tab[pointer+1],tab[pointer] = tab[pointer],tab[pointer+1]
            pointer -= 1
    return tab

def insertion_sort():
    for i in range(1,11):
        tab = [random.randint(0, 100) for i in range(1000*i)]
        start: float = time.time()
        insertion(tab)
        end : float = time.time()
        print("Temps écoulé pour " + str(1_000 * i) + ":", end - start, "s")
    
insertion_sort()