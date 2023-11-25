import time
from sort.range import generate_array_of_number

def sort(array: list[int]) -> list[int]:
    """Tri par insertion"""
    
    # On lance une boucle for qui prendra chaque élément 1 par 1 pour les trier
    # On commence à 1 car 0 est déjà trié
    for item_to_sort in range (1, len(array)):
        
        # la variable item_to_test aura pour but de tester les éléments placés
        # avant l'élément que nous voulons trier
        item_to_test = item_to_sort - 1
        current_item = array[item_to_sort]
        # Puis on lance une boucle while qui " déplacera " notre élément tant
        # qu'il n'est pas à la bonne place
        while array[item_to_sort] < array[item_to_test] and item_to_test >= 0:
            # On décales les éléments car nous ne voulons pas insérer notre
            # élément ici
            array[item_to_test + 1] = array[item_to_test]
            item_to_test -= 1
        array[item_to_test + 1] = current_item
    return array

def time_to_sort_insertion(length: int):
    """Temps pour trier un tableau d'une taille donnnée en paramètre avec le
    tri par instertion"""
    array = generate_array_of_number(length)
    start: float = time.time()
    sort(array)
    end: float = time.time()
    print("Taille du tableau = " , length)
    print("Temps écoulé : ", end - start )
    
time_to_sort_insertion(1000)
time_to_sort_insertion(2000)
time_to_sort_insertion(3000)
time_to_sort_insertion(4000)
time_to_sort_insertion(5000)
time_to_sort_insertion(6000)
time_to_sort_insertion(7000)
time_to_sort_insertion(8000)
time_to_sort_insertion(9000)
time_to_sort_insertion(10000)


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