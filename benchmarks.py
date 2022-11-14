"""
Timing benchmarks of the sorting functions
"""

from sort.timer import test_function_execution_times
from sort.range import generate_array_of_number


def main():
    """Get execution time for several functions"""
    print("Génération d'un tableau de nombres aléatoires :")
    test_function_execution_times(generate_array_of_number, 1_000_000)


main()
