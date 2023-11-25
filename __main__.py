from sort.range import time_to_generate_array, generate_array_of_number
from sort.selection import time_to_sort_selection
from sort.insertion import time_to_sort_insertion
from sort.fusion import time_to_sort_fusion
import time


def main():
    """Fonction principale, ici permettra de tester l'efficacité des algos"""

    # print("---Temps Exec Génération Tableau---")
    # time_to_generate_array(1000000)
    # time_to_generate_array(2000000)
    # time_to_generate_array(3000000)
    # time_to_generate_array(4000000)
    # time_to_generate_array(5000000)
    # time_to_generate_array(6000000)
    # time_to_generate_array(7000000)
    # time_to_generate_array(8000000)
    # time_to_generate_array(9000000)
    # time_to_generate_array(10000000)

    # print("---Temps Exec Tri Selection---")
    # time_to_sort_selection(1000)
    # time_to_sort_selection(2000)
    # time_to_sort_selection(3000)
    # time_to_sort_selection(4000)
    # time_to_sort_selection(5000)
    # time_to_sort_selection(6000)
    # time_to_sort_selection(7000)
    # time_to_sort_selection(8000)
    # time_to_sort_selection(9000)
    # time_to_sort_selection(10000)

    # print("---Temps Exec Tri Insertion---")
    # time_to_sort_insertion(1000)
    # time_to_sort_insertion(2000)
    # time_to_sort_insertion(3000)
    # time_to_sort_insertion(4000)
    # time_to_sort_insertion(5000)
    # time_to_sort_insertion(6000)
    # time_to_sort_insertion(7000)
    # time_to_sort_insertion(8000)
    # time_to_sort_insertion(9000)
    # time_to_sort_insertion(10000)

    # print("---Temps Exec Tri Fusion---")
    # time_to_sort_fusion(1000)
    # time_to_sort_fusion(2000)
    # time_to_sort_fusion(3000)
    # time_to_sort_fusion(4000)
    # time_to_sort_fusion(5000)
    # time_to_sort_fusion(6000)
    # time_to_sort_fusion(7000)
    # time_to_sort_fusion(8000)
    # time_to_sort_fusion(9000)
    # time_to_sort_fusion(10000)

    print("---Temps Exec Sort By Python---")
    time_to_sort_by_pyhton(1000)
    time_to_sort_by_pyhton(2000)
    time_to_sort_by_pyhton(3000)
    time_to_sort_by_pyhton(4000)
    time_to_sort_by_pyhton(5000)
    time_to_sort_by_pyhton(6000)
    time_to_sort_by_pyhton(7000)
    time_to_sort_by_pyhton(8000)
    time_to_sort_by_pyhton(9000)
    time_to_sort_by_pyhton(10000)
    time_to_sort_by_pyhton(999999)


def time_to_sort_by_pyhton(length: int):
    """Temps pour trier un tableau d'une taille donnnée en paramètre avec le
    tri par selection"""
    array = generate_array_of_number(length)
    start: float = time.time()
    array.sort()
    end: float = time.time()
    print("Taille du tableau = ", length)
    print("Temps écoulé : ", end - start)


main()
