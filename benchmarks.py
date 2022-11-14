"""
Timing benchmarks of the sorting functions
"""

from sort.timer import test_sort_function, test_array_generation_function
from sort.selection import sort as selection_sort


def main():
    """Get execution time for several functions"""
    print("Génération d'un tableau de nombres aléatoires :")
    test_array_generation_function(1_000_000)

    print("Tri par séléction")
    test_sort_function(selection_sort, 1_000)


main()
