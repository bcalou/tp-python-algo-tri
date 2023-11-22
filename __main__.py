import time
from enum import Enum, unique, auto
from sort.range import generate_array_of_number
from sort.selection import sort as selection_sort
from sort.insertion import sort as insertion_sort
from sort.recursion import get_factorial
from sort.fusion import sort as fusion_sort


@unique
class Function(Enum):
    GENERATE_ARRAY = auto()
    SELECTION_SORT = auto()
    INSERTION_SORT = auto()
    FACTORIAL = auto()
    FUSION_SORT = auto()


LOOP_REQUIRED = [element*1000 for element in range(1, 11)]


def main(use_tri: Function):
    """main function call two other fonction
    and take on parameter the sort we want use"""
    write_result(do_function(use_tri), use_tri)


def do_function(use_tri: Function) -> list[float]:
    """do_function make ten time the right sort
    and return a tab of time different for the number of element"""
    timer_tab: list[float] = []
    for element in range(len(LOOP_REQUIRED)):
        start: float = time.time()

        # Generate a tab from 1_000_000 to 10_000_000
        if (use_tri == Function.GENERATE_ARRAY):
            generate_array_of_number(LOOP_REQUIRED[element] * 1000)

        # Use selection sort on tab from 1_000 to 10_000
        if (use_tri == Function.SELECTION_SORT):
            selection_sort(generate_array_of_number(LOOP_REQUIRED[element]))

        # Use insertion sort on tab from 1_000 to 10_000
        if (use_tri == Function.INSERTION_SORT):
            insertion_sort(generate_array_of_number(LOOP_REQUIRED[element]))

        # Use factorial on number from 10 to 100
        if (use_tri == Function.FACTORIAL):
            get_factorial(LOOP_REQUIRED[element] // 100)

        # Use fusion sort on tab from 10_000 to 100_000
        if (use_tri == Function.FUSION_SORT):
            fusion_sort(generate_array_of_number(LOOP_REQUIRED[element] * 100))

        end: float = time.time()
        timer_tab.append(end-start)
    return timer_tab


def write_result(timer_tab: list[float], use_tri: Function):
    """write_result take tab of time and the sort for write them to user"""

    for element in range(len(timer_tab)):

        # print time for generate array from 1_000_000 to 10_000_000
        if (use_tri == Function.GENERATE_ARRAY):
            print("Le résultat pour " + str(LOOP_REQUIRED[element] * 1000) +
                  " entrées est " + str(timer_tab[element]))

        # print time for factorial from 10 to 100
        elif (use_tri == Function.FACTORIAL):
            print(f"Le résultat pour " + str(LOOP_REQUIRED[element] // 100) +
                  " entrées est " + str(timer_tab[element]))

        # print time for fusion sort from 10_000 to 100_000
        elif (use_tri == Function.FUSION_SORT):
            print("Le résultat pour " + str(LOOP_REQUIRED[element] * 100) +
                  " entrées est " + str(timer_tab[element]))

        # print time for fusion sort from 1_000 to 10_000
        else:
            print("Le résultat pour " + str(LOOP_REQUIRED[element]) +
                  " entrées est " + str(timer_tab[element]))

# main(Function.GENERATE_ARRAY)
# main(Function.SELECTION_SORT)
# main(Function.INSERTION_SORT)
# main(Function.FACTORIAL)
# main(Function.FUSION_SORT)
