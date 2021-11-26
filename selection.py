import random
import time

array = [random.randint(0, 100) for i in range(10_000)]



def selection_sort(array: list[int]) -> list[int]:
    #on parcourt tous les éléments du tableau en gardant la valeur 
    for i, value in enumerate(array):
        #pour chaque élement on parcours la suite du tableau
        permut_index = i
        for j in range(i+1, len(array)):
            #si on en trouve un plus petit on le celui conservé on
            #le prend à la place
            if value > array[j]:
                value = array[j]
                permut_index = j
        #une fois à la fin on permutte le plus petit nombre trouvé avec
        #le premier sélectionné
        array[i], array[permut_index] = array[permut_index], array[i]

    return array

start: float = time.time()

selection_sort(array)

end: float = time.time()

print("Temps écoulé :", end - start)

####### correction


