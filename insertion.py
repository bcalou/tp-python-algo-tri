import random
import time

array = [random.randint(0, 100) for i in range(1)]

def insertion_sort(array: list[int]) -> list[int]:
    #on parcourt tous les éléments du tableau
    for i in range(1, len(array)):
        #pour chaque valeur on parcours tous les élements après lui
        start_value = array[i]
        for j in range(i-1, -1, -1):
            #on parcours tous les nombres avant celui sélectionné
            #(ceux d'avant sont déjà trié)
            #dès qu'il tombe sur un plus petit on le place devant lui
            #et on avance tous les nombres plus grand d'un index
            if start_value < array[j] and j == 0:
                array[j+1] = array[j]
                array[j] = start_value
            if start_value < array[j]:
                array[j+1] = array[j]
            if start_value >= array[j] and j == i:
                array[j+1] = start_value
                break

    return array

start: float = time.time()

insertion_sort(array)

end: float = time.time()

print("Temps écoulé :", end - start)
