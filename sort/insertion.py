import time
from sort.range import generate_array_of_number


def sort(array: list[int]) -> list[int]:
    """Tri par insertion."""

    # On lance une boucle for qui prendra chaque élément un par un pour les
    # trier. On commence à 1 car 0 est déjà trié.
    for item_to_sort in range(1, len(array)):

        # La variable item_to_test aura pour but de tester les éléments placés
        # avant l'élément que nous voulons trier.
        item_to_test = item_to_sort - 1
        current_item = array[item_to_sort]

        # Puis on lance une boucle while qui "déplacera" notre élément tant
        # qu'il n'est pas à la bonne place.
        while current_item < array[item_to_test] and item_to_test >= 0:
            # On décale les éléments car nous ne voulons pas insérer notre
            # élément ici.
            array[item_to_test + 1] = array[item_to_test]
            item_to_test -= 1

        array[item_to_test + 1] = current_item

    return array


def time_to_sort_insertion(length: int):
    """Temps pour trier un tableau d'une taille donnée en paramètre avec le
    tri par insertion."""
    array = generate_array_of_number(length)
    start_time = time.time()
    sort(array)
    end_time = time.time()
    print("Taille du tableau =", length)
    print("Temps écoulé :", end_time - start_time)
