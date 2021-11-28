import random
import time

def selection(tab: list[int])-> list[int]:
    for index in range(len(tab)):
        smallest_number = tab[index]
        for pointer in range(index+1,len(tab)):
            if(tab[pointer] < tab[smallest_number]):
                smallest_number = pointer
        tab[index], tab[smallest_number] = tab[smallest_number] , tab[index]
    return tab

def selection_sort():
    for i in range(1,11):
        tab = [random.randint(0, 100) for i in range(1_000*i)]
        start: float = time.time()
        selection(tab)
        end : float = time.time()
        print("Temps écoulé pour " + str(1_000 * i) + ":", end - start, "s")

selection_sort()