import time
from sort.range import generate_array_of_number

def sort(array: list[int]) -> list[int]:
    """Tri par sélection"""

    # On parcourt la liste une fois de moins que sa taille
    for iteration in range(len(array) - 1):

        # On affecte la première valeur non triée à la variable smallest_number
        smallest_number = array[iteration]
        index_pop = iteration

        # On parcourt la liste pour trouver la plus petite valeur non triée
        for iteration2 in range(iteration + 1, len(array)):

            if smallest_number > array[iteration2]:

                # Quand on trouve une valeur plus petite, on la stocke dans la variable
                smallest_number = array[iteration2]
                index_pop = iteration2

        # On échange la plus petite valeur trouvée avec l'élément non trié actuel
        array[index_pop], array[iteration] = array[iteration], array[index_pop]

    #print(array)
    return array

def time_to_sort_selection(length: int):
    array = generate_array_of_number(length)
    start: float = time.time()
    sort(array)
    end: float = time.time()
    print("Taille du tableau = " , length)
    print("Temps écoulé : ", end - start )
    


time_to_sort_selection(1000)
time_to_sort_selection(2000)
time_to_sort_selection(3000)
time_to_sort_selection(4000)
time_to_sort_selection(5000)
time_to_sort_selection(6000)
time_to_sort_selection(7000)
time_to_sort_selection(8000)
time_to_sort_selection(9000)
time_to_sort_selection(10000)

# array1 = [1, 3, 1, 4, 3, 4]
# array2 = [73, 16, 829, 2, 6]
# array3 = [-4, -282, 0, 7, 0]
# array4 = [1, 1, 1, 1, 1]
# array5 = []
# array6 = [8]

# sort(array1)
# sort(array2)
# sort(array3)
# sort(array4)
# sort(array5)
# sort(array6)
