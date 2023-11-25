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
    PYTHON_SORT = auto()


# We create a loop where there are all the element we need  for test our sort
LOOP_REQUIRED = list[int](((element % 10)+1) * 10 if element < 10
                          else
                          ((element % 10)+1) * 1_000 if 10 <= element < 20
                          else
                          ((element % 10)+1) * 10_000 if 20 <= element < 30
                          else
                          ((element % 10)+1) * 1_000_000
                          for element in range(0, 40))

TEN_PART: int = 0
THOUSAND_PART: int = 10
TEN_THOUSAND_PART: int = 20
MILLION_PART: int = 30


def main(use_tri: Function):
    """main function call two other fonction
    and take on parameter the sort we want use"""
    write_result(do_function(use_tri), use_tri)


def do_function(use_tri: Function) -> list[float]:
    """do_function make ten time the right sort
    and return a tab of time different for the number of element"""
    timer_tab: list[float] = []
    for element in range(len(LOOP_REQUIRED)//4):
        tab_generate = generate_array_of_number(
            generate_index_tab_with_sort(use_tri, element))

        start: float = time.time()
        # Generate a tab from 1_000_000 to 10_000_000
        if (use_tri == Function.GENERATE_ARRAY):
            generate_array_of_number(LOOP_REQUIRED[element + MILLION_PART])

        # Use factorial on number from 10 to 100
        if (use_tri == Function.FACTORIAL):
            get_factorial(LOOP_REQUIRED[element//3] // 100)

        # Use selection sort on tab from 1_000 to 10_000
        if (use_tri == Function.SELECTION_SORT):
            selection_sort(tab_generate)

        # Use insertion sort on tab from 1_000 to 10_000
        if (use_tri == Function.INSERTION_SORT):
            insertion_sort(tab_generate)

        # Use fusion sort on tab from 10_000 to 100_000
        if (use_tri == Function.FUSION_SORT):
            fusion_sort(tab_generate)

        # Use python sort on tab from 1_000_000 to 10_000_000
        if (use_tri == Function.PYTHON_SORT):
            tab_generate.sort()

        end: float = time.time()
        timer_tab.append(end-start)

    return timer_tab


def generate_index_tab_with_sort(use_tri: Function, element: int) -> int:
    """Generate a tab with different length for different sort"""

    # Generate a tab from 10 to 100
    if (use_tri == Function.FACTORIAL):
        return LOOP_REQUIRED[element + TEN_PART]

    # Generate a tab from 10_000 to 100_000
    elif (use_tri == Function.FUSION_SORT):
        return LOOP_REQUIRED[element + TEN_THOUSAND_PART]

    # Generate a tab from 1_000_000 to 10_000_000
    elif (use_tri == Function.PYTHON_SORT):
        return LOOP_REQUIRED[element + MILLION_PART]

    # Generate a tab from 1_000 to 10_000
    else:
        return LOOP_REQUIRED[element + THOUSAND_PART]


def write_result(timer_tab: list[float], use_tri: Function) -> None:
    """write_result take tab of time and the sort for write them to user"""

    for element in range(len(timer_tab)):
        tab_generate = generate_index_tab_with_sort(use_tri, element)
        # print time for function use
        print("Le résultat pour " + str(tab_generate) +
              " entrées est " + str(timer_tab[element]))


# A décommenter
# main(Function.GENERATE_ARRAY)
# main(Function.SELECTION_SORT)
# main(Function.INSERTION_SORT)
# main(Function.FACTORIAL)
# main(Function.FUSION_SORT)
# main(Function.PYTHON_SORT)


"""
Le tri sort de python est environ 100 fois plus rapide que notre tri fusion.
Sa complexité semble etre N

Résultat du python sort :
Le résultat pour 1000000 entrées est 0.10117459297180176
Le résultat pour 2000000 entrées est 0.24679017066955566
Le résultat pour 3000000 entrées est 0.31505799293518066
Le résultat pour 4000000 entrées est 0.42998576164245605
Le résultat pour 5000000 entrées est 0.537330150604248
Le résultat pour 6000000 entrées est 0.6411576271057129
Le résultat pour 7000000 entrées est 0.7325379848480225
Le résultat pour 8000000 entrées est 0.9010059833526611
Le résultat pour 9000000 entrées est 0.9867992401123047
Le résultat pour 10000000 entrées est 1.0364351272583008
"""
