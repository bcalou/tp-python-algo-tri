"""
Timing benchmarks of the sorting functions
"""

from sort.timer import test_sort_function, test_array_generation_function
from sort.selection import sort as selection_sort
from sort.insertion import sort as insertion_sort
from sort.fusion import sort as fusion_sort


def main():
    """Get execution time for several functions"""
    print("\nGénération d'un tableau de nombres aléatoires")
    test_array_generation_function(1_000_000)

    print("\nTri par séléction")
    test_sort_function(selection_sort, 1_000)

    print("\nTri par insertion")
    test_sort_function(insertion_sort, 1_000)

    print("\nTri par fusion")
    test_sort_function(fusion_sort, 1_000)

    print("\nTri natif de python")
    test_sort_function(sorted, 1000)

main()
